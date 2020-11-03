---
title: Migration from Ethereum 1.0 to Ethereum 2.0 - EthHub

description: There are many things to consider in the migration of Eth 1.0 to Eth 2.0 including Ether migration and state.
---

# Eth 1.0 to 2.0 Migration

## Introduction

There are two important factors to consider when it comes to migrating from the Eth 1.0 chain to the Eth 2.0 chain. First, we have the need to migrate existing ether over and secondly, we have to transition the state of the chain over.

## Ether Migration

The current proposal is that in [phase 0](./eth-2.0-phases.md#phase-0-beacon-chain), users on the Eth 1.0 chain will be able to lock their ether up in a contract and will be credited with that same amount of ether on the Beacon Chain in Eth 2.0. At that point, they can stake that ether and begin to earn rewards on the Eth 2.0 chain. However, there is also some community interest in creating a two way bridge for that ether between the 1.0 and 2.0 chains. Pros and cons of each bridge are found below.

**One-way bridge**

| Pros | Cons |
| :--- | :--- |
| Steady security, deposits can only go up | High lockup risk for early stakers (at least ~1.5 years) |
| Less complexity for early stages | Potential for two coins via futures market |
| Keeps forks isolated to each chain | Fragmented community/economics |
 

**Two-way bridge**

| Pros | Cons |
| :--- | :--- |
| Less risk of lockup, more deposit inflow | High volatility of total stake |
| Keeps just a single ETH coin, no Beacon ETH \(BETH\) ([only if issuance of Eth 1.0 is changed](https://medium.com/@fubuloubu/economically-linking-ethereum-1-0-2-0-e5af0fec02ed)) | Additional code complexity in early stages |
| If issues arise with Eth 2.0, can bring coins back | Risk of lockup is absent, will likely see more games played on early code |

Having a one-way bridge promises security, less complexity, but the lockup risk is significant as ether from Eth 1.0 is effectively burned. Transfers in phase 0 have been [disabled since version 0.6.0 of the spec](https://github.com/ethereum/eth2.0-specs/pull/965), with no current plans of being re-enabled. As resuming validator duties is tied to the transfer mechanism, this also means that if you decide to stop validating for a bit, you can't resume validating until such a time as the transfer functionality is implemented.

Danny Ryan tells us more about why two-way bridge is not included in phase 0:

"The more we encumber the 1.0 consensus with 2.0, the more we tie the development and fork processes which would likely slow down the shipping/iterating on 2.0. It is not technically infeasible. It would require 2.0 light clients to be run by all 1.0 clients and some changes to the 1.0 consensus rules allowing for a similar burn/receipt method in the opposite direction. If we were to create fungibility, the path would be \(1\) release 2.0 beacon chain, \(2\) once stable beacon chain and light clients exist then require 1.0 clients to be light clients of 2.0 and finalize 1.0 with 2.0 and expose beacon chain state root to 1.0 \(3\) add additional consensus rules to 1.0 and 2.0 to handle the reminting on 1.0 with proof of burn on 2.0.

I think it would be detrimental to 2.0 development to demand fungibility out the gate. Over time as light clients are released and we begin to finalize 1.0 with 2.0 if the community wants fungibility, then we can assess proposals then.

...we can't prove things about the beacon chain until we force 1.0 clients to agree on the current state of the beacon chain \(thus the light client requirement\). That's why it logically falls after finalizing 1.0 if the community really wants it."

Validators will also be able to sell their Eth 2.0 ether balance to another validator, presumably at some discount to the prevailing ether price due to the lock-up and risks. Nonetheless, anyone can exit with funds if they really need to.
This is a nice feature that will hopefully encourage more participants to feel comfortable committing to staking.

Using BETH on shard chains (for smart contracts) will be available in phase 2.


## State Migration

### Old Proposal

The old proposal is that in [phase 2](./eth-2.0-phases.md#phase-2-state-execution), the state of the current Eth 1.0 chain will be transferred into a shard on the Eth 2.0 chain. At this point, all information from the Eth 1.0 chain will be available on the Eth 2.0 chain.

Currently Lighthouse is working upon a state transition [library](https://github.com/libp2p/go-libp2p-daemon).

**Replacing EVM with eWASM?**

Ethereum-flavoured web assembly is a deterministic smart contract execution engine built on the modern, standard WebAssembly virtual machine. It was first proposed in [EIP 48](https://github.com/ethereum/EIPs/issues/48). It may be the future execution engine for smart contracts on the Ethereum blockchain and is the primary candidate to replace EVM (the Ethereum virtual machine) as part of the phase 2 of Ethereum 2.0 roadmap.

Buterin also thinks that the EVM should be retired soon and contracts should be on Ewasm with an EVM interpreter ([source](https://medium.com/ethereum-magicians/demystifying-the-road-to-ethereum-2-0-8130ade8d00f#a32b)).

Since EVM makes use of 256-bit bytecode, smaller computations have to be converted to 256-bit strings before the EVM can process them.
The WASM code, however, has been designed with production in mind. The elimination of precompiling is an added advantage for eWASM. WASM is an open standard \(backed by Google, Microsoft, Apple\) and because of this it will allow more programming languages \(C/C++, JS, Go\) to be used for smart contract development (Solidity included).
 
**Challenges of Old Proposal**

* There are speculations that phase 2 might be divided into sub-forks and there will be a fork during/after phase 2 to bring in the Eth 1.0 state into a contract.

* Before we migrate the state there's going to be validators earning rewards, and overall the cumulative issuance of ether will go up. So what will be the economics of ETH throughout?


### New Proposal

An Alternative Proposal for early transition is proposed by Vitalik Buterin, Which is getting accepted by among the wider community.

**Goals**

* **Getting rid of PoW chain** & moving everything onto the beacon chain.
* Development of Stateless clients.

**Stateless Client Features**

* A pure function for verifying blocks and witnesses, Along with a method for generating witnesses for the block.
* Available with multiple implementations.
* Eth1-side protocol changes to bound witness size to ~1-2 MB.
* Development of Stateless Clients requires much less rearchitecting to accomplish as it neither requires stateless miners or webassembly.
* Stateless Client is an important feature for the switch as it stops the malicious actions, [according to Buterin](https://www.reddit.com/r/ethereum/comments/eemp28/vitalik_alternative_proposal_for_early_eth1_eth2/fbxon3w/?utm_source=share&utm_medium=web2x).

**New beacon chain features**

* State root of the eth1 system transfers to the state of shard 0
* New Validator list known as `eth1_friendly_validators` will be added. Any validator has the right to register themselves as eth1-friendly (and deregister) at any time.
* The proposer on shard 0 at any given slot is chosen randomly out of the eth1-friendly validators.
* Committee of shard 0 verifies the blocks of shard 0, which are expressed in this format `Block body(currently exists) & stateless client witness`. All the other shard committees verify their shard blocks, where they would only be verifying data availability, not the state execution, as shard 0 is the only shard that would be running computation.

**Operation**

The eth1 system would “live” as shard 0 of eth2 (eventually, Will be one of the execution environments, but at the beginning, it can be the entire shard). Validators that want to participate in the eth1 system can register themselves as eth1-friendly validators and would be expected to maintain an eth1 full node in addition to their beacon node. The eth1 full node would download all blocks on shard 0 and maintain an updated full eth1 state.

**Advantages of New Proposal over the Old Proposal**

* Earlier proposal transfers the whole Eth1.0 chain to Eth2 shard, but now it will get rid of PoW, which solves the challenges faced during the Old proposal. As instead of Miners there will eth1_friendly_validators to validate the blocks.

* Development of Stateless Clients requires much less rearchitecting to accomplish.

According to Danny Ryan, the Eth2.0 lead:
He thinks it only depends on a successful and stable phase 0 and Phase 1 release, which may be demonstrating the security instability.

Core developers: 
They seem to be in the consensus of the Alternative Proposal and agreed that there is a decent amount of work to be done on the Eth1.x statelessness and is going to be a huge priority this year. But this approach is a much cleaner way for Eth1 to utilize the scalable data layer of Phase 1. There's a lot to learn and figure out before it comes into action but most of them seem positive about it. 

It was made official that the 'Alternative proposal for early eth1 <-> eth2 merge' model will be followed for the switch and the transition would still be done using a procedure similar to the [eth1 -> eth2 transition](https://ethresear.ch/t/the-eth1-eth2-transition/6265).