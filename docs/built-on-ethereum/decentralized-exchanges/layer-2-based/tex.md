title: TEX by Liquidity Network - Ethhub

description: TEX is a decentralized exchange.

# TEX

## Description

TEX is a commit-chain based decentralized exchange, built on top of the [NOCUST commit-chain](../../../ethereum-roadmap/layer-2-scaling/commit-chains.md) by the Liquidity Network team.

TEX works so that final trades periodically get broadcasted on-chain in bulks, but transactions have instant finality within the commit-chain.

Orders are kept similarly to off-chain order book exchanges, but the order host (the operator) is unable to front-run orders due to the novel concept of 'moonwalk orders'.

Moonwalk orders use time-lock puzzles, ZKPs and Merkle tree ranges, which make it impossible for the operator to decrypt the order before it becomes suspicious and the operator’s actions can be challenged.

### Pros
* Faster order management than on-chain solutions
* Faster trade settlement than other solutions
* Does not require any blockchain transaction fees
* Orders can’t be front run by the operator like other relayer based models

### Cons
* Inherits the potential weaknesses of the underlying layer 2 solution

## Interface

![](https://i.imgur.com/eCdaoII.png)

## Liquidity Network as exchange protocol

TEX is built on Liquidity Network's client library, which is a commit-chain layer 2 scaling solution for Ethereum based on academic research and papers.

Similar to 0x, anyone is free to build an exchange on top of Liquidity Network.

## Resources

* [TEX Website](https://tex.liquidity.network/) 
* [Liquidity Network](https://liquidity.network/)  
* [Liquidity Network Client Library](https://docs.liquidity.network/)  
