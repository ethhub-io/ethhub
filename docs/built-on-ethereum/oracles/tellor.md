title: Tellor - EthHub

description: Tellor is a decentralized oracle.  

# Tellor

## Summary

Tellor is a decentralized oracle that provides off-chain pricing data for smart contracts on the Ethereum network.  Tellor formed in March 2019, was  part of the Binance Labs incubator and launched to mainnet in August 2019.  

## How Tellor Works

The Tellor network mints a token, Tributes (TRB).  Tellor utilizes a network of miners, required to stake 1000 TRB, competing to solve PoW challenges for the right to submit data to Tellor’s on-chain price feed database.  A user submits a query to the Oracle using TRB to incentivize miners to choose this query over other submissions.  Other users who want the same data ‘tip’ this data series to further incentivize selection by miners.  Every 10 minutes, the Oracle selects the best funded query and provides a new challenge for miners to solve. Miners submit their PoW solution and off-chain data point to the Oracle contract. The Oracle contract sorts the values as they come in and as soon as five values are received, the official value (median of the five) is selected and saved on-chain. The miners are then allocated their payout (base reward + tips).  Anyone holding TRB can dispute the validity of a mined value within one day of it being mined by paying a dispute fee.  Over the next week, Tellor token holders will vote on the validity of the data point; if the data point is deemed to be false, the miner will lose their stake. However, if the vote determines the value is correct, the reporting party’s dispute fee is given to the reported miner.

## Resources

* [Website](https://www.tellor.io)
* [Whitepaper](https://tellor.io/whitepaper/)
* [FAQ](https://www.tellor.io/faq)
* [Twitter](https://twitter.com/wearetellor)
* [Medium](https://medium.com/@tellor)
* [Telegram](https://t.me/tellor)
* [Discord](https://discord.gg/n7drGjh)

