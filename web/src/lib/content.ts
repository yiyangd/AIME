import raw from '../data/workbook.json';
export type Part='A'|'B'|'C';
export interface PrintRef {href:string;bodyPage?:number;physicalPage?:number;pageCount?:number}
export type PrintResources=Partial<Record<'workbook'|'textbook'|'solutions_en'|'solutions_zh',PrintRef>>;
export interface Chapter {id:number;code:string;titleEn:string;titleZh:string;questionCount:number;sectionCount:number}
export interface Section {id:string;slug:string;chapterId:number;code:string;titleEn:string;titleZh:string;questionIds:string[];partCounts:Record<Part,number>;definitionEn:string;definitionZh:string;methods:any[];prerequisites:string[];print:PrintResources}
export interface Question {id:string;year:number;form:string;number:number;chapterId:number;sectionId:string;part:Part;statementEn:string;statementZh:string;sourceUrl:string;answer:{value:string;stepsEn:string[];stepsZh:string[]};secondary:string[];reasonEn:string;reasonZh:string;reviewStatus:string;print:PrintResources;answerStatus?:string;correctedAnswerEn?:string;correctedAnswerZh?:string;sourceAnswer?:string;editorialNoteEn?:string;editorialNoteZh?:string;image?:{src:string;width:number;height:number}}
export const chapters:Chapter[]=raw.chapters;
export const sections:Section[]=raw.sections as Section[];
export const questions:Question[]=raw.questions as Question[];
export const yearRange=questions.length?`${Math.min(...questions.map(q=>q.year))}–${Math.max(...questions.map(q=>q.year))}`:'2000–2026';
export const chapterById=new Map(chapters.map(c=>[c.id,c]));
export const questionById=new Map(questions.map(q=>[q.id,q]));
export const sectionQuestions=(section:Section)=>section.questionIds.map(id=>questionById.get(id)!);
export const url=(path='')=>`${import.meta.env.BASE_URL.replace(/\/$/,'')}/${path.replace(/^\//,'')}`;
export const sectionUrl=(s:Section)=>url(`sections/${s.slug}/`);
export const chapterUrl=(id:number)=>url(`chapters/${id}/`);
export const knowledgeUrl=(s:Section)=>url(`knowledge/${s.slug}/`);
export const questionUrl=(q:Question)=>`${sectionUrl(sections.find(s=>s.id===q.sectionId)!)}#q-${q.id.toLowerCase()}`;
