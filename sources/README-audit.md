# AIME source audit

Audit date: 2026-11-05 (UTC).

## Scope actually present

The requested archive lists AIME I and AIME II for every year 2000–2026: 54 paper identities and 810 question appearances. Each fetched contest page contains exactly 15 `baseQuestions` records and all 810 contain a nonempty English solution and answer. No additional 2020 paper identity or alternate sitting is listed by this archive within the requested range. The archive labels, rather than an independently verified administration calendar, define this project inventory.

Primary archive: https://live.poshenloh.com/past-contests

## Access and extraction

- Contest page: `https://live.poshenloh.com/past-contests/aime/2026I`
- Single problem: `https://live.poshenloh.com/past-contests/aime/2026I/problem/1`
- Complete solutions page: `https://live.poshenloh.com/past-contests/aime/2026I/solutions`
- Answer key: `https://live.poshenloh.com/past-contests/aime/2026I/answers`
- Printable source PDF: `https://live.poshenloh.com/images/past-contests/pdf/aime-2026I-exam.pdf`

The public HTML embeds a Next.js JSON script named `__NEXT_DATA__`. Its `props.pageProps.baseQuestions` array contains native LaTeX, HTML diagram tags, numerical answers, concepts, two hints, full solutions, a source Elo estimate and source solve-time estimate. Fetch scripts decode the HTTP bytes explicitly as UTF-8 and preserve the native strings. English and Chinese locale pages were fetched, but `baseQuestions` in the Chinese locale remains English; Chinese interface translation must not be mistaken for Chinese problem/solution content.

**Critical numbering rule:** the actual exam question number is the `baseQuestions` array index plus one. `aimeProblemNumber` is a difficulty calibration field, as are `amc8ProblemNumber` / `amc10ProblemNumber` / `amc12ProblemNumber`; these values have duplicates and gaps and do not identify source exam positions. This rule was checked against the source UI and answer page. The extractor does not sort these arrays.

## Diagrams

There are 82 diagram occurrences and 82 unique SVG URLs in the extracted question/solution strings. The native JSON shorthand `/aime/2026I/15.svg` is rewritten by the source frontend to `/images/past-contests/aime/2026I/15.svg`; simply resolving the shorthand against the source host gives a 404. `diagram_source_urls` in normalized records contains the verified rendered paths. All 82 SVGs were fetched successfully to `sources/assets/` for private inspection, with SHA-256 hashes in `asset_manifest.json`.

## Files

- `fetch_manifest.json`: fetched EN/ZH page URLs, retrieval timestamps, raw HTML SHA-256 hashes and byte lengths.
- `inventory.json`: 54 paper identities, actual and expected question positions, diagram counts and source JSON locations.
- `raw/`: structured Next.js source snapshots, for private audit only.
- `records/<year><form>.json` and `.md`: normalized source records and readable review input, for private audit only.
- `records/all_source_records.json`: all 810 source records, correctly numbered.
- `records/concept_answer_index.tsv`: concise ID / answer / concepts / diagram count index.
- `assets/` and `asset_manifest.json`: private source diagram references.
- `../scripts/audit_source.py`: reproducible source fetcher.
- `../scripts/extract_source_records.py`: reproducible source extraction.
- `../scripts/fetch_source_assets.py`: reproducible diagram fetching.

The manifest hash currently describes the fetched HTML bytes, while the raw path points to extracted structured JSON; these are deliberately different representations. Do not treat the HTML hash as a JSON file hash.

## Verification boundaries

- Extraction verifies count, identity and presence, not mathematical correctness.
- All 810 question and solution strings were checked for Unicode U+FFFD replacement characters: none were present. Some Windows console output displays mojibake despite correct persisted UTF-8.
- Source concepts and ratings are metadata, not this project's reviewed classification or difficulty policy.
- Raw source questions, source solutions and source SVGs are private review input and are not public deployment content. Public delivery should use independently authored concise English mathematical restatements, Chinese equivalents, original worked solutions, original diagrams or complete verbal descriptions, and links back to the source pages.
- The source site's statement that it reproduces MAA problems with permission describes that site's permission; it does not grant this project republication rights.

## Source cross-check examples

2026 AIME I answer page shows Q1 = 277, Q2 = 62, Q3 = 79, matching the first three array positions. Q3's `aimeProblemNumber` is 2, proving that field cannot be used as the exam identifier. The 2026 I printable PDF is six physical pages, and contains the same sequence of 15 questions. These sample source checks do not constitute a per-question mathematical review of all papers.

