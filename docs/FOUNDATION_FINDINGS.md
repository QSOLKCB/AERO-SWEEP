# Foundation Findings — adversarial records

## AS-FOUNDATION-001 — Self-consistent incorrect determinant

**Status:** documented design counterexample; regression implementation **NOT RUN**.

**Origin:** independent multi-model critique of a proposed SPARK Ada 2×2 determinant. The incorrect implementation and its postcondition both computed `a*b-c*d`, whereas the mathematical determinant of `[[a,b],[c,d]]` is `a*d-b*c`.

**Minimal reproduction (mathematical, not an executed source test):**

```text
matrix:          |1 2|
                 |3 4|
required:         1*4 - 2*3 = -2
incorrect draft:  1*2 - 3*4 = -10
```

**Failure mode:** proving a function satisfies its own incorrect postcondition can be logically valid while violating the intended mathematical contract. A verified implementation is not necessarily a verified specification.

**Expected mitigation:**
1. Freeze canonical `det2(a,b,c,d)=a*d-b*c` in an independently reviewed document.
2. Require a separately implemented oracle derived from this definition, not from the kernel.
3. Require `(1,2,3,4)->-2` in boundary/differential fixtures and negative mutation test `a*b-c*d`.
4. For every proof claim, identify the actual statement established and assumptions used.

**Closure:** OPEN until AS-001's real implementation and test evidence show a regression detecting the incorrect expression. Do not describe this finding as experimentally closed.

## AS-FOUNDATION-002 — Inconsistent foreign-language status and signature designs

**Status:** design risk documented, not empirically reproduced.

Earlier sketches used a procedure with output status in Ada versus a function returning status in C/Rust; an enum status crossing into Rust was also proposed. Corrective **design target** is a single reviewed C prototype returning `uint32_t`, with integer status decode, a real matching Ada export wrapper, and ABI integration tests. An Ada procedure with `out Status` is not C-ABI-equivalent to a C function returning status.

## AS-FOUNDATION-003 — Null check is not wild-pointer validation

**Status:** design risk documented.

Rejecting a null C output pointer cannot prove that a non-null pointer is aligned, writable, or valid. C caller obligations and a Rust-owned output object must be explicit. No claim of complete memory safety for arbitrary C callers.

## AS-FOUNDATION-004 — Determinant scalar bounds differ from orientation-coordinate bounds

**Status:** design risk documented.

The `[-32767,32767]` bound applies to direct matrix elements for AS-001. Computing vector components by subtracting 2D points may double their magnitude. Do not reuse a determinant proof over bounded elements for orientation predicates without proving intermediate bounds separately.
