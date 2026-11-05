# AMC8/10/12 template audit

Read-only audit completed 2026-11-05. No `AGENTS.md` files were found in the audited template directories.

## Exact current AMC8 website

Use `D:/AMC8_Codex/amc8-web`, not the older `D:/AMC8_Codex/website`. The former README names the user's live `https://yiyangd.github.io/AMC8/` site and the final 650-question workbook. Astro static framework, base `/AMC8`, Inter font, navy `#173f65`, orange `#e77736`, 72px masthead and 260px reading sidebar.

Reusable files: `src/styles/global.css`, `src/layouts/Layout.astro`, `src/components/{Sidebar,QuestionCard,ChapterIcon,MathText}.astro`, `src/pages/index.astro`, `src/pages/chapters/[chapter].astro`, `src/pages/sections/[section].astro`, `src/scripts/workbook.ts`, and `src/lib/content.ts`. Search index is a generated JSON endpoint. Interactions include search dialog/keyboard shortcuts, chapter drawer, part filtering, question deep links, image zoom and collapsed answer panels.

The original data contract is chapters `{id,titleEn,titleZh,questionCount,sectionCount}`, sections `{id,slug,chapterId,code,titleEn,titleZh,questionIds,partCounts}`, questions `{id,year,number,chapterId,sectionId,part,workbookPage,image,answer:{choice,value,steps}}`. AIME requires full IDs with I/II, three-digit numerical answers and 1–5/6–10/11–15 practice parts. All fixed 650/7/55 counters, dates and `/AMC8` base must be replaced. English source statements/solutions and source assets were not copied into AIME.

## Cover, contents and textbook design

Latest AMC8 workbook is `output/pdf/AMC8_2000-2026_Topic_Workbook_Updated.pdf`. `output/amc8_topic_workbook/build_design_update.py` refreshes frontmatter, while `build_workbook.py` supplies `toc_layout` and `draw_toc`. The accepted book has the supplied raster cover, orange-blue chapter overview, detailed linked bilingual contents, then topic practice pages. The cover at `output/amc8_topic_workbook/cover_update/front_cover.png` was visually inspected: off-white paper, large navy AMC and orange 8, orange/blue broad brush strokes, Hti/STEMHUB marks, mathematical figures and bilingual motto.

`D:/AMC10_Codex/scripts/pack_frontmatter.py` is a more practical reusable vector frontmatter implementation: A4, two-column orange/blue rounded chapter cards, full bilingual titles, body and PDF page numbers, actual navigation links, Arial/微软雅黑 fonts. It consumes canonical taxonomy and real workbook placements. Its seven-active-chapter assertion and reserved-CO08 check are AMC10-specific and must be removed for AIME. Design assets are under `D:/AMC10_Codex/data/design/amc10_frontmatter`.

AMC8 companion textbook is only one accepted pilot, not a full existing textbook: `output/amc8_companion_textbook/pilot/AR03_simple/manuscript.json` and `sources/render_simple.py` (uses `render_pilot.py`). This 8-page accepted style uses original examples, diagrams, 3–4 steps and direct practice IDs; English main text with short Chinese notes. Do not claim AMC8 has a completed full textbook.

## Matrix and canonical pack schema

AMC8 matrix sources: `output/amc8_audit_matrix/{taxonomy.json,audit_records.json,record_contract.json}`, with HTML templates and `build_artifacts.mjs`, `build_bilingual_site.mjs`. Taxonomy has categories and subtypes with definitions/exclusions; each question has one primary `{category_id,subtype_id,reason_zh}`, necessary secondary topics, recomputation/classification/review evidence, source refs and stable ID. Seven category labels and 56 dictionary codes are reference only; AIME needs its own actual coverage.

AMC10 is the most complete integrated pack: `data/{questions,solutions,taxonomy,knowledge,practice_map}.json`; build scripts `pack_integrate.py`, `pack_knowledge.py`, `pack_print.py`, `pack_site.py`, `pack_matrix.mjs`, `pack_matrix_print.py`, `pack_frontmatter.py`. Questions use `amc-pack/1.0`, full IDs, source refs, bilingual solution records and separate primary/secondary classification. The public website under `output/website` is a buildless pack site, not the user's exact Astro template; use its data architecture and print builders but preserve AMC8 Astro visual framework.

AMC12 has extensive source/matrix verification scripts, `matrix.config.json`, `data/source_manifest.json`, `scripts/matrix_parse_live.py`, `build_pack_site.py`, `build_pack_teaching.py`, and `build_workbook_toc.py`. These are useful workflow examples, with AMC12-specific scopes and current archival-source limitations. Do not import their content or acceptance claims into AIME.

## AIME implementation handoff

`D:/AIME/web` reuses the exact current AMC8 global CSS, ChapterIcon and interaction script, adapted layouts/routes and local KaTeX assets. Canonical import is `python web/scripts/import_content.py`; the website does not depend on a source D: project after `npm ci`. No `.git`, source problem crops, raw source PDFs, original workbook data or private audit content were copied into the website.
