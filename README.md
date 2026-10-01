# AI Lore Books Pipeline

Experimental production pipeline elements for generating new AI-assisted [Lost Books Lorecore volumes](https://payhip.com/lorecore).

These custom skills support book production from the initial premise through image exploration and Vellum-ready document assembly. The workflow supports strange fiction, recovered documents, procedural writing, obsessive mystery, and mythology. Manuscripts and images remain subject to human selection and revision.

## Workflow

1. Generate a manuscript using `manuscript-generation` or `gated-manuscript-generation`. Both use `namer` when new proper names are needed.
2. Review the manuscript.
3. Explore its visual world using `visual-ecology` or `gated-visual-ecology`.
4. Review and select images, optionally using the separately published [Image Approval Queue](https://github.com/lost-books/Image-Approval-Queue).
5. Assign approved images to exact manuscript anchors using `text-mapping`.
6. Assemble an illustrated DOCX using `doc-assembly`.
7. Prepare listing copy using `product-description`.

## Skills

| Skill | Purpose |
| --- | --- |
| [manuscript-generation](skills/manuscript-generation/SKILL.md) | Write a complete Markdown manuscript from a premise, target length, selected modes, and optional source lore. |
| [gated-manuscript-generation](skills/gated-manuscript-generation/SKILL.md) | Apply internal checks before composition to catch weak creative commitments, repetition, and premise drift. Loads the current manuscript-generation skill. |
| [namer](skills/namer/SKILL.md) | Develop necessary proper names from the manuscript's cultural and linguistic context while preserving established names. |
| [visual-ecology](skills/visual-ecology/SKILL.md) | Develop varied visual treatments for an approved manuscript, with treatment approval before generation. |
| [gated-visual-ecology](skills/gated-visual-ecology/SKILL.md) | Evaluate treatments internally before generating an image round, including tall, unlettered cover candidates. |
| [text-mapping](skills/text-mapping/SKILL.md) | Assign each selected illustration to a distinct, exact text anchor. |
| [doc-assembly](skills/doc-assembly/SKILL.md) | Combine the manuscript and mapped images into an illustrated DOCX prepared for Vellum import. |
| [product-description](skills/product-description/SKILL.md) | Write compact Lost Books / Lorecore catalog copy and Payhip descriptions. |

## Companion project: Image Approval Queue

[Image Approval Queue](https://github.com/lost-books/Image-Approval-Queue) is published separately because it can support image workflows beyond book production.

It provides a persistent review interface with previews, approval and rejection controls, and an independent configurable mark—for example, identifying a cover candidate without changing its approval status.

The queue is an example of a lightweight, task-specific control surface: a small interface connected to the decisions needed for one stage of ongoing work. The broader approach is described in [Generative Control Surfaces](https://github.com/lost-books/generative-control-surfaces).

## What “gated” means

Gated skills evaluate creative choices before committing to a complete manuscript or image generation. The checks address specificity, meaningful consequences, coherence, and repeated defaults.

These gates run internally. They do not add a mandatory approval meeting or guarantee a successful result. Feedback on the actual manuscript and images remains the main guide for subsequent work.

## Using the skills

Each skill's instructions begin in its `SKILL.md`. Supporting scripts, references, and assets belong with the skill folder.

The skills require an AI environment with the capabilities needed for the selected stage. Image generation requires an image tool; local review interfaces and document assembly require file access and suitable runtimes. Individual skills describe their dependencies and operating requirements.

The gated manuscript skill depends on `manuscript-generation` and `namer`. Related skill folders should remain together so relative references continue to work. The visual skills also include a local review-board helper; the separate [Image Approval Queue](https://github.com/lost-books/Image-Approval-Queue) provides a reusable review workflow beyond this pipeline.

## Review and continuity

Generated work is not automatically approved. Image approval and cover selection are separate decisions. Revisions preserve earlier versions unless replacement is explicitly requested.

Text mapping carries approved image choices into assembly. Assembly preserves manuscript wording and produces a DOCX for the next publishing stage. Final cover typography and publication remain separate tasks.
