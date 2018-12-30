# Is Ether needed for transaction fees?

Yes. The notion that transaction fees on Ethereun can be paid in-protocol by something other than ether (an ERC20 token) is called 'economic abstraction'. Eric Conner explains why the Ethereum protocol is unlikely to integrate economic abstraction below.

Why is economic abstraction used to argue Ether will go to 0? The theory is that users could pay their transaction costs to miners in something other than Ether. Therefore, if that becomes rampant, Ether itself would have no value. This argument can be used against ANY PoW blockchain (yes, even Bitcoin).

Quick recap on how transactions work on Ethereum. Each transaction uses a set amount of gas. Users pay miners to include their transaction using a gas price. Gas * Gas Price = transaction cost. The base protocol assumes gas price in ETH and every wallet calculates transaction cost in total ETH to pay.

The argument against ETH value begins here. It says that users could pay their transaction cost in some token instead of ETH. This is actually true (in a very roundabout way) but it’s very irrational for a user to do this. It adds both friction, cost and a UX nightmare and would typyically look like this:

1. Open communication with a miner 
2. Manually calc the cost of the tx in that tokens value
3. Send miner payment & wait for confirm
4. Execute initial TX and get the nonce
5. Tell the miner the nonce and wait for his next block

On top of the added friction to users mentioned above, there is an added cost to users to pay for their transaction in something other than ETH. Sending ETH in a transaction costs 21000 gas while sending tokens costs 40000 gas or more. Calculating gas cost and understanding the gas market is no easy task. Wallets have spent years making this UX smooth. There is no incentive for a wallet to streamline the payment of gas in tokens as the complexities are deep.

Now let's talk about miners. Miners are trying to make a profit and have to pay for hardware/electricity costs. They do not want to have a portfolio of 50 different ERC20s with wild volatility and no liquidity. This creates an operational nightmare. As mentioned, this is possible on all PoW chains. Bitcoin even has a tool that enables users to pay for transaction speed in payments other than BTC [http://confirmtx.com](http://confirmtx.com). However, because of the arguments above, it's not rampant in BTC or ETH, because it's not logical.

The key that most miss when arguing the above is that Ether has value well beyond just being used to pay for gas in transactions. Proof of Stake will allow users to stake only ETH to secure the network and receive payments for doing so. This is a great value add for ETH.

In 2 years, Ether’s inflation will fall from the current ~7% to near 0. As an in demand asset with rising scarcity, it is a strong store of value. Many open finance applications are coming online and the future looks bright for Ether as money. 

## Resources:
* [Eric Conners Twitter Thread](https://twitter.com/econoar/status/1055845633754447872/)
* [Vitalik Buterins Comment on Economic Abstraction](https://old.reddit.com/r/ethtrader/comments/9ch5ls/the_collapse_of_eth_is_inevitable_techcrunch_can/e5av470/)
