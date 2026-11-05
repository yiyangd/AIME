from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'src'
for p in ROOT.rglob('*.astro'):
 s=p.read_text(encoding='utf-8-sig')
 for variable in ['c','s','chapter','section']:
  for element in ['h1','h2']:
   s=s.replace(f'<{element}>{{{variable}.titleEn}}</{element}>',f'<{element} data-title-en={{{variable}.titleEn}} data-title-zh={{{variable}.titleZh}}>{{{variable}.titleEn}}</{element}>')
 s=s.replace('<h1 class="home-title" id="home-title">','<h1 class="home-title" id="home-title" data-title-en="Small steps. Stronger problem solvers." data-title-zh="循序渐进，建立解题实力。">')
 s=s.replace('<strong class="section-link-title">{s.titleEn}</strong>','<strong class="section-link-title" data-title-en={s.titleEn} data-title-zh={s.titleZh}>{s.titleEn}</strong>')
 s=s.replace('<span class="nav-chapter-title">{chapter.titleEn}','<span class="nav-chapter-title" data-title-en={chapter.titleEn} data-title-zh={chapter.titleZh}>{chapter.titleEn}')
 s=s.replace('<span class="section-label">{s.titleEn}','<span class="section-label" data-title-en={s.titleEn} data-title-zh={s.titleZh}>{s.titleEn}')
 p.write_text(s,encoding='utf8')
