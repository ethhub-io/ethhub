title: Stateless-Clients - Ethhub

description: Exploring the stateless client and how this implementation of data processing and storing could greatly reduce the
workload on the Ethereum blockchain, improving performance and scalability.

# Stateless Clients

## Introduction

The state as it relates to Ethereum refers to "state of affairs."  The state refers to the values of all wallets and all
smart contract memories at single moment in time on the blockchain.  With the creation of each new block the state gets changed and updated.
A root hash is generated from the totality of the entire blockchain which is then compared against the value found by other nodes to
determine consensus on the network.

Recording the entire state of the blockchain is cumbersome and uses a lot of computational power.  Instead, the change of the state
can be recorded and packaged with verifiable witness data so that consensus can still be reached with less resource consumption.  Increased scalability and significantly improved transaction speeds that result. Using only the change value of the before and after
creates statelessness.  Statelessness actually exists on a spectrum, it is not absolute.  The degree of statelessness will depend upon the
task being performed on the blockchain.

## Overview

A stateless client is one that uses the delta change, that is the hash of the values changed on the blockchain.  The stateful client uses
the value of the entire blockchain balances and smart contract memories to generate a hash for validation.  The stateless client requires
far less computational resources resulting in faster transaction speeds and greater scalability.  Another goal of creating stateless clients is
to allow nodes to be created and brought online much quicker than present speeds.  Because a node verifies transaction data it must hold a
copy of the entire blockchain for verification.  This uses a massive amount of storage and can take up to two weeks to download.  The
other syncing method nodes can use is fast-sync.  This is where a node races the tip of the blockchain to get a certain amount of the state.
When the node reches this predetermined milestone and is in agreement with the blockchain the rest of the historical blockchain data
can be built in the background and allow the node to work.

When a node comes online it will be fully stateless since it will hold zero information regarding state.  Over time it will soak up the
state as transactions touch upon it, putting together a more complete state with every change of state presented.  New nodes will start as stateless clients which utilizes lower memory, disk space, and I/O.  Bandwidth usage will be the highest on a stateless node because peers need to send larger
proofs to the new node as it develops its own state data.  More stateful clients will have higher demands on memory, disk, and I/O while
bandwidth requirements would decrease.  Nodes can become more stateful until a certain tradeoff point is reached and then halted from
further acquisition of state information to optimize the trade off in computing power and bandwidth.

## Applications of Stateless Clients in Ethereum

Ethereum 1.X implements stateless clients in beam-sync (a method of fast syncing).  Beam sync initializes as a stateless node.  
It creates what is called a launch-block and only records the input and output state of this block locally.  The launch block is
a predetermined block number that is a certain amount of time in the future.  The future dated deadline is so that the node can work
on constructing the launch-block.  Witness data is called by the node to construct blocks.  As long as the launch-block is created early
or on time, the creation of blocks will continue and the node is active.  Use of only the witness data and input/output states make this a stateless client.

Ethereum 2.0 implements stateless clients in Sharding.  All nodes are stateless so that faster processing with less data
increases scalability greatly.  Currently the Ethereum blockchain is a sequential chain of blocks where one is
completed on top of another in a linear fashion.  This leads to traffic jams and an overall inefficency in data processing.   Sharding
is a design where the Ethereum network is split into groups referred to a shards.  Each shard has its own independant state.  Transactions
are delegated to different shards for processing, so rather than the entire network processing the same transaction, parallel computing
increases efficiency by allowing the work to be split up and executed concurrently.

## Additional Benefits of Stateless Clients

Mining new blocks will be moved from proof of work (PoW) to proof of stake (PoS).  A user can become a miner by staking a minimum
amount of Ethereum live on the blockchain.  This allows a miner to vote on the next block to create.  Consensus comes very quickly,
within one block of the evaluated block, because lengthy hash cryptography is no longer used to create blocks. This greatly reduces
electricity requirements, therefore cost of running a node.  Additionally, the held stake is an economic incentive / punishement for
any miner that performs nefarious activity.

Nodes will realize one of the largest improvements due to stateless clients.  The need to store large amounts of blockchain data
will be obsolete.   The time to set up a node will drop from weeks to hours.  Transaction speed will increase greatly since so much
data has been cut out of the state verifying work.

## Security Considerations

Casper is the proof of staking algorithm used in Ethereum 2.0.  The following are a list of theoretical attacks that could be executed
on Casper for furthe research on your own.
* [Casper Weaknesses](https://ethstaking.io/guide-to-ethereum-proof-of-stake-and-casper/casper-weaknesses/)
* [Casper Sybil Attack](https://ethstaking.io/guide-to-ethereum-proof-of-stake-and-casper/casper-sybil-attack/)
* [Casper 51% Attack](https://ethstaking.io/guide-to-ethereum-proof-of-stake-and-casper/casper-51-attack/)
* [Casper Bribe Attack](https://ethstaking.io/guide-to-ethereum-proof-of-stake-and-casper/casper-bribe-attack/)
* [Casper Censorship Attack](https://ethstaking.io/guide-to-ethereum-proof-of-stake-and-casper/casper-censorship-attack/)
* [Casper Liveness Denial Attack](https://ethstaking.io/guide-to-ethereum-proof-of-stake-and-casper/casper-liveness-denial-attack/)
* [Casper Long Range Attack](https://ethstaking.io/guide-to-ethereum-proof-of-stake-and-casper/casper-long-range-attack/)

## Resources

* [The 1.x Files: The State of Stateless Ethereum](https://blog.ethereum.org/2019/12/30/eth1x-files-state-of-stateless-ethereum/)
* [The Stateless Client Concept](https://ethresear.ch/t/the-stateless-client-concept/172)
* [The shades of statefulness (in Ethereum nodes)](https://medium.com/@akhounov/the-shades-of-statefulness-in-ethereum-nodes-697b0f88cd04)
* [Data from the Ethereum stateless prototype](https://medium.com/@akhounov/data-from-the-ethereum-stateless-prototype-8c69479c8abc)
* [The Basics of State Channels](https://education.district0x.io/general-topics/understanding-ethereum/basics-state-channels/)
* [Ethereum Sharding Explained](https://education.district0x.io/general-topics/understanding-ethereum/ethereum-sha)
* [Intro to Beam Sync](https://medium.com/@jason.carver/intro-to-beam-sync-a0fd168be14a)
* [Casper 51% Attack](https://ethstaking.io/guide-to-ethereum-proof-of-stake-and-casper)
