# Independent feasibility review: AIME-2016-I-Q09

Reviewer: source_audit. Date: 2026-11-05. Verdict: source/official answer conflict; do not certify 744 as the constrained maximum.

## Original wording checked visually

The MAA original problem pamphlet, physical page 3, problem 9, explicitly places B on segment QR and C on segment RS (both overlined), and says the triangle is inscribed in the rectangle. It gives AB=40, AC=31 and sin A=1/5. This is not merely a LIVE transcription from segments to lines.

- Original problem pamphlet: https://www.isinj.com/mt-aime/2016AIME-IProblems.pdf
- Original solutions pamphlet, physical page 4: https://www.isinj.com/mt-aime/2016AIME-ISolutions.pdf
- Private source copies: sources/raw/2016I-verified-1.pdf and sources/raw/2016AIME-ISolutions.pdf
- Visual evidence: sources/2016I-problem-p2.png and sources/2016I-sol-p4.png

The official solution gives the upper bound 744 and claims equality at beta=gamma=(90 degrees-A)/2. It does not check that B,C remain on the segments.

## Independent derivation

Put A=(0,0), Q=(w,0), R=(w,h), S=(0,h), with B=(w,b), C=(c,h), 0<=b<=h, 0<=c<=w. Let beta=angle BAQ and gamma=angle CAS. Since the triangle is inside a rectangle corner, A is acute, cos A=2 sqrt(6)/5 and beta+gamma=90 degrees-A.

The lengths give w=40 cos beta, b=40 sin beta, c=31 sin gamma and h=31 cos gamma. The unconstrained area is

    K=1240 cos beta cos gamma
     =620[cos(beta-gamma)+1/5].

It would equal 744 only at beta=gamma. At that point tan beta=sqrt(2/3). Segment membership b<=h would require

    40 sin beta <=31 cos beta,
    equivalently 40 sqrt(2/3)<=31.

This fails: squaring gives 3200/3 > 961. Numerically b-h is about 1.2857245. Thus the official equality configuration lies outside segment QR.

To impose all segment conditions, substitute gamma=90 degrees-A-beta. The B condition is

    (40-31 cos A) sin beta <=31 sin A cos beta,
    tan beta <= (31/5)/(40-62 sqrt(6)/5).

The C condition is automatic, since 31 sin gamma=31 cos(A+beta)<=31 cos A cos beta<40 cos beta=w. Hence the feasible beta interval is [0,beta_max], where

    beta_max=arctan(31/(200-62 sqrt(6))) approximately 32.78424998 degrees.

The unconstrained maximizer beta_0 approximately 39.23152048 degrees is beyond this interval. Since K is strictly increasing up to beta_0, the constrained maximum occurs at beta_max, where B=R.

Let d=BC. Cosine law gives d^2=2561-992 sqrt(6). At B=R, BC is horizontal. The triangle determinant gives h*d=AB*AC*sin A=248. Dot products give w*d=1600-496 sqrt(6). Thus the true constrained maximum is

    K_max=248(1600-496 sqrt(6))/(2561-992 sqrt(6))
         approximately 728.365125470659.

This value is attained with h=248/d and w=(1600-496 sqrt(6))/d, B=R and C=(w-d,h); all points satisfy the stated segment constraints. The rectangle diagonal AB is 40, AC is 31, and the sine of A is 1/5 by construction.

## Delivery recommendation

Retain source_answer=744 for historical traceability. Present an editorial verification note explaining that the source's displayed equality configuration violates segment containment. Do not silently change QR/RS to lines to make the answer work, and do not mark this record independently verified. A separately identified relaxed-lines variant has maximum 744. The literal original segment version has the nonintegral maximum above. This review proves the mathematical conflict, but does not claim that MAA has published or acknowledged an erratum.
