# Sharding

## The Scalability Trilemma

The Scalability Trilemma claims that blockchain systems can only at most have two of the following three properties:

* Decentralization (defined as the system being able to run in a scenario where each participant only has access to O(c) resources, i.e. a regular laptop or small VPS)

* Scalability (defined as being able to process many transactions)

* Security (defined as being secure against attackers with up to O(n) resources)

The key challenge of scalability is finding a way to achieve all three at the base layer of a blockchain - Sharding is one such approach to this challenge.

## What is sharding?

Currently, in all blockchain protocols each node stores the entire state (account balances, contract code and storage, etc.) and processes all transactions. This provides a large amount of security, but greatly limits scalability: a blockchain cannot process more transactions than a single node can. In large part because of this, Bitcoin is limited to ~3-7 transactions per second, Ethereum to 7-15, etc.

However, this poses a question: are there ways to create a new mechanism, where only a small subset of nodes verifies each transaction? As long as there are sufficiently many nodes verifying each transaction that the system is still highly secure, but a sufficiently small percentage of the total validator set that the system can process many transactions in parallel, could we not split up transaction processing between smaller groups of nodes to greatly increase a blockchain's total throughput?

## What is the basic idea behind sharding?

We split the state and history of Ethereum up into partitions that we call “shards”. For example, a sharding scheme on Ethereum might put all addresses starting with 0x00 into one shard, all addresses starting with 0x01 into another shard, etc. In the simplest form of sharding, each shard also has its own transaction history, and the effect of transactions in some shard are limited to the state of shard of that same shard. One simple example would be a multi-asset blockchain, where there are many shards and each shard stores the balances and processes the transactions associated with one particular asset. In more advanced forms of sharding, some form of cross-shard communication capability, where transactions on one shard can trigger events on other shards, is also included.

#### Resources: https://github.com/ethereum/wiki/wiki/Sharding-FAQs
