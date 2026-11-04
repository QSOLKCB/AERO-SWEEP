# Architecture — AS-000

Status: **proposed**. The repository currently contains design documentation, not executable implementations.

## Dependency direction

```text
IMPULSE (Rust + GTK4, optional)
        |
        v
C99-compatible public ABI / Rust safety wrapper
        |
        v
SPARK Ada numerical kernel (authoritative runtime computation)
        |
   deterministic numerical result + explicit status

Independent checking plane (not runtime authority):
  Python arbitrary-precision oracle
  Lean 4 mathematical theorems
  Agda constructive structural models
  Rocq independent functional specification
  GNATprove/AoRTE analysis of SPARK source
```

The GUI must not silently replace kernel outputs with its own arithmetic. Test and proof models must be capable of disagreeing with the kernel: independence is a feature.

## Logical components

| Component | Planned role | Boundary |
| --- | --- | --- |
| `kernel/algebra` | Det2, bounded arithmetic, rational predicates | SPARK types/contracts |
| `kernel/geometry` | Orientation, degeneracy and segment semantics | Exact mathematical inputs/results |
| `kernel/sweep` | Earliest simultaneous contact/time-of-impact | Single time axis; interval defined |
| `kernel/impulse` | Later frictionless/frictional collision response | Explicit physical assumptions |
| `abi/include` + `abi/ada` | Versioned C99-facing calls; no exception propagation | ABI fields and signedness audited |
| `IMPULSE/` | Matrix and trajectory controls, visuals, evidence browser | Rust FFI; no authority over results |
| `verification/` | Proof obligations and independent specifications | Cross-model conformance tests |
| `reference/` | Independently derived Python stdlib oracle | Arbitrary-precision integers/Fraction |
| `tests/`, `evidence/` | Differential, boundary, ABI, hostile-case results | Exact SHA and toolchain receipts |

## Non-goals for initial releases

Not a general-purpose game engine, a CAD replacement, a real-time safety certification, a hardware-specific GPU accelerator, a networking framework, or a flight-control stack. Avoid premature extensibility and hidden concurrency.

## Engineering sequence

1. Freeze mathematical meaning and status/domain semantics.
2. Implement headless SPARK kernel, with precise success/failure contracts.
3. Build and verify ABI interoperability with an independently compiled C99 caller.
4. Establish proof and differential evidence; track discrepancies.
5. Integrate optional IMPULSE UI only after the kernel boundary is testable.

A C calling convention alone does not guarantee a safe ABI: verify integer widths and alignment, output-pointer validity requirements, Ada elaboration/runtime setup, linker configuration, symbol names, and exception containment in actual toolchains. A GNATprove proof over SPARK code is not automatically a proof about arbitrary external callers.
