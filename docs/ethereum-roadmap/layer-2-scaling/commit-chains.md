title: Commit-Chains  - EthHub

description: Commit-chains a layer 2 scaling solution for Ethereum.

# Commit-Chains

## What are commit-chains?

Commit-chains are the more generic term for what is also called Plasma for Ethereum blockchain. 

Vitalik Buterin has jokingly said, 
*"Commit chains" is more on-brand for bitcoin whereas "plasma" is more on-brand for ethereum.*

Commit-chains, also sometimes described as non-custodial side chains, don’t introduce a new consensus mechanism like side chains, they rely on the parent-blockchain consensus, which makes them as safe as the parent-blockchain itself. 

In commit-chains, untrusted and non-custodial operator facilitates the communication between transacting parties. The operator is expected to commit the state of user account balances by sending periodic updates to the parent-blockchain.

## How commit-chains work?

![](https://i.imgur.com/9ekBVjB.png)

Unlike payment channels, commit-chains are on an always ongoing state once launched and don’t rely on a three-state - opening, live, dispute/closure - model.

After an operator launches a commit-chain, users can join and conduct transactions that are recorded on the commit-chain while keeping the freedom to withdraw or exit their assets to the parent-blockchain at any time.

### Periodic Checkpoint Commitments

Commit-chain users may need to periodically observe on-chain checkpoint commitments, which can be instantiated as a Merkle tree root or Zero-Knowledge Proof (ZKP). 

While ZKPs enforce consistent state transitions on-chain, Merkle root commitments do not, requiring users to participate in challenge-response protocols to challenge operator misbehavior.

### Data Availability Requirement

Data availability requirement means users must retrieve and maintain data required to exit a commit-chain since data isn’t broadcasted. 

Depending on the implementation, if the data is unavailable, you are either forced to exit, like in Plasma or the operator can be challenged to provide the necessary data, like in NOCUST. 

On misbehavior, users are allowed to exit with their last confirmed balance.

### Centralized but Untrusted Intermediary

The centralized operator never holds custody of funds so, in case of failure to be available, the worst-case scenario is that you’re just unable to make any further off-chain transactions, but users can exit and move to another commit-chain at any time.

### Transaction Finality
Unlike payment channels, the commit-chain operator does not require on-chain collateral to securely route payments between users.

Commit-chain transactions do not offer instant transaction finality like channels but offer eventual finality after an on-chain checkpoint. 

However, if an operator chooses to allocate collateral to each user, essentially implementing a payment channel on top of a commit-chain, instant transaction finality becomes possible.

### Reduced Routing Requirements
A single commit-chain can potentially host millions of users, so a few statically connected commit-chains are envisioned to spaw stable networks with low routing complexity. Atomic cross commit-chain transactions have not been proposed yet.

## Commit-chain security properties

The user-side security properties can be generalized as follows:

### Agreed transition

A commit-chain transaction is agreed by at least the sender and the commit-chain operator.

### Balance security

Honest users can always withdraw agreed balances from the commit-chain with an on-chain dispute.

Balance security is provided for honest users even if the operator and all other commit-chain users collude since transactions are only considered final when the sender and operator agree to the payment and it’s committed with the periodic on-chain checkpoint.

### State progression

User can anytime enforce an off-chain state transition on-chain.

### Commitment integrity

Since there isn’t a fixed 3-phase lifetime for a commit-chain, users of the commit-chain are able to verify the integrity of the operator’s commitments at any point in time and force the operator to seize operation and rollback to the previous periodic commitment.

## NOCUST commit-chain

### Overview

NOCUST commit-chain was first introduced by the team at [Liquidity Network](https://liquidity.network/) and their peers in the form of an [academic paper](https://eprint.iacr.org/2018/642.pdf).

NOCUST is an account-based commit-chain, where an on-chain address is associated to a commit-chain account.

The NOCUST on-chain contract expects to periodically receive a constant-sized commitment to the state of the commit-chain ledger from the operator, containing each user’s account in the
collateral pool.

### Free establishment

Users can deposit any amount of coins within the contract and perform commit-chain payment of any denomination towards other users and with free establishment, users can join the commit-chain without on-chain transaction by requesting an operator signature and immediately receive commit-chain transactions.

### Agreed transition

A transaction within NOCUST is enacted with the signature of the sender and the operator to deter potential double-spend scenarios.

### Instant transaction finality

State progression is only possible if the operator stakes collateral towards the recipient. NOCUST specifies a mechanism to allocate collateral towards all commit-chain users within a constant-size on-chain commitment, which enables instant transaction finality for specified amounts.

Allocated collateral is reusable after each on-chain checkpoint and at this point, the transaction throughput is only limited by the operator’s bandwidth and computational throughput, and independent of checkpoint commitment interval.

### Commitment integrity
Each user is only required to verify their own balance proof by requesting data from the operator and comparing it with their locally stored state at regular time intervals to observe integrity. 

In the case of misbehavior, a user can issue a challenge using the NOCUST smart contract. If the operator comes back with invalid information or does not respond, users have an accountable proof of misbehavior. 

NOCUST supports a provably consistent mode of operation through zkSNARKS. Layer two-state transitions will be validated by the underlying smart contract and the operator is unable to commit invalid state transition without being halted.

## Comparing commit-chains

Comparing NOCUST commit-chain with Plasma Cash, which is the most comprehensive working draft of Plasma implementation.

Comparison data is based on the [systemization of knowledge academic paper](https://eprint.iacr.org/2019/360.pdf) and sourced from discussions with Georgios Konstantopoulos.

| General properties              | Plasma Cash | NOCUST              |
|---------------------------------|-------------|---------------------|
| Security Proofs                 | ✕           | ✓                   |
| Offline transaction reception   | ✓           | ✓                   |
| Fungible payments               | ✕           | ✓                   |
| Clients can remain offline      | ✕           | ✕ (online each eon) |
| Safe mass exit                  | ✓           | ✓                   |
| Instant transaction finality    | ✕           | ✓ (with collateral) |
| Token support                   | ✓           | ✓                   |
| Non-fungible tokens             | ✓           | ✕                   |
| Provably consistent state (ZKP) | ✕           | ✓                   |
| Commit-chain swaps              | ✕           | ✓                   |

Plasma is a UTXO-based commit-chain when NOCUST is account-based. 

In Plasma Cash, a coin is minted with an on-chain deposit and cannot be merged or split with another coin on the commit-chain, hence it is useful for non-fungible tokens, but not practical as a payment system.

NOCUST uses ZKPs to enforce consistent state transitions on-chain, Plasma Cash uses Merkle root commitments, which do not and require users to participate in challenge-response protocols to challenge operator misbehavior.

## Resources
* [Commit-Chains: Secure, Scalable Off-Chain Payments Academic Paper](https://eprint.iacr.org/2018/642.pdf)
* [Systemization of Knowledge: Off The Chain Transactions Academic Paper](https://eprint.iacr.org/2019/360.pdf)
* [Liquidity Network Research Papers](https://liquidity.network/research)
