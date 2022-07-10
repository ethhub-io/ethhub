---
title: ZK-Rollups - Ethhub

description:  ZK-Rollups are a type of layer 2 construction that runs on top of the Ethereum to improve scalability.
---

# ZK-Rollups

## Background

Plasma is a construction scalability method that places layer 2 blocks on top of the Ethereum blockchain in the form of a side chain.  The implementation of Plasma enables hundreds of side chain transactions to be processed offline with only a single hash of the side chain block being added to the Ethereum blockchain.  Fundamental flaws exist preventing further scalability.  An exit game must be played for a user to withdraw from the side chain which requires side chain users to retain a high amount of data so that enough exists for validation.  Also, a lengthy challenge period requires users to stay online or lose their rewards.  More user friendly and less resource intensive solutions are in development to improve layer 2 scalability.

## Introduction

ZK-Rollups are one layer 2 construction option that increases scalability through mass transfer processing rolled into a single transaction.  Where Plasma creates one transaction per transfer, ZK-Rollups bundle hundreds of transfers into a single transaction.  The smart contract will deconstruct and verify all of the transfers held in a single transaction.

A "zero knowledge proof" approach is used to present and publicly record the validity of the block on the Ethereum blockchain.  ZK reduces computing and storage resources for validating the block by reducing the amount of data held in a transaction. Zero knowledge of the entire data is needed.  

## Simple Overview

The ZK-Rollup scheme consists of two types of users:  transactors and relayers.  Transactors create their transfer and broadcast the transfer to the network.  The transfer data consists of an indexed "to" and  "from" address, a value to transact, the network fee, and nonce. A shortened 3 byte indexed version of the addresses reduces processing resource needs.  The value of the transaction being greater than or less than zero creates a deposit or withdrawal respectively.  The smart contract records the data in two Merkle Trees; addresses in one Merkle Tree and transfer amounts in another.

Relayers collect a large amount of transfers to create a rollup.  It is the relayers job to generate the SNARK proof.  The SNARK proof is a hash that represents the delta of the blockchain state.  State refers to "state of being."  SNARK proof compares a snapshot of the blockchain before the transfers to a snapshot of the blockchain after the transfers (i.e. wallet values) and reports only the changes in a verifiable hash to the mainnet.  

It is worth noting that anyone can become a relayer so long as they have staked the required bond in the smart contract.  This incentivises the relayer not to tamper with or withhold a rollup.

## User Experience

Users on a dapp running the ZK-Rollup scheme will pay less in transaction fees.  Creating zero knowledge proofs requires a large amount of computing power.  The implementation is proposed to be a "commit-verify" approach.  The latency to block confirmation will increase because the SNARK proof will be delayed by a number of blocks.  How this will affect users will not be known until implementation.

## Pros/Cons

Pros:

* Reduced fees per user transfer
* Faster than Optimistic Rollup and Plasma
* Blocks will be computed in a parallel computing model which encourages decentralization
* Less data contained in each transaction increases throughput and scalability of layer 2
* Does not require a fraud game verification like Optimistic Rollup, which can delay withdrawals by up to two weeks

Cons:

* The difficulty in computing zero knowledge proof will require data optimization to get maximum throughput
* The initial set up of ZK-Rollups promotes a centralized scheme (see Security Considerations)
* The security scheme assumes a level of unverifiable trust
* Quantum computing poses a threat to hacking the blockchain

## Example

* [zkSync](https://zksync.io) is a ZK-Rollup live on Ethereum mainnet.
* [Scroll](https://scroll.io/) is a ZK-Rollup in active development.

## Security Considerations

The initial setup of ZK-Rollups is assumed to be a trusted state, when this trust cannot be proven.  A small group of developers will be subject matter experts on the initial trusted state.  This undermines decentralization and opens the risk of social engineering hacking attacks by convincing a developer to manipulate code or provide vulnerability information.

Quantum computing poses a threat to the ability of being able to crack ZK-Rollups due to the fact that a higher probability exists in being able to "guess" the correct SNARK proof hash than the current encryption protocol.

## Resources

* [Zero Knowledge Proof - Video Overview](https://youtu.be/0Sy6nb72gCk)
* [zkSNARKs in a nutshell](https://blog.ethereum.org/2016/12/05/zksnarks-in-a-nutshell/)
* [On-chain scaling to potentially ~500tx/sec through mass tx validation](https://ethresear.ch/t/on-chain-scaling-to-potentially-500-tx-sec-through-mass-tx-validation/3477)
* [ZK Rollup & Optimistic Rollup (En)](https://medium.com/coinmonks/zk-rollup-optimistic-rollup-70c01295231b)
* [On-chain scaling with full data availability.  Moving verification of chains off-chain?](https://ethresear.ch/t/on-chain-scaling-with-full-data-availability-moving-verification-of-transactions-off-chain/3847)
* [Moving verification of chains off-chain?](https://ethresear.ch/t/on-chain-scaling-with-full-data-availability-moving-verification-of-transactions-off-chain/3847)
