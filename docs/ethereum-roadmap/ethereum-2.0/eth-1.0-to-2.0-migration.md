title: Migration from Ethereum 1.0 to Ethereum 2.0 - EthHub
description: There are many things to consider in the migration of Eth 1.0 to Eth 2.0 including Ether migration and state.

# Eth 1.0 to 2.0 Migration

## Introduction

There are two important factors to consider when it comes to migrating from the Eth 1.0 chain to the Eth 2.0 chain. First we have the need to migrate existing Ether over and second we have to transition the state of the chain over.

## Ether Migration

The current proposal is that in [Phase 0](./#phase-0-beacon-chain-late-2019), users on the Eth 1.0 chain will be able to lock their Ether up in a contract and will be credited with that same amount of Ether on the Beacon Chain in Eth 2.0. At that point, they can stake that Ether and begin to earn interest. However, there is also some community interest in creating a two way bridge for that Ether between the 1.0 and 2.0 chains. Here we will weigh the pros and cons of each in order to help stimulate discussion.

**One-way bridge**

| Pros | Cons |
| :--- | :--- |
| Steady security, deposits can only go up | High lockup risk for early stakers |
| Less complexity for early stages | Potential for two coins via futures market |
| Keeps forks isolated to each chain | Fragmented community/economics |

**Two-way bridge**

| Pros | Cons |
| :--- | :--- |
| Less risk of lockup, more deposit inflow | High volatility of total stake |
| Keeps just a single ETH coin | Additional code complexity in early stages |
| If issues arise with Eth 2.0, can bring coins back | Risk of lockup is absent, will likely see more games played on early code |

## State Migration

The current proposal is that in [Phase 2](./#phase-2-state-execution), the state of the current Eth 1.0 chain will be transferred into a shard on the Eth 2.0 chain. At this point, all information from the Eth 1.0 chain will be available on the Eth 2.0 chain. However, there is also some community interest in not doing this state transition. Here we will weight the pros and cons of each in order to help stimulate discussion.

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

