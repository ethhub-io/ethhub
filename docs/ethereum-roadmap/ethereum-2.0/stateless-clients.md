title: Stateless-Clients - Ethhub

description: Exploring the stateless client and how this implementation of data processing and storing could greatly reduce the
workload on the Ethereum blockchain, improving performance and scalability.

# Stateless Clients

## Introduction

Ethereum is based on blockchain technology.  A blockchain is defined as a "cryptographically secure transactional singleton machine with shared-state."  

* "Cryptographically secure" means that creation and movement of the digital currency is mathematically obscured by extremely complex algorithms nearly impossible to decode.  

* "Transaction singleton machine" means a single canonical instance of the machine is being created in the system to handle transactions.  This is a singular truth that all participants on the network believe in.  

* "With shared-state" means that the state of the machine is stored and shared with everyone.

This is an examination of the concept of state in a virtual machine which introduces the concept of a stateless client in Ethereum.

## What does state mean?

State defines the values contained in a block at any given time.  The state of the virtual machine changes after each set of transactions are processed.

![Flow of transactions causing a state change.](https://miro.medium.com/max/1282/1*jZ-VRXBJtOnePofB0z2Q8A.png "State changes")

## State-defining Objects

###  Account State

The global "shared-state" is comprised of many objects called accounts.  Two types of accounts exist, externally owned and contract accounts.  Externally owned accounts are  controlled by private keys and have no code associate with them.  Contract accounts are controlled by their contract code and have code associated with them.

Account state is further broken down into:

* nonce: For externally owned accounts this refers to number of transactions sent from the address.  Contract accounts would store the number of contracts created by the account.

* balance:  The amount of Ether stored on the account.

* storageRoot: A hash of the root node of a Merkle Patricia tree.  This encodes a hash of storage contents on the account.

* codeHash: The hash of the EVM (Ethereum Virtual Machine) code of this account.  Contract account code gets hashed and stored here.  Externally owned accounts contain the hash of an empty string.

### World State

World state is a mapping of account addresses between account states.  This mapping is stored as a Merkle Patricia tree.

![https://miro.medium.com/max/1488/1*N8YtAcAqdtHtzUaZAJgUJQ.png](https://miro.medium.com/max/1488/1*N8YtAcAqdtHtzUaZAJgUJQ.png "State Tree")

This same structure is used to store transactions and receipts.  This becomes a large amount of data which needs to be stored and processed if the entire state is stored and traversed when creating new blocks.

## Ethereum Stateless Client

The way a block is constructed on Ethereum offers a method to create a sort of stateless client.  It is important to know that as Ethereum evolves, statelessness is ultimately going to be a spectrum.  Some knowledge of data in surrounding nodes will be required in order to create valid hashes.

![Ethereum Block Header](https://miro.medium.com/max/1056/1*4EQFjXD2-dbiVgVv-8Si8g.png "Ethereum Block Header")

Statelessness allows the creation of light nodes.  A light node contains only the chain of headers without the execution of any transactions or associated states.

When a node comes online it will be fully stateless since it will hold zero information regarding state.  Over time it will soak up the
state as transactions touch upon it, putting together a more complete state with every change of state presented.  New nodes will be more stateless offering benefits of lower memory usage, disk, and I/O.  Bandwidth usage will be the highest because peers need to send larger
proofs to the new node as it develops its own state data.  More stateful clients will have higher demands on memory, disk, and I/O while
bandwidth requirements would decrease.  Nodes can become more stateful until a certain tradeoff point is reached and then halted from
further acquisition of state information to optimize the trade off in computing power and bandwidth.

## Applications of Stateless Clients in Ethereum

Ethereum 1.X implements stateless clients but not stateless miners.  Fast sync initializes as a stateless node.  
It creates what is called a launch-block and only records the input and output state of this block locally.  The launch block is
a predetermined block number that is a certain amount of time in the future.  The future dated deadline is so that the node can work
on constructing the launch-block.  Witness data is called by the node to construct blocks.  As long as the launch-block is created early
or on time, the creation of blocks will continue and the node is active.  Use of witness data and input/output states only make this a
stateless client.

Ethereum 2.0 implements stateless clients and stateless miners in Sharding.  All nodes are stateless so that faster processing with less data
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
* [Casper 51% Attack](https://ethstaking.io/guide-to-ethereum-proof-of-stake-and-casper/casper-51-attack/)
* [Ethereum Platform Review Opportunities and Challenges for Private and Consortium Blockchains](http://www.smallake.kr/wp-content/uploads/2016/06/314477721-Ethereum-Platform-Review-Opportunities-and-Challenges-for-Private-and-Consortium-Blockchains.pdf)
* [How Does Ethereum Work Anyway?](https://medium.com/@preethikasireddy/how-does-ethereum-work-anyway-22d1df506369)
* [Early Eth1<->Eth2 Switch is official!](https://etherworld.co/2020/01/09/early-eth1-eth2-switch-is-official/)
