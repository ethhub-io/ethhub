# Understanding Uniswap

## Summary

Uniswap is an exchange protocol that allows users to trustlessly swap ERC20 tokens. Rather using the traditional order book model, Uniswap pools tokens into smart contracts and users trade against these liquidity pools. Anyone can trustless swap tokens, add tokens to the pool to earn fees, or list a token on Uniswap.

This guide is meant to help beginners understand how Uniswap works under the hood. While the interface may appear simple, there is a lot going on behind the scenes.

*I recommend this [resource](https://defitutorials.substack.com/p/the-ultimate-guide-to-uniswap) if you are more interested in understanding how to use the Uniswap interface rather than how it works.*


## Why Decentralized Exchanges are Interesting

It is important to have some context as to why decentralized exchanges are useful. First, users are able to custody their own funds and don’t need to worry about needing to deposit their cryptocurrency into a custodial account. This is important due to the amount of hacks that happen to exchanges in the cryptocurrency space. Second, the fact that these decentralized exchanges live on the blockchain means that they are easily able to operate with other protocols built on top of Ethereum. Lastly, there is a 100% uptime for the exchange since the code lives on the blockchain and not on a centralized server.


## ERC20 Token Primer

ERC20 tokens are the most common type of token built on top of Ethereum. They are [fungible](https://en.wikipedia.org/wiki/Fungibility) in nature, meaning that there isn’t a distinction between individual tokens. For example, if I have 100 metal marbles in my hand that are all the same size and color, it doesn’t matter which one I give you. In the same way, if I have 100 of all the same ERC20 token and I give you one token, it doesn’t matter which one I give you. This contrasts with ERC721 tokens which are non-fungible tokens (NFTs) such as cryptokitties.

!['fungible token image'](/docs/assets/images/uniswap_guide/fungible_tokens.png)

ERC20s can be thought of as a simple unit of account for a wide range of use cases including currency, rewards points, debt slips, interest accruing bonds, and much more. They are also highly divisible and can be sent in small increments. Since this type of token is so pervasive, it is important to develop a simple way to swapping between them.

*Please view the link [here](https://eips.ethereum.org/EIPS/eip-20) for more information on ERC20s.*


## Overview of Uniswap’s Contracts

When viewing Uniswap’s website, it is important to keep in mind that it is much more than just the interface. Uniswap starndaizes how ERC20s are exchanged with a set of smart contracts. Anyone can build an interface that connects to their contracts and instantly be able to start exchanging with everyone else that is using Uniswap. In addition, for machines, they simply need to know the addresses of the contracts and with a little extra code, they too are able to trade on Uniswap as well. 

There are two different types of contracts that make up Uniswap. The first type is known as an Exchange contract. Exchange contracts hold a pool of a specific token and Ether which users can swap against. The second kind of contract is the Factory contract which is in charge of creating new Exchange contracts and registers the ERC20 token address address to its Exchange contract address.

!['uniswap contract overview'](/docs/assets/images/uniswap_guide/uniswap_contract_overview.png)

There are no listing fees to add a token on Uniswap, instead any can call a function on the Factory contract to register a new token. The Factory contract checks with its records to see if that token already has an exchange contract. If it doesn’t then a new Exchange contract is deployed, however, each unique token can only have one exchange contract.


## Liquidity Pools
Uniswap is unique in that an order book isn’t used to derive the price of an asset. In a traditional exchange, such as Coinbase Pro, the price of an asset listed on the exchange is determined by the highest price someone is willing to pay and the lowest price someone is willing to sell meet. We can see in the image below, that the highest bid price for BTC on Coinbase Pro at that point was $9301.36 and the lowest asking price was $9301.37.

!['orderbook example'](/docs/assets/images/uniswap_guide/orderbook_example.png)

Instead Uniswap uses Exchange contracts to pool both Ether and a specific ERC20. When trading Ether for a token, Ether is sent to the contract’s pool and the token is given back to the user. As a result, the user doesn’t need to wait for a counterparty in order to exchange or worry about specifying a price. Since anyone can add a token and you don’t need to worry about matching with someone else, it is very easy to avoid any bootstrapping issue when first launching a token.

!['swap example'](/docs/assets/images/uniswap_guide/swap_example.png)

The amount that is returned from swapping is based on a constant market maker formula. The graph below illustrates how the formula works. Essentially, a user is guaranteed to have their trade executed due to the fact that no matter how much of an asset you put into the contract, there will always be some amount returned back to you. This is due to the fact that the more that you add to one side of the pool the further along the line it pushes you for the other asset and the worse return you get.

!['constant market maker graph'](/docs/assets/images/uniswap_guide/market_graph.png)

*You can learn more about the formula [here](https://ethresear.ch/t/improving-front-running-resistance-of-x-y-k-market-makers/1281).*

But if users are only just sending cryptocurrency and a not specifying a price and the formula determines the output of swap, how does the ratio of Ether to token remain priced correctly in the Exchange contract? The answer is the pools maintain a price relative to the rest of the market through people [arbitraging](https://en.wikipedia.org/wiki/Arbitrage) the pool. 

Imagine that the DAI:ETH pool is expressed in terms of a scale and when the scale is balanced, the pool is appropriately priced relative to the market price of a centralized exchange. Let's make this more clear with an example. Let’s say that the current price for ETH in USD on a centralized exchange is $150 and the ratio in the Uniswap DAI:ETH pool is 150 Dai for 1 Eth. As a result, our scale is balanced because the pool reflects what the market price is. 

!['scale 150 balanced'](/docs/assets/images/uniswap_guide/scale_150_balanced.png)

Now let’s assume that there is a movement in the market that pushes the price of ETH to $100 on the centralized exchange. Due to the price movement we can now see that our scale is off balance relative to the market price because people can now buy 1 ETH for 150 DAI when the market price on a centralized exchange is $100 for 1 ETH. 

!['scale 100 unbalanced'](/docs/assets/images/uniswap_guide/scale_100_unbalanced.png)

In response, someone can now put ETH into the pool, draw out DAI, then sell the DAI back for ETH on the centralized exchange, and repeat. They can do this until the pool has balanced out and reflects the current market price on a different exchange.

!['scale 100 balanced'](/docs/assets/images/uniswap_guide/scale_100_balanced.png)


## Swapping ETH ⇄ ERC20
As stated before each Exchange contract contains a pool of both Ether and a specific ERC20 token. In other decentralized exchanges, in order to trade Ether for tokens the Ether will need to be converted to WETH in order to exchange Ether for tokens. With Uniswap a user does not need to  convert to WETH. However, when either going from ERC20 to ETH or vice versa there is 0.03% fee that is taken to incentivise people to contribute liquidity to the pool.


## Swapping ERC20 ⇄ ERC20
Uniswap allows users to directly swap an ERC20 to another ERC20 in a single transaction. In the image below, a user calls the tokenToTokenSwap() function and passes in address of the token they would like to receive. In the example below, the user has DAI and would like to receive Maker. So they call the tokenToTokenSwap function which adds DAI to the DAI Exchange pool and kicks Ether to the MKR Exchange contract pool and returns MKR to the user that initially sent the transaction. Since the user is going into and out of two different pool, the fee is roughly 0.06%

!['swapping erc20s'](/docs/assets/images/uniswap_guide/swapping_erc20s.png)


## Listing a New Token

One of the most interesting aspects of Uniswap is that anyone can create a liquidity pool for any ERC20. No permission or no listing fees are needed. However, only one pool can only be created once for each token. The graphic below is an example of when DAI was added to Uniswap. Someone first called the createExchange function in the Factory contract with DAI’s contract address. The Factory contract checks it’s registry to see if an Exchange contract has been created for that token address. If there is no Exchange address listed, the factory contract deploys an exchange contract and records the Exchange address in its registry.

!['creating new pool'](/docs/assets/images/uniswap_guide/new_pool_creation.png)

Initially, the contract’s Eth and token pool will be empty. As a result, the first person to provide liquidity to the pool is the one that sets the ratio. However, if the ratio is off from what the current market rate, then someone can step in to correct the ratio of the pool by arbitraging the pool. 


## Liquidity Providers

When an Exchange contract is first created for a token, both the pools are empty. The first person that deposits into the contract is the one that determines the ratio between the token and Ether. If they deposit a ratio that is different from what the current market rate is, then an arbitrage opportunity is available. 

Special tokens known as liquidity tokens which are minted to the address in proportion to how much liquidity the user contributed to the pool. The tokens are burned when the user gives them back to the contract in exchange for the liquidity they contributed plus the fees that we accumulated while their liquidity was locked. 

I recommend reading [this article](https://medium.com/@pintail/uniswap-a-good-deal-for-liquidity-providers-104c0b6816f2) if you are curious about the advantages and risk of being a liquidity provider


## Swapping vs Transferring
Uniswap also has one unique feature that doesn’t get brought up too often, which is that after either a token or Ether is deposited, you are able to forward the funds in the same transaction to another address. Rather than swapping, this is referred to as transferring in the white paper. Rather than calling ethToTokenSwap(), tokenToEthSwap(), or tokenToTokenSwap() to have the tokens be sent back to the address that sent the transaction, a user can call and pass in a specified address to either ethToTokenTransfer(), tokenToEthTransfer(), or tokenToTokenTransfer() on an exchange contract.


## Resources

* [Uniswap Whitepaper](https://hackmd.io/C-DvwDSfSxuh-Gd4WKE_ig)
* [Uniswap — A Unique Exchange](https://medium.com/scalar-capital/uniswap-a-unique-exchange-f4ef44f807bf)
* [Improving front running resistance of x*y=k market makers](https://ethresear.ch/t/improving-front-running-resistance-of-x-y-k-market-makers/1281)