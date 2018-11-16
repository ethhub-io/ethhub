# Set Protocol

## Description

Set Protocol allows grouping multiple tokens into one asset.

Each set is a deployed smart contract. Therefore, sets are fully-collateralized.  Anyone can deposit token to the set contract and withdraw them back, meaning that sets are also permissionless.

Sets comply with the ERC20 standard, so they can be transferred and traded on exchanges. This also means that sets can be grouped into other sets.

To reduce friction, users can acquire multi-token sets with a single token (for example, with WETH or DAI). To do that, they will need to make or take an issue order. This order is transported off-chain via issuance relayers for anyone to fill them. Liquidity for underlying tokens will be taken from the decentralized exchanges.

Users can opt to a rebalancing set. In a rebalancing set, weights of each token can be realigned to maintain desired properties in a changing market. For example, rebalancing set can represent equal shares of the top 10 Ethereum tokens. Then, if one of the tokens will appreciate in value, the set manager will sell some of it and will buy other tokens in equal amounts to maintain value distribution.

## Important links

* Website: https://setprotocol.com/
* Set explorer: [TokenSets](https://www.tokensets.com/)
