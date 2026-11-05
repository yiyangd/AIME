# STEMHUB AIME 2000–2026

This project builds a bilingual AIME learning pack and an AMC8-template static website at [STEMHUB AIME](https://yiyangd.github.io/AIME/).

## Scope and content

- Source archive: https://live.poshenloh.com/past-contests
- Verified inventory: AIME I and II, 2000–2026, 54 papers and 810 problems.
- Public content consists of independently worded mathematical restatements, original worked explanations, original diagrams and source links.
- Downloaded source records and source diagrams are private working inputs under ignored `sources/` subdirectories. They are not public website assets.
- AIME Parts A/B/C mean original Q1–5 / Q6–10 / Q11–15, independent of exam forms I/II.

The shared content contains 810 independently reviewed questions, six first-level topics, 44 second-level sections and 399 bilingual teaching methods. Each method has a procedure, a worked teaching example, cautions and links to applicable contest questions. See `output/qa/coverage.json`, `output/qa/knowledge-coverage.json` and the independent receipts in `audit/` for the checks actually performed.

## Products

- `output/matrix/`: six-sheet Excel matrix; English, Chinese and bilingual offline HTML matrices; print matrices and a full-width poster.
- `output/workbook/`: bilingual practice book and 44 section extracts, grouped by primary subtype and original question ranges A/B/C.
- `output/solutions/`: separate English and Chinese step-by-step solution books, with section extracts.
- `output/textbook/`: bilingual knowledge textbook, including the teaching methods and linked practice references.
- `web/`: the searchable bilingual website, matching the latest AMC8 navigation, chapter pages, knowledge pages, exercise layout and download framework.

One source discrepancy is explicitly documented: the historical answer key 744 for 2016 AIME I Q9 uses an equality configuration outside the stated side segment. The products distinguish that historical key from the independently verified attainable result. See `audit/reviews/2016I-Q09-feasibility.md`; this does not claim an officially acknowledged erratum.

## Authoritative data

`data/batches/*.json` holds authoring batches; `audit/reviews/*.json` supplies independent review overlays. `scripts/integrate.py` validates identities, answer consistency, classification references and bilingual structure, then writes canonical `data/questions.json`, `solutions.json`, `topics.json` and `sections.json`. Classification names, definitions, boundaries and stable subtype codes are in `data/taxonomy.json`.

`data/knowledge_batches/*.json` and exact-content review receipts in `audit/knowledge_reviews/` are combined by `scripts/integrate_knowledge.py` into `data/knowledge.json`. Coverage is checked in both directions between every method and its applicable primary/secondary question routes. The textbook and website import this same canonical knowledge file.

Full builds fail if any expected question is missing. `--allow-partial` is exclusively for internal previews.

## Rebuild

```text
python scripts/integrate.py --require-reviewed
python scripts/integrate_knowledge.py --require-reviewed
python scripts/build_matrix_html.py
node scripts/build_matrix.mjs
<bundled-python> scripts/build_print.py
python web/scripts/import_content.py
cd web
npm ci
npm run check
npm run check-math
npm run build
npm run validate
```

The spreadsheet builder uses the Codex bundled `@oai/artifact-tool` dependency. ReportLab, pypdf and Chromium/KaTeX generate the print products. See `scripts/build_print.py` for local prerequisites. The website is an independent Astro static project with a lockfile; it does not depend on the AMC8 source folder after initial template extraction.

For deployment and the explicit public-file allowlist, see [DEPLOYMENT.md](DEPLOYMENT.md). The site deployment builds the reviewed imported snapshot; it does not retrieve source contest prose or diagrams.

## Design provenance

The website source structure, CSS and page composition derive from the user's latest `D:/AMC8_Codex/amc8-web`, not the older `website` folder. Print covers and contents reproduce its STEMHUB blue/orange visual system with AIME-specific text. See `audit/template-audit.md` for the reference inventory.
