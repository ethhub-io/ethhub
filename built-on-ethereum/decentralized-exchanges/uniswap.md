# Uniswap

## Description

Uniswap is a decentralized token exchange protocol that utilizes a "constant product market maker" model. This model allows defining the asset price based on the available staked liquidity of traded assets. There is no token to facilitate the exchange as ether is used as an intermediary of each trade.

In Uniswap, each token has its own smart contract and liquidity pool. If there’s no smart contract for a given token, anyone can create one using the 'factory' contract. Only one contract can be deployed for each token address.

The price of tokens is based on the amount of liquidity in the contract. That is, if someone is buying a token with ETH, the supply of that token in the pool will decrease while the supply of ether will increase, so the price of the token will increase. If someone is selling token with ETH, the price of the token will decrease. In other words, token price reflects the supply and demand of that token. In case a token price significantly shifts from its market price, arbitrage opportunities are created, and the price will eventually be corrected.

Anyone can send their tokens and ether to the liquidity pool. There is a small fee \(0.3%\) for each trade which is given to liquidity providers to incentivize pooled liquidity.

## Important links

* Website: [https://uniswap.io/](https://uniswap.io/)
* Exchange: [https://uniswap.exchange/](https://uniswap.exchange/)

