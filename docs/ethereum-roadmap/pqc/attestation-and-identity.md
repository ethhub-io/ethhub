---
title: Attestation and Identity Migration - EthHub

description: Migration patterns for identity attestation signatures during post-quantum transition.
---

## Attestation and Identity Migration

### Scope

This page describes how to migrate attestation signature schemes with minimal trust regression and clear operational controls.

### Core migration model

1. Keep compatibility mode available during transition.
2. Add post-quantum-capable signature mode for new attestations.
3. Bind signature mode metadata into signed payloads.
4. Enforce anti-replay controls for stateful signature systems.

### Why metadata binding matters

If mode and signature metadata are not part of the signed digest, attackers can attempt metadata substitution without changing the signed payload bytes.

Required binding fields should include:

1. Signature algorithm identifier.
2. Signature index or sequence marker when stateful signing is used.
3. Key identifier used to verify the signature.

### State management requirements

For stateful signature families, operations must enforce:

1. Monotonic signature index progression.
2. Replay rejection for previously seen indices.
3. Durable persistence of latest accepted index.
4. Recovery procedures for index desynchronization events.

### Migration plan

1. Introduce algorithm mode negotiation in validators and verifiers.
2. Add observability for verification failures by algorithm and reason.
3. Run shadow verification for the new mode before hard cutover.
4. Switch default issuance to the new mode.
5. Decommission compatibility mode after stability window.

### Failure handling

1. If verification failures increase, first determine if cause is mode mismatch, key distribution lag, or state index drift.
2. Prefer temporary policy relaxation only with time-bounded controls and incident tracking.

### Operator checklist

1. Confirm deterministic key loading or documented key lifecycle process.
2. Confirm replay protection tests pass under restart and failover scenarios.
3. Confirm monitoring includes per-mode success and failure counters.
4. Confirm emergency policy override is auditable and access-controlled.

### Resources

- [NIST Post-Quantum Cryptography project](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [PQC Source Map](source-map.md)

### Related

- [PQC Overview](overview.md)
- [Dual-Signature Migration](dual-signature-migration.md)
- [PQC Source Map](source-map.md)
