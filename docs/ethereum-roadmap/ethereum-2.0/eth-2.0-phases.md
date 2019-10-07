title: Ethereum 2.0 (Serenity) Phases - EthHub

description: A guide to the phases and implementation plans of Ethereum 2.0, aka Serenity.

# Ethereum 2.0 \(Serenity\) Phases

_This page is a WIP._

## Introduction

Ethereum’s Serenity upgrade will bring Sharding, Proof of Stake, a new virtual machine \(eWASM\) and more. It’s important to understand that this upgrade will not take place at a single point in time - instead, it will be rolled out in phases. This document attempts to be a reference point for these phases and what each includes.

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

#### **ETH2:The New Ether**

Phase 0 will introduce ETH2 which will be a new asset for stakers \(validators\) to be used on the Beacon Chain. It will be created by two methods:

* As a reward for validating the Beacon Chain \(and shards after phase1\).
* Purchasing it for 1 ETH by any ETH1.X user via a [registration contract](https://github.com/ethereum/beacon_chain/blob/master/contracts/validator_registration.v.py). The contract refers to it as a deposit.

There is currently no way to withdraw ETH2 from the beacon chain in Phase 0. Once deposited in the ETH1.x validator registration contract, the ETH1 is effectively burned. Beacon Chain validators watch this contract and submit deposit information to the Beacon Chain, which then issues ETH2 to the depositors.

Lastly, the Beacon Chain will generate good quality \(distributed, verifiable, unpredictable, and (reasonably) unbiasable\) randomness for the rest of the system. It will use RANDAO which is simply a way to combine contributions \(individual random numbers\) provided by many participants into a single output number.

This will be used to organize validators into block proposers and committees.

### **What will the network look like?**

Once Phase 0 is complete, there will be two active Ethereum chains. For the sake of clarity let’s call them the Eth 1.0 chain \(current, PoW main chain\) and the Eth 2.0 chain \(new Beacon Chain\). During this phase, users will be able to migrate their ETH from the Eth 1.0 chain to the Eth 2.0 chain and become validators. However, they will NOT be able to migrate this ETH back. The reason someone may want to do this is that they could be earning interest paid in ETH on the Eth 2.0 chain.

In order to run the Beacon Chain you’re going to need a Beacon Chain client. These are currently being developed separately from the familiar suite of standard Ethereum clients (Geth, Parity, Pantheon, et al.) by a number of [teams](/ethereum-roadmap/ethereum-2.0/eth2.0-teams/teams-building-eth2.0/). Prysmatic and Lighthouse are putting out periodic updates on their client development progress, and some of the teams are offering bounties to contributors to include more and more developers in building 2.0. You can contribute on Gitcoin grants [here](https://gitcoin.co/grants/)

On its own, the Beacon Chain might not seem particularly useful. But, as the first component of Ethereum 2.0 to be delivered, it is the foundation of the entire system.

**Important Considerations**

* ETH2 is transferable to and from shards once Phase 2 is complete.
* There will be a minimum amount of ETH stake needed in order to first bootstrap the beacon chain. This is defined as `CHAIN_START_FULL_DEPOSIT_THRESHOLD` in the [deposit contract that will live on the Eth 1.0 chain](https://github.com/ethereum/deposit_contract/blob/master/deposit_contract/contracts/validator_registration.v.py#L3). Currently, this is set to 65536 validators needed. That would mean 2,097,152 ETH in total stake is needed. This would pay ~11% interest to stakers.
* To become a validator, you'll need to stake 32 ETH2.
* During Phase 0, all user transactions and smart contract computations will still occur on the Eth 1.0 chain.


## Phase 1 - Shard Chains

### What is included?

Shard chains are the key to future scalability as they allow parallel transaction throughput.

Phase 1 is primarily concerned with the construction, validity, and consensus on the data of these shard chains. Phase 1 does not specify shard chain state execution or account balances. It'll be like a trial run for the sharding structure rather than an attempt to use shards to scale. The Beacon Chain will treat shard chain blocks as simple collections of bits with no structure or meaning.

**Crosslinks** <br/>
Periodically, the current state (the “combined data root”) of each shard gets recorded in a Beacon Chain block as a crosslink. When the Beacon Chain block has been finalised, the corresponding shard block is considered finalised, and other shards know that they can rely on it for cross-shard transactions. <br/>

Crosslinks are a set of signatures from a committee attesting to a block in a shard chain, which can be included into the Beacon Chain. Crosslinks are the main means by which the Beacon Chain "learns about" the updated state of shard chains. Crosslinks also serve as infrastructure for asynchronous cross-shard communication.

Shard validators, who are randomly selected by the Beacon Chain for each shard at each slot, merely come to agreement on each block’s content. They attest to the shard’s contents and state through crosslinking. It doesn’t matter what information appears in shards blocks, so long as all committees reach consensus and update the Beacon Chain on the shard regularly.

### What will the network look like?

The Eth 1.0 and 2.0 chains will still operate in parallel after Phase 1.

### Important Considerations

* In Phase 0, 1, and 2 the main PoW chain (Eth 1.0) will remain live while testing and transitioning is happening on the Eth 2.0 chain. This means that rewards will be paid to both Ethereum 2.0 validators as well as the normal PoW block rewards. Therefore, the combined inflation of the 2 chains may spike initially but then start to trend towards the 0-1% range as the PoW chain is gradually de-emphasized.

## Phase 2 - State Execution

### What is included?

Phase 2 is where the functionality will start to come together. Shard chains transition from simple data containers to a structured chain state and Smart Contracts will be reintroduced. Each shard will manage a virtual machine based on [eWASM](https://github.com/ewasm/design). It'll support accounts, contracts, state, and other abstractions that we’re familiar with from solidity. We can expect familiar tools like truffle, solc, ganache ported to support eWASM before or during phase 2.

State Rent is also a very likely inclusion for Phase 2 and it poses challenges to developers. Rather than being able to store code and data indefinitely, state rent would require contract developers and users to pay for eWASM storage over time. This ensures that unused information falls out of the state over time.

Currently, not much information is available about this phase and whatever is available is almost certainly going to change over time.

### Important Considerations
* A dApp will have to choose what shard it wants to be on. That decision matters because “Cross-shard communication will definitely be slow at base layer, however there are higher-level mechanisms that can be used to implement fast cross-shard communication on top of a base layer that allows any cross-shard communication at all even if slow,” according to Vitalik Buterin.<br/>
* A dApp would have to be really big to consume all the resources in a given shard to justify spreading itself over multiple ones.<br/>
* This phase will endow shards with eWASM as the EVM 2.0.
* It is an open question when and how Ethereum 1.0 accounts and contracts will be migrated to Ethereum 2.0, there are some [upgrade plans](https://ethereum-magicians.org/t/ethereum-1-dot-x-a-half-baked-roadmap-for-mainnet-improvements/1995)

## What's next ?
The sharding roadmap according to the official wiki suggests 6 phases. Justin Drake strongly believes that the sharding phases 1 and 2 will come in 2020 and 2021, respectively \(assuming that the Beacon Chain launches in 2019\). <br/>
From Phase 3 onwards any speculation made is subjected to change, you can go and check out the [wiki](https://github.com/ethereum/wiki/wiki/Sharding-roadmap#phase-3-light-client-state-protocol) for further phase's information.

## Resources

* [Eth 2.0 Specs](https://github.com/ethereum/eth2.0-specs)
* [Phase 0 for Humans](https://notes.ethereum.org/jDcuUp3-T8CeFTv0YpAsHw?view)
* [Sharding Roadmap](https://github.com/ethereum/wiki/wiki/Sharding-roadmap#strongphase-3strong-light-client-state-protocol)
* [State of Ethereum Protocol](https://media.consensys.net/state-of-ethereum-protocol-2-the-beacon-chain-c6b6a9a69129)
* [Ethereum 2.0 Design Goals](https://media.consensys.net/exploring-the-ethereum-2-0-design-goals-fd2d901b4c01)
* [Q&A Session ETHMagicians](https://medium.com/ethereum-magicians/demystifying-the-road-to-ethereum-2-0-8130ade8d00f)
* [eWASM](https://www.coindesk.com/open-heart-surgery-inside-ethereums-crucial-replacement-of-the-evm)
