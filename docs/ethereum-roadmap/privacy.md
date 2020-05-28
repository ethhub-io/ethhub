---
title: Privacy on Ethereum - EthHub

description: Solutions proposed to build out privacy technology on Ethereum.
---

# Privacy

## Summary

Privacy on Ethereum is being actively worked on by a number of different teams.

### There are a couple of key technologies to know about:

The main technology used for privacy are called 'zero knowledge proofs'. This technology allows for privacy by mathematically preventing certain information (such as amount, sender, recipient, etc.) from being revealed to the public while the protocol can still guarantee the transaction executes correctly. An older technology called 'Mixers' have some benefits for privacy as well as they serve to obfuscate the data, often making it confusing (or even empirically impossible) to correlate the information correctly.

#### Zero Knowledge-based
  * zk-SNARKs \(used in Zcash\) 
  * zk-STARKs

zk-SNARKs are the more studied type of zero-knowledge proof. Due to their widespread usage, the community is reletively certain of their effectiveness. However, they come with a notable downside. zk-SNARKs rely on a polynomial for determining certain computations in the algorithm. If the full factorization of this polynomial is known by someone, then it is trivial for that person to make proofs for that specific zk-SNARK to say incorrect statements. Therefore, it is required that no single person or entity know the entire factorization of the polynomial.

The main way this has been achieved is by opening up the polynomial creation process publicly. When Zcash did their last fork, they updated their polynomial and underwent a public polynomial creation ("powers of tau ceremony"). If each person privately submits a factor and then destroys that information - so long as a single person in the whole process did it correctly, then no single entity will know the complete factorization. This part is generally called the "trusted setup" of a zk-SNARK. So long as you participated, then you can be 100% certain that this issue is not present.

There are other studied methods to handle this issue. One of the most interesting is to use a specific type of polynomial that only has complex (imaginary) factors. This prevents there from even existing a factorization which could fool the system. However, it is generally accepted that this method is understudied and needs more research before it is ready to secure significant money.

zk-STARKs are a second type of zero-knowledge proof. STARKs rely on slightly different mathematics and dont need a trusted setup. The biggest issue with STARKs is that they require a lot of space (a lot of data for proofs). SNARKs also require a lot of space but more optimizations have been found, making them smaller at the moment. As blockchains are particularly space constrained, the large size of STARKs is a significant issue. There is continued research into reducing the size requirements. But at the moment they are prohibitively large.

Both STARKs and SNARKs require a non-0 amount of computation and so if they are to be implemented at large scale, computation can also become a limiting factor.


[Aztec Protocol](../built-on-ethereum/infrastructure/aztec-protocol.md) is building an efficient zero-knowledge privacy protocol and decentralised exchange. The protocol is already live on Ethereum's mainnet.

[Starkware Industries](https://www.starkware.co/) is using STARK technology to improve scalability and privacy on Ethereum.

[Enigma Protocol](https://blog.enigma.co/welcome-to-enigma-start-here-e65c8c9125ef) are building ['secret contracts'](https://blog.enigma.co/defining-secret-contracts-f40ddee67ef2) which enable [computation over encrypted data](https://blog.enigma.co/computing-over-encrypted-data-d36621458447).

[Zether](https://ethresear.ch/t/zether-the-first-privacy-mechanism-designed-for-ethereum/5029) is a confidential (transaction amounts are hidden) and anonymous (transaction sender and receiver are hidden) payment mechanism on blockchains with the account model like Ethereum. [More info on Zether](https://medium.com/@loveshharchandani/notes-on-zether-towards-privacy-in-a-smart-contract-world-6c4333f975d).


#### Mixers

Mixers work a bit differently to zero-knowledge proof technology. In truth, both technologies work by scrambling transactions together. But Mixers only work with transactions happening at that moment by using a set of fake transactions (called "Mix-ins") plus several real transactions all which sum to approximated the same number of units of ETH. Basically, when you send a transaction for 5 units of ETH, you need to wait for 1 or 2 other people to also send 5 ETH so that you can scramble all 3 transactions together. Mixers send the outputs to a bunch of addresses with smaller amounts which sum to your original units. This way it can be very confusing to line up who sent what to where when you are actively trying to make transactions look similar. The system works better the more people who are using it at that moment.

[Tornado](https://tornado.cash/) is mixer, which uses zk-SNARKS.

[Heiswap](https://heiswap.exchange/) uses [stealth addresses and linkable ring signatures](https://kndrck.co/posts/heiswap_internal_arch_tour/). Currently lives on Ropsten.

Vitalik Buterin created [a post](https://ethereum-magicians.org/t/meta-we-should-value-privacy-more/2475) on EthMagicians calling for more attention towards privacy solutions:
> Mixers

> We can encourage the development of easy-to-use, and importantly decentralized (ie. not just “trustless”, completely serverless) mixers targeting privacy-preserving transfer of small amounts of ETH, so if you want to send gas payment to another account you can do so without linking the two.

> Note that here, one major challenge with (eg. ringsig or zk snark based) smart contract mixers is that if you want to send funds from A to B, B still needs to have ETH to pay gas to submit the proof to receive their funds, and sending that gas would be a privacy leak; this can be solved with a layer-2 protocol where a user can broadcast their proof (including a commitment to what address they want to receive to and what fee they are willing to pay) over something like Whisper, and a specialized set of nodes could accept these proofs, include them into a transaction and pay for the gas, and collect the fee from the recipient. But this protocol needs to be specced out, standardized and implemented…

#### DApp-specific addresses

Vitalik Buterin created [a post](https://ethereum-magicians.org/t/meta-we-should-value-privacy-more/2475) on EthMagicians calling for more attention towards privacy solutions:

> " If we make a default that for every dapp, a user uses a separate account, we have to overcome a few challenges:

> **Address generation:** It would be nice to keep wallet software stateless, so users can easily export and import their keys between wallets; this implies using some deterministic scheme like privkey_for_dapp = hash(master_key + dapp_id). But then what is the dapp_id? How would that work for multi-contract dapps?

> **Dapp interaction:** The most common category here is using ERC20 tokens inside another dapp. What is the workflow by which they would do that? To use KNC on Uniswap, would you first transfer KNC from their “Kyber account” to your “Uniswap account” and then do whatever you wanted to do with Uniswap? Something else? Ideally from a UX point of view, it would still feel like the user makes one operation; the UX of dapps that requires users to sign three transactions in a row to do something honestly really sucks."

## Resources:

* [Master ZKP Reading List](https://zkp.science/)
* [Private DAI transactions on Ethereum using Zk-SNARKs](https://medium.com/@atvanguard/zkdai-private-dai-transactions-on-ethereum-using-zk-snarks-9e3ef4676e22)
* [Explain Like I’m 5: Zero Knowledge Proof](https://hackernoon.com/eli5-zero-knowledge-proof-78a276db9eff)

