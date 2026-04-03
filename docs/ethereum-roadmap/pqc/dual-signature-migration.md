---
title: Dual-Signature Migration - EthHub

description: Digest-first dual-signature migration pattern for moving accounts from legacy to post-quantum controls.
---

## Dual-Signature Migration

### Scope

This page covers migration flows where a transfer or account move must be authorized by both a legacy signature and a post-quantum signature during a transition period.

### Digest-first workflow

Use deterministic signing payloads and canonical serialization before signatures are generated.

Recommended flow:

1. Build normalized payload fields.
2. Serialize in canonical format.
3. Compute a digest over canonical bytes.
4. Obtain legacy and PQ signatures over that digest.
5. Submit one migration request containing payload and both signature bundles.

### Minimal payload fields

1. Legacy account identifier.
2. PQ account identifier.
3. Asset symbol and amount in base units.
4. Nonce.
5. Optional idempotency key.
6. Optional memo.

### Security controls

#### Replay protection

1. Reject duplicate nonce per source account.
2. Optionally bind nonce scope to asset and destination.

#### Idempotency

1. Allow safe retries by keying on an idempotency token.
2. Return same result for identical repeated requests.

#### Algorithm policy

1. Validate that submitted algorithms are in allowed policy set.
2. Reject unknown or deprecated algorithm labels.

#### Epoch cutover

1. Define a migration epoch after which cryptographic signatures are mandatory.
2. Reject boolean or placeholder approval flags after cutover.

### Migration timeline template

#### Preparation window

1. Enable digest endpoint and client tooling.
2. Publish signing reference vectors.

#### Parallel window

1. Accept both legacy and dual-signature submissions where policy allows.
2. Encourage migration traffic toward dual-signature path.

#### Enforcement window

1. Require cryptographic dual-signature fields.
2. Optionally lock legacy-only transfers for migrated accounts.

### Testing requirements

1. Cross-language digest consistency tests.
2. Negative tests for malformed keys and signature length mismatches.
3. Replay and idempotency race-condition tests.
4. Post-cutover policy rejection tests.

### Resources

- [NIST Post-Quantum Cryptography project](https://csrc.nist.gov/projects/post-quantum-cryptography)
- [PQC Source Map](source-map.md)

### Related

- [PQC Overview](overview.md)
- [Attestation and Identity Migration](attestation-and-identity.md)
- [Operational Readiness Checklist](operational-readiness.md)
- [PQC Source Map](source-map.md)
