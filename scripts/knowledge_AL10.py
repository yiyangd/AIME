from knowledge_root_helpers import Section
s=Section('AL10',r'Extract only the binomial terms the question actually needs. Integer exponents give exact coefficients; fractional exponents require an explicit remainder bound before a decimal or integer part is certified.',r'只提取题目真正需要的二项式项。整数指数给出精确系数；分数指数则必须先给余项界，才能确定小数位或整数部分。',['AL02'])
s.add(r'Compare adjacent coefficients by cancellation',r'消去公因子比较相邻系数',
 [r'In $(ax+b)^n$, write $[x^k]=\binom nk a^kb^{n-k}$.',r'For consecutive coefficients, divide before expanding: their ratio is $(n-k)a/((k+1)b)$.',r'Keep signs and nonzero conditions; if integer parameters are required, reduce the ratio and apply coprimality.'],
 [r'在 $(ax+b)^n$ 中，$[x^k]=\binom nk a^kb^{n-k}$。',r'比较相邻系数时先相除，得到比值 $(n-k)a/((k+1)b)$。',r'保留符号及非零条件；若参数为整数，约去公因子后使用互质性。'],
 r'Find the ratio of the coefficient of $x^4$ to that of $x^3$ in $(1-2x)^9$.',r'求 $(1-2x)^9$ 中 $x^4$ 系数与 $x^3$ 系数之比。',
 [r'The two coefficients are $\binom94(-2)^4$ and $\binom93(-2)^3$.',r'Their ratio is $((9-3)/4)(-2)=-3$.',r'The negative sign is essential: the even-degree coefficient is positive and the odd-degree coefficient is negative.'],
 [r'两系数分别为 $\binom94(-2)^4$ 与 $\binom93(-2)^3$。',r'相除得 $((9-3)/4)(-2)=-3$。',r'负号不可忽略：偶数次系数为正，奇数次系数为负。'],
 r'A coefficient equality gives a ratio of parameters, not their individual values.',r'系数相等先给出参数比，不能直接确定各参数。','2000-I-Q03',prerequisites=['NT02'])
s.add(r'Find the actual degree after leading cancellations',r'首项抵消后确认实际次数',
 [r'Expand from the highest powers downward and combine coefficients before applying a degree-dependent theorem.',r'Continue until the first nonzero coefficient; also extract the next coefficient if Vieta is needed.',r'Use the actual degree and leading coefficient, counting complex roots with multiplicity.'],
 [r'从最高次幂向下展开，合并系数后再使用依赖次数的定理。',r'直到找到第一个非零系数；若要使用韦达关系，还须提取下一系数。',r'使用实际次数及首项系数，并按重数计算复根。'],
 r'Choose $c$ so $(x+1)^8-(x-1)^8-cx^7$ has degree below seven. Find its actual degree and leading coefficient.',r'选择 $c$，使 $(x+1)^8-(x-1)^8-cx^7$ 次数小于七，求实际次数及首项系数。',
 [r'The $x^8$ terms cancel. The $x^7$ coefficient is $8-(-8)=16$, so choose $c=16$.',r'All even powers cancel in the difference. The next possible power is $x^5$.',r'Its coefficient is $2\binom83=112\ne0$, so the degree is five and the leading coefficient is $112$.'],
 [r'$x^8$ 项抵消，$x^7$ 系数为 $8-(-8)=16$，故取 $c=16$。',r'差式中所有偶次幂均抵消，下一可能非零项为 $x^5$。',r'其系数为 $2\binom83=112\ne0$，所以实际次数为五，首项系数为 $112$。'],
 r'Applying Vieta before locating the first surviving term changes the answer.',r'尚未确定首个保留项就用韦达公式，会使用错误次数。','2001-I-Q03',prerequisites=['AL02'])
s.add(r'Bound a fractional-power remainder before extracting digits',r'提取数字前先控制分数幂余项',
 [r'Write $f(T+1)=T^r+rT^{r-1}+R$ with $T$ large and positive.',r'Taylor remainder gives $R=f^{\prime\prime}(\xi)/2$ for some $T<\xi<T+1$, where $f^{\prime\prime}(t)=r(r-1)t^{r-2}$; use its sign and endpoint bounds.',r'Separate the integer and fractional parts of the retained terms, using modular arithmetic when needed.',r'Compare the full remainder bound with the distance to both neighboring decimal or integer boundaries.'],
 [r'对正的大数 $T$，写成 $f(T+1)=T^r+rT^{r-1}+R$。',r'泰勒余项为某个 $T<\xi<T+1$ 处的 $R=f^{\prime\prime}(\xi)/2$，其中 $f^{\prime\prime}(t)=r(r-1)t^{r-2}$；用其符号与端点估界。',r'分离保留项的整数及小数部分，必要时用同余求小数部分。',r'将全部余项界与相邻两个小数或整数边界的距离比较。'],
 r'Find $\left\lfloor100(10001)^{3/4}\right\rfloor$ without decimal approximation.',r'不用小数近似，求 $\left\lfloor100(10001)^{3/4}\right\rfloor$。',
 [r'Take $T=10000,r=3/4$. The first two terms are $1000+3/40=1000.075$.',r'The second derivative is negative, and $|R|<(3/32)T^{-5/4}=3/3200000<10^{-6}$.',r'Thus $100007.4999<100(10001)^{3/4}<100007.5$. Both bounds have floor $100007$, so that is the exact result.'],
 [r'取 $T=10000,r=3/4$，前两项为 $1000+3/40=1000.075$。',r'二阶导数为负，且 $|R|<(3/32)T^{-5/4}=3/3200000<10^{-6}$。',r'所以 $100007.4999<100(10001)^{3/4}<100007.5$，上下界的整数部分均为 $100007$，故结果精确确定。'],
 r'A tiny error is useful only after the nearest digit boundary has been checked.',r'只有检查了最近的数字边界，“误差很小”才足以确定答案。','2002-I-Q07',prerequisites=['NT04'],extensions_en=[r'The second-order remainder bound follows by integrating $f^{\prime\prime}$ twice: $R=\int_T^{T+1}(T+1-t)f^{\prime\prime}(t)\,dt$. The nonnegative weight has integral $1/2$, giving the same endpoint bounds without an infinite-series convergence assumption.'],extensions_zh=[r'二阶余项界也可由两次积分得到：$R=\int_T^{T+1}(T+1-t)f^{\prime\prime}(t)\,dt$。非负权重的积分为 $1/2$，所以端点界直接给出余项界，不必假定无穷级数收敛。'])
s.save()
