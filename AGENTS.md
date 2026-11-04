# AERO-SWEEP — Agent Instructions

Applies repository-wide, including `IMPULSE/`, `kernel/`, `abi/`, `verification/`, tests, and documentation. Read [docs/INVARIANTS.md](docs/INVARIANTS.md), [docs/MATHEMATICS.md](docs/MATHEMATICS.md), [docs/VERIFICATION.md](docs/VERIFICATION.md), and [docs/ROADMAP.md](docs/ROADMAP.md) before changing behavior.

## Operating rules

1. **Exact head first.** Record base/head commit SHA, changed paths, intended scope, and applicable contract IDs. Do not assume earlier reviews cover later heads.
2. **No silent authority drift.** The SPARK Ada kernel owns production numerical results; the C ABI transports them; IMPULSE displays them. Reference implementations and formal specifications independently check the kernel rather than silently sharing its incorrect logic.
3. **Documentation-first change control.** If a proposed implementation changes input domain, determinant ordering, error codes, time semantics, overflow rules, ownership, or ABI representation, amend and review the corresponding docs before calling implementation complete.
4. **No unsupported proof claims.** A Lean/Agda/Rocq theorem is not a proof about compiled Ada/C/Rust. A passing GNATprove run does not by itself prove external FFI memory safety or the mathematical intent. Label unexecuted arguments as design hypotheses.
5. **Input is hostile by default.** Negative values, boundary values, collinear/parallel/degenerate geometry, invalid pointers, unknown status codes, ABI mismatches, and numerical overflow require defined tests and outcomes.
6. **No avoidable dependencies.** Prefer standard C99, SPARK Ada, Rust and Python stdlib. Use `uv run` for Python when useful, but do not make `uv` a runtime dependency. No Docker, Node/npm, network services, or cloud APIs by default.
7. **Review evidence honestly.** State exact commands, tool versions, OS/architecture, exit codes, seed/domain, proof obligations, warnings, and whether each test was executed. Preserve failures and unknowns; do not retitle a skipped test as a pass.
8. **No autonomous release operations.** Do not merge, force-push, tag, publish, deploy, enable auto-merge, or change repository security settings without explicit owner authorization for the exact operation. Keep PRs reviewable and do not modify `main` directly.
9. **Minimal blast radius.** Keep PRs phase-scoped; do not slip GUI work into a proof PR or change public ABI without a dedicated review. Avoid updating unrelated files.
10. **Review discipline.** Report actionable defects with exact SHA, file/line, smallest counterexample, actual vs expected, severity, and executed vs inferred status. Do not repeat fixed findings.
11. **License and source integrity.** Respect MPL-2.0 and source provenance; do not import code or proof libraries with incompatible terms or hidden download steps.
12. **Preserve history.** Maintain adversarial findings, including AS-FOUNDATION-001, as regression cases; never rewrite history to conceal a failed experiment.

## PR acceptance checklist

- [ ] Exact base and head SHAs supplied; changed-path list reviewed.
- [ ] All relevant invariants and failure cases identified; docs updated if needed.
- [ ] Independent oracle/reference agreement demonstrated when functionality exists.
- [ ] Exact tool evidence attached or marked **NOT RUN** with explanation.
- [ ] No unsupported claims about ABI, AoRTE, end-to-end verification, determinism, or certification.
- [ ] No unapproved merge, tag, deployment, or widening of scope.

At AS-000, **only documentation review** is required; software test or formal proof success cannot yet be reported.
