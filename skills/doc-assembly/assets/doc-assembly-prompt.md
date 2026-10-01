# DOC ASSEMBLY prompt

Assemble the supplied manuscript and text-mapped images into a large-image illustrated `.docx` ready for import into Vellum.

Use the manuscript, placement record, selected images, and explicit approvals as the source of truth. Preserve all visible manuscript wording, punctuation, order, notes, and scene breaks. Convert Markdown emphasis into Word bold and italics without rewriting prose. Do not invent captions, credits, author names, metadata, or front matter.

Use real Word styles:

- book title → `Title`;
- chapter or fragment headings → `Heading 1`;
- subordinate headings → `Heading 2` or `Heading 3`;
- prose → `Normal`;
- quotations → a consistent quote style.

Begin every `Heading 1` chapter or fragment on a new page unless the manuscript clearly uses continuous sections. Keep headings with the following paragraph. Preserve the supplied chapter structure; do not invent or reorganize chapters.

Use Letter-size portrait pages with restrained typography, approximately 0.7-inch top and bottom margins and 0.8–0.85-inch side margins. Use readable 11-point serif body text. Keep headings black. Do not use floating shapes, columns, decorative rules, headers, footers, page numbers, or an automatic table of contents unless requested.

Reuse the mapping inventory and images already inspected in the conversation; reopen only changed or ambiguous images. Resolve every mapped image to an available file. Insert every approved image with a body placement exactly once at its recorded exact anchor and before/after position. Keep rejected, pending, duplicate, unresolved, or unmapped images out. Cover candidacy does not preclude body placement. Reconcile approved, mapped-for-body, and embedded counts; list any intentionally unplaced approved images.

Images must be centered and inline, preserve aspect ratio, and appear large. Use up to about 6.8 inches of width and constrain height to about 8.7–9.0 inches so each image fits safely on a page. Use the largest size that satisfies both limits. Preserve original image data and avoid unnecessary recompression. Add no captions unless supplied. Set useful image alt text from stable filenames or approved descriptions.

If a cover is explicitly selected for inclusion, place it alone on the first page at the largest safe size, then insert a page break before the title page. Otherwise omit cover artwork.

Before building, check the chosen runtime and required imports. Reuse a compatible verified builder where available. Set fonts and black heading colors explicitly and remove inherited decorative borders or conflicting theme overrides. Let Word paginate prose naturally; do not estimate paragraph heights to insert body page breaks. Ordinary whitespace, short fragments, and dedicated image pages are acceptable for Vellum import. Do not shrink images merely to reduce page count.

Run building and structural verification sequentially. Stop a failed stage before starting dependent work. Resume from verified existing work rather than restarting. Do not render routine page images or a PDF for Vellum-import QA.

After building, verify that the exact title, chapter count, heading structure, approved/body/embedded image counts, image order, exact anchors, and before/after positions match the inputs. Check inline image dimensions, aspect ratios, source identity, media relationships, and DOCX validity. Extract visible DOCX text and compare it with visible manuscript text; only approved title changes and Markdown-to-Word formatting conversion may differ.

Vellum controls final pagination. Do not make page PNGs, a PDF, or a contact sheet unless the user explicitly asks about Word-page appearance or a concrete import defect requires a targeted visual check. Deliver the final DOCX only, plus the placement record if requested. State the verified chapter count and embedded-image count.

Exact title:
[TITLE]

Subtitle:
[SUBTITLE OR NONE]

Manuscript text or file:
[PASTE TEXT OR PROVIDE FILE/PATH]

TEXT MAPPING record:
[PASTE MAPPING OR PROVIDE FILE/PATH]

Image source:
[THREAD ASSETS, UPLOADS, OR FOLDER PATH]

Image approvals and exclusions:
[APPROVED, PENDING, REJECTED]

Selected cover:
[IMAGE OR NONE]

Output folder or filename:
[PATH OR DEFAULT]
