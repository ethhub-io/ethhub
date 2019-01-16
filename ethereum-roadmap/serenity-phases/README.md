# Serenity \(Eth 2.0\)

_This page is a WIP._

## Introduction

Ethereum’s Serenity upgrade will bring Sharding, Proof of Stake, a new virtual machine \(eWASM\) and more. It’s important to understand that this upgrade will not take place at a single point in time. Instead, it will be rolled out in phases. This document attempts to be a reference point for these phases and what each includes.

To start, here is a [nice visual](https://docs.google.com/presentation/d/1G5UZdEL71XAkU5B2v-TC3lmGaRIu2P6QSeF8m3wg6MU/edit#slide=id.g3c326bb661_0_58) from Hsiao-Wei Wang on what the different layers and phases look like.

![](../../.gitbook/assets/screen-shot-2018-12-10-at-2.01.26-pm.png)

## Phase 0 - Beacon Chain \(~Late 2019\)

### **What is included?**

Phase 0 is the name given to the launch of the Beacon Chain. The Beacon Chain will manage the Casper Proof of Stake protocol. As Ben Edgington [puts it](https://media.consensys.net/state-of-ethereum-protocol-2-the-beacon-chain-c6b6a9a69129), “There are a number of aspects to this: managing validators and their stakes; nominating the chosen block proposer for each shard at each step; organising validators into committees to vote on the proposed blocks; applying the consensus rules; applying rewards and penalties to validators; and, being an anchor point on which the shards register their states to facilitate cross-shard transactions.”

Phase 0 will use Casper FFG for finality and RANDAO to select block proposers and committees.

### **What will the network look like?**

Once Phase 0 is complete, there will be two active Ethereum chains. For the sake of clarity let’s call them the Eth 1.0 chain \(current, PoW mainchain\) and the Eth 2.0 chain \(new beacon chain\). During this phase, users will be able to migrate their ETH from the Eth 1.0 chain to the Eth 2.0 chain and become validators. However, they will NOT be able to migrate this ETH back. The reason someone may want to do this is that they could be earning interest paid in ETH on the Eth 2.0 chain.

**Important Considerations**

* There will be a minimum amount of ETH stake needed in order to first bootstrap the beacon chain. This is defined as `CHAIN_START_FULL_DEPOSIT_THRESHOLD` in the spec. Currently, this is set to 16384 validators needed. That would mean 524,288 ETH in total stake is needed. This would pay ~11% interest to stakers.
* ETH rewards earned by validators won’t be transferable until Phase 2 of the Serenity roll-out as that is when state execution is implemented.
* During Phase 0, all user transactions and smart contract computations will still occur on the Eth 1.0 chain.

## Phase 1 - Shard Chains

### What is included?

Phase 1 will bring shard chains to the Eth 2.0 side. Shard chains are the key to future scalability as they allow parallel transaction throughput. In Phase 1, the Beacon Chain will now start to manage multiple shards at once.

### What will the network look like?

The Eth 1.0 and 2.0 chains will still operate in parallel after Phase 1.

### Important Considerations

* In Phase 0, 1, and 2 the main PoW chain will remain live while testing and transitioning is happening on the Eth 2.0 chain. This means that rewards will be paid to both Ethereum 2.0 validators as well as the normal PoW block rewards. Therefore, the combined inflation of the 2 chains may spike a bit initially but then start to trend towards the 0-1% range as the PoW chain is gradually deemphasized.

## Phase 2 - State Execution

### What is included?

Phase 2 is where the functionality will start to come together. At this point, the Beacon Chain and shards chains are live, but they are somewhat useless from an end user perspective until smart contracts and transactions can be executed. This will be added in Phase 2.

### Important Considerations

* This phase will endow shards with eWASM as the EVM.
* It is an open question when and how Ethereum 1.0 accounts and contracts will be migrated to Ethereum 2.0.

## Resources

* [Sharding Roadmap](https://github.com/ethereum/wiki/wiki/Sharding-roadmap#strongphase-3strong-light-client-state-protocol)
* [State of Ethereum Protocol](https://media.consensys.net/state-of-ethereum-protocol-2-the-beacon-chain-c6b6a9a69129)
* [Eth 2.0 Specs](https://github.com/ethereum/eth2.0-specs)
