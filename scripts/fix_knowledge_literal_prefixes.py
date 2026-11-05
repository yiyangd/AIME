from pathlib import Path
import io,re,tokenize
for p in Path(__file__).parent.glob('author_knowledge_*.py'):
 if not re.fullmatch(r'author_knowledge_(?:CO\d\d|AL06)\.py',p.name):continue
 tokens=[]
 for t in tokenize.generate_tokens(io.StringIO(p.read_text(encoding='utf8')).readline):
  if t.type==tokenize.STRING and '\\' in t.string and 'r' not in re.match('[a-zA-Z]*',t.string).group().lower():
   t=t._replace(string='r'+t.string)
  tokens.append(t)
 p.write_text(tokenize.untokenize(tokens),encoding='utf8')
