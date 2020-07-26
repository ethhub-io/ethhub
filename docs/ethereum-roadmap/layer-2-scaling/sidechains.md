---
title: Sidechains - Ethhub

description:  Public sidechains are independent EVM chains which are interoperable with Ethereum.
---

# Sidechains

## Summary

Sidechains are Ethereum-compatible, independent blockchains which employ their own consensus models and block parameters to efficiently process transactions. Public EVM Sidechains are designed for interoperability with Ethereum. Contracts are typically portable and assets and data may be transferred cross-chain. Public sidechains are useful in many different contexts including micro-transactions, stable transactions, and application-specific transactions (NFT-based art, DAO voting, community currencies, etc). 


## How Do Sidechains work?

Layer 2 sidechains are distributed ledgers which operate independently and in a parallel capacity to the Ethereum mainnet. Nodes within a sidechain network are responsible for confirming & processing transactions, writing transactions to blocks, and maintaining consensus across the network. Security is the responsibility of each sidechain; it is not directly inherited from Ethereum. Sidechains often incorporate alternate validator selection and consensus mechanisms to provide faster transaction times.

### Security & Consensus

Sidechains are responsible for their own security and consensus processes. This allows for innovation and optimization, with the opportunity for increased transaction throughput and higher speed/lower cost transactions for users. Sidechains use a variety of validator selection methods to achieve these goals while maintaining security. Smaller validator sets are more susceptible to collusion-based attacks, so strong incentives must be in place to encourage honest validation and discourage malicious behavior. Examples include:

*Proof-of-Authority*: Validators (network nodes responsible for signing transactions and maintaing a consistent ledger) are pre-selected for the protocol. An example is the[POA Network](https://poa.network). POA uses an [Authority Round](https://openethereum.github.io/wiki/Aura) consensus where selected validators, in this case US Notary Publics with public reputations at stake, take turns signing transactions and sealing blocks. The POA model improves scalability (5 second block times, low transaction fees) while sacrificing a degree of decentralization (validators are pre-selected and the protocol has a limited validator set).

*Proof-of-Stake*: A set of validators are selected based on the staking amount they commit to the protocol. Nodes which have placed more stake are more likely to be selected as validators. With delegated proof-of-stake, users can add additional staking amounts to a node, serving to increase that node's likelihood of becoming a validator. An example is the [xDai chain](https://xdaichain.com), where nodes who commit a higher amount of STAKE (the xDai governance token, staked by both validator candidates and delegators) into the protocol have a higher probability of selection to a dynamic validator set. Once selected, staking incentives promote honest validation. 

Sidechains also rely on different Byzantine Fault Tolerant methods to ensure consensus. Examples include Peppermint BFT used by the [Matic Network](https://matic.network/) and Asynchronous Binary Byzantine Agreement by [Skale](https://skale.network/).

Ultimately, application-specific transactions may be better suited for sidechain adoption. Examples include DAO voting, small cash transfers, crypto art and NFTs, community currencies, small-cap exchanges, and many other use-cases which may not require the same security guarantees as high-value financial transactions. On a sidechain, transactions can be optimized for speed and cost. After they are processed, they can then be moved and stored on Ethereum through interoperability mechanisms.


### Interoperability

The ability to move assets and data between chains is an important aspect of the sidechain environment. Applications use sidechains for fast & inexpensive transactions, but the results of these transactions should be easily transferrable cross-chain. This is sometimes referred to as a two-way peg. Since chains are independent of one another, resources are typically locked on one chain and minted(created) on another. When they are transferred back, they are burned(destroyed) and unlocked. 

The [TokenBridge](https://docs.tokenbridge.net/) application exemplifies this architecture. Smart contracts deployed to both networks are connected by a bridge oracle where bridge validators confirm and sign cross-network transactions.


## Public Sidechain examples


* [POA Network](https://poa.network)
* [xDai Stable Chain](https://xdaichain.com)
* [SKALE](https://skale.network/)
* [Matic](https://matic.network/) 


_Note on Private Sidechains:  Sidechains may also be deployed in an enterprise capacity designed for private smart contracts and internal transactions. [Quorum](https://www.goquorum.com/) is an example of a private sidechain run by permissioned validators within JP Morgan._


## Resources

- [Enabling Blockchain Innovations with Pegged Sidechains](https://blockstream.com/sidechains.pdf)
- [Sidechain technologies in blockchain networks: An examination and state-of-the-art review](https://www.sciencedirect.com/science/article/pii/S1084804519303315)
