# Set Protocol

## Description

Set Protocol allows grouping multiple tokens into one asset.

Each set is a deployed smart contract with each set being fully-collateralized.  Anyone can deposit a token to the set contract and withdraw them back, which makes the sets permissionless.

Sets comply with the ERC20 standard, so they can be transferred and traded on exchanges. This also means that sets can be grouped into other sets.

To reduce friction, users can acquire multi-token sets with a single token (for example, with WETH or DAI). To do that, they will need to make or take an issue order. This order is transported off-chain via issuance relayers for anyone to fill them. Liquidity for the underlying tokens is taken from decentralized exchanges.

Users can opt to a rebalancing set. In a rebalancing set, weights of each token can be realigned to maintain desired properties in a changing market. For example, a rebalancing set can represent equal shares of the top 10 Ethereum tokens. Then, if one of the tokens appreciates in value, the set manager will sell some of it and will buy other tokens in equal amounts to maintain value distribution.

## Important links

* Website: https://setprotocol.com/
* Set explorer: [TokenSets](https://www.tokensets.com/)
