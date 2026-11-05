from knowledge_root_helpers import Section
s=Section('PS06',r'Means preserve total sums; medians preserve order thresholds; a unique mode constrains multiplicities. Choose the matching representation before performing arithmetic or counting.',r'平均数对应总和，中位数对应有序位置，唯一众数对应重数限制。先选对表示，再计算或计数。',['AL01'])
s.add(r'Convert changed means to changed totals',r'把平均数变化转为总量变化',
 [r'For an unknown sample size $n$ and mean $M$, write its sum as $nM$.',r'Account for every added or removed observation in both the sum and the sample size.',r'Subtract the mean equations to eliminate a shared unknown, then verify a positive integer size and the original observations.'],
 [r'若样本量为 $n$、平均数为 $M$，先把总和写成 $nM$。',r'每次增删观测值，都同时修改总和及样本量。',r'将平均数方程相减，消去公共未知量，再验证正整数样本量及原观测条件。'],
 r'A data set has mean $18$. Adding observations $10$ and $30$ raises its mean to $18.4$. How many original observations were there?',r'一组数据平均数为 $18$，加入 $10,30$ 后，平均数变为 $18.4$。原来有多少个观测值？',
 [r'For original size $n$, the new sum is $18n+40$ and the new size is $n+2$.',r'Thus $18n+40=(92/5)(n+2)$, or $(2/5)n=16/5$, giving $n=8$.',r'The original sum is $144$; the new sum $184$ divided by ten is $18.4$, verifying the result.'],
 [r'设原样本量为 $n$，新总和为 $18n+40$，新样本量为 $n+2$。',r'所以 $18n+40=(92/5)(n+2)$，解得 $n=8$。',r'原总和为 $144$，新总和 $184$ 除以十恰为 $18.4$，验证无误。'],
 r'Adding a value to a set may leave the size unchanged if it was already present; determine the intended set or list convention.',r'若对象为集合，加入已存在的值不会增加元素数；须先分清集合与列表的约定。','2001-I-Q02',prerequisites=['AL01'])
s.add(r'Average independent positions by symmetry and linearity',r'用对称性与线性性逐位求平均',
 [r'Write each data value as a weighted sum of digits or position indicators.',r'Find the mean at each position from its actual allowed choices or symmetry; positions need not be independent for linearity.',r'Add the weighted means, checking that the enumeration weights every allowed object equally.'],
 [r'将每个数写成数字或位置指示量的加权和。',r'根据各位置真实的允许取值或对称性求平均；线性性不要求各位置独立。',r'加总加权平均，并检查所枚举对象是否确实等权。'],
 r'Find the mean integer represented by all five-bit binary strings with exactly three ones, allowing leading zeros.',r'求所有恰有三个一的五位二进制串所代表整数的平均值，允许前导零。',
 [r'There are $\binom53=10$ strings. Each bit position occurs in $\binom42=6$ of them.',r'Thus the average indicator at every position is $6/10=3/5$. The five positional weights sum to $1+2+4+8+16=31$.',r'The mean is therefore $(3/5)31=93/5$. The bit indicators are dependent, but linearity still applies.'],
 [r'共有 $\binom53=10$ 个串，每个位置恰在 $\binom42=6$ 个串中为一。',r'所以每位指示量平均为 $3/5$，五个位置权重和为 $31$。',r'整数平均值为 $(3/5)31=93/5$。各位虽不独立，平均数的线性性仍然成立。'],
 r'Repeated digit appearances share a parameter; include its full positional weight.',r'重复出现的同一数字共用参数，必须计入它的全部位权。','2021-II-Q01',prerequisites=['NT06'])
s.add(r'Count nested medians through threshold patterns',r'按阈值模式计数嵌套中位数',
 [r'Replace values by categories below, equal to, or above the target median.',r'Translate each inner median condition into counts in these categories, then impose the outer median condition.',r'Count category patterns first; restore distinct labels within each category afterward.',r'Check whether row order, within-row order, and identical symbols create different multiplicities.'],
 [r'按低于、等于或高于目标中位数，把数值替换为类别符号。',r'将内层中位数条件转为类别个数，再加入外层中位数条件。',r'先数类别模式，再恢复每类内部的不同标号。',r'检查行顺序、行内顺序及相同符号分别造成的重数。'],
 r'Choose four cells uniformly from a $3\times3$ grid and write ones there, zeros elsewhere. Take the median of each row, then the median of those three values. What is the probability the final value is one?',r'从 $3\times3$ 方格中等可能选四格填一，其余填零。先求各行中位数，再求三个行中位数的中位数。最终为一的概率是多少？',
 [r'A row has median one exactly when it contains at least two ones. The final median is one exactly when at least two rows qualify.',r'There are only four ones, so the row counts must be $2,2,0$. Choose the empty row in three ways and the two selected positions of each other row in three ways each.',r'There are $27$ favorable choices out of $\binom94=126$. The probability is $27/126=3/14$.'],
 [r'一行至少有两个一时，其中位数为一；最终中位数为一，当且仅当至少两行满足此条件。',r'总共只有四个一，所以行内个数只能为 $2,2,0$。空行三种，每个非空行选两个位置又各三种。',r'有利选择为 $27$，总选择为 $\binom94=126$，概率为 $3/14$。'],
 r'A median of medians is determined by row thresholds; it need not equal the median of all entries.',r'中位数的中位数取决于各行的阈值，不能直接当作全体数据的中位数。','2017-I-Q11',prerequisites=['CO01'])
s.add(r'Use unique mode and an absent integer median to bound multiplicities',r'用唯一众数及缺失的整数中位数约束重数',
 [r'Sort the list. An integer median absent from the list requires an even length and two distinct middle entries.',r'Use uniqueness of the mode to bound every other multiplicity and the number of entries.',r'Enumerate the permitted positions of the repeated mode, enforcing middle-entry parity and the original size or sum bound.',r'Check all shorter and longer feasible cases before declaring uniqueness.'],
 [r'先排序。若整数中位数不在列表中，长度必须为偶数，且中间两项不同。',r'由众数唯一，限制其他值的重数以及项数。',r'枚举重复众数的位置，同时使用中间两项的奇偶条件及原数量或总和界。',r'宣称唯一之前，必须排除所有较短或较长的可行情形。'],
 r'Classify all sorted four-entry integer lists using values $1$ through $6$, with unique mode $4$ and an integer median absent from the list.',r'分类所有使用 $1$ 至 $6$ 的整数、含四项的有序非降列表，要求唯一众数为 $4$，且中位数是未出现在列表中的整数。',
 [r'Three or four copies of $4$ would make the median $4$. Thus there are exactly two copies, and the other two entries $a<b$ are distinct and different from $4$.',r'If they straddle $4$, the middle entries are both $4$. If both exceed $4$, they must be $5,6$, with noninteger median $9/2$.',r'If both lie below $4$, the median is $(b+4)/2$, so $b$ must be even. The only choice is $b=2,a=1$. Therefore the unique list is $1,2,4,4$, with absent median $3$.'],
 [r'若有三个或四个 $4$，中位数就是 $4$，不合要求。因此恰有两个 $4$，另两项 $a<b$ 互异且均不为 $4$。',r'若两项分处 $4$ 两侧，中间两项均为 $4$；若都大于 $4$，只能为 $5,6$，中位数为非整数 $9/2$。',r'若都小于 $4$，中位数为 $(b+4)/2$，故 $b$ 为偶数，只能取 $b=2,a=1$。唯一列表为 $1,2,4,4$，其中位数 $3$ 未出现。'],
 r'Unique mode means a strictly greater frequency, so tied repetitions must be excluded.',r'唯一众数的频数须严格大于其他频数，不能保留并列重复值。','2024-II-Q02',prerequisites=['LO03'])
s.save()
