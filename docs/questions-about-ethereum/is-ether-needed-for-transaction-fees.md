title: Is Ether needed for transaction fees?
description: Ether is necessary for Ethereum network security and operational efficiency for miners.

# Is Ether needed for transaction fees?

## Answer

Yes. Ether is necessary for Ethereum network security and operational efficiency for miners.

## Explanation

The notion that transaction fees on Ethereum can be paid in-protocol by something other than ether \(such as an ERC20 token\) is called 'economic abstraction'. We explain why the Ethereum protocol is unlikely to integrate economic abstraction below.

Economic abstraction is often used to argue that the value of Ether will go to 0. The theory is that users could pay their transaction costs to miners in something other than Ether. Therefore, if that becomes rampant, Ether itself would have no value. This argument can be used on any Proof-of-Work blockchain, it's an especially popular criticism against Ethereum since it appears easy to create additional ERC20 tokens that can be exchanged for Ether.

Quick recap on how transactions work on Ethereum. Each transaction uses a set amount of gas. Users pay miners to include their transaction using a gas price. Gas \* Gas Price = transaction cost. The base protocol assumes gas price in ETH and every wallet calculates transaction cost in total ETH to pay.

The argument against ETH value begins here. It says that users could pay their transaction cost in some currency or token instead of Ether, including digital USD. Miners could then directly sell tokens or currency into the currency of their choice. While rebuilding Ethereum to accept multiple currencies \(even USD\) is theoretically possible, this argument ignores how digital native tokens like Ether or Bitcoin act as a layer of security for the system.

Tokens like Ether reduce the profitability of network hacks by tying network security to the value of the network's medium of exchange. If network security gets hit, so does the value of the token transacted on the network. Imagine a rogue miner on Ethereum gathers enough computing power to successfully 51% attack the network and divert the network's currency to a personal account. If the currency's value isn't tied to network security \(say, USD\), the hacker could easily sell these proceeds at full value in reasonably liquid markets. This cannot happen with Ether. Other miners would see this behavior immediately and make it known to relevant markets for Ether. As a result, not only would prices for Ether drop, Ether would also become highly illiquid, making it difficult for the hacker to make off with the pre-hack market value of the stolen Ether. This argument applies for any decentralized blockchain, including Bitcoin.

Practically speaking, paying with multiple currencies also adds friction, cost, and a UX nightmare to the operations of a miner. It would have to go through the following process:

1. Open communication with a miner 
2. Manually calc the cost of the tx in that tokens value
3. Send miner payment & wait for confirm
4. Execute initial TX and get the nonce
5. Tell the miner the nonce and wait for his next block

On top of the added friction to users mentioned above, there is an added cost to users to pay for their transaction in something other than ETH. Sending ETH in a transaction costs 21000 gas while sending tokens costs 40000 gas or more. Calculating gas cost and understanding the gas market is no easy task. Wallets have spent years making this UX smooth. There is no incentive for a wallet to streamline the payment of gas in tokens as the complexities are deep.

Now let's talk about miners. Miners are trying to make a profit and have to pay for hardware/electricity costs. They do not want to have a portfolio of 50 different cryptocurrencies with wild volatility and no liquidity. This creates an operational nightmare. As mentioned, this is possible on all PoW chains. Bitcoin even has a tool that enables users to pay for transaction speed in payments other than BTC [http://confirmtx.com](http://confirmtx.com). However, because of the arguments above, it's not rampant in BTC or ETH because it violates core security assumptions and has extreme practical limitations for miners.

## Resources:

* [Eric Conners Twitter Thread](https://twitter.com/econoar/status/1055845633754447872/)
* [Vitalik Buterins Comment on Economic Abstraction](https://old.reddit.com/r/ethtrader/comments/9ch5ls/the_collapse_of_eth_is_inevitable_techcrunch_can/e5av470/)

