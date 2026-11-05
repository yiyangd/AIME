# STEMHUB · AIME

Static bilingual topic workbook matching the current AMC8 Astro website. Canonical content lives in `../data/{questions,taxonomy,knowledge}.json`; public source statements are mathematical restatements, with original-source links.

```powershell
python scripts/import_content.py
npm ci
npm run check
npm run check-math
npm run build
npm run validate
python scripts/verify-print-links.py
npm run preview
```

The deployed base is `/AIME/`. The importer copies deliverable PDF/XLSX/HTML files from `../output/{matrix,workbook,textbook,solutions}` into the downloads directory. It never includes raw source records, source PDFs or private review evidence. Every route is built as static HTML and supports direct navigation on GitHub Pages. KaTeX and fonts are local assets and require no CDN.

Practice Parts A/B/C mean original Q1–5 / Q6–10 / Q11–15; they are distinct from exam form I/II. Displayed counts and year range derive from the imported question collection. Re-run the importer after content, classification, method notes or deliverables change.

The importer also reads `../output/print/*/{layout_manifest,section_manifest}.json`. Printed body-page labels remain distinct from physical PDF pages: question and method links use the physical page in `#page=`, while compact labels show the printed body page. Section downloads prefer the corresponding split PDF. `verify-print-links.py` requires the pack's Python `pypdf` dependency and checks actual printed IDs at every question anchor, method page ranges, and all section page counts. Run it after the final print files and manifests are refreshed.

Original teaching diagrams are overlaid through `../data/knowledge_diagrams.json`, keyed by stable method ID with `diagram_path`, `alt_en`, and `alt_zh`. Only SVGs under `../data/diagrams` may enter the public build. They use the same accessible enlargement interaction as question diagrams.
