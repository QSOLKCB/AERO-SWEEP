# Failure and Threat Model — AS-000

This document describes both accidental and adversarial failures; it does not claim the engine is currently hardened.

## Assets and trust boundaries

- **Mathematical intent:** canonical formulas and domain declarations.
- **Computed results:** SPARK kernel and status.
- **C ABI:** untrusted scalar inputs and caller-provided output pointer.
- **Rust/GTK4 GUI:** untrusted UI input and presentation, never numerical authority.
- **Toolchain/verification:** independently pinned tools, hypotheses, proof reports.
- **Evidence:** receipts linked to exact code SHA; no fabricated or redacted success.
- **Supply chain:** dependencies/build scripts with no hidden network requirements.

## Failure classes

| Hazard | Consequence | Planned mitigation |
| --- | --- | --- |
| Self-consistent wrong postcondition | Wrong result called proved | Independent formula/oracle; AS-FOUNDATION-001 |
| Signed overflow or narrowed intermediate | False determinant sign or UB | Explicit widths, bounded inputs, GNATprove + boundary tests |
| Coordinate difference overflow | Wrong orientation classification | Separate point-coordinate contract |
| Parallel/degenerate division | Runtime error, fabricated intersection | Total status semantics and exhaustive case splits |
| Crossed paths at unequal times | False collision | Common physical time parameter |
| Invalid C output pointer | Crash/memory corruption | Document caller preconditions; reject null only; safe Rust allocation |
| Ada exception crosses ABI | Undefined/uncontrolled cross-language behavior | Verified containment and integration test |
| Rust foreign enum invalid discriminant | Undefined behaviour | Raw integer status and checked decode |
| ABI width/layout mismatch | Corrupt results or crash | Compile/link tests and target evidence |
| GUI recomputes answers | Divergence from kernel | Read-only display of authoritative kernel outputs |
| Unpinned tools / fake evidence | Non-reproducible assurance claim | Evidence receipts + exact SHA |
| External agent mutates main | Irreversible unreviewed change | Owner approval and PR-based changes |

## Boundaries of assurance

Explicit null checks do not validate arbitrary pointers, ABI-level testing does not make unknown foreign code memory-safe, and formal proofs of a mathematical specification do not establish the compiled implementation's correctness without a validated refinement/link. The AS-000 documents are not a security certification or proof report.

## Response to mismatch

Fail closed; record the smallest counterexample, expected vs actual, which component differed, exact code head, and executed/inferred classification. Retain the failure case in tests before accepting a fix. No silent fallbacks, result replacement, or auto-updating of the oracle to match the implementation.
