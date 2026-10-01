#!/usr/bin/env python3
"""Local image approval board; saves each click to a JSON decision ledger."""

import argparse
import html
import json
import mimetypes
import threading
from urllib.parse import unquote
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--decisions", type=Path)
    parser.add_argument("--port", type=int, default=0)
    args = parser.parse_args()
    manifest_path = args.manifest.resolve()
    decisions_path = (args.decisions or manifest_path.with_name("image-decisions.json")).resolve()
    def read_images():
        images = json.loads(manifest_path.read_text())["images"]
        ids = [item["id"] for item in images]
        if len(ids) != len(set(ids)):
            raise ValueError("Image IDs must be unique")
        return images

    read_images()
    lock = threading.Lock()

    def read_ledger():
        return json.loads(decisions_path.read_text()) if decisions_path.exists() else {"images": {}}

    class Handler(BaseHTTPRequestHandler):
        def send_data(self, data, content_type, status=200):
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(len(data)))
            self.send_header("Cache-Control", "no-store")
            self.end_headers()
            self.wfile.write(data)

        def do_GET(self):
            if self.path == "/decisions":
                return self.send_data(json.dumps(read_ledger()).encode(), "application/json")
            if self.path.startswith("/image/"):
                try:
                    image_id = unquote(self.path.removeprefix("/image/"))
                    item = next(item for item in read_images() if item["id"] == image_id)
                    path = Path(item["path"])
                    return self.send_data(path.read_bytes(), mimetypes.guess_type(path)[0] or "application/octet-stream")
                except (ValueError, IndexError, OSError, StopIteration):
                    return self.send_data(b"Not found", "text/plain", 404)
            if self.path != "/":
                return self.send_data(b"Not found", "text/plain", 404)
            statuses = read_ledger().get("images", {})
            images = read_images()

            def card(item):
                image_id = html.escape(item["id"], quote=True)
                name = html.escape(item["name"])
                decision = statuses.get(item["id"], {})
                status = decision.get("status", "pending")
                if status not in ("approved", "rejected"):
                    status = "pending"
                label = {"pending": "Unrated", "approved": "Approved", "rejected": "Rejected"}[status]
                cover = bool(decision.get("marked_cover", False))
                cover_label = "Marked as cover" if cover else "Not marked as cover"
                return f'''<article data-id="{image_id}" data-decision="{status}"><h3>{image_id} — {name}</h3>
<img loading="lazy" src="/image/{image_id}" alt="{name}"><p class="status" role="status">{label}</p>
<div class="actions"><button data-status="approved" aria-pressed="{str(status == 'approved').lower()}">Approve</button>
<button data-status="rejected" aria-pressed="{str(status == 'rejected').lower()}">Reject</button>
<button data-status="pending" aria-pressed="{str(status == 'pending').lower()}">Clear rating</button>
<button data-cover="true" aria-pressed="{str(cover).lower()}">Mark as cover</button></div><p class="cover">{cover_label}</p></article>'''

            def round_number(item):
                return int(item.get("round", 0))

            rounds = sorted({round_number(item) for item in images}, reverse=True)
            pending_sections, reviewed_sections = [], []
            total_pending = 0
            for number in rounds:
                members = [item for item in images if round_number(item) == number]
                pending = [item for item in members if statuses.get(item["id"], {}).get("status") not in ("approved", "rejected")]
                reviewed = [item for item in members if item not in pending]
                total_pending += len(pending)
                if pending:
                    pending_sections.append(f'<section class="round"><header><h2>Round {number:02d} — Awaiting review</h2><p>{len(pending)} unrated · {len(reviewed)} already reviewed</p></header>' + ''.join(card(item) for item in pending) + '</section>')
                if reviewed:
                    approved = sum(statuses[item["id"]].get("status") == "approved" for item in reviewed)
                    state = "Complete" if not pending else "Reviewed items"
                    reviewed_sections.append(f'<details class="round finished"><summary>Round {number:02d} — {state}<span>{approved} approved · {len(reviewed)-approved} rejected</span></summary>' + ''.join(card(item) for item in reviewed) + '</details>')
            content = f'<p class="overview">{total_pending} unrated · {len(images)-total_pending} reviewed · newest unrated rounds first</p>'
            content += ''.join(pending_sections) or '<p class="empty">All images have been reviewed.</p>'
            if reviewed_sections:
                content += '<h2 class="archive-title">Previously reviewed rounds</h2><p class="hint">Expand a round to see or change saved decisions.</p>' + ''.join(reviewed_sections)
            page = '''<!doctype html><html><head><meta charset="utf-8"><title>Image review</title><style>
body{font:16px system-ui;background:#141719;color:#f1f3f4;max-width:960px;margin:auto;padding:24px}h1{margin-bottom:8px}
.overview,.hint,.cover{color:#b6c0c8}.round{border:2px solid #526b7a;margin:32px 0 56px;border-radius:12px;overflow:hidden}.round header{background:#263844;padding:18px 22px}.round header h2{margin:0}.round header p{margin-bottom:0;color:#c5d6e1}
article{background:#20262a;padding:22px;border-top:1px solid #53616a}article h3{margin-top:0}img{display:block;max-width:100%;max-height:800px;object-fit:contain;background:#121416}
.actions{display:flex;gap:10px;flex-wrap:wrap}button{font:inherit;padding:10px 16px;border:2px solid #697781;border-radius:7px;background:#293139;color:#eef2f5;cursor:pointer}button:focus-visible,summary:focus-visible{outline:3px solid #fff;outline-offset:4px}button:disabled{opacity:.6;cursor:wait}
button[data-status="approved"][aria-pressed="true"]{background:#216b42;border-color:#79e3a5;color:white}button[data-status="rejected"][aria-pressed="true"]{background:#962f40;border-color:#ff9aab;color:white}button[data-cover][aria-pressed="true"]{background:#594295;border-color:#c6b1ff;color:white}
button[aria-pressed="true"]:not([data-status="pending"])::before{content:'✓ ';font-weight:700}.status{font-weight:600}article[data-decision="approved"] .status{color:#8bedb4}article[data-decision="rejected"] .status{color:#ffa5b3}
.archive-title{border-top:5px solid #56616b;padding-top:34px;margin-top:64px}.finished{border-color:#46525b;margin:20px 0;background:#1c2227}.finished summary{padding:22px;cursor:pointer;font-size:20px;font-weight:600}.finished summary span{display:block;font-size:15px;font-weight:400;color:#b6c0c8;margin-top:8px}.empty{padding:28px;background:#20352a;border-radius:8px}
</style></head><body><h1>Image review</h1>''' + content + '''<script>
document.querySelectorAll('button[data-status]').forEach(button=>button.addEventListener('click',async()=>{
 const card=button.closest('article'); const buttons=card.querySelectorAll('button'); buttons.forEach(b=>b.disabled=true);
 try {const response=await fetch('/decision',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id:card.dataset.id,status:button.dataset.status})});
 if(!response.ok) throw new Error();
 card.dataset.decision=button.dataset.status; card.querySelector('.status').textContent={approved:'Approved — saved',rejected:'Rejected — saved',pending:'Unrated'}[button.dataset.status];
 card.querySelectorAll('button[data-status]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.status===button.dataset.status)));
 }catch(error){alert('Decision was not saved');}finally{buttons.forEach(b=>b.disabled=false);}
}));
document.querySelectorAll('button[data-cover]').forEach(button=>button.addEventListener('click',async()=>{
 const card=button.closest('article'); const marked=button.getAttribute('aria-pressed')!=='true';
 button.disabled=true;try{
 const response=await fetch('/decision',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({id:card.dataset.id,marked_cover:marked})});
 if(!response.ok)throw new Error();button.setAttribute('aria-pressed',String(marked));card.querySelector('.cover').textContent=marked?'Marked as cover':'Not marked as cover';
 }catch(error){alert('Cover choice was not saved');}finally{button.disabled=false;}
}));</script></body></html>'''
            return self.send_data(page.encode(), "text/html; charset=utf-8")

        def do_POST(self):
            if self.path != "/decision":
                return self.send_data(b"Not found", "text/plain", 404)
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 8192:
                    raise ValueError()
                choice = json.loads(self.rfile.read(length))
                if choice.get("id") not in {item["id"] for item in read_images()} or not (choice.get("status") in ("approved", "rejected", "pending") or type(choice.get("marked_cover")) is bool):
                    raise ValueError()
            except (ValueError, TypeError, json.JSONDecodeError):
                return self.send_data(b"Invalid decision", "text/plain", 400)
            with lock:
                ledger = read_ledger()
                entry = ledger.setdefault("images", {}).setdefault(choice["id"], {})
                entry["updated_at"] = datetime.now(timezone.utc).isoformat()
                if choice.get("status") in ("approved", "rejected", "pending"):
                    entry["status"] = choice["status"]
                    event = {"status": entry["status"], "at": entry["updated_at"]}
                else:
                    entry["marked_cover"] = choice["marked_cover"]
                    event = {"marked_cover": entry["marked_cover"], "at": entry["updated_at"]}
                entry.setdefault("history", []).append(event)
                temporary = decisions_path.with_name(decisions_path.name + ".tmp")
                temporary.write_text(json.dumps(ledger, indent=2) + "\n")
                temporary.replace(decisions_path)
            self.send_data(b"{}", "application/json")

    server = ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"Review board: http://127.0.0.1:{server.server_port}/", flush=True)
    print(f"Decisions: {decisions_path}", flush=True)
    server.serve_forever()


if __name__ == "__main__":
    main()
