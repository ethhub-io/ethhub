---
title: Ethereum 2.0 Phases - EthHub

description: A guide to the phases and implementation plans of Ethereum 2.0.
---

# Ethereum 2.0 Phases

_As Ethereum 2.0 is in heavy research and development, this page may become outdated spontaneously. It is kept up to date on a best-effort basis. Last updated 16th of November, 2019._

This page is also available in [German](eth-2.0-phases-german.md) and [Portuguese](eth-2.0-phases-portuguese.md).

## Introduction

Ethereum's major network upgrade, dubbed Ethereum 2.0, Eth2 or Serenity, will bring with it Sharding, Proof of Stake, a new virtual machine \(eWASM\) and more. It’s important to understand that this upgrade will not take place at a single point in time - instead, it will be rolled out in phases. This document attempts to be a reference point for these phases and what each one includes.

## Design Goals

Ethereum researcher Danny Ryan has [stipulated](https://github.com/ethereum/eth2.0-specs#design-goals) 5 distinct design goals for Ethereum 2.0:

* **Decentralization:** to allow for a typical consumer laptop with O(C) resources to process/validate O(1) shards (including any system level validation such as the beacon chain).
* **Resilience:** to remain live through major network partitions and when very large portions of nodes go offline.
* **Security:** to utilize crypto and design techniques that allow for a large participation of validators in total and per unit time.
* **Simplicity:** to minimize complexity, even at the cost of some losses in efficiency.
* **Longevity:** to select all components such that they are either quantum secure or can be easily swapped out for quantum secure counterparts when available.

## Phase 0 - Beacon Chain

### **What is included?**

Phase 0 is the name given to the launch of the Beacon Chain. The Beacon Chain will manage the Casper Proof of Stake protocol for itself and all of the shard chains. As Ben Edgington [puts it](https://media.consensys.net/state-of-ethereum-protocol-2-the-beacon-chain-c6b6a9a69129), “There are a number of aspects to this: managing validators and their stakes; nominating the chosen block proposer for each shard at each step; organizing validators into committees to vote on the proposed blocks; applying the consensus rules; applying rewards and penalties to validators; and, being an anchor point on which the shards register their states to facilitate cross-shard transactions.”

The primary source of load on the Beacon Chain will be "attestations". Attestations are availability votes for a shard block and, simultaneously, proof of stake votes for a beacon block. A sufficient number of attestations for the same shard block will create a "crosslink" which confirms the shard segment up to that shard block into the Beacon Chain.

Phase 0 will use Casper the Friendly Finality Gadget (FFG) for finality. Finality, in very loose terms, means that once a particular operation has been done, it will forever be etched in history and nothing can revert that operation.

#### **Getting ether onto the beacon chain**
All ether on the beacon chain in phase 0 will be from a one-way transaction to the deposit contract. A deposit is made to this contract with transaction data indicating the validator the deposit is for. The deposit contract is watched by every validator on the network, who will submit the deposits to the beacon chain.

After a validator public key reaches a balance of 32 ETH, it is registered as active validator and entered into queue for activation.

**Please note:** this transfer to the deposit contract is only one-way, for phase 0 there is no way for the deposited eth to return to Eth1.x. This is expected to change as part of phase 1.

### **What will the network look like?**

Once Phase 0 is complete, there will be two active Ethereum chains. For the sake of clarity let’s call them the Eth1 chain \(current, PoW main chain\) and the Eth2 chain \(new Beacon Chain\). During this phase, users will be able to send their ETH from the Eth1 chain to the Eth2 chain and become validators. They will NOT be able to migrate this ETH back to Eth1 (for now).

In order to run the Beacon Chain, you’re going to need a Beacon Chain client. These are currently being developed separately from the familiar suite of standard Ethereum clients (Geth, Nethermind, Pantheon, et al.) by a number of [teams](/ethereum-roadmap/ethereum-2.0/eth2.0-teams/teams-building-eth2.0/). Most of the teams are putting out periodic updates on their client development progress, and some of the teams are offering bounties to contributors to include more and more developers in building 2.0. You can contribute on Gitcoin grants [here](https://gitcoin.co/grants/)

On its own, the Beacon Chain might not seem particularly useful. But, as the first component of Ethereum 2.0 to be delivered, it is the foundation of the entire system.

**Important Considerations**

* There will be a minimum amount of ETH stake needed in order to first bootstrap the beacon chain. This is defined as `MIN_GENESIS_VALIDATOR_ACTIVE_COUNT` in the [beacon chain specification](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/phase0/beacon-chain.md).
* During Phase 0, the Eth1 chain will live uninterrupted. Nothing will change for Eth1.

## Phase 1 - Shard Chains

### What is included?

Shard chains are the key to future scalability as they allow parallel transaction throughput and there will be 64 of them deployed in Phase 1 (with the possibility of adding more over time as hardware scales).

Phase 1 is primarily concerned with the construction, validity, and consensus on the data of these shard chains. Phase 1 does not specify shard chain state execution or account balances. It'll be like a trial run for the sharding structure rather than an attempt to use shards to scale. The Beacon Chain will treat shard chain blocks as simple collections of bits with no structure or meaning.

**Crosslinks** <br/>
Periodically, the current state (the “combined data root”) of each shard gets recorded in a Beacon Chain block as a crosslink. When the Beacon Chain block has been finalised, the corresponding shard block is considered finalised, and other shards know that they can rely on it for cross-shard transactions. <br/>

Crosslinks are a set of signatures from a committee attesting to a block in a shard chain, which can be included into the Beacon Chain. Crosslinks are the main means by which the Beacon Chain "learns about" the updated state of shard chains. Crosslinks also serve as infrastructure for asynchronous cross-shard communication.

Shard validators, who are randomly selected by the Beacon Chain for each shard at each slot, merely come to agreement on each block’s content. They attest to the shard’s contents and state through crosslinking. It doesn’t matter what information appears in shards blocks, so long as all committees reach consensus and update the Beacon Chain on the shard regularly.

### What will the network look like?

The Eth1 and Eth2 chains will still operate in parallel after Phase 1.

### Important Considerations

* In Phase 0, 1, and 2 the main PoW chain (Eth1) will remain live while testing and transitioning is happening on the Eth2 chain. This means that rewards will be paid to both Ethereum 2.0 validators as well as the normal PoW block rewards. Therefore, the combined inflation of the two chains may spike initially but then start to trend towards the 0-1% range as the PoW chain is gradually de-emphasized.

## Phase 2 - State Execution

### What is included?

Phase 2 is where the functionality of the entire system will start to come together. Shard chains transition from simple data containers to a structured chain state and Smart Contracts will be reintroduced. Each shard will manage a virtual machine based on [eWASM](https://github.com/ewasm/design). It'll support accounts, contracts, state, and other abstractions that we’re familiar with from solidity. We can expect familiar tools like truffle, solc, ganache ported to support eWASM before or during Phase 2.

Phase 2 also introduces the concept of 'Execution Environments (EEs)'. EEs within a shard can be constructed in whatever way a developer sees fit - there could be an EE for a UTXO-style chain, a Libra-style system, an EE for a fee market relayer and beyond. Every shard has access to all execution environments and has the ability to make transactions within them as well as run and interact with smart contracts. Do note that the concept of execution environments is still in heavy research and development.

### Important Considerations
* A dApp will have to choose what shard it wants to be on. That decision matters because cross-shard communication differs on Eth2 as it is not synchronous which means some composability is lost between shards<br/>
* A dApp would have to have rather large data to consume all the resources in a given shard to justify spreading itself over multiple ones.<br/>
* This phase will endow shards with eWASM as the EVM 2.0.
* It is an open question when and how Ethereum 1.0 accounts and contracts will be migrated to Ethereum 2.0, there are some [upgrade plans](https://ethresear.ch/t/the-eth1-eth2-transition/6265)

## Resources

* [Ethereum Roadmap](https://ethos.dev/ethereum-2020-roadmap/)
* [Ethereum 2.0 Info](https://hackmd.io/e4cNiocFTiS67j6yJ_XHPw?view)
* [Eth 2.0 Specs](https://github.com/ethereum/eth2.0-specs)
* [Phase 0 for Humans](https://notes.ethereum.org/jDcuUp3-T8CeFTv0YpAsHw?view)
* [Sharding Roadmap](https://github.com/ethereum/wiki/wiki/Sharding-roadmap#strongphase-3strong-light-client-state-protocol)
* [State of Ethereum Protocol](https://media.consensys.net/state-of-ethereum-protocol-2-the-beacon-chain-c6b6a9a69129)
* [Ethereum 2.0 Design Goals](https://media.consensys.net/exploring-the-ethereum-2-0-design-goals-fd2d901b4c01)
* [Q&A Session ETHMagicians](https://medium.com/ethereum-magicians/demystifying-the-road-to-ethereum-2-0-8130ade8d00f)
* [eWASM](https://www.coindesk.com/open-heart-surgery-inside-ethereums-crucial-replacement-of-the-evm)
 # Step 1: Authentication

 $ Cat ~ / GH_TOKEN.txt | docker login docker.pkg.github.com -u tex 101 -password -stdin

#Step 2: tag

 $ Docker tag IMAGE_ID docker.pkg.github.com/101/ eth hub / IMAGE_NAME: version

 #Step 3: Publish

 $ Docker.pkg.github.com/101/ eth hub / IMAGE_NAME: version
