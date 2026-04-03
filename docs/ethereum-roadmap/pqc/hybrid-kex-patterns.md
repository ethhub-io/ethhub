---
title: Hybrid Transport Migration - EthHub

description: Practical migration patterns for classical-plus-post-quantum transport key exchange in distributed systems.
---

## Hybrid Transport Migration

### Scope

This page covers practical rollout patterns for migrating transport key exchange from classical-only modes to hybrid modes that combine classical and post-quantum primitives.

### Why hybrid first

1. It preserves compatibility with existing systems while introducing quantum-resistant components.
2. It reduces migration risk compared with immediate classical removal.
3. It gives operators measurable transition milestones.

### Reference pattern

A common staged pattern is:

1. Baseline mode: classical-only key exchange.
2. Transition mode: hybrid key exchange enabled in policy and negotiation.
3. Enforcement mode: reject non-compliant handshakes after migration window.

### Implementation checklist

1. Define explicit KEX policy values and allowed combinations.
2. Validate keyshare metadata and expected size ranges at runtime.
3. Add strict mode mismatch handling with clear error telemetry.
4. Add health metrics for handshake success, latency, and rejection causes.
5. Define rollback toggles that can be activated without full redeploy.

### Rollout plan

#### Canary

1. Enable hybrid mode on a small, low-risk service subset.
2. Compare handshake failure ratios and p95 latency against baseline.

#### Rolling migration

1. Move one service group at a time.
2. Keep mixed-mode windows short to reduce mismatch churn.

#### Enforcement

1. Set policy to require hybrid mode after readiness criteria pass.
2. Alert on any non-hybrid negotiation attempt.

### Rollback criteria

Trigger rollback if any of the following occur for sustained periods:

1. Handshake failure ratio exceeds agreed SLO threshold.
2. Latency regression exceeds migration budget without stabilization.
3. Service-level error budgets are consumed faster than planned.

### Metrics to track

1. Handshake success rate by mode.
2. Handshake latency p50 and p95.
3. Mode mismatch rejections.
4. Connection retry volume.
5. End-to-end service availability during rolling restarts.

### Operator notes

1. Hybrid transport migration is operationally sensitive because both peers must agree on mode and metadata expectations.
2. If mismatch errors spike during rolling changes, finishing the rollout quickly can reduce prolonged mixed-mode instability.

### Resources

- [NIST Post-Quantum Cryptography project](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [PQC Source Map](source-map.md)

### Related

- [PQC Overview](overview.md)
- [Operational Readiness Checklist](operational-readiness.md)
- [PQC Source Map](source-map.md)
