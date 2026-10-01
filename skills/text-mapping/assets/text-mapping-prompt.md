# TEXT MAPPING prompt

Run TEXT MAPPING for the manuscript and selected images supplied below. Analyze the images and the manuscript, then assign each interior image to the best exact text anchor without rewriting the manuscript.

Image sources may include any combination of:

- selected, named, or ID-labelled images already visible in this conversation;
- images uploaded directly into this conversation;
- files in a local folder path, when local file access is available.

Use only the images listed or otherwise clearly placed in scope. Preserve their names or IDs. Confirm the selected image count before mapping. Inspect each image once; images clearly visible in the conversation count as inspected. Reopen only changed or ambiguous images. Keep one reusable inventory and concise descriptions focused on placement. If an image cannot be viewed, rely only on its supplied description or filename, do not invent visual details, and mark the result low confidence. An explicit request to assemble the supplied selection approves that use. Otherwise treat approval as provisional unless explicit.

Parse the manuscript into sections, scenes, paragraphs, lists, poems, tables, and breaks. For each image, prefer a direct match to an event, object, place, figure, or artifact. If no direct match is strong, use a thematic match to mood, pressure, argument, ritual, or consequence. If several placements remain equally plausible, choose through structural balance or randomized tie-breaking and label that choice honestly.

Map every selected interior image once by default. Keep cover candidates separate unless explicitly included as interiors. Give every image a distinct anchor copied verbatim from the manuscript. Multiple images may share a section but may not share an anchor. Do not split a sentence, dialogue exchange, poem, quoted block, list, table, or meaningful paragraph. Do not add captions or change manuscript wording.

Honor explicit motif-spacing requests across the full manuscript, rather than clustering similar images in inspection order.

Return the placements in manuscript order. For every image include:

- stable image ID or filename;
- source: thread, upload, or folder;
- role: interior, cover candidate, excluded, or unresolved;
- section or fragment;
- exact anchor text;
- before or after the anchor;
- fit: direct, thematic, structural, or randomized;
- confidence: high, medium, or low;
- one-sentence rationale;
- approval status when known.

When assembly is also requested, save the placement record and pass it directly to assembly without repeating image inspection or copying the entire record into chat.

Also list unavailable images, excluded duplicates, and anything left unmapped. Check that every mapped interior image appears exactly once, anchors are distinct and verbatim, manuscript order is preserved, cover candidates remain separate, and low-confidence or randomized placements are clearly marked.

Selected images already in this conversation:
[IMAGE NAMES OR IDS, OR NONE]

Local image folder:
[FOLDER PATH, OR NONE]

New uploaded images:
[UPLOADS, OR NONE]

Image approvals or exclusions:
[APPROVED, PENDING, REJECTED, OR UNKNOWN]

Manuscript title:
[TITLE]

Manuscript text or Markdown:
[PASTE TEXT OR PROVIDE FILE/PATH]
