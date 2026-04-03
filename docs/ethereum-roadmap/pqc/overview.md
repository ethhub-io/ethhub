---
title: Post-Quantum Readiness Overview - EthHub

description: A practical plan for documenting and evaluating post-quantum migration patterns in the Ethereum ecosystem.
---

## Post-Quantum Readiness Overview

## Summary

This section documents practical post-quantum cryptography (PQC) migration patterns in a neutral, source-cited format.

It is not protocol-level Ethereum guidance by default. Instead, it is an operator and ecosystem research track that can be updated as standards, libraries, and deployments evolve.

## Concrete Integration Plan for EthHub

### Phase 1 (start now)

1. Define a PQC docs track in the roadmap section.
2. Add a source map that classifies each external claim.
3. Add core glossary terms (PQC, KEM, ML-KEM, ML-DSA, XMSS).

### Phase 2 (available pages)

1. [Hybrid transport migration](hybrid-kex-patterns.md) (classical + PQ KEX patterns).
2. [Identity and attestation migration patterns](attestation-and-identity.md).
3. [Dual-signature account migration and replay protection](dual-signature-migration.md).
4. [Operations checklist with rollout and rollback gates](operational-readiness.md).

## PQC Page Registry

| Page | Owner | Review cadence | Status |
| --- | --- | --- | --- |
| [PQC Overview](overview.md) | EthHub contributors | Quarterly | Active |
| [Ethereum PQC Readiness Playbook](ethereum-pqc-readiness-playbook.md) | EthHub contributors | Quarterly | Active |
| [Hybrid Transport Migration](hybrid-kex-patterns.md) | EthHub contributors | Quarterly | Active |
| [Attestation and Identity Migration](attestation-and-identity.md) | EthHub contributors | Quarterly | Active |
| [Dual-Signature Migration](dual-signature-migration.md) | EthHub contributors | Quarterly | Active |
| [Operational Readiness Checklist](operational-readiness.md) | EthHub contributors | Quarterly | Active |
| [PQC Source Map](source-map.md) | EthHub contributors | Quarterly | Active |

### Phase 3 (maintenance policy)

1. Add review timestamps on each source-backed claim.
2. Mark each claim with one of:
   - `Proposed`
   - `Experimental`
   - `Production-used`
   - `Ethereum-core-adopted`
3. Re-validate external links and statuses every quarter.

## Why this approach is the best fit for this repository

1. EthHub is documentation-first, so educational integration is low-risk and high-value.
2. It avoids importing stack-specific defaults that may not generalize.
3. It preserves neutrality by clearly separating external implementation claims from Ethereum core decisions.
4. It creates a durable path to track progress as NIST-standardized and ecosystem-specific PQC primitives mature.

## Case Study Input: Sovereign-Mohawk-Proto

As one external case study, the Sovereign-Mohawk-Proto repository currently describes a migration model centered on:

1. Hybrid transport key exchange profiles.
2. Attestation signature mode selection.
3. Digest-first dual-signature migration flows.
4. Operational readiness and rotation drills.

EthHub should treat this as an implementation example, not a normative baseline, and present it with clear source links and status labels in the [PQC Source Map](source-map.md).

## Editorial Guardrails

1. No verbatim code import from external repositories.
2. Prefer conceptual diagrams, process descriptions, and checklists.
3. Require at least one primary source link per major claim.
4. Explicitly note when a mechanism is compatibility-mode rather than full post-quantum signing.

## Resources

- [Ethereum upgrades](https://ethereum.org/en/upgrades/)
- [Ethereum consensus specs](https://github.com/ethereum/consensus-specs)
- [NIST Post-Quantum Cryptography project](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [PQC Source Map](source-map.md)

## Related

- [Ethereum PQC Readiness Playbook](ethereum-pqc-readiness-playbook.md)
- [Ethereum Upgrades](../ethereum-2.0/eth-2.0-phases.md)
- [Privacy](../privacy.md)
- [PQC Source Map](source-map.md)
