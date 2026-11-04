# Roadmap — AERO-SWEEP / IMPULSE

All gates are prospective. No phase is complete until evidence exists for its exact merged source SHA and applicable scope. Small, inspectable PRs; no auto-merge, unsolicited tags, or deployments.

| Phase | Deliverable | Exit gate |
| --- | --- | --- |
| **AS-000** | Canonical architecture, maths, invariants, ABI proposal, agents, threat model, roadmap | Documentation review; record decisions and unresolved assumptions |
| **AS-001** | Headless SPARK Ada det2 and Python `int` oracle | Exact `a*d-b*c`, bounded-domain/overflow proof obligations, failed-input behavior and differential cases |
| **AS-002** | Lean 4, Agda, Rocq independent specification/proof experiments | Pinned toolchains, concrete theorem statements, executed proof evidence, explicit unproved obligations |
| **AS-003** | C99 ABI, Ada export adapter, independent C caller, Rust FFI wrapper | Layout/width/linkage/exception tests, unknown-status rejection, version 1 freeze review |
| **AS-004** | `IMPULSE/` Rust/GTK4 native matrix laboratory | GUI exactly reflects kernel results/status; works without proof tools installed at runtime |
| **AS-005** | Robust stationary geometry and swept time-of-impact | Degenerate taxonomy, simultaneous-time semantics, exact/guarded comparisons and differential tests |
| **AS-006** | Impulse response research kernel | Declared physical model, conservation tests, separating-contact and invalid-mass guards |
| **AS-007** | Benchmarks, cross-platform evidence and hardening | Measured performance, reproducible matrix, regression and artifact provenance |
| **AS-008** | Stable package/release review | Public API stability, versioning, licensing, release notes and owner approval |

## AS-001 implementation order

1. Implement canonical `a*d-b*c` in explicit bounded SPARK types with pre/postconditions.
2. Run GNATprove on actual source, and report proved/unproved obligations without exaggeration.
3. Implement an independently derived Python standard-library integer oracle; use Fraction only where rational arithmetic is needed.
4. Build a headless test harness with known positive/negative/boundary examples.
5. Preserve regression AS-FOUNDATION-001. Publish evidence and only then consider an implementation PR complete.

The latest Gemini draft is **input to review**, not code to copy blindly: its earlier `a*b-c*d` implementation, unsafe FFI assumptions, and mock build targets are recorded as design pitfalls.

## Release policy

Use kernel `v0.x.y` releases only after owner approval. The IMPULSE UI may use `impulse-v0.x.y` tags once implemented. Propose ABI `aerosweep-abi/1`; do not declare compatibility until compiled interop tests are executed.

## Dependencies and tooling

SPARK/GNATprove/GPRbuild required only for Ada builds; Lean/Agda/Rocq only for their verification jobs; Rust + GTK4 only for IMPULSE; Python standard library for oracle. Prefer offline operation and version pinning. CI must keep headless/kernel validation independent of optional GUI and proof toolchains.
