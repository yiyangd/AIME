from pathlib import Path
p=Path(__file__).with_name('review_template_flags.py')
s=p.read_text(encoding='utf8').replace('On the circumcircle, the central direction from the minor-arc midpoint $M$ toward $A$ has ordinary angle','The ray $OM$ points toward the midpoint of the minor arc $BC$; the chord/arc-angle relations give')
p.write_text(s,encoding='utf8')
