# Architecture Decision Record — AS-000

These decisions are accepted as **design intent**, not implementation evidence. Any changed decision needs a documented amendment with downstream invariants/tests reviewed.

## ADR-001 — One monorepo; optional IMPULSE workbench

**Decision:** `AERO-SWEEP` is the repository; `IMPULSE/` is a native Rust/GTK4 consumer. Kernel builds must not depend on GUI assets or packages.

**Reason:** shared versioning and evidence, independent headless operation.

## ADR-002 — SPARK Ada as authoritative computational engine

**Decision:** use SPARK Ada for initial numerical computation; C99-compatible ABI bridges clients. No independent fallback GUI solver is authoritative.

**Risk:** proof assumptions and Ada runtime/ABI interactions need explicit verification.

## ADR-003 — Separate verification layers

**Decision:** Lean 4 (algebra), Agda (constructive states), Rocq (independent executable model), GNATprove (in-scope SPARK properties), Python stdlib (independent exact arithmetic), C/Rust ABI tests (integration). Cross-language equivalence is a test/proof obligation, not a given.

## ADR-004 — Deliberately bounded det2 profile

**Decision:** scalar matrix inputs `[-32767,32767]` inclusive; exact result `a*d-b*c`; intended ABI output int64_t. Domain bounds for point-coordinate differences will be separately justified.

**Reason:** simple auditable arithmetic, no silent wraparound. Wider integer profiles may be introduced later only with separate proofs.

## ADR-005 — Raw integer status interface

**Decision:** proposed ABI returns `uint32_t`, not an unchecked foreign enum. Required statuses: OK=0, OVERFLOW=1, INVALID_INPUT=2, NULL_POINTER=3. The pointer's non-nullness is not a proof of validity; the caller owns its writable output storage.

## ADR-006 — Documentation and evidence precede releases

**Decision:** define contracts before implementation, keep adversarial regressions, require exact SHA/command/toolchain receipts. Owner authorizes merges, tags and release operations.

## Open questions

- Concrete C-target/Ada integer representation and initialization across Linux, Windows, ARM64.
- Whether orientation needs a wider intermediate or additional coordinate-domain restriction.
- Precision strategy for time-of-impact discriminants and tangencies.
- Which Rocq extraction path, if any, is useful without adding runtime dependencies.
- Proof-tool version pins and offline reproducible installation strategy.
- Future shapes, interval/time units and impulse response conventions.

These questions are intentionally unresolved in AS-000 and cannot be treated as implicit guarantees.
