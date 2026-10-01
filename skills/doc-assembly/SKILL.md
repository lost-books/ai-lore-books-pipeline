---
name: doc-assembly
description: Assemble a manuscript and text-mapped images into a large-image illustrated DOCX prepared for Vellum import. Use for DOC ASSEMBLY, illustrated manuscript assembly, Vellum-ready Word files, or rebuilding a mapped-image DOCX. Preserve manuscript wording and image approvals; do not generate images or rewrite prose unless separately requested.
---

# DOC ASSEMBLY

Create a clean illustrated `.docx` whose chapter structure, text formatting, and inline image placement survive Vellum import. Treat the manuscript, placement record, selected images, and explicit approvals as the complete source of truth.

Use the bundled workspace runtime when available. This specialized skill defines the Vellum-import workflow; do not automatically add a general document-design workflow or print-pagination polish. Follow any separately required skills and higher-priority instructions.

## Required inputs

Accept:

- manuscript text, Markdown, or a readable manuscript file;
- a TEXT MAPPING record in Markdown, JSON, or chat form;
- the mapped image files, uploads, or resolvable thread assets;
- the exact book title and any explicit subtitle;
- any selected cover artwork and requested front matter;
- the output folder when supplied.

Do not infer image approval from a filename, generation history, or mapping alone. If the mapping is provisional, preserve that status and state it. If no mapping exists, run or request TEXT MAPPING before assembly rather than placing images casually.

Resolve every mapped image to an actual file before building. Inventory dimensions and orientation, detect missing or pixel-identical duplicate files, and verify that each exact anchor occurs in the manuscript. Stop for correction only when a missing image or ambiguous anchor makes deterministic assembly impossible.

## Efficient execution

Reuse the mapping inventory and visual descriptions when files are unchanged. Check file identity and availability without reopening every already-inspected image. A user-supplied selection explicitly requested for assembly is approval for that use; unrelated assets remain out of scope.

Discover the runtime once and check required imports before writing the builder. For a simple illustrated DOCX, use available DOCX and image libraries; do not add PDF-analysis dependencies unless actually needed. Reuse a compatible verified builder when available, after checking its assumptions against this manuscript.

Build and structural verification are dependent stages: run them sequentially. If a stage fails, diagnose it before continuing. On resumption, inspect existing outputs and verification records before repeating completed work. Do not render the DOCX to PDF or page images for routine Vellum-import QA.

## Preserve the manuscript

Keep all visible manuscript wording, punctuation, order, section breaks, and notes unchanged except for explicitly approved title changes or formatting conversions. Preserve Markdown bold and italics as Word emphasis. Preserve block quotes, lists, tables, and deliberate scene breaks. Do not invent captions, credits, author names, copyright pages, running heads, or metadata.

Use existing manuscript structure rather than inventing new chapters:

- book title → Word `Title`;
- chapter or fragment headings → true Word `Heading 1`;
- subordinate headings → true Word `Heading 2` or `Heading 3`;
- body prose → Word `Normal`;
- intentional quotations → a consistent quote style;
- scene breaks → centered `* * *` or the manuscript's supplied marker.

Start each `Heading 1` chapter or fragment on a new page unless the source or user requests continuous sections. Set headings to keep with the following paragraph. Do not convert arbitrary bold paragraphs into headings.

## Vellum-ready layout

Build a restrained Word document that imports predictably:

- Letter size, 8.5 × 11 inches, portrait unless requested otherwise;
- approximately 0.7-inch top and bottom margins and 0.8–0.85-inch side margins;
- readable 11-point serif body text with consistent paragraph spacing and modest first-line indents where appropriate;
- black title and heading text without decorative rules, text boxes, or floating shapes;
- no headers, footers, page numbers, automatic table of contents, columns, or ornamental section objects unless requested;
- page breaks and Word paragraph styles rather than blank paragraphs used for spacing.

Vellum will control final ebook and print styling. The DOCX should communicate hierarchy and content cleanly without relying on fragile Word layout tricks.

Set fonts and black heading colors explicitly before the first build, clearing conflicting theme overrides and inherited decorative paragraph borders. Let Word paginate body text naturally. Do not estimate text height or line widths to insert body page breaks. Constrain image dimensions numerically within the usable width and height. Do not shrink images or add manual breaks merely to reduce page count.

Short fragments, ordinary whitespace, and dedicated image pages are acceptable in an import document. They are not defects requiring repeated repagination.

## Embed mapped images

Insert every approved image assigned a body placement once, inline with text, at its recorded `before` or `after` anchor. Preserve the placement order. Cover candidacy and interior use are independent: a cover candidate with a body placement belongs in the body. Exclude a cover candidate only when it has no body placement or the user explicitly excludes it. Reconcile the approved count, body-placement count, and embedded count before delivery; investigate any mismatch instead of silently dropping images by role.

Make images large:

- center each image in its own paragraph;
- preserve aspect ratio;
- use up to about 6.8 inches of width within the default margins;
- constrain tall images numerically to about 8.7–9.0 inches within the default page geometry;
- use the largest size that fits both limits;
- keep source image data at original resolution and avoid unnecessary recompression or raster conversion;
- do not upscale visibly weak files without flagging the limitation.

Keep images inline, never floating. Add short spacing before and after without captions unless captions were supplied. Give each image useful alt text derived from its stable descriptive filename or approved description.

If a selected cover is explicitly included, place the unlettered or finished cover on its own first page at the largest safe size, followed by a page break and the manuscript title page. Otherwise omit cover artwork.

## Build and verify

Create the DOCX with a deterministic builder in a writable work directory. Save the builder when reproducibility is useful, but deliver the finished document rather than temporary scripts or renders.

After assembly, verify structurally:

- the title is exact;
- chapter count and `Heading 1` count match the source structure;
- every approved image with a body placement is embedded exactly once, with its stable ID preserved in the placement record;
- approved count, body-placement count, and embedded count reconcile, with any intentionally unplaced approved images listed explicitly;
- no rejected, pending, duplicate, or unmapped image was inserted;
- each image appears after or before the specified exact anchor;
- images are inline, linked to the expected source files, and retain their aspect ratios and numerical width/height limits;
- visible text extracted from the DOCX matches visible source text, allowing only approved title changes and Markdown-to-Word formatting conversion;
- the DOCX package and media relationships are valid and it reopens with a DOCX parser.

Do not generate page PNGs, a PDF, a contact sheet, or a visual-review round as part of routine assembly. Vellum controls final pagination, so Word-page clipping, widows, blank pages, and spacing are not acceptance criteria here. Render only if the user explicitly asks for Word-page appearance or a concrete import problem cannot be diagnosed structurally; limit that check to the affected content.

## Deliverables

Save the final file as `[Exact title] illustrated.docx` unless the user gives another filename. Keep or update the associated `Image placement.md` or `image-placement.json` when available so the assembly remains reproducible. Return the final DOCX directly and state the verified image count, chapter count, and any unresolved provisional approval.

For an ordinary chat without this skill installed, use [assets/doc-assembly-prompt.md](assets/doc-assembly-prompt.md).
