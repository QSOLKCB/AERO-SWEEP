# Verification and Evidence Strategy — AS-000

**Status: verification plan, not a completed verification report.**

## Separate assurance layers

| Layer | Task | Not sufficient for |
| --- | --- | --- |
| Mathematical definition | Specify det2, orientation, exact segment and swept-time semantics | Actual machine arithmetic |
| Lean 4 | Prove algebraic identities and later geometry theorems | Proving generated Ada machine code |
| Agda | Model constructive valid-state structures and degenerate cases | Automatic equivalence to Rust/Ada |
| Rocq | Independently define functional semantics and check extracted/testable model when useful | Proof that C FFI memory is valid |
| SPARK/GNATprove | Prove scoped absence of runtime errors and functional contracts under stated assumptions | Mathematical intent if postcondition is wrong |
| Python stdlib oracle | Arbitrary-precision independent expected results, Fraction for rational problems | Formal proof of all cases |
| C99/Rust integration | Verify ABI status, widths, linkage, pointer contract, exception boundary | Mathematical correctness for all inputs |
| IMPULSE tests | Verify GUI displays exact kernel statuses/results | Establishing kernel correctness |

Proof assistants have distinct kernels/assumptions; maintain a shared **human-readable property ledger**, not an assertion that cross-language terms are mechanically identical. Translate independently and expose disagreements.

## Differential testing

- Generate deterministic small-domain exhaustive Cartesian cases where feasible; record exact bounds and case counts. **Do not** claim exhaustive verification over all 65,535 possible scalar values per input unless actually executed.
- Test all sign patterns, full boundary extremes, zeros, equal rows/columns, swapped rows/columns, random seeded samples, invalid input, and the known wrong `a*b-c*d` variant.
- The Python oracle MUST implement `a*d-b*c` from the canonical specification independently rather than importing SPARK/Rust logic.
- Python arbitrary-precision `int` suffices for det2; use `fractions.Fraction` for later exact rational intersection parameters.
- Compare status and output; mismatch fails the test. Never silently coerce or ignore unfamiliar status codes.

## Required adversarial partitions

1. determinant mapping mismatch, sign reversal, arithmetic extremes;
2. malformed/invalid matrix fields and inclusive-bound off-by-one;
3. ABI null output, output aliasing assumptions, invalid caller preconditions (do not deliberately dereference wild pointers as if the library can guard them);
4. orientation on large point-coordinate differences;
5. segment endpoint, parallel, collinear overlap, point segments, opposite directions;
6. trajectories crossing at different times, initial overlap, tangency, zero relative velocity;
7. future impulse: separating contacts, zero/invalid mass, restitution limits, normal orientation.

## Evidence receipt format

Each claim of a test/proof must include:
- `case_id` and linked invariant IDs;
- exact repository/head SHA (and file digest when artifact provenance matters);
- timestamp with timezone; OS, architecture, compiler, toolchain and versions;
- command line, environment constraints, deterministic seed/domain and expected result;
- exit status, actual result and relevant warnings;
- proof obligation counts (proved/unproved/assumed/timeout) or test case counts;
- classification: **PASS**, **FAIL**, **INCONCLUSIVE**, **NOT RUN**, or **BLOCKED**;
- paths or hashes for archived logs/artefacts.

CI success alone is not proof of source-level or end-to-end correctness. Treat unsupported platforms and skipped tests as explicit coverage gaps.

## First regression

AS-FOUNDATION-001 is mandatory. A postcondition mirroring an incorrect computation is not evidence that the determinant specification is correct. See [FOUNDATION_FINDINGS.md](FOUNDATION_FINDINGS.md).

## AS-000 gate

Documentation coherence and review only; **no commands or proof executions are claimed** by this phase.
