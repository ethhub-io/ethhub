title: Synthetix - EthHub

description: Synthetix is a decentralized platform on Ethereum for the creation synthetic assets which track the value of real-world assets.

# Synthetix

## Summary

Synthetix is a decentralized platform on Ethereum for the creation of Synths: on-chain synthetic assets that track the value of real-world assets. Born as stablecoin project Havven, [launched first USD pegged stablecoin in June 2018](https://blog.havven.io/nusd-launches-today-e24fbe0ee9c9). [Havven rebranded as Synthetix](https://blog.havven.io/havven-is-transforming-into-synthetix-2fdf727b8892) and expanded its scope to a synthetic asset platform [launching on mainnet December 2018](https://blog.synthetix.io/launch-synths-are-now-live-on-mainnet/). As of June 2019, the Synthetix platform supports over 20 Synths representing fiat currencies, commodities (e.g., gold), and cryptoassets. Stocks, indices, and other derivatives are expected to be added soon. It is one of the only platforms that supports shorting some tokens via the Synthetic inverse tokens such as iMKR, iXTZ, iBNB, iETH, iBTC. Synthetix has explored novel incentive mechanisms in token economics, including an inflationary monetary policy, establishing a liquidity ramp on Uniswap for traders to enter and exit the Synthetix exchange, and creating a pool of SNX to reward arbitraguers who buy sETH when it is more than 1 basis point off its peg to ETH. Synthetix also created a first-of-its-kind Exchange Index Synth. 

## How Synthetix Works

Synthetix has a native token called SNX. Holders lock SNX as collateral to mint Synths, which are freely tradeable ERC20 tokens. Trading fees from Synths exchanged on Synthetix’s non-custodial DEX, Synthetix.Exchange, go to SNX holders/Synth minters, incentivizing Synth creation and giving value to the underlying collateral (i.e., the SNX token).

## Monetary Policy

Synthetix initially started with supply of 100 million SNX ECR-20 tokens. In February 2019, shortly after the pivot from Havven to Synthetix, a new monetary policy was [instituted](https://blog.synthetix.io/synthetix-monetary-policy-changes/#targetText=Why%20Synthetix%20is%20implementing%20an,distributed%20across%2075%2C000%20SNX%20holders) to encourage staking on the platform while bootstrapping network effects. 
Recognizing the SNX token is fundamentally a work token, and not a currency whose primary purpose is purchasing power, the inflation schedule provides for a sequence of decreasing inflationary rewards to SNX stakers. Under the schedule, SNX increases in supply by 75 million from 100 million to 175 million from March 2019 to March 2020 (75% increase). Running up to March 2021, the SNX supply will increase from 175 million to 212.5 million (21% increase). In March 2022, the SNX supply will reach 231.25 million (9% increase. By March 2023, supply will grow to 240.625 million (4% increase). In March 2024, total supply will hit 245,312,500 SNX (2% increase). 
To mitigate instant dumping of SNX rewards by SNX stakers, which puts downward pressure on SNX price and therefore weakens the value of staked SNX collateral, SNX rewards distributed from March 2019 to March 2020 are locked and cannot be sold on the open market during this period. SNX earned from staking can be collateralized to mint new Synths, however. 

## Uniswap sETH Pool Liquidity Incentive Mechanism

In July 2019, Synthetic founder Kain Warwick [announced](https://blog.synthetix.io/uniswap-seth-pool-incentives/) "an experiment we will be running for the next four weeks to test whether protocol level incentives lead to a deep liquidity pool for the sETH/ETH pair on Uniswap." Explaining the motivation for the experiment, Warwick said, "Think of Uniswap as a gateway into the Synthetix ecosystem, in order to trade on sX you need to have Synths, which right now typically means converting ETH into sUSD. Once you have Synths you can trade on sX and take advantage of the infinite liquidity mechanism allowing you to convert between Synths. What happens though, when you are done trading and want to exit the system back into ETH? Unfortunately there is a significant cost to exit the system as slippage on Uniswap is high and the exchange rate between sUSD/ETH typically trades at a discount of 5-10%."
The experiment tested how well an incentive of 72,000 SNX per week, 5% of inflation, could attract ETH holders to provide liquidity on Uniswap. "This experiment will hopefully demonstrate a new kind of composability within the DeFi ecosystem, where protocols can combine incentives across protocols to align incentives in a symbiotic and self reinforcing fashion," Warwick said in a blog post at the time. In fewer than three months, the Synthetic Eth:ETH liquidity pool became [the largest pool](https://defistats.io/#/uniswap/) on Uniswap with more than 12,000 ETH and 12,000 sETH. The four-week experiment evolved into [Synthetix Improvement Proposal (SIP) 8](https://github.com/Synthetixio/SIPs/blob/master/SIPS/sip-8.md). 
SIP 8 states "The distribution will be managed by an m/n multisig contract with signers selected from LP providers...By implementing this distribution mechanism using a multisig, we prepare for the next phase of the project where the foundation can no longer modify distribution and other aspects of the system and begin to test aspects of decentralised goveranance."

## sETH:ETH Arbitrage Incentives

To strengthen the soft peg between sETH and ETH, Synthetix introduced an [arb contract](https://etherscan.io/dapp/0xa6b5e74466edc95d0b6e65c5cbfca0a676d893a4#writeContract) to create an incentive for maintaining sETH:ETH parity. Following a successful experimentation of the arb contract over several weeks in August 2019, 2% of inflation was dedicated toward supporting the arb contract. 
According to a Synthetix [blog post](https://blog.synthetix.io/our-new-seth-snx-arb-contract-is-now-live/), "If the sETH/ETH rate on Uniswap falls below 99/100, people can send ETH to the arb contract, which is then converted to SNX at par value. Essentially this means if the sETH ratio falls too low you can use this to exchange ETH to SNX at a discounted rate."

## Index Synths: sCEX and iCEX

In August 2019, the [first exchange index synths](https://blog.synthetix.io/introducing-our-first-index-tokens-scex-and-icex/) went live on Synthetix.exchange. Dubbed sCEX, the sCEX token represents a basket of tokens issued by the top centralized exchanges (CEXs) in the industry: Binance Coin (BNB), Bitfinex's LEO, Huobi's HT, Okex's OKB, and Kucoin's KuCoin Shares (KCS). This basket provides unique exposure to a new strain of synthetic assets that enables traders and investors to gain exposure to the price of several exchanges' tokens without having to own the underlying tokens or maintain an account with one of the represented exchanges. 
When sCEX was introduced, so too was iCEX born, which effectively enables beneficial exposure to downward price movement in the aforementioned tokens. Like iXTZ, iMKR, or iBNB, iCEX appreciates in price when its underlying components depreciate. This is akin to taking a short position, though the parameters of Inverse Synths makes the term inverse more appropriate. The inaugural sCEX and iCEX tokens are weighted as follows: BNB (50%), LEO (20%), HT (10%), OKB (10%) and KCS (10%.)

## Resources

* [DeFi Pulse](https://defipulse.com/synthetix)
* [Litepaper](https://www.synthetix.io/uploads/synthetix_litepaper.pdf)
* [Website](https://www.synthetix.io/)
* [Dashboard](https://dashboard.synthetix.io/)
* [Mintr](https://mintr.synthetix.io/)
* [Synthetix.Exchange](https://synthetix.exchange/)
* [Synthetix for Dummies](https://medium.com/@TwiceCrypto/synthetix-for-dummies-477a0760d335)
* [github](https://github.com/Synthetixio/)
* [Developer docs](https://developer.synthetix.io/api/docs/deployed-contracts.html)
* [Monetary Policy](https://blog.synthetix.io/synthetix-monetary-policy-changes/#targetText=Why%20Synthetix%20is%20implementing%20an,distributed%20across%2075%2C000%20SNX%20holders)

