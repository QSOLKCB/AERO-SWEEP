# Canonical Mathematical Specification — AS-000

**Authority for intended semantics:** this document and its reviewed invariants, not a copied implementation postcondition. Proofs and oracles shall be independently checked against the definitions here.

## MATH-DET-001: 2×2 determinant

For matrix rows `(a,b)` and `(c,d)`:

```text
det2(a,b,c,d) = a*d - b*c
  |a b|
  |c d|
```

The ABI parameters MUST preserve the order `a,b,c,d`. Never substitute `a*b-c*d`. This mapping is frozen for AS-001.

Basic identities over integers (with exact mathematical arithmetic):
- Identical rows or columns imply determinant 0.
- Swapping exactly two rows or two columns negates the determinant.
- A determinant of zero means linear dependence over the rationals for these two vectors; zero-length vectors are included.
- `det2(r_x,r_y,s_x,s_y)` is the signed 2D cross product of row vectors `r,s`.

Counterexample: `det2(1,2,3,4)=-2`; incorrect `a*b-c*d=-10`.

## MATH-DOMAIN-001: AS-001 bounded profile

Initial *scalar matrix elements* are signed integers in `[-32767,32767]` inclusive. Then `|a*d-b*c| <= 2*(32767)^2 = 2147352578`, which fits signed 32-bit. Compute with a checked, explicitly sized internal representation; specify the actual intermediate type rather than assuming Ada `Long_Integer` means 64-bit.

The bound is a deliberately conservative **input contract**, not a universal geometric or numerical limit. For orientation `det2(B-A,C-A)`, coordinate subtraction expands the scalar range; the matrix-element bound must **not** be reused blindly as a bound on input points. Establish a separate orientation domain and intermediate width before implementing it. The public result is intended as exact int64_t for the initial ABI profile, subject to cross-language representation checks.

## MATH-SEG-001: stationary finite segment intersection

Let `P(t)=p+t*r` and `Q(u)=q+u*s`, with `0<=t,u<=1` and **r,s nonzero** for the standard formula. Put `w=q-p`, `den=det2(r_x,r_y,s_x,s_y)`. If `den != 0`:

```text
t = det2(w_x,w_y,s_x,s_y) / den
u = det2(w_x,w_y,r_x,r_y) / den
```

Use exact rational comparisons, not rounded floating-point decisions. Intersection occurs when both ratios lie in the closed unit interval. If `den=0`, classify parallel-disjoint versus collinear first; represent collinear-overlap as an interval rather than inventing a unique intersection parameter. Zero-length input segments are points and require separate classification. Endpoint contact is included unless a later API explicitly introduces open endpoints.

## MATH-SWEEP-001: moving-body contact differs from crossing paths

Spatial segments can cross while objects arrive at different times. For a swept contact, both bodies must occupy a common contact configuration at the **same physical time** within the declared interval `[0,T]`. Define units, frame, interpolation model, shapes, and initial-overlap semantics. Earliest contact rather than an arbitrary line intersection is the required result.

For future translational discs, define relative position `p_rel(t)=p0+v_rel*t`, relative speed and combined radius `R>=0`, and solve earliest `t` for `|p_rel(t)|²<=R²`, with degenerate zero-relative-speed and initial-overlap cases explicit. Implementation and precision policy are deferred to AS-005.

## MATH-IMPULSE-001: later physics

Do not equate collision detection with physical response. A normal impulse solver must document positive mass, approach direction, restitution, contact normal orientation, rotation/inertia/friction, unit system, energy/momentum assumptions, and zero-denominator cases. Deferred to AS-006.

## Contract revision rule

Any changed determinant ordering, domain bounds, segment endpoint policy, time interpretation, or shape model requires a separately reviewed change to this specification and corresponding proof/oracle fixtures.
