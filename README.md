# AERO-SWEEP

**No missed intersections. No silent overflow. No unverified assumptions.**

AERO-SWEEP is a proposed deterministic geometric and numerical kernel, implemented in **SPARK Ada** and exposed through a narrow, versioned **C99-compatible API**. **IMPULSE/** is its planned native **Rust/GTK4** mathematical and collision-visualization workbench.

**Project state: AS-001 implementation candidate.** A headless SPARK Ada determinant, independent Python reference and differential-test harness are now proposed. The Ada build and GNATprove proof status must be checked from actual run evidence; no ABI or GUI is implemented.

## Scope

- Exact bounded 2×2 determinants and geometric predicates.
- Robust line/segment intersection and continuous **time-of-impact**, distinguishing spatial path crossing from simultaneous contact.
- Later: collision impulse response, with physical assumptions and validation explicitly documented.
- Independent mathematical specifications in Lean 4, Agda, and Rocq; SPARK contracts/GNATprove for the actual Ada implementation.
- Reproducible tests against an independently derived arbitrary-precision Python standard-library reference.
- Headless kernel usable without the optional IMPULSE UI.

## Planned monorepo

```text
AERO-SWEEP/
├── kernel/                 # SPARK Ada bounded det2 kernel (AS-001)
├── abi/                    # C99 interface and Ada exports (planned)
├── IMPULSE/                # Native Rust/GTK4 workbench (planned)
├── verification/           # Lean 4, Agda, Rocq and SPARK evidence (planned)
├── reference/              # Independent Python exact det2 oracle (AS-001)
├── tests/                  # Headless/differential tests (AS-001); ABI later
├── evidence/               # Immutable test/proof receipts (planned)
├── docs/                   # Authoritative design and development policy
├── AGENTS.md
├── LICENSE
└── README.md
```

`IMPULSE/`, `abi/`, `verification/` and `evidence/` remain planned. AS-001 adds kernel, headless CLI, oracle and tests without introducing the future C ABI.

## Read first

- [Architecture](docs/ARCHITECTURE.md)
- [Mathematical specification](docs/MATHEMATICS.md)
- [Invariants and contracts](docs/INVARIANTS.md)
- [Proposed C ABI](docs/ABI_CONTRACT.md)
- [Verification plan](docs/VERIFICATION.md)
- [Threat and failure model](docs/THREAT_MODEL.md)
- [Development roadmap](docs/ROADMAP.md)
- [Design decisions](docs/DECISIONS.md)
- [AS-001 build, test and assurance status](docs/AS001_IMPLEMENTATION.md)
- [AS-FOUNDATION-001 adversarial finding](docs/FOUNDATION_FINDINGS.md)
- [Agent protocol](AGENTS.md)

## Engineering rules

Correctness outranks speed; bounded, explicit behaviour outranks silent approximation. No external services or unnecessary build dependencies. Keep the kernel headless, do not let the GUI compute authoritative answers, and report **executed vs inferred** evidence separately. Changes to the mathematical definition or ABI require reviewed contract updates before code changes.

**License:** Mozilla Public License 2.0 (see LICENSE). **Qualification:** no claim of aerospace certification or flight suitability. The name reflects rigorous engineering ambitions, not an achieved assurance level.

## AS-001 headless development

```sh
make test-oracle      # Python standard-library oracle tests only
make build            # requires GPRbuild and GNAT Ada; compiles CLI
make test-differential # requires compiled Ada CLI; cross-checks oracle
make prove            # requires GNATprove; inspect proof obligations
```

No C99 ABI, Rust/GTK4 app, collision solver, or completed cross-language proof is delivered by AS-001.
