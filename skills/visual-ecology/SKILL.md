---
name: visual-ecology
description: Develop varied image worlds for approved book manuscripts through distinct treatment briefs, approval, and one-image-at-a-time generation. Use for VIS-ECO, visual ecology, visual-world exploration, or varied image rounds for a book. Keep final placement and cover typography outside this skill.
---

# Visual Ecology

Create an environmental field of images drawn from a book's pressure, mood, artifacts, settings, and implications. The set may include scenes, objects, damaged documents, diagrams, promotional fragments, rituals, thresholds, emotional afterimages, and displaced pieces of the same world. It should not look like one illustration style applied repeatedly. Directly pictorial or illustrative images are welcome when they serve the book.

## Establish the round

Use the approved manuscript as reference material. Also collect any premise, desired count, round direction, previous images or briefs, bans, and orientation needs. Default to eight images when no count is supplied. Honor any positive count the user requests; the 2/4/8/16 restriction applies only when a particular application enforces it. Include tall, unlettered cover candidates in every round: one in a one- or two-image round, and at least two when the count permits. They remain eligible for interior use.

Before proposing new work, inventory prior-round subjects, media, palettes, compositions, and rejected treatments when they are available. Treat informal feedback as constraints for the next round. Preserve accepted images and variants; an edit or replacement creates a new sibling unless replacement was explicitly requested.

If no approved manuscript or usable text is available, request it. Do not infer manuscript approval from a filename such as `final`.

## Phase 1: treatment briefs

Read the manuscript and write exactly N numbered briefs. Each brief should identify:

- the image's conceptual function or pressure;
- subject or visual event;
- actual medium or physical process;
- style, era, or production context when useful;
- composition, scale, distance, or angle;
- palette and emotional temperature;
- orientation and intended role, including an unlettered cover candidate when requested.

Keep each brief concise but specific enough to become a generation prompt.

Build diversity into the concepts rather than merely naming different media. Vary primary media and processes, but reuse one when two strong concepts require it and their subjects, compositions, and emotional effects differ substantially. Each pair should also differ in at least two of subject type, era, scale, composition, spatial logic, palette, literalness, and emotional temperature. Vary the imagined human hand and material history. Prefer process-specific media when they strengthen the image; do not force visible texture or damage onto a pictorial scene that works without it.

Draw from different parts of the manuscript and different scales: landscape, interior, figure, object, evidence, diagram, fragment, infrastructure, or ritual. Avoid repeating dominant subjects, compositions, and treatments from earlier rounds.

Take conceptual risks. Prefer images that enact an idea through their material or visual logic rather than merely depict a sentence. Do not make every image literal, but do not ban concrete manuscript subjects when they provide a strong anchor. A balanced round can combine oblique images with carefully chosen scenes or objects. Honor explicit requests for more literal or more abstract work. Do not penalize an image merely for being pictorial, illustrative, or beautiful; judge whether its choices carry the manuscript's particular tension.

Avoid decorative random weirdness, generic ominous imagery, and stock impossible corridors. Also reject bland, cute, reassuring, or stock-editorial treatments when they flatten a strange or dystopian book. Do not default to conventionally pretty, polished people, flattering poses, or repeated tidy hairstyles; people should have the specificity, age, wear, ambiguity, and emotional stakes the scene calls for. Strangeness should carry emotional, ritual, or material consequence. Honor all bans.

Present the briefs for selection and steering before generation. If the user explicitly authorizes immediate generation, the supplied direction is sufficient approval and generation may proceed without another confirmation.

## Phase 2: generation

After approval, generate exactly one separate image per approved brief with the available image-generation tool. Use one generation call per image. Preserve the approved concept while turning it into a production-ready prompt.

Generate in order and present small batches as they complete so later prompts can absorb steering. Do not silently replace a failed concept with a different one. If a generation fails, report it and retry only that image with a targeted correction.

For every image:

- make the physical process and composition visible, rather than relying on a style label;
- keep text, title lettering, logos, and watermarks out unless expressly requested;
- preserve requested orientation and useful negative space;
- avoid reusing subjects, palettes, or compositions within the round;
- save the result with a stable number and descriptive filename when project storage is available.

Show each image with its stable round number and short name, for example `R03-02 — Engineered Escape`, matching its saved filename. Do not reuse an ID for a variant or replacement. Do not create a contact sheet unless specifically requested.

## Record image decisions

Keep a per-book image manifest and decision ledger when project storage is available. The manifest records stable ID, round, number, name, file path, and planned cover candidacy. The ledger records `approved`, `rejected`, or `pending`, a separate `marked_cover` choice, any user note, and the latest explicit decision. New images start pending and unmarked; never infer approval or user cover selection from generation, a filename, silence, or a planned cover-candidate label. Cover selection is independent of approval and later interior use.

Present Approve, Reject, and a separate toggleable Mark as cover control directly with each numbered, named image. Mark as cover is secondary to approval and must never silently approve, reject, or exclude interior use. Use functional inline HTML controls if the host supports them. Do not emit inert HTML buttons in chat. When chat HTML cannot persist clicks, provide one local HTML review page with these controls beneath each image; use `scripts/review_board.py` to save clicks immediately to `image-decisions.json`. A plain numbered chat response remains valid: record those decisions in the same ledger without making the user repeat them in a different format. Later feedback supersedes earlier status for that ID; preserve the note/history needed to understand a reversal.

Before the next round or Text Mapping, read the ledger and reconcile the number of approved images against the image inventory. Pass both the manifest and decisions forward. Do not silently exclude an approved image because it was also proposed as a cover.

## Covers and later stages

Every Visual Ecology round includes tall, unlettered cover candidates as specified above. Final cover selection, typography, and storefront-thumbnail testing are separate work. Do not add title treatments during an ordinary ecology round.

Text Mapping also follows Visual Ecology. It selects approved images, assigns distinct text anchors and placement order, and feeds document assembly. Do not choose placements or imply approval merely because an image was generated.

Stop after the round for selection and steering. Keep later rounds and replacements for the same book in the same conversation when possible so prior choices and bans remain visible.

For a copy-paste prompt suitable for a fresh ordinary chat, use [assets/round-prompt.md](assets/round-prompt.md).
