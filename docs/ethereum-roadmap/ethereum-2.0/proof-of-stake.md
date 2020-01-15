title: Ethereum Proof of Stake - EthHub

description: Information on Proof of Stake and how it will work on Ethereum.

# Proof of Stake (PoS)

## Summary

Proof of Stake represents a class of consensus algorithms in which validators vote on the next block, and the weight of the vote depends upon the size of its stake.
It is considered an improvement over Proof of Work (PoW) because of less consumption of electricity, reduced centralization risks, security against different types of 51% attacks, and more.

PoS can be classified into two major types:
* Chain-Based: Rely on the synchronicity of the network
* BFT-Based: Favour consistency of nodes over availability

To participate in voting \(i.e. to become a validator\) you are required to stake ETH for which you'll be rewarded with additional ETH at some interest rate in addition to receiving a portion of the network transaction fees.

## What is Proof of Stake

Proof of Stake \(PoS\) is a category of consensus algorithms for public blockchains that depend on a validator's economic stake in the network. In Proof of Work \(PoW\) based public blockchains \(e.g. Bitcoin and the current implementation of Ethereum\), the algorithm rewards participants who solve cryptographic puzzles in order to validate transactions and create new blocks \(i.e. mining\). In PoS-based public blockchains \(e.g. Ethereum's upcoming Casper implementation\), a set of validators take turns proposing and voting on the next block, and the weight of each validator's vote depends on the size of its deposit \(i.e. stake\). Significant advantages of PoS include security, reduced risk of centralization, and energy efficiency.

In general, a PoS algorithm looks as follows. The blockchain keeps track of a set of validators, and anyone who holds the blockchain's base cryptocurrency \(in Ethereum's case, ETH\) can become a validator by sending a special type of transaction that locks up their ETH into a deposit. The process of creating and agreeing to new blocks is then done through a consensus algorithm in which all current validators can and are expected to participate.

There are many kinds of consensus algorithms, and many ways to assign rewards to validators who participate in the consensus algorithm, so there are many "flavors" of PoS. From an algorithmic perspective, there are two major types: chain-based and BFT-style PoS.

In chain-based PoS, the algorithm pseudo-randomly selects a validator during each time slot \(e.g. every period of 10 seconds might be a time slot\), and assigns that validator the right to create a single block, and this block must point to some previous block \(normally the block at the end of the previously longest chain\), and so over time most blocks converge into a single constantly growing chain.

In BFT-style PoS, validators are randomly assigned the right to propose blocks, but agreeing on which block is canonical is done through a multi-round process where every validator sends a "vote" for some specific block during each round, and at the end of the process all \(honest and online\) validators permanently agree on whether or not any given block is part of the chain. Note that blocks may still be chained together; the key difference is that consensus on a block can come within one block, and does not depend on the length or size of the chain after it.

### What are the benefits of Proof of Stake over Proof of Work?

* No need to consume large quantities of electricity in order to secure a blockchain. \(It's estimated that both Bitcoin and Ethereum burn over $1 million worth of electricity and hardware costs per day as part of their consensus mechanism.\)
* Because of the lack of high electricity consumption requirements there is not as much need to issue as many new coins in order to motivate participants to keep participating in the network. It may theoretically even be possible to have negative net issuance, where a portion of transaction fees is "burned" thus decreasing the supply over time.
* Proof of Stake opens the door to a wider array of techniques that use game-theoretic mechanism design in order to more effectively discourage centralized cartels from forming and, if they do form, from acting in ways that are harmful to the network \(such as selfish mining in Proof of Work\).
* Reduced centralization risks, as economies of scale are much less of an issue. $10 million of coins will get you exactly 10 times higher returns than $1 million of coins, without any additional disproportionate gains because at the higher level you can afford better mass-production equipment, which is an advantage for Proof of Work.
* Ability to use economic penalties to make various forms of 51% attacks vastly more expensive to carry out than Proof of Work. To paraphrase Vlad Zamfir, "it's as though your ASIC farm burned down if you participated in a 51% attack".

### What would the equivalent of a 51% attack against Casper look like?

There are four basic types of 51% attack:

* Finality reversion: validators that already finalized block A then finalize some competing block A', thereby breaking the blockchain's finality guarantee.
* Invalid chain finalization: validators finalize an invalid \(or unavailable\) block.
* Liveness denial: validators stop finalizing blocks.
* Censorship: validators block some or all transactions or blocks from entering the chain.

In the first case, users can socially coordinate out-of-band to agree which finalized block came first, and favor that block. The second case can be solved with fraud proofs and data availability proofs. The third case can be solved by a modification to PoS algorithms that gradually reduces \("leaks"\) non-participating nodes' weights in the validator set if they do not participate in consensus; the Casper FFG paper includes a description of this.

The fourth is most difficult. The fourth can be recovered from via a "minority soft fork", where a minority of honest validators agree the majority is censoring them, and stop building on their chain. Instead, they continue their own chain, and eventually the "leak" mechanism described above ensures that this honest minority becomes a 2/3 supermajority on the new chain. At that point, the market is expected to favor the chain controlled by honest nodes over the chain controlled by dishonest nodes.

## Staking Logistics

### Why would I want to stake my ETH?

For staking your ETH and attesting to correct blocks, you will be rewarded with additional ETH through a network wide interest rate as well as receive a portion of network transaction fees. Details can be found [here](https://docs.ethhub.io/ethereum-roadmap/ethereum-2.0/eth-2.0-economics).

### What are the minimum requirements to stake?

* A minimum of 32 ETH per validator
* Computer with sufficient hardware specs
* Internet connection

### What software do I need to run to stake?

There are two main types of software to be aware of when considering staking on Ethereum:

* Beacon nodes: This is the hub for your validators. 
  * Stores canonical state, handles peers and incoming sync, propagates blocks and attestations.
  * Has a gRPC server that clients can connect to and provides a public API.
* Validator clients: Talks to your beacon node and signs blocks. You can have multiple of these at 32 ETH each.
  * Stores important secrets such as RANDAO reveal, proof of custody for shared data, and BLS private key.
  * Can swap underlying beacon nodes efficiently.
  * Tracks shared state execution data and data blobs that the validator has signed.

This means that there are three possible combinations of software to run:

1. Beacon node only
2. Beacon node + validator client
3. Beacon node + multiple validator clients

### What are the hardware requirements to run this software?

Still TBD. Ideally we can get minimum requirements for all three setups mentioned above.

### What happens if I lose my internet connection while staking?

The key to being a validator is to ensure that you are consistently available to vote for blocks which in turn secures the network. Therefore, there is a slight penalty if your validator client goes offline at any point, in order to encourage validator availability. There are two scenarios where this can happen:

1. If blocks are finalizing and you're offline, you can lose x% of your deposit over a year where x=current\_interest
   * For example, if the current interest rate is 5%, you would lose 0.0137% of your deposit every day, but gain that for every day you're online.
2. If blocks aren't finalizing \(&gt;33% of validators are offline\) and you're offline, you can lose 60% in 18 days. 

If at any point your deposit drops below 16 ETH you will be removed from the validator set entirely.

### How long is my Ether locked up if I stake?

There is a withdraw queue that you are placed into when wanting to withdraw ETH from your validator. If there is no queue, then the minimum withdraw time is 18 hours and adjusts dynamically depending on how many people are withdrawing at that time.

### Resources

* [Proof of Stake FAQ](https://github.com/ethereum/wiki/wiki/Proof-of-Stake-FAQ)
* [CBC Casper Resources](https://docs.google.com/document/d/1Iz4d5qhb5OeIajTwfmdE0DZeWjxq7ebD70_0WWOqGa8/edit#)
* [Beacon and Validator explanations](https://twitter.com/terencechain/status/1070738081337106432)
* [Some details around staking from Vitalik](https://www.reddit.com/r/ethereum/comments/a41u9k/_/ebbm03t/?context=1)

