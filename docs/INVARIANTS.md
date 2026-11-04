# Invariant Register — AS-000

Each invariant must have a named implementation owner, independent check, negative test where meaningful, and an evidence reference once implemented. **All statuses below are PLANNED, not verified.**

| ID | Required invariant | Planned check |
| --- | --- | --- |
| AS-I-001 | Every successful det2 output equals exactly `a*d-b*c` for ABI-order inputs `a,b,c,d`. | Python integer oracle, Lean identity, boundary differential tests |
| AS-I-002 | Initial valid scalars are inclusive `[-32767,32767]`; out-of-domain scalars never reach the bounded kernel unchecked. | SPARK precondition and C-facing boundary cases |
| AS-I-003 | No silent integer overflow, division by zero, or unhandled Ada exception on a supported call. | GNATprove over in-scope code + ABI integration tests |
| AS-I-004 | A non-null pointer is **not** automatically safe; each caller guarantees writable, properly aligned `int64_t` storage. Null is rejected before dereference. | C ABI contract and sanitizer/hostile caller tests where applicable |
| AS-I-005 | On any non-OK result, the valid `out_result` is set to 0 (except NULL_POINTER where it is not accessed); output is not reported as a successful numerical answer. | ABI edge tests |
| AS-I-006 | Status transport is a `uint32_t` wire value, never an unvalidated foreign enum or panic; Rust checks unknown values. | C/Rust interface tests |
| AS-I-007 | Matrix element ordering is identical in SPARK, C header, Rust wrapper, oracle and proof fixtures. | `(1,2,3,4)->-2` regression and generated fixtures |
| AS-I-008 | Parallel, collinear, zero-length and endpoint-contact cases are distinct, documented geometric classifications. | Predicate test partitions |
| AS-I-009 | Swept contact uses **simultaneous time** and specifies earliest contact, including initial overlap. | Analytic scenarios + independent oracle |
| AS-I-010 | GUI presentation cannot silently override or redefine kernel status/numerical output. | IMPULSE integration test |
| AS-I-011 | The numerical kernel works headlessly, without GTK4, network, Python, or any proof assistant at runtime. | Independent build/link smoke tests |
| AS-I-012 | Assertions about proof/test success are anchored to exact source SHA, tool versions, commands, and captured outcomes. | Evidence manifest audit |
| AS-I-013 | Specifications and reference oracles are derived independently; proof of a self-consistent but wrong implementation is insufficient. | AS-FOUNDATION-001 cross-check |
| AS-I-014 | No silent API, domain, status, or units change under the same published ABI version. | ABI compatibility and spec review |
| AS-I-015 | No release, merge, tag, or deployment without explicit owner authorization and project release gates. | PR/release review |

## Det2 boundary fixtures (planned)

| Inputs `(a,b,c,d)` | Exact result | Why |
| --- | ---: | --- |
| `(1,2,3,4)` | `-2` | Catches `a*b-c*d` confusion |
| `(32767,32767,-32767,32767)` | `2147352578` | Max positive |
| `(32767,-32767,32767,32767)` | `2147352578` | Independent max positive arrangement |
| `(32767,32767,32767,-32767)` | `-2147352578` | Max negative |
| `(0,0,0,0)` | `0` | All-zero |
| `(1,1,1,1)` | `0` | Equal rows |
| `(32768,0,0,1)` | INVALID_INPUT | Out-of-domain |

The first six examples are mathematical expectations, not executed tests. **Status = NOT RUN.**
