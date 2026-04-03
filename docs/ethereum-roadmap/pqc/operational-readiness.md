---
title: Operational Readiness Checklist - EthHub

description: Operator checklist for safe post-quantum migration rollout, enforcement, and rollback.
---

## Operational Readiness Checklist

### Purpose

Use this checklist before enabling PQC-related enforcement in production environments.

### 1. Policy and configuration

1. Document active transport mode policy and allowed fallback behavior.
2. Document identity attestation mode policy and verification requirements.
3. Document migration epoch and post-epoch enforcement rules.
4. Confirm all policy changes are versioned and peer-reviewed.

### 2. Observability

1. Handshake success and failure metrics are available by mode.
2. Attestation verification metrics are available by algorithm and reason.
3. Migration API metrics capture digest requests, submission success, replay rejections, and idempotent retries.
4. Dashboards include p95 latency and error budget burn rate.

### 3. Testing and drills

1. Run staged KEX rotation drill with one-service-at-a-time restart sequencing.
2. Run replay and nonce collision tests under concurrent load.
3. Run dual-signature malformed-input tests.
4. Run failover and restart tests for stateful signature index persistence.

### 4. Security controls

1. Access to enforcement toggles is role-gated and audited.
2. Emergency rollback controls are documented and tested.
3. Key material handling procedures are documented and validated.
4. Incident response runbook includes migration-specific failure modes.

### 5. Go-live gates

1. Baseline and migration-period SLOs are explicitly defined.
2. Canary rollout has passed for a minimum observation window.
3. Production-readiness artifacts are generated and reviewed.
4. Cutover decision has named approvers and rollback owner.

### 6. Post-go-live monitoring

1. Track mode mismatch spikes and convergence time.
2. Track migration backlog and completion ratio.
3. Track policy bypass attempts or unexpected fallback usage.
4. Schedule formal post-mortem for any rollback event.

### Quarterly review template

1. Review source-map statuses and update any stale claim labels.
2. Re-validate external references and implementation assumptions.
3. Re-run migration drills and capture new evidence artifacts.
4. Update this checklist with lessons learned.

### Resources

- [Ethereum upgrades](https://ethereum.org/en/upgrades/)
- [PQC Source Map](source-map.md)

### Related

- [Ethereum PQC Readiness Playbook](ethereum-pqc-readiness-playbook.md)
- [PQC Overview](overview.md)
- [Hybrid Transport Migration](hybrid-kex-patterns.md)
- [Dual-Signature Migration](dual-signature-migration.md)
- [PQC Source Map](source-map.md)
