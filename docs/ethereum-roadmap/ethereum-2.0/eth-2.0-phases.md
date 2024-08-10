---
title: Ethereum upgrades - EthHub

description: A guide to the roadmap and implementation plans of major Ethereum upgrades.
---

# Ethereum Upgrades

_As current Ethereum upgrades are in heavy research and development, this page may become outdated spontaneously. It is kept up to date on a best-effort basis. Last updated February, 2021._

This page is also available in [German](eth-2.0-phases-german.md) and [Portuguese](eth-2.0-phases-portuguese.md).

## Introduction

Ethereum's major network upgrades (previously collectively called Ethereum 2.0) will bring a Proof of Stake consensus mechanism, sharding chains, and more improvements along the way. It’s important to understand that these will not take place at a single point in time - instead, it will be rolled out in multiple upgrades. This document attempts to be a reference point for these phases and what each one includes.
## Design Goals

Ethereum researcher Danny Ryan has [stipulated](https://github.com/ethereum/consensus-specs#design-goals) 5 distinct design goals for Ethereum 2.0:

* **Decentralization:** to allow for a typical consumer laptop with O(C) resources to process/validate O(1) shards (including any system level validation such as the beacon chain).
* **Resilience:** to remain live through major network partitions and when very large portions of nodes go offline.
* **Security:** to utilize crypto and design techniques that allow for a large participation of validators in total and per unit time.
* **Simplicity:** to minimize complexity, even at the cost of some losses in efficiency.
* **Longevity:** to select all components such that they are either quantum secure or can be easily swapped out for quantum secure counterparts when available.

## Beacon Chain

### **What is included?**

The Beacon Chain is the first step towards the new consensus mechanism. The Beacon Chain manages the Casper Proof of Stake protocol for itself and later for all of the shard chains. As Ben Edgington [puts it](https://media.consensys.net/state-of-ethereum-protocol-2-the-beacon-chain-c6b6a9a69129), “There are a number of aspects to this: managing validators and their stakes; nominating the chosen block proposer for each shard at each step; organizing validators into committees to vote on the proposed blocks; applying the consensus rules; applying rewards and penalties to validators; and, being an anchor point on which the shards register their states to facilitate cross-shard transactions.”

The primary source of load on the Beacon Chain will be "attestations". Attestations are availability votes for a shard block and, simultaneously, proof of stake votes for a beacon block. A sufficient number of attestations for the same shard block will create a "crosslink" which confirms the shard segment up to that shard block into the Beacon Chain.

Beacon chain uses Casper the Friendly Finality Gadget (FFG) for finality. Finality, in very loose terms, means that once a particular operation has been done, it will forever be etched in history and nothing can revert that operation.

#### **Getting ether onto the Beacon Chain**

Ether staked by validators on the Beacon Chain is from a one-way transaction to the [deposit contract](https://etherscan.io/address/0x00000000219ab540356cbb839cbe05303d7705fa). A deposit is made to this contract with transaction data indicating the validator the deposit is for. The deposit contract is watched by every validator on the network, who will submit the deposits to the beacon chain.

After a validator public key reaches a balance of 32 ETH, it is registered as active validator and entered into queue for activation.

**Please note:** this transfer to the deposit contract is only one-way. Withdrawals will be enabled some time after The Merge.

### **What will the network look like?**

Beacon Chain is running as its own network but it is connected to the Ethereum network where deposit contract defines current set of validators. There are no transactions or any contracts, only validators are participating in this network. 

In order to run the Beacon Chain, you’re going to need a Beacon Chain (consensus) client. There are [multiple](https://ethereum.org/en/upgrades/get-involved/) of them being developed and production ready - Lighthouse, Prysm, Teku, Nimbus, Lodestar. Consensus client needs to be connected to execution client. In other words, you need fully synced execution client (Geth, Nethermind, Besu, Erigon..) and point the Beacon node to it.

The Beacon Chain running since December 2020 is not that useful for normal users but enables bootstrapping liquidity, testing and building the infrastructure for the new Ethereum consensus. 

**Important Considerations**

* There is a minimum amount of ETH stake needed in order to first bootstrap the Beacon Chain. This is defined as `MIN_GENESIS_VALIDATOR_ACTIVE_COUNT` in the [Beacon Chain specification](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/beacon-chain.md).
  *  This was achieved before December 1st 2020 and staked amount keeps growing.
* During this phase, the Ethereum network will live uninterrupted. Nothing will change for Ethereum users.


## The Merge

### What is included?

The Merge is where Beacon Chain, previously separted chain, merges with current Ethereum network. Proof of Work Ethereum network will start listening only to Beacon Chain validators, dropping PoW miners and switching to Proof of Stake consensus. 

Data in the Ethereum network stays the same. All the history, accounts, contracts, and transactions will continue the same as today, just validated by PoS consensus. Future blocks are validated by PoS validators from the Beacon Chain, and non historical data is lost. More on [The Merge](https://ethereum.org/en/upgrades/merge/). 

## Shard Chains

### What is included?

Shard chains are the key to future scalability as they allow parallel transaction throughput and there will be 64 of them deployed (with the possibility of adding more over time as hardware scales).

Sharding is primarily concerned with the construction, validity, and consensus on the data of these shard chains. Phase 1 does not specify shard chain state execution or account balances. It'll be like a trial run for the sharding structure rather than an attempt to use shards to scale. The Beacon Chain will treat shard chain blocks as simple collections of bits with no structure or meaning.

**Crosslinks** <br/>
Periodically, the current state (the “combined data root”) of each shard gets recorded in a Beacon Chain block as a crosslink. When the Beacon Chain block has been finalised, the corresponding shard block is considered finalised, and other shards know that they can rely on it for cross-shard transactions. <br/>

Crosslinks are a set of signatures from a committee attesting to a block in a shard chain, which can be included into the Beacon Chain. Crosslinks are the main means by which the Beacon Chain "learns about" the updated state of shard chains. Crosslinks also serve as infrastructure for asynchronous cross-shard communication.

Shard validators, who are randomly selected by the Beacon Chain for each shard at each slot, merely come to agreement on each block’s content. They attest to the shard’s contents and state through crosslinking. It doesn’t matter what information appears in shards blocks, so long as all committees reach consensus and update the Beacon Chain on the shard regularly.

### Important Considerations

* A dApp will have to choose what shard it wants to be on. That decision matters because cross-shard communication differs as it is not synchronous which means some composability is lost between shards
* A dApp would have to have rather large data to consume all the resources in a given shard to justify spreading itself over multiple ones.
* [Sharding specs](https://github.com/ethereum/consensus-specs#sharding) are still being researched and developed at the moment. 

## Other upgrades

[Ethereum upgrades](https://twitter.com/VitalikButerin/status/1466411377107558402/photo/1) are not limited neither finish with these major upgrades. The path of improving Ethereum is very long and there are always new ideas emerging and priorities changing. Currently, strong research focus is on statlessness, verkle trees, history expiry and alternative history access, account abstraction, and zero knowledge cryptography.

## Resources

* [Ethereum Roadmap](https://ethos.dev/ethereum-2020-roadmap/)
* [Ethereum Upgrades](https://ethereum.org/en/upgrades/)
* [Ethereum 2.0 Info](https://hackmd.io/@benjaminion/eth2_info)
* [Conensus Specs](https://github.com/ethereum/eth2.0-specs)
* [Phase 0 for Humans](https://notes.ethereum.org/jDcuUp3-T8CeFTv0YpAsHw?view)
* [Sharding Roadmap](https://eth.wiki/en/sharding/sharding-roadmap)
* [State of Ethereum Protocol](https://media.consensys.net/state-of-ethereum-protocol-2-the-beacon-chain-c6b6a9a69129)
* [Ethereum 2.0 Design Goals](https://media.consensys.net/exploring-the-ethereum-2-0-design-goals-fd2d901b4c01)
* [Q&A Session ETHMagicians](https://medium.com/ethereum-magicians/demystifying-the-road-to-ethereum-2-0-8130ade8d00f)
* [eWASM](https://www.coindesk.com/open-heart-surgery-inside-ethereums-crucial-replacement-of-the-evm)
