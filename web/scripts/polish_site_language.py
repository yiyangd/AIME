from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]/'src'
changes={
 'layouts/Layout.astro':[("{url,questions,chapters,sections,yearRange}","{url,questions,yearRange}"),('>Skip to content</a>','><Bi en="Skip to content" zh="跳至正文"/></a>'),('<small>Topic-Based Practice Workbook</small>','<small><Bi en="Topic-Based Practice Workbook" zh="按题型编排的专题练习册"/></small>'),('STEMHUB · Learn with purpose. Practise with confidence.','STEMHUB · <Bi en="Learn with purpose. Practise with confidence." zh="明确目标，稳步练习。"/>'),('Try “2020-I-Q01”, “2026”, “polynomials”, or “多项式”.','<Bi en="Try a question ID, year, or topic name." zh="可输入题号、年份或题型名称。"/>')],
 'pages/index.astro':[('THE STEMHUB WORKBOOK','<Bi en="THE STEMHUB WORKBOOK" zh="STEMHUB 专题练习册"/>'),('CHAPTER {String(c.id).padStart(2,\'0\')}','<Bi en="CHAPTER" zh="章节"/> {String(c.id).padStart(2,\'0\')}')],
 'pages/knowledge/index.astro':[('LEARN THE METHOD','<Bi en="LEARN THE METHOD" zh="掌握解题方法"/>'),('<h2>{c.id}. {c.titleEn}</h2>','<h2 data-title-en={`${c.id}. ${c.titleEn}`} data-title-zh={`${c.id}. ${c.titleZh}`}>{c.id}. {c.titleEn}</h2>')],
 'pages/matrix.astro':[('SEE THE WHOLE PICTURE','<Bi en="SEE THE WHOLE PICTURE" zh="题型全景"/>'),('{c.titleEn}<br/>{c.titleZh}','<Bi en={c.titleEn} zh={c.titleZh}/>'),('{s.code} · {s.titleEn}<br/>{s.titleZh}','{s.code} · <Bi en={s.titleEn} zh={s.titleZh}/>')],
 'pages/chapters/[chapter].astro':[('>Chapter {chapter.id}</span>','><Bi en={`Chapter ${chapter.id}`} zh={`第 ${chapter.id} 章`}/></span>'),('>CHAPTER {String(chapter.id).padStart(2,\'0\')}</p>','><Bi en="CHAPTER" zh="章节"/> {String(chapter.id).padStart(2,\'0\')}</p>'),('<strong>{previous.titleEn}</strong>','<strong><Bi en={previous.titleEn} zh={previous.titleZh}/></strong>'),('<strong>{next.titleEn}</strong>','<strong><Bi en={next.titleEn} zh={next.titleZh}/></strong>')],
 'pages/sections/[section].astro':[('>Chapter {chapter.id}</a>','><Bi en={`Chapter ${chapter.id}`} zh={`第 ${chapter.id} 章`}/></a>'),('>Section {section.id}</span>','><Bi en={`Section ${section.id}`} zh={`第 ${section.id} 节`}/></span>'),('· {chapter.titleEn}</p>','· <Bi en={chapter.titleEn} zh={chapter.titleZh}/></p>'),('<strong>{previous.id}. {previous.titleEn}</strong>','<strong>{previous.id}. <Bi en={previous.titleEn} zh={previous.titleZh}/></strong>'),('<strong>{next.id}. {next.titleEn}</strong>','<strong>{next.id}. <Bi en={next.titleEn} zh={next.titleZh}/></strong>')],
 'components/QuestionCard.astro':[('{code} {section.titleEn} / {section.titleZh}','{code} <Bi en={section.titleEn} zh={section.titleZh}/>')]
}
for name,replacements in changes.items():
 p=ROOT/name;s=p.read_text(encoding='utf8')
 for a,b in replacements:s=s.replace(a,b)
 p.write_text(s,encoding='utf8')
