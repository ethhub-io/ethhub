title: Privacy on Ethereum - EthHub
description: Solutions proposed to build out privacy technology on Ethereum.

# Privacy

## Summary

Privacy on Ethereum is being actively worked on by a number of different teams.

### There are a couple of key technologies to know about:

#### Zero Knowledge-based
  * zk-SNARKs \(used in Zcash\) 
  * zk-STARKs

[Aztec Protocol](../built-on-ethereum/infrastructure/aztec-protocol.md) is building an efficient zero-knowledge privacy protocol and decentralised exchange. The protocol is already live on Ethereum's mainnet.

[Starkware Industries](https://www.starkware.co/) is using STARK technology to improve scalability and privacy on Ethereum.

[Enigma Protocol](https://blog.enigma.co/welcome-to-enigma-start-here-e65c8c9125ef) are building ['secret contracts'](https://blog.enigma.co/defining-secret-contracts-f40ddee67ef2) which enable [computation over encrypted data](https://blog.enigma.co/computing-over-encrypted-data-d36621458447).

[Zether](https://ethresear.ch/t/zether-the-first-privacy-mechanism-designed-for-ethereum/5029) is a confidential (transaction amounts are hidden) and anonymous (transaction sender and receiver are hidden) payment mechanism on blockchains with the account model like Ethereum. [More info on Zether](https://medium.com/coinmonks/notes-on-zether-towards-privacy-in-a-smart-contract-world-6c4333f975d).

#### Mixers
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

* [Private DAI transactions on Ethereum using Zk-SNARKs](https://medium.com/@atvanguard/zkdai-private-dai-transactions-on-ethereum-using-zk-snarks-9e3ef4676e22)
* [Explain Like I’m 5: Zero Knowledge Proof](https://hackernoon.com/eli5-zero-knowledge-proof-78a276db9eff)

