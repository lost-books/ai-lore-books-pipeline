---
name: manuscript-generation
description: Generate a complete strange book manuscript from a title, premise, length, optional source lore, and blendable recovered, procedural, mystery, or mythology modes. Use for Pressworks text generation, UNDERPASS-style manuscripts, recovered books, or the text stage before Visual Ecology. Deliver Markdown for review; do not generate images or assume manuscript approval.
---

# TEXT GENERATION

Produce the complete manuscript that precedes Visual Ecology, Text Mapping, and DOC Assembly. Write the book itself rather than an outline, treatment, editorial report, or process transcript.

## Inputs

Accept:

- title or working title;
- premise and explicit corrections;
- approximate final word count, default 2,000;
- one or more modes: recovered, procedural, mystery, or mythology;
- optional exact chapter count;
- optional sources, style authority, exclusions, ending limits, or existing draft plus revision note.

Do not require additional fields when the brief is sufficient. Explicit user corrections override sources and defaults.

## Source grounding

When source collections or reference texts are selected and accessible, search for the premise's distinctive subjects and terms. Read a small number of relevant passages in context, normally no more than about 800 source words. Prefer passages that establish what the subject is, does, or affects. Do not fill a quota with generic matches.

Distinguish established source properties from source speculation while reading. Transform that knowledge directly into the manuscript; do not insert a lore report. Keep source titles and locations outside the fiction for later questions. If requested sources are unavailable, state that before writing and do not claim grounding.

Never name another book merely because it supplied research. Use source lore obliquely through events, beings, beliefs, materials, imagery, and conflicting interpretations. Do not copy source sentences or import its plot. The current book's own title is allowed.

## Compose in one pass

Write one finished Markdown manuscript directly. Combine invention, selective transformation, pruning, and continuity judgment during composition. Do not simulate hidden agents, scoring passes, Wreckers, or independent conversations. Do not automatically generate comparison drafts or a later smoothing pass.

Find a particular being, object, practice, place, or material process through which the premise develops. Preserve the premise's ambition and chosen form. Use purposeful activity, specific observations, decisions, resistance, and consequences. Strangeness must alter what can happen, what someone must do, or what is lost.

Let strong implications branch, overturn assumptions, and selectively replace weaker ideas. Preserve productive contradictions and incomplete understanding. Avoid decorative randomness, generic ominous prose, interchangeable surreal images, repeated impossible corridors, arbitrary talking objects, and a mechanical uncanny final sentence in every paragraph.

Choose characters, institutions, settings, and language for this book. Do not default to domestic anecdote, corporate bureaucracy, handbook, named investigator, or stock discovery preface. Never leak assistant identity, chat etiquette, skill names, or internal process language into the fiction.

## Naming through Namer

Before inventing any new proper name, read and apply the [Namer skill](../namer/SKILL.md). Apply it during composition whenever a person, family, place, institution, religion, deity, object, event, or other entity needs a new name. This is a skill handoff within the same composition process, not a separate agent or additional manuscript draft.

Provide Namer with the entity type, narrative function, and whether naming is necessary; the available cultural, linguistic, regional, historical, social, family, and religious context; relevant existing names across categories; known naming rules; broader worldbuilding evidence; patterns to avoid reinforcing; reader-confusion conflicts; and other constraints. Use the brief, source grounding, existing draft, and manuscript composed so far. Infer missing fields from that context without demanding a completed form or substituting genre assumptions.

Accept Namer's determination that no proper name is needed. Otherwise use its selected name and retain the entity type and naming-system context for continuity. Keep candidate lists, analysis, and handoff metadata outside the prose and normally undisclosed. Preserve all established names exactly unless renaming is explicitly requested.

Before each subsequent invention, consider the broader naming evidence across categories rather than copying the most recent name. Where naming evidence is sparse, preserve provisional systems and ordinary forms. Manuscript-specific evidence takes precedence over name blacklists.

## Modes

Blend selected modes throughout one manuscript rather than writing separate mode sections.

- Recovered: imply original use, traces of handling, missing shared knowledge, and incomplete understanding. Let the premise choose the document form. A discovery preface and fragments are optional. Call fragment sections `fragments`, never `leaves`.
- Procedural: develop practical tasks whose rules, costs, and consequences escalate. Keep action particular and readable. Do not turn procedure automatically into administration or corporate bureaucracy.
- Mystery: write compulsively readable conspiracy exposition in an unreliable obsessive voice. Evidence, speculation, memory, and certainty collide. Each major discovery should destabilize the current explanation and force a stranger replacement theory. Objections become pressure, not balanced analysis. Escalate the argument rather than physical danger. Avoid a conventional protagonist or tidy plot.
- Mythology: develop cultural memory, powers, ritual, weather, names, migration, and transformation through concrete activity and cost. Keep cosmology incomplete. Do not import a specific mythology unless requested or supported by selected sources.

When a finished style example is supplied, treat it as authority for motion, density, and voice without borrowing its events, entities, or sentence-level language.

## Structure and ending

Use the exact requested chapter count with Markdown H2 headings when supplied. If mystery is the sole mode and no count is supplied, default to eight H2 chapters. Otherwise choose the structure that serves the brief; do not impose chapters or fragments automatically.

Use the requested title exactly as the Markdown H1. Chapter titles should contribute pressure or movement rather than merely label topics.

Respect requests for no ending. Stop while the document's activity remains underway, without a concluding lesson, retrospective summary, solved mechanism, last-minute twist, or cosmetic ellipsis. Otherwise provide an ending appropriate to the selected form without explaining away the central unknown.

## Delivery and checks

Deliver the complete Markdown manuscript. Save a `.md` file when file access is available; otherwise return the manuscript directly. Preserve an existing draft as a separate version when revising it.

Check the result for approximate word count, title accuracy, requested chapter count, premise and mode drift, compliance with Namer for new proper names, exact preservation of established names, unsupported naming-pattern concentration and reader confusion, source-title leakage, assistant self-identification, and an unwanted ending. Correct obvious problems without launching another generative pass. Do not pad merely to hit a count.

Report the actual word count and selected modes outside the manuscript. Label the manuscript ready for review, not approved. Do not start Visual Ecology until the user approves this version or explicitly requests image exploration.

For an ordinary chat without this skill installed, use [assets/text-generation-prompt.md](assets/text-generation-prompt.md).
