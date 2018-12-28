# Proof of Stake

## What is Proof of Stake
Proof of Stake (PoS) is a category of consensus algorithms for public blockchains that depend on a validator's economic stake in the network. In proof of work (PoW) based public blockchains (e.g. Bitcoin and the current implementation of Ethereum), the algorithm rewards participants who solve cryptographic puzzles in order to validate transactions and create new blocks (i.e. mining). In PoS-based public blockchains (e.g. Ethereum's upcoming Casper implementation), a set of validators take turns proposing and voting on the next block, and the weight of each validator's vote depends on the size of its deposit (i.e. stake). Significant advantages of PoS include security, reduced risk of centralization, and energy efficiency.

In general, a proof of stake algorithm looks as follows. The blockchain keeps track of a set of validators, and anyone who holds the blockchain's base cryptocurrency (in Ethereum's case, ether) can become a validator by sending a special type of transaction that locks up their ether into a deposit. The process of creating and agreeing to new blocks is then done through a consensus algorithm that all current validators can participate in.

There are many kinds of consensus algorithms, and many ways to assign rewards to validators who participate in the consensus algorithm, so there are many "flavors" of proof of stake. From an algorithmic perspective, there are two major types: chain-based proof of stake and BFT-style proof of stake.

In chain-based proof of stake, the algorithm pseudo-randomly selects a validator during each time slot (e.g. every period of 10 seconds might be a time slot), and assigns that validator the right to create a single block, and this block must point to some previous block (normally the block at the end of the previously longest chain), and so over time most blocks converge into a single constantly growing chain.

In BFT-style proof of stake, validators are randomly assigned the right to propose blocks, but agreeing on which block is canonical is done through a multi-round process where every validator sends a "vote" for some specific block during each round, and at the end of the process all (honest and online) validators permanently agree on whether or not any given block is part of the chain. Note that blocks may still be chained together; the key difference is that consensus on a block can come within one block, and does not depend on the length or size of the chain after it.

## What are the benefits of proof of stake as opposed to proof of work?

* No need to consume large quantities of electricity in order to secure a blockchain (e.g. it's estimated that both Bitcoin and Ethereum burn over $1 million worth of electricity and hardware costs per day as part of their consensus mechanism).

* Because of the lack of high electricity consumption, there is not as much need to issue as many new coins in order to motivate participants to keep participating in the network. It may theoretically even be possible to have negative net issuance, where a portion of transaction fees is "burned" and so the supply goes down over time.

* Proof of stake opens the door to a wider array of techniques that use game-theoretic mechanism design in order to better discourage centralized cartels from forming and, if they do form, from acting in ways that are harmful to the network (e.g. like selfish mining in proof of work).

* Reduced centralization risks, as economies of scale are much less of an issue. $10 million of coins will get you exactly 10 times higher returns than $1 million of coins, without any additional disproportionate gains because at the higher level you can afford better mass-production equipment, which is an advantage for Proof-of-Work.

* Ability to use economic penalties to make various forms of 51% attacks vastly more expensive to carry out than proof of work - to paraphrase Vlad Zamfir, "it's as though your ASIC farm burned down if you participated in a 51% attack".

What would the equivalent of a 51% attack against Casper look like?
There are four basic types of 51% attack:

* Finality reversion: validators that already finalized block A then finalize some competing block A', thereby breaking the blockchain's finality guarantee.

* Invalid chain finalization: validators finalize an invalid (or unavailable) block.

* Liveness denial: validators stop finalizing blocks.

* Censorship: validators block some or all transactions or blocks from entering the chain.

In the first case, users can socially coordinate out-of-band to agree which finalized block came first, and favor that block. The second case can be solved with fraud proofs and data availability proofs. The third case can be solved by a modification to proof of stake algorithms that gradually reduces ("leaks") non-participating nodes' weights in the validator set if they do not participate in consensus; the Casper FFG paper includes a description of this.

The fourth is most difficult. The fourth can be recovered from via a "minority soft fork", where a minority of honest validators agree the majority is censoring them, and stop building on their chain. Instead, they continue their own chain, and eventually the "leak" mechanism described above ensures that this honest minority becomes a 2/3 supermajority on the new chain. At that point, the market is expected to favor the chain controlled by honest nodes over the chain controlled by dishonest nodes.


## Resources: https://github.com/ethereum/wiki/wiki/Proof-of-Stake-FAQs

