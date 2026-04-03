---
title: Is Ethereum Quantum-Safe? - EthHub

description: What quantum risk means for Ethereum today and what post-quantum readiness work is needed next.
---

## Is Ethereum Quantum-Safe?

Not fully today in an absolute sense.

Ethereum and its ecosystem currently rely on cryptographic components that were not originally designed as full post-quantum replacements. At the same time, there is active work on migration strategies and readiness planning.

## What this means in practice

1. Quantum risk is a forward-looking security concern, not a single switch flip.
2. Readiness is a phased process across transport, identity, and signing systems.
3. Different parts of the stack will migrate at different speeds.

## What "ready" should include

1. Hybrid transport migration with observability and rollback controls.
2. Identity and attestation migration plans with anti-replay protections.
3. Dual-signature migration paths for sensitive account transitions.
4. Operational cutover runbooks, drills, and evidence-based go-live gates.

## Where to follow EthHub guidance

- [Ethereum PQC Readiness Playbook](../ethereum-roadmap/pqc/ethereum-pqc-readiness-playbook.md)
- [PQC Overview](../ethereum-roadmap/pqc/overview.md)
- [Operational Readiness Checklist](../ethereum-roadmap/pqc/operational-readiness.md)
- [PQC Source Map](../ethereum-roadmap/pqc/source-map.md)

## References

- [Ethereum upgrades](https://ethereum.org/en/upgrades/)
- [Ethereum consensus specs](https://github.com/ethereum/consensus-specs)
- [NIST Post-Quantum Cryptography project](https://csrc.nist.gov/projects/post-quantum-cryptography)
