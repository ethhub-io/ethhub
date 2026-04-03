---
title: PQC Source Map - EthHub

description: Source-indexed map of post-quantum migration claims used in this documentation track.
---

## PQC Source Map

## How to read this page

Each item maps an external claim to a source and status tag.

Status tags:

- `Proposed`: design intent or plan
- `Experimental`: implemented but early or compatibility-focused
- `Production-used`: used in deployed systems (non-Ethereum-core)
- `Ethereum-core-adopted`: part of accepted Ethereum protocol path

## External case-study sources (Sovereign-Mohawk-Proto)

| Topic | Claim Summary | Status | Source |
| --- | --- | --- | --- |
| Hybrid transport KEX | Describes default use of hybrid x25519 + ML-KEM-768 transport mode. | Proposed | [README.md](https://github.com/rwilliamspbg-ops/Sovereign-Mohawk-Proto/blob/main/README.md) |
| Attestation signature mode | Documents XMSS-mode identity attestation and mode switching controls. | Experimental | [SPRINT_PQC_BUILD_LOCAL.md](https://github.com/rwilliamspbg-ops/Sovereign-Mohawk-Proto/blob/main/SPRINT_PQC_BUILD_LOCAL.md) |
| Migration flow | Documents digest-first dual-signature migration payloads and controls. | Experimental | [pqc_migration_payload_cli.py](https://github.com/rwilliamspbg-ops/Sovereign-Mohawk-Proto/blob/main/scripts/pqc_migration_payload_cli.py) |
| API surface for migration | Exposes migration digest + migrate endpoints with legacy and PQC signature fields. | Experimental | [RELEASE_NOTES_PQC_OVERHAUL.md](https://github.com/rwilliamspbg-ops/Sovereign-Mohawk-Proto/blob/main/RELEASE_NOTES_PQC_OVERHAUL.md) |
| Rotation drill | Includes staged KEX rotation drill script for rolling restarts. | Experimental | [quantum_kex_rotation_drill.sh](https://github.com/rwilliamspbg-ops/Sovereign-Mohawk-Proto/blob/main/scripts/quantum_kex_rotation_drill.sh) |
| Runtime profile defaults | Defines environment defaults for transport mode, attestation mode, and migration epoch controls. | Proposed | [mainnet_one_click.sh](https://github.com/rwilliamspbg-ops/Sovereign-Mohawk-Proto/blob/main/scripts/mainnet_one_click.sh) |

## Ethereum status notes

At time of writing, the above sources are implementation-specific and should not be interpreted as `Ethereum-core-adopted` by default.

For Ethereum protocol roadmap context, see:

- [consensus-specs](https://github.com/ethereum/consensus-specs)
- [Ethereum upgrades](https://ethereum.org/en/upgrades/)

## Review metadata

- Last reviewed: 2026-04-03
- Reviewer: EthHub contributors
- Next review target: 2026-07-03

## Related

- [PQC Overview](overview.md)
- [Ethereum PQC Readiness Playbook](ethereum-pqc-readiness-playbook.md)
- [Hybrid Transport Migration](hybrid-kex-patterns.md)
- [Attestation and Identity Migration](attestation-and-identity.md)
- [Dual-Signature Migration](dual-signature-migration.md)
- [Operational Readiness Checklist](operational-readiness.md)
