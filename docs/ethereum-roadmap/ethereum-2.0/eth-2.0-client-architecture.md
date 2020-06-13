---
title: Ethereum 2.0 Client Architecture - EthHub

description: How will Ethereum clients work in Ethereum 2.0?
---

# Eth 2.0 Client Architecture

With Ethereum 2.0, we move away from the concept of a single full node to maintain the security of the network to two separate clients, the beacon node and the validator client.

## Beacon node

The beacon node is the primary link in the beacon chain that forms the backbone of the Eth 2.0 blockchain.  Below are the beacon node's responsibilities:

* Run and maintain the random beacon chain from the genesis block
* Sync this beacon chain with peer nodes via peer to peer (as Eth1.0 nodes do today when they maintain the Eth 1.0 blockchain)
* Process block attestations from validator clients/committees
* Serve as RPC server/endpoint for validator clients to leverage to propose/attest beacon blocks
* Handle beacon chain state transitions for each beacon block
* Serve as source of randomness for validator slot/shard assignment
* Sync and maintain current state of a subset of shards (anticipated to be the shards that connected validator clients are staking on)
* Listen for block hashes/validator deposits on Eth 1.0 chain for new validators
* Maintain the validator registry on the beacon chain, including adding and removing validators as necessary
* Maintain a synchronized clock with other beacon nodes to help enforce slashing rules for validator clients

### Beacon Node Hardware requirements

Beacon nodes are intended to be high-performance, highly available platforms that can support connections to numerous validator clients and maintain ongoing p2p connectivity with other beacon nodes.  As such, their hardware requirements are anticipated to be server-grade CPU/SSD/networking connections

### Beacon Node Staking requirements

Beacon nodes are the fundamental building blocks of Eth 2.0. Theoretically, anyone can run a beacon node and sync the current state of the overall beacon chain as there is ***no*** staking requirement to operate a beacon node.  It is expected that most wouldbe validators on Eth 2.0 will run their own beacon nodes as validator clients will need to trust the beacon node they connect to ensure that their block proposals/attestations are broadcasted correctly.

## Validator client

The validator client is more or less equivalent to the miner on the Ethereum 1.0 blockchain and responsibilities are outlined below:

* Propose new blocks on shards to which the validator is assigned
* Participate in committees by signing attestations on blocks proposed by other validators within the committee
* Aggregrate attestations from other validators on a committee when assigned for broadcasting to the beacon chain
* Maintain an RPC connection to a trusted beacon node to listen for validator assignment/shuffling
* Sync assigned shard with beacon chain for each proof of custody period

### Validator Client Staking requirements

Each validator client requires a 32 ETH stake in the deposit contract on the Eth 1.0 blockchain.

### Validator Client Hardware requirements

Unlike miners on the Eth 1.0, PoW chain, PoS is designed to be resource efficient and run on consumer-grade hardware like a mobile phone or single-board-computer with minimal processing/storage capacity.  Several of the Eth 2.0 teams have designed their clients to run on resource-constrained devices like a Raspberry Pi.

### Slashing Conditions

Slashing is defined as when a validator is ejected from the active validator set and has some portion of deposited validator funds burned.  This can occur for two specific violations as part of Phase 0

* Proposer slashing - occurs when a validator signs two different `beacon blocks` in the same epoch
* Attester slashing - occurs when a validator signs two conflicting attestations

## Differences between beacon nodes and validator clients

* Networking - Beacon nodes are connected via p2p to other beacon nodes while validator clients maintain a dedicated connectionn with a single beacon node
* Staking - Only validator clients are required to stake Eth to be able to participate in the network
* Block creation - Only validator clients may propose/sign blocks and beacon nodes merely validate attestations and propogate blocks across the beacon chain

## Eth 2.0 APIs

There are two main APIs defined by the Eth 2.0 spec that should be supported by beacon nodes.  All APIs are currently defined using a REST spec served over HTTP with a JSON return type.

### [Beacon Node API](https://github.com/ethereum/eth2.0-APIs/tree/master/apis/beacon)

The Beacon Node API allows for interactions between beacon nodes, including p2p networking connectivity as well as getting current beacon chain state and blocks from other nodes.

### [Validator Client API](https://github.com/ethereum/eth2.0-APIs/tree/master/apis/validator)

The Validator Client API is specifically designed for the interactions between a single validator client and the beacon node it is connected to for purposes of propagating block proposals and attestations to the network.
