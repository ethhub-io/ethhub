title: Is Ethereum more expensive to use as price rises? - EthHub

description: The Ethereum fee market is independent of fiat prices.

# Is Ethereum more expensive to use as price rises?

## Answer  <a id="answer"></a>

No, the Ethereum fee market is independent of fiat prices.

## Explanation  <a id="explanation"></a>

### Basics of a transaction  <a id="basics-of-a-transaction"></a>

There are many concepts to understand when diving into the answer to this question. First, it's essential to understand how an Ethereum transaction works. As explained in the [gas section](https://docs.ethhub.io/using-ethereum/transactions/#gas), every transaction that occurs on the network requires a set amount of gas, which is a unit used to measure the computational power required to process the transaction. To process a transaction and include it in a block, miners expect to be compensated. This is accomplished by setting a gas price with every transaction, which is the cost of 1 unit of gas, denominated in Gwei \(1 ETH = 1,000,000,000 Gwei\). For example, when you simply send ETH from one account to another, this cost 21000 gas. If you were to set a gas price of 1 Gwei, this transaction would cost 0.000021 ETH.

### Fee market  <a id="fee-market"></a>

Currently, the Ethereum network is working at or near capacity. This means that a [fee market](https://docs.ethhub.io/using-ethereum/transactions/#fee-market) is created because some users may be willing to pay more to get to the front of the line while others may not be in as big of a rush. Tools such as [EthGasStation](https://ethgasstation.info/) offer a great view into the current fee market and what it current costs to get a basic or fast transaction through.

You'll notice that so far, we haven't talked about fiat or the cost of a transaction in fiat value. That's because at its core, the fee market is independent from the cost of Ether. Users have the ability to send a transaction from 0 gas price all the way to as high as they'd like and miners have the ability to accept the same range.

### Rising and falling Ether price   <a id="rising-and-falling-ether-price"></a>

While the gas market by design is purely Ether related, it'd be misleading to not acknowledge that a lot of users and miners think of their fees in fiat terms. So while the above example may have cost 0.000021 ETH, some users will instead think of that in terms of fiat cost \($0.002793 for instance\). This means that the fee market, while independent of fiat prices at its core, will react to moves in Ether prices. If we use the example above and assume price spikes 5x, all of a sudden that transaction will cost $0.0139 in fiat terms. When price spikes \(assuming network demand stays the same\), users will start to lower their gas price. When price falls \(assuming network demand stays the same\), miners will start to raise their minimum accepted gas. We can [see the fluctuation in average gas price](https://etherscan.io/chart/gasprice) in the past.

### Network demand  <a id="network-demand"></a>

As previously mentioned, network demand plays a much larger role on gas price than Ether price. If no one was using the network, gas prices paid would be near 0. If the network is full, gas prices will start to spike. This is an important consideration when trying to draw conclusions between Ether price and gas prices paid.

