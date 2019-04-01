title: Migration from Ethereum 1.0 to Ethereum 2.0 - EthHub
description: There are many things to consider in the migration of Eth 1.0 to Eth 2.0 including Ether migration and state.

# Eth 1.0 to 2.0 Migration

## Introduction

There are two important factors to consider when it comes to migrating from the Eth 1.0 chain to the Eth 2.0 chain. First, we have the need to migrate existing Ether over and secondly, we have to transition the state of the chain over.

## Ether Migration

The current proposal is that in [Phase 0](./#phase-0-beacon-chain-late-2019), users on the Eth 1.0 chain will be able to lock their Ether up in a contract and will be credited with that same amount of Ether on the Beacon Chain in Eth 2.0. At that point, they can stake that Ether and begin to earn rewards on the Eth 2.0 chain. However, there is also some community interest in creating a two way bridge for that Ether between the 1.0 and 2.0 chains. Pros and cons of each bridge are found below.

**One-way bridge**

| Pros | Cons |
| :--- | :--- |
| Steady security, deposits can only go up, possibility to transfer staking balance between validator accounts | High lockup risk for early stakers (~almost 1.5years) |
| Less complexity for early stages | Potential for two coins via futures market |
| Keeps forks isolated to each chain | Fragmented community/economics |
 

**Two-way bridge**

| Pros | Cons |
| :--- | :--- |
| Less risk of lockup, more deposit inflow | High volatility of total stake |
| Keeps just a single ETH coin, no Beacon ETH \(BETH\) | Additional code complexity in early stages |
| If issues arise with Eth 2.0, can bring coins back | Risk of lockup is absent, will likely see more games played on early code |

Having a one-way bridge promises security, less complexity, even the lockup risk shouldn't matter much as the validator will earn interest on performing honestly.

Danny Ryan tells us more about why two-way bridge is not included in Phase 0:

"The more we encumber the 1.0 consensus with 2.0, the more we tie the development and fork processes which would likely slow down the shipping/iterating on 2.0. It is not technically infeasible. It would require 2.0 light clients to be run by all 1.0 clients and some changes to the 1.0 consensus rules allowing for a similar burn/receipt method in the opposite direction. If we were to create fungibility, the path would be \(1\) release 2.0 beacon chain, \(2\) once stable beacon chain and light clients exist then require 1.0 clients to be light clients of 2.0 and finalize 1.0 with 2.0 and expose beacon chain state root to 1.0 \(3\) add additional consensus rules to 1.0 and 2.0 to handle the reminting on 1.0 with proof of burn on 2.0.

I think it would be detrimental to 2.0 development to demand fungibility out the gate. Over time as light clients are released and we begin to finalize 1.0 with 2.0 if the community wants fungibility, then we can assess proposals then.

..we can’t prove things about the beacon chain until we force 1.0 clients to agree on the current state of the beacon chain \(thus the light client requirement\). That’s why it logically falls after finalizing 1.0 if the community really wants it."

Validators will also be able to sell their Eth2.0 Ether balance to another validator, presumably at some discount to the prevailing Ether price due to the lock-up and risks. Nonetheless, anyone can exit with funds if they really need to.
This is a nice feature that will hopefully encourage more participants to feel comfortable committing to staking.

Two way transfers between the beacon chain and the shards, as well as between shards, will be available in Phase 2.


## State Migration

The current proposal is that in [Phase 2](./#phase-2-state-execution), the state of the current Eth 1.0 chain will be transferred into a shard on the Eth 2.0 chain. At this point, all information from the Eth 1.0 chain will be available on the Eth 2.0 chain.

Again, quoting Danny Ryan:

"Once the state execution layer is in the new 1024 shards, users will be able to transfer ETH directly to the shards from the PoW chain. In the long term, the plan is to roll the PoW state into one of the shards."

**Will eWASM replace EVM?**
Ethereum-flavoured web assembly is a deterministic smart contract execution engine built on the modern, standard WebAssembly virtual machine. It was first proposed in [EIP 48](https://github.com/ethereum/EIPs/issues/48). It may be the future execution engine for smart contracts on the Ethereum blockchain and is the primary candidate to replace EVM (the Ethereum virtual machine) as part of the Ethereum 2.0 roadmap.

Vitalik also thinks that the EVM should be retired soon and contracts should be on Ewasm with an EVM interpreter.

Since EVM makes use of 256-bit bytecode, smaller computations have to be converted to 256-bit strings before the EVM can process them.
The WASM code, however, has been designed with production in mind. The elimination of precompiling is an added advantage for eWASM. WASM is an open standard \(backed by google, microsoft, apple\) and because of this it will allow more programming languages to be used for smart contract development (Solidity included).

However, there is also some community interest in not doing this state transition. Here we will weight the pros and cons of each in order to help stimulate discussion.

**State migration in Phase 2**

| Pros | Cons |
| :--- | :--- |
|  |  |
|  |  |

**No state migration in Phase 2**

| Pros | Cons |
| :--- | :--- |
|  |  |
|  |  |

