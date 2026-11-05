type Language='en'|'zh'|'bi';
const blocks=[...document.querySelectorAll<HTMLElement>('[data-en][data-zh]')];
const stacked=[...document.querySelectorAll<HTMLElement>('[data-title-en][data-title-zh]')].map(el=>({el,original:el.innerHTML}));
function applyLanguage(language:Language){
 document.body.dataset.language=language; document.documentElement.lang=language==='zh'?'zh-Hans':'en';
 blocks.forEach(el=>{el.textContent=language==='bi'?`${el.dataset.en} / ${el.dataset.zh}`:el.dataset[language]!;});
 stacked.forEach(({el,original})=>{if(language==='bi')el.innerHTML=original;else el.textContent=language==='en'?el.dataset.titleEn!:el.dataset.titleZh!;});
 document.querySelectorAll<HTMLElement>('[data-language-choice]').forEach(el=>el.setAttribute('aria-pressed',String(el.dataset.languageChoice===language)));
 try{localStorage.setItem('aime-language',language);}catch{}
 const render=(window as any).renderMathInElement;
 if(render)render(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'$',right:'$',display:false}],throwOnError:false,strict:'ignore'});
 window.dispatchEvent(new CustomEvent('aime:language'));
}
document.querySelectorAll<HTMLElement>('[data-language-choice]').forEach(el=>el.addEventListener('click',()=>applyLanguage(el.dataset.languageChoice as Language)));
try{const saved=localStorage.getItem('aime-language');if(saved==='en'||saved==='zh'||saved==='bi')applyLanguage(saved);}catch{}
const renderer=(window as any).renderMathInElement;
if(renderer)renderer(document.body,{delimiters:[{left:'$$',right:'$$',display:true},{left:'\\[',right:'\\]',display:true},{left:'$',right:'$',display:false},{left:'\\(',right:'\\)',display:false}],throwOnError:false,strict:'ignore'});
