# AS-001 — Headless determinant implementation

Status: **implementation candidate; local Ada compilation and GNATprove proof not yet executed**. This PR introduces no C ABI, GUI, Lean, Agda, or Rocq implementation.

## Public mathematical profile

- Input matrix rows: (a,b), (c,d), determinant a*d - b*c.
- Direct element bounds: inclusive [-32767,32767].
- Internal numerical types: Interfaces.Integer_32 and Interfaces.Integer_64 (actual fixed-width signed types), widened before multiplication.
- Internal Ada-only Result: OK/exact integer or Invalid_Input/zero. This is **not** the proposed external uint32_t ABI.
- Maximum absolute valid result: 2147352578.

## Files

- kernel/algebra/determinant.ads/.adb: SPARK-mode bounded Compute_2x2 and total Try_Compute_2x2 for signed 32-bit inputs.
- kernel/aero_sweep.gpr: headless Ada kernel project.
- examples/det2_cli.adb + tests/det2_cli.gpr: Ada CLI integration probe outside the SPARK proof boundary.
- reference/oracle.py: independent Python standard-library arbitrary-precision arithmetic.
- tests/: pinned fixtures, mapping-mutation regression, exhaustive [-2,2]^4 domain (625 cases), seeded boundary cases (512 cases), oracle identities.
- Makefile: explicit build, prove, and test targets.

## Reproduce (requires installed GNAT/GPRbuild; GNATprove separately for proofs)

```sh
make test-oracle                    # Python stdlib only
make build                          # gprbuild -p -P tests/det2_cli.gpr
make test-differential              # real Ada CLI vs Python exact oracle
make prove                          # GNATprove, report actual obligations
```

For the compiled CLI:

```sh
build/bin/det2_cli 1 2 3 4          # OK -2
build/bin/det2_cli 32768 0 0 1      # INVALID_INPUT 0
python3 -B reference/oracle.py 1 2 3 4
```

Malformed CLI arguments return PARSE_ERROR 0 and nonzero exit status; they are a CLI transport error, not a mathematical result. Python oracle test cases reject bool/float inputs rather than pretending they are matrix elements.

## Assurance and nonclaims

- A specification postcondition is **not** an independent proof of mathematical intent; pinned regression AS-FOUNDATION-001 must reject the a*b-c*d mutation.
- A successful Python-only oracle test does **not** establish Ada functional correctness.
- GNATprove may prove the scoped Ada function's contracts only after a real run. No AoRTE, source compilation, cross-language equivalence or ABI guarantees are claimed beforehand.
- No source-level C ABI, pointer marshaling, Rust/GTK4 frontend or proof-assistant experiments are part of AS-001.
- The CLI is intentionally outside SPARK_Mode and uses standard Ada text/command-line libraries.

## Evidence reporting

Record separate statuses for Python oracle checks, Ada compilation, differential integration, and GNATprove. Capture exact git head, tool versions, OS, commands, exit status, observed tests, proved/unproved obligations, and logs. Do not mark AS-FOUNDATION-001 closed until an actual compiled Ada test matches the independent oracle and the negative mutation is detected.
