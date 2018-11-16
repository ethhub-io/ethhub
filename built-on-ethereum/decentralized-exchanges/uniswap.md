# Uniswap

## Description

Uniswap is a decentralized token exchange protocol that utilizes “Constant product market maker“ model. This model allows defining asset price based on the available staked liquidity of traded assets. There is no token to facilitate the exchange: ether used as an intermediary of each trade.

In Uniswap, each token has its own smart contract and liquidity pool. In case there’s no smart contract for a given token, anyone can create one using Factory contract. Only one contract can be deployed for each token address.

The price of tokens is based on the amount of liquidity in the contract. That is, if someone is buying a token with ETH, the supply of that token in the pool will decrease while the supply of ether will increase, so the price of the token will increase. If someone is selling token with ETH, the price of the token will decrease. In other words, token price reflects supply and demand of that token. In case a token price will significantly shift from its market price, arbitrage opportunity will be created, and the price will be eventually corrected.

Anyone can send his tokens and ether to the liquidity pool. There is a small fee for each trade which is given to liquidity providers to incentivize staking.

## Important links

* Website: https://uniswap.io/
* Exchange: https://uniswap.exchange/
