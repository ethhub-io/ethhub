title: Sharding on Ethereum - EthHub
description: Information on sharding and how it will work on Ethereum.

# Sharding

## Summary

There is a trilemma in blockchain systems that can be visualized in form of a triangle known as DCS triangle, what it conevys is "It is impossible to achieve all three Decentralization, Consistency, and Scalability simultaenously. A tradeoff is necessary \(you can choose any two but not all\)". 

![](/assets/images/dcs-triangle.png)

Sharding is an attempt to solve this challenge. It simply means partitioning large chains \(databases\) into smaller, faster ones hence making the entire system more scalable. How?
To solve scalability we split the state and history stored on main chain into shards. Each shard manages it's own shit, has it's own  transaction history, and the effect of transactions in some shard are limited to that shard only.

Examples for this would be:
* A dApp having a whole shard by himself so that all tx's related to it will be on that one shard only.
* Several dApps related to a particular domain will be on one single shard.

The later phases of ETH2.0 considers the possibility of cross-shard communications.

Sharding also introduces different types of nodes like "Light Node", "Super-Full Node" etc. depending upon how much data it downloads, how much it verifies. 

## The Scalability Trilemma

The Scalability Trilemma claims that blockchain systems can only at most have two of the following three properties:

* Decentralization \(defined as the system being able to run in a scenario where each participant only has access to O\(c\) resources, i.e. a regular laptop or small VPS\)
* Scalability \(defined as being able to process many transactions\)
* Security \(defined as being secure against attackers with up to O\(n\) resources\)

The key challenge of scalability is finding a way to achieve all three at the base layer of a blockchain - sharding is one such attempt at solving this challenge.

## What is sharding?

Currently, in all blockchain protocols each node stores the entire state \(account balances, contract code and storage, etc.\) and processes all transactions. This provides a large amount of security, but greatly limits scalability: a blockchain cannot process more transactions than a single node can. In large part because of this, Bitcoin is limited to ~3-7 transactions per second, Ethereum to 7-15, etc.

However, this poses a question: are there ways to create a new mechanism, where only a small subset of nodes verifies each transaction? As long as there are sufficiently many nodes verifying each transaction that the system is still highly secure, but a sufficiently small percentage of the total validator set that the system can process many transactions in parallel, could we not split up transaction processing between smaller groups of nodes to greatly increase a blockchain's total throughput?

## What is the basic idea behind sharding?

We split the state and history of Ethereum up into partitions that we call “shards”. For example, a sharding scheme on Ethereum might put all addresses starting with 0x00 into one shard, all addresses starting with 0x01 into another shard, etc. In the simplest form of sharding, each shard also has its own transaction history, and the effect of transactions in some shard are limited to the state of shard of that same shard. One simple example would be a multi-asset blockchain, where there are many shards and each shard stores the balances and processes the transactions associated with one particular asset. In more advanced forms of sharding, some form of cross-shard communication capability, where transactions on one shard can trigger events on other shards, is also included.
/
## What might a basic design of a sharded blockchain look like?

There exists a set of validators \(ie. proof of stake nodes\), who randomly get assigned the right to create shard blocks. During each slot \(eg. an 8-second period of time\), for each shard in \[0...999\] a random validator gets selected, and given the right to create a block on a shard, which might contain up to, say, 32 kb of data. Also, for each shard, a set of 100 validators get selected as attesters. The header of a block together with at least 67 of the attesting signatures can be published as an object that gets included in the "main chain" \(also called the beacon chain\).

Note that there are now several "levels" of nodes that can exist in such a system:

* Super-full node - downloads the full data of the beacon chain and every shard block referenced in the beacon chain.
* Top-level node - processes the beacon chain blocks only, including the headers and signatures of the shard blocks, but does not download all the data of the shard blocks.
* Single-shard node - acts as a top-level node, but also fully downloads and verifies every collation on some specific shard that it cares more about.
* Light node - downloads and verifies the block headers of main chain blocks only; does not process any collation headers or transactions unless it needs to read some specific entry in the state of some specific shard, in which case it downloads the Merkle branch to the most recent collation header for that shard and from there downloads the Merkle proof of the desired value in the state.

## Resources

* [Sharding FAQ](https://github.com/ethereum/wiki/wiki/Sharding-FAQs)
* [Sharding Roadmap](https://github.com/ethereum/wiki/wiki/Sharding-roadmap)
* [DCS Triangle](https://blog.bigchaindb.com/the-dcs-triangle-5ce0e9e0f1dc)

