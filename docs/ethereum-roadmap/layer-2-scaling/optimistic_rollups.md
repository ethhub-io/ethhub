title: Optimistic Rollups - EthHub

description: Optimistic Rollups (ORs) are one type of layer 2 constructions that do not run on Ethereum's base layer but on top of it.

# Optimistic Rollups

## Introduction
Optimistic Rollups (ORs) are one type of layer 2 constructions that do not run on Ethereum's base layer but on top of it. This enables running smart contracts at scale while still being secured by Ethereum. These constructions resemble Plasma, but trade the almost infinite scalability of Plasma to run an EVM compatible Virtual Machine called OVM (Optimistic Virtual Machine) which enables ORs to run anything Ethereum can.

The name Optimistic Rollups originates from how the solution works. 'Optimistic' is used because aggregators publish only the bare minimum information needed with no proofs, assuming the aggregators run without commiting frauds, and only providing proofs in case of fraud. 'Rollups' is used because transactions are commited to main chain in bundles (that is, they are rolled-up).

## A Simple Overview
Much like most Layer-2 solutions, the funds transacted on Optimistic Rollups are stored in a smart-contract on Ethereum, where users deposit funds, aggregators sign up and fraud proofs are commited. The usual process one can interact with such solutions are as follows:

1. A user sends a deploy transaction of a smart contract off-chain to an aggregator (a block producer in this construction)

2. An aggregator locally deploys the transaction creating the new smart contract

3. That aggregator computes the new state root (aka a merkle root)

4. That aggregator creates an Ethereum transaction which contains that state root calculated in step 3

5. Any user that sees an aggregator deploying an invalid state root (a state root created by including invalid transactions) can challenge that aggregator by posting the valid state root along with the merkle proofs required to prove it, slashing (removing a portion of the bond) and the aggregator that commited such fraud and any that built blocks on top of the fraudulent one and claiming those rewards.

6. After an invalid block has been commited and a fraud proof is finalized, the chain in layer 2 can be rolled back and resume from the previous non-fraudelent block.

Note: Anyone can become an aggregator as long as they lock a bond in the smart contract.

Note 2: The front-running problem associated with step 5 can be solved by numerous methods, such as by using [submarine sends(https://libsubmarine.org/).

## User Experience
Any user that uses a Dapp that is deployed to a layer 2 with an Optimistic Rollup construction can enjoy economic abstraction (eg: fee-free transactions, pay with ERC-20, etc.) and quasi-instant transactions (transactions in the ball-park of 200ms, don't blink or you'll miss it!).

## Pros/Cons
Pros:
 * Flexibility in generalized Computation (Turing-complete / EVM compatible)
 * Increase in scalability (200 to 2000 transactions-per-second (tps) vs Ethereum layer 1's current 10 tps)
 * All Data is available on-chain (no need to trust off-chain data providers)
 * Better UX (as explained above)

Cons:
 * Limited Throughput when compared with some other Layer 2 solutions (Plasma, ZK Rollups, etc.)
 * Some additional security issues are raised (discussed below)

## Demo
A Uniswap-like exchange called Unipig was developed by both Uniswap and Plasma Group teams as a Proof of Concept application and demonstrated at Devcon5, which you can try for free at [unipig.exchange](unipig.exchange).

## Security Overview
For Optimistic Rollups to work, we must assume that there exists a honest majority of Ethereum validators (miners in Eth1, stakers in Eth2), and that there is at least one aggregator that is not censoring transactions.

## Resources

[Unipig](https://unipig.exchange)
[Plasma group forum](https://plasma.group/)
[ZK Rollups vs Optimistic Rollups](https://blog.idex.io/all-posts/rollup-rundown)
[Optimistic vs. ZK Rollup: Deep Dive](https://medium.com/matter-labs/optimistic-vs-zk-rollup-deep-dive-ea141e71e075)
