---
name: text-mapping
description: Analyze selected book images and a manuscript, then assign each image to a distinct exact text anchor for later layout. Use for TEXT MAPPING, image placement plans, mapping illustrations to manuscript text, or rebuilding a placement record. Accept images already visible in the thread, local image folders, or direct uploads; do not assemble the final document unless separately requested.
---

# TEXT MAPPING

Map a selected image set into a manuscript without rewriting the manuscript. Produce a reviewable placement plan that can later drive DOCX, EPUB, or print assembly.

## Inputs

Accept manuscript text pasted into the conversation, an uploaded Markdown or text file, or a readable local path. Preserve its wording and section order exactly.

Accept images through any combination of:

- selected, named, or ID-labelled images already visible in the current thread;
- a readable local folder path containing image files;
- images uploaded directly into the current conversation.

Use only the images the user places in scope. Read any Visual Ecology image manifest and decision ledger first; the latest explicit user decision for each stable ID controls. Also incorporate later approvals or rejections given in chat. If approval is not explicit, label the mapping provisional rather than treating generation, filenames, or prior presence as approval.

When a local folder is supplied, inventory supported image files recursively only when requested; otherwise inspect the named folder itself. Record filename, dimensions, orientation, and a short visual description. Inspect each image once before mapping it; images already clearly visible in the conversation count as inspected. Reopen only unavailable, ambiguous, or changed images. Ignore hidden files, thumbnails, contact sheets, and pixel-identical duplicates unless the user includes them deliberately.

For images already in the thread or directly uploaded, retain their supplied names or IDs. If an image is unavailable visually, use any supplied description and filename cautiously. Never invent visual details. Mark filename-only mappings as low confidence.

Confirm the selected image count early, before mapping. Keep one inventory with stable IDs and file paths for assembly to reuse. If the user explicitly requests assembling the supplied selection, record that as approval for this use. Preserve explicit exclusions.

## Analyze the manuscript and images

Parse the manuscript into title, headings or fragments, scenes, paragraphs, lists, poems, tables, and breaks. Identify exact sentences or short paragraph endings that can serve as stable anchors.

For each image, record a short description of the subject and the visual details relevant to placement. Analyze medium, mood, palette, scale, or other details only when they help choose an anchor; do not produce an exhaustive visual essay for every image.

Consider three kinds of fit:

1. Direct fit: the image closely corresponds to an event, object, place, figure, or artifact in the nearby text.
2. Thematic fit: the image expresses a section's pressure, mood, argument, ritual, consequence, or visual metaphor without depicting it literally.
3. Structural fit: the image improves rhythm, spacing, escalation, contrast, or section balance when no stronger semantic match exists.

Prefer direct or thematic fit. If several anchors remain equally plausible, choose among valid locations by structural balance or randomized tie-breaking. Label the placement method and confidence honestly. Random placement must still respect section boundaries, reading order, and layout constraints.

## Assign placements

Map every approved in-scope image once by default unless the user explicitly excludes it from the interior. Cover candidacy alone does not exclude an image from body placement; record cover candidacy and interior use as separate fields. Reconcile approved, mapped, excluded, and unresolved counts before handing the placement plan to assembly.

Use a distinct anchor for every image. Multiple images may appear in one section when warranted, but never reuse the same prose anchor. Do not force even distribution when the manuscript supports a better thematic sequence; also avoid accidental clustering caused only by the order in which images were inspected.

Honor explicit motif-spacing requests, such as spreading sheep images throughout the manuscript. Track those images as a group and check their distribution across the full text before finalizing the map.

Choose whether the image belongs before or after the anchor. Prefer `after` when the text introduces or earns the image. Use `before` when the image should establish a location, interruption, or threshold before the reader enters the passage.

Avoid splitting:

- a sentence or dialogue exchange;
- a poem or quoted block;
- a list or table;
- a scene-break marker from the scene it separates;
- a paragraph whose meaning depends on uninterrupted continuation.

Do not add captions, credits, explanations, chapter titles, or new prose. Do not alter the manuscript to make a weak placement fit.

## Output

Provide a placement record in manuscript order. For each image include:

- stable image ID or filename;
- image source: thread, upload, or folder path;
- role: interior, cover candidate, excluded, or unresolved;
- section or fragment;
- exact anchor text copied verbatim;
- placement: before or after;
- fit: direct, thematic, structural, or randomized;
- confidence: high, medium, or low;
- one-sentence rationale;
- approval status when known.

State any images that could not be inspected, duplicates excluded, or images intentionally left unmapped. If project storage is available, save a human-readable `Image placement.md` and a machine-readable `image-placement.json`. Otherwise return the full record in chat. When assembly is also requested, pass the saved record directly to assembly and summarize the count and any issues; do not duplicate the entire record in chat or restart image analysis.

Finish by checking that every mapped interior image appears exactly once, anchors are distinct and verbatim, manuscript order is preserved, covers are separate, and low-confidence or randomized placements are visible for review.

For use in an ordinary text-only chat without this skill installed, copy [assets/text-mapping-prompt.md](assets/text-mapping-prompt.md).
