# AERO-SWEEP

**No missed intersections. No silent overflow. No unverified assumptions.**

AERO-SWEEP is a proposed deterministic geometric and numerical kernel, implemented in **SPARK Ada** and exposed through a narrow, versioned **C99-compatible API**. **IMPULSE/** is its planned native **Rust/GTK4** mathematical and collision-visualization workbench.

**Project state: AS-000, design and contract documentation only.** No computational kernel, verified proofs, ABI implementation, or GUI is supplied by this documentation milestone. Do not infer correctness, tool execution, certification, or performance from design documents.

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
├── kernel/                 # SPARK Ada numerical authority (planned)
├── abi/                    # C99 interface and Ada exports (planned)
├── IMPULSE/                # Native Rust/GTK4 workbench (planned)
├── verification/           # Lean 4, Agda, Rocq and SPARK evidence (planned)
├── reference/              # Independent Python exact oracle (planned)
├── tests/                  # Boundary, adversarial, ABI, differential (planned)
├── evidence/               # Immutable test/proof receipts (planned)
├── docs/                   # Authoritative design and development policy
├── AGENTS.md
├── LICENSE
└── README.md
```

The planned subdirectories above **do not exist yet**; AS-000 deliberately creates documentation only.

## Read first

- [Architecture](docs/ARCHITECTURE.md)
- [Mathematical specification](docs/MATHEMATICS.md)
- [Invariants and contracts](docs/INVARIANTS.md)
- [Proposed C ABI](docs/ABI_CONTRACT.md)
- [Verification plan](docs/VERIFICATION.md)
- [Threat and failure model](docs/THREAT_MODEL.md)
- [Development roadmap](docs/ROADMAP.md)
- [Design decisions](docs/DECISIONS.md)
- [AS-FOUNDATION-001 adversarial finding](docs/FOUNDATION_FINDINGS.md)
- [Agent protocol](AGENTS.md)

## Engineering rules

Correctness outranks speed; bounded, explicit behaviour outranks silent approximation. No external services or unnecessary build dependencies. Keep the kernel headless, do not let the GUI compute authoritative answers, and report **executed vs inferred** evidence separately. Changes to the mathematical definition or ABI require reviewed contract updates before code changes.

**License:** Mozilla Public License 2.0 (see LICENSE). **Qualification:** no claim of aerospace certification or flight suitability. The name reflects rigorous engineering ambitions, not an achieved assurance level.
