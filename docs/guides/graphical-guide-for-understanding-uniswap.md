# A Graphical Guide for Understanding Uniswap

## Summary

Uniswap is an exchange protocol that allows users to trustlessly swap ERC20 tokens. Rather using the traditional order book model, Uniswap pools tokens into smart contracts and users trade against these liquidity pools. Anyone can swap tokens, add tokens to a pool to earn fees, or list a token on Uniswap.

This guide is meant to help beginners understand how Uniswap works under the hood. While the interface may appear simple, there is a lot going on behind the scenes.

*I recommend this [resource](https://defitutorials.substack.com/p/the-ultimate-guide-to-uniswap) if you are interested in understanding how to use the Uniswap specifically.*


## ERC20 Token Primer

ERC20 tokens are the most common type of token built on top of Ethereum. They are [fungible](https://en.wikipedia.org/wiki/Fungibility) in nature, meaning that there isn’t a distinction between individual tokens. For example, if I have 100 metal marbles in my hand that are all the same size and color, it doesn’t matter which one I give you. In the same way, if I have 100 of the same ERC20 token, it doesn’t matter which one I give you. This contrasts with ERC721 tokens which are non-fungible tokens (NFTs) such as cryptokitties.

![fungible token image](/assets/images/uniswap_guide/fungible_tokens.png)

ERC20s can be thought of as the most simple unit of account for a wide range of use cases including currency, rewards points, debt slips, interest accruing bonds, and much more. They are also highly divisible and can be sent in small increments. Since this type of token is so pervasive, it is important to develop a simple way of swapping between them.

*Please view the link [here](https://eips.ethereum.org/EIPS/eip-20) for more information on ERC20s.*


## Overview of Uniswap’s Contracts

When viewing Uniswap’s website, it is important to keep in mind that it is much more than just the interface. Uniswap starndaizes how ERC20s are exchanged with a set of smart contracts. Anyone can build an interface that connects to these contracts and instantly be able to start exchanging with everyone else that is using Uniswap.

There are two different types of contracts that make up Uniswap. The first is known as an Exchange contract. Exchange contracts hold a pool of a specific token and Ether that users can swap against. The second kind of contract is the Factory contract which is in charge of creating new Exchange contracts and registering the ERC20 token address to its Exchange contract address.

![uniswap contract overview](/assets/images/uniswap_guide/uniswap_contract_overview.png)

There are no listing fees to add a token on Uniswap, instead anyone can call a function on the Factory contract to register a new token. The graphic below is an example of when DAI was added to Uniswap. Someone first called the createExchange function in the Factory contract with DAI’s contract address. Then the Factory contract checks it’s registry to see if an Exchange contract has been created for that token address. If no Exchange address is listed, the factory contract deploys an Exchange contract and records the Exchange address in its registry.

![creating new pool](/assets/images/uniswap_guide/new_pool_creation.png)


## Liquidity Pools

Uniswap is unique in that it doesn’t use an order book to derive the price of an asset. In a centralized exchange, such as Coinbase Pro, the price of an asset listed on the exchange is determined by where the highest price someone is willing to pay and the lowest price someone is willing to sell meet. We can see in the image below, that the highest bid price for BTC on Coinbase Pro at that point was $9301.36 and the lowest asking price was $9301.37.

![orderbook example](/assets/images/uniswap_guide/orderbook_example.png)

Instead Uniswap uses the Exchange contracts to pool both Ether and a specific ERC20. When trading Ether for a token, Ether is sent to the contract’s pool and the token is given back to the user. As a result, the user doesn’t need to wait for a counterparty in order to exchange or worry about specifying a price. Since anyone can list a token and users don't need to worry about matching with someone else, it is very easy to avoid any bootstrapping issue when first launching a token.

![swap example](/assets/images/uniswap_guide/swap_example.png)

The amount that is returned from swapping is based on an automated market maker formula. The graph below helps illustrate how the formula works. Essentially, the amount that is returned to you is based on the ratio of Ether to token in in the pool. No matter the size of a swap, the user is guaranteed to have their trade execute because the more of an asset that you add to one side of the pool, the further along the curve it pushes you for the other asset. Meaning the larger the order relative to the pool, the worst rate you will receive as the ratio moves along the curve.

![constant market maker graph](/assets/images/uniswap_guide/market_graph.png)

*You can learn more about the formula [here](https://ethresear.ch/t/improving-front-running-resistance-of-x-y-k-market-makers/1281).*

But if users are only just sending cryptocurrency, how does the ratio of Ether to token remain priced correctly relative to external markets? The answer is the pools maintain a ratio relative to the price of the rest of the market through people [arbitraging](https://en.wikipedia.org/wiki/Arbitrage) the pool. Imagine that the DAI:ETH pool is expressed in terms of a scale and when the scale is balanced the pool is appropriately priced relative to the market price of a centralized exchange. Let’s say that the current price for ETH in USD on a centralized exchange is $150 and the ratio in the Uniswap DAI:ETH pool returns 150 DAI for 1 ETH. As a result, our scale is balanced because the pool matches the current market price on the centralized exchange. 

![scale 150 balanced](/assets/images/uniswap_guide/scale_150_balanced.png)

Now let’s assume that there is a movement in the market that pushes the price of ETH to $100 on the centralized exchange. Due to the price movement, we can now see that our scale is off balance relative to the market price because people can now swap 1 ETH for 150 DAI on Uniswap when the market price on a centralized exchange is $100 for 1 ETH. 

![scale 100 unbalanced](/assets/images/uniswap_guide/scale_100_unbalanced.png)

In response, someone can now put ETH into the pool, draw out DAI, then sell the DAI back for ETH on the centralized exchange for profit, and then repeat. They can do this until the pool has balanced out and reflects the current market price on a different exchange.

![scale 100 balanced](/assets/images/uniswap_guide/scale_100_balanced.png)

As a result, third party arbitrages play a large role in maintaining the correct ratio of token to Ether in Uniswap pools.


## Swapping ERC20 ⇄ ERC20
When interacting with a single Exchange contract, a user is able to swap between Ether and a specific ERC20 token. However, Uniswap does allow users to directly swap an ERC20 to another ERC20 in a single transaction. In the example below, the user has DAI and would like to receive MKR. As a result, the user calls the tokenToTokenSwap function which adds DAI to the DAI pool and kicks ETH to the MKR pool and returns MKR to the address that initially sent the transaction. 

![swapping erc20s](/assets/images/uniswap_guide/swapping_erc20s.png)


## Liquidity Providers

When an Exchange contract is first created for a token, both the token and Ether pools are empty. The first person that deposits into the contract is the one that determines the ratio between the token and Ether. If they deposit a ratio that is different from what the current market rate is, then an arbitrage opportunity is available. When liquidity providers are adding to an established pool, they should add a proportional amount of token and Ether to the pool. If they don’t, the liquidity they added is at risk of being arbitraged as well.

In addition, larger liquidity pools are beneficial to users because they allow for larger swaps to happen without skewing the token to ETH ratio too far along the curve. Uniswap incentives users to add liquidity to pools by rewarding providers with fees that are collected by the protocol. A 0.3% fee is taken for swapping between Ether and a token and roughly a 0.6% is token for token to tokens swaps.

Lastly, special ERC20 tokens known as liquidity tokens are minted to the provider’s address in proportion to how much liquidity they contributed to the pool. The tokens are burned when the user wants to receive the liquidity they contributed plus the fees that we accumulated while their liquidity was locked.

![adding liquidity](/assets/images/uniswap_guide/liquidity_token_image.png)


*I recommend reading [this article](https://medium.com/@pintail/uniswap-a-good-deal-for-liquidity-providers-104c0b6816f2) if you are curious about the advantages and risks of being a liquidity provider.*

## Resources

* [Uniswap Whitepaper](https://hackmd.io/C-DvwDSfSxuh-Gd4WKE_ig)
* [Uniswap — A Unique Exchange](https://medium.com/scalar-capital/uniswap-a-unique-exchange-f4ef44f807bf)
* [Improving front running resistance of x*y=k market makers](https://ethresear.ch/t/improving-front-running-resistance-of-x-y-k-market-makers/1281)