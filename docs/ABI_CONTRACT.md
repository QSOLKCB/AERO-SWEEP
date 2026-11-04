# Proposed C99 ABI Contract — AS-000

**Design proposal only. No shipped header, library, or binary compatibility guarantee exists yet.** Version identifier proposed: `aerosweep-abi/1`; it must be frozen only when AS-003 integration tests succeed.

## Intended public function

```c
#include <stdint.h>

#define AEROSWEEP_STATUS_OK             UINT32_C(0)
#define AEROSWEEP_STATUS_OVERFLOW       UINT32_C(1)
#define AEROSWEEP_STATUS_INVALID_INPUT  UINT32_C(2)
#define AEROSWEEP_STATUS_NULL_POINTER   UINT32_C(3)

uint32_t aerosweep_det2x2(
    int32_t a, int32_t b, int32_t c, int32_t d,
    int64_t *out_result);
```

The signature is a design target, not a header installed in AS-000. The full 2×2 matrix is `[[a,b],[c,d]]`, and successful output equals `a*d-b*c` exactly. Support requires an implementation whose `stdint.h` defines the exact-width types. Use documented C linkage and verify Ada sizes against the C target rather than relying on `Interfaces.C.int`, `Long_Integer`, or `Long_Long_Integer` being the desired sizes across all targets.

## Parameters and status

- Scalars are signed 32-bit **transport fields**; `[-32767,32767]` is the accepted **mathematical profile** for AS-001.
- `out_result` is caller-allocated, writable, properly aligned storage for one `int64_t`. It must be valid for the duration of the call. The library cannot reliably determine whether an arbitrary non-null pointer is valid.
- A null `out_result` returns NULL_POINTER without dereference (takes precedence over invalid numeric inputs).
- Non-null, valid output storage plus an out-of-domain scalar returns INVALID_INPUT and stores zero.
- On success, returns OK and stores the exact determinant.
- OVERFLOW is reserved as a defined failure status for future guarded profiles; no valid AS-001 inputs should produce it.
- Any known non-OK result with a valid output pointer stores zero. A returned unknown status must be treated as a failure by Rust and C callers.

## Safety constraints

1. No Ada exception may unwind across the C boundary. Implement and test an exception containment strategy compatible with the proof boundary.
2. No caller-supplied raw pointer is considered safe because of a null check alone; pointer validity remains a caller-side precondition. Rust's safe wrapper must always provide its own valid local output.
3. Verify object format, calling convention, signed/unsigned widths, exact symbol, alignment, GNAT initialization/elaboration/link setup and runtime dependencies on each platform. Record actual evidence.
4. The Rust wrapper shall receive an integer `uint32_t` status, map known codes exhaustively, and reject unknown codes. It must not construct a foreign Rust enum from unchecked representation.
5. ABI version changes require explicit compatibility evaluation; no silent behaviour change or new success interpretation.
6. Do not describe the C-facing layer as zero-overhead, runtime-free, memory-safe for arbitrary callers, or proven until measured and verified.

## Out-of-scope

The ABI does not yet promise concurrency, re-entrancy, time-of-impact structs, multi-precision types, allocator sharing, callbacks, or shared-memory usage. These require separate documented contracts.
