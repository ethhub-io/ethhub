title: Oracles on Ethereum - EthHub

description: Oracles refers to a number of decentralized protocols building means for smart contracts to access data from the world outside Ethereum.

# Oracles

## Summary

Smart contracts on Ethereum are fully self-contained and any information or access to off-chain data is restricted. This is required for security reasons as execution in blockchains must be deterministic and the response to subsequent calls to outside API's could change in unknown ways. Nevertheless, certain desirable types of smart contracts are only possible with additional outside data.

An [Oracle](https://ethereum.stackexchange.com/questions/85178/what-is-a-blockchain-oracle) is a conceptual solution which takes real-world off-chain data and submits an immutable copy of this information into blocks – thereby making it available for future smart contract use.

## The Oracle Problem 

The (‘Oracle’) problem is that there are no currently successful decentralized designs. Therefore, all currently functioning oracles are centralized and introduce a series of attack vectors & issues including:

* Accuracy – even without malice, a centralized entity is often mistaken about the status or value of something. This prevents an oracle from providing the “real” answer to be memorialized on the blockchain.
* Gaming – many oracles are critical for the functioning of smart contracts holding significant amounts of assets. If an attacker can trick the oracle into changing its value then it becomes quite simple to steal assets.
* Consistency – the most desired oracles are information streams, where the values change constantly. This means users expect oracles to accurately and consistently provide information on a certain schedule (often every block). However, there is no guarantee that a transaction (to post the information) will be certain to enter a block, no matter the fee that is paid. This is both a usability issue and an attack vector.

## Solutions

Solutions to the oracle problem center around ways to both validate the data being queried and also place this data on chain in both an available and non-centralized manner. The solutions come in two forms. One is to make your centralized oracles better and the second is to make your oracles decentralized.

In certain cases, a centralized oracle may be the best solution. 

For example, for a proprietary dataset which is posted directly by the owner with a widely accepted signature. An example might be a centralized exchange’s daily settlement value posted to the exchange’s website and certified by the exchange’s private key. In such a case, no new risks are incurred by using this oracle above what was already incurred by using the centralized price feed in general.

In other cases, a decentralized solution is desirable. This is an active area of research but attempted solutions include consensus-based truth, schelling point oracles (e.g. prediction markets), staked reporters (skin-in-the-game), trusted execution environments (TEEs), and many combinations of the various game theoretic crypto-economic security measures.

The main drawback with most of these methods is the same main drawback of blockchains in general. Data points (from the oracle) like blocks (on a blockchain), can only be trusted up to a certain threshold (“this number/block is correct or $50k will be slashed”). But again, like a blockchain, in certain circumstances by gaming the oracle, an attacker can make more than $50k. So designing systems where assets at stake actually guarantee the validity of the number/content/block is hard and continues to be researched.

## Resources
[Decentralized Oracles](https://medium.com/fabric-ventures/decentralised-oracles-a-comprehensive-overview-d3168b9a8841)
