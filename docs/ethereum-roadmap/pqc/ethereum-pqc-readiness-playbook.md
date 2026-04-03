---
title: Ethereum PQC Readiness Playbook - EthHub

description: A practical, phased playbook for Ethereum ecosystem teams to prepare for post-quantum cryptography migration.
---

## Ethereum PQC Readiness Playbook

## Scope

This playbook is for Ethereum ecosystem teams, including client teams, L2s, wallets, infra operators, custodians, and application operators.

It is not an announcement that Ethereum core protocol has fully migrated to PQC. It is a practical execution guide for staged readiness.

## Target outcomes

1. Minimize cryptographic migration risk without disrupting availability.
2. Define measurable gates for transport, identity, and signing migration.
3. Keep ecosystem guidance aligned with standards and audited evidence.

## Readiness phases

### Phase A: Inventory and risk classification

#### Dependency inventory by layer

1. Transport handshake and session setup.
2. Validator and service identity mechanisms.
3. User key and transaction signing paths.
4. Bridge and interop proofs.

#### Upgrade complexity classes

1. Config-only changes.
2. Library and runtime changes.
3. Protocol-level changes requiring broad coordination.

#### Asset exposure priority

1. Hot-path custody and signing systems.
2. Infrastructure trust anchors.
3. Long-term data confidentiality and archives.

### Phase B: Hybridization and telemetry

1. Introduce hybrid key-establishment where appropriate.
2. Add signature-mode migration controls for identity and attestations.
3. Add digest-first migration APIs for dual-signature transitions.
4. Add per-mode telemetry and migration-specific SLO dashboards.

### Phase C: Cutover preparedness

1. Define migration epochs and enforcement windows.
2. Define rollback ownership and emergency controls.
3. Run chaos drills for mode mismatch, replay pressure, and verifier failure.
4. Require go-live evidence packages before strict enforcement.

### Phase D: Enforcement and deprecation

1. Enforce post-epoch cryptographic controls.
2. Disable legacy-only compatibility paths after observation window.
3. Publish post-cutover incident and performance reports.
4. Track removal of technical debt and temporary bypasses.

## Role-based checklist

### Client and protocol teams

1. Publish migration-impact notes for consensus and execution clients.
2. Define compatibility windows and version-negotiation behavior.
3. Add tests for malformed algorithm labels and downgrade attempts.

### Wallets and custody systems

1. Define migration UX for key rotation and account continuity.
2. Require explicit anti-replay and idempotency controls for migrations.
3. Add user-facing warnings for non-compliant signing flows.

### Infrastructure and operators

1. Run staged KEX and attestation migration drills.
2. Track p95 latency and failure modes during rolling upgrades.
3. Validate backup and restore for stateful signing metadata.

### Application teams

1. Avoid hard-coding algorithm assumptions in app-layer logic.
2. Support migration-safe retries and deterministic signing payloads.
3. Expose migration status and safety checks in admin surfaces.

## Exit criteria for "PQC-ready" in this documentation context

### Policy

1. Published policy profiles for transport, identity, and migration cutover.

### Evidence

1. Reproducible evidence artifacts for drills and go-live gates.

### Security

1. Verified anti-replay, downgrade resistance, and rollback controls.

### Operations

1. On-call runbooks and incident playbooks updated for PQC failure modes.

### Governance

1. Quarterly review cadence active, source map current, stale claims removed.

## Important limitation

Within this repository, "complete making eth pqc ready" means complete documentation readiness and ecosystem migration guidance.

Actual protocol and production readiness requires coordinated implementation across Ethereum clients, wallets, infrastructure providers, and standards bodies.

## Resources

- [Ethereum upgrades](https://ethereum.org/en/upgrades/)
- [Ethereum consensus specs](https://github.com/ethereum/consensus-specs)
- [NIST Post-Quantum Cryptography project](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [PQC Source Map](source-map.md)

## Related

- [PQC Overview](overview.md)
- [Hybrid Transport Migration](hybrid-kex-patterns.md)
- [Attestation and Identity Migration](attestation-and-identity.md)
- [Dual-Signature Migration](dual-signature-migration.md)
- [Operational Readiness Checklist](operational-readiness.md)
- [PQC Source Map](source-map.md)
