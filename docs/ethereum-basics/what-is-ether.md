title: What is Ether? - EthHub
description: Ether is the native cryptocurrency used on the Ethereum network.

# What is Ether?

## Summary

Ether \(ETH or Ξ\) is the native cryptocurrency used on the Ethereum network and is used to compensate miners who secure transactions. A planned upgrade to the Ethereum protocol in 2019-2021 would replace mining with a less computationally expensive Proof of Stake mechanism which will be secured by validators, who are also expected to receive a proportional compensation in Ether. Ether also has many current use cases, such as a store of value \(e.g. in lending collateral\), a medium of exchange \(e.g. in trade and payments\), and a unit of account \(e.g. in digital marketplaces\).

## Ether Use Cases

### Network Usage

Ether is required to transact on the Ethereum network.

As explained in the [gas section](https://docs.ethhub.io/-LTo-PwFj1VwulVCZAFW/~/drafts/-LUpsUsOLWLhW7Fftje4/primary/using-ethereum/ethereum-network-basics/transactions/gas), every transaction that occurs on the network requires a set amount of gas, which is a unit used to measure the computational power required to process the transaction. To process a transaction and include it in a block, miners expect to be compensated. This is accomplished by setting a gas price with every transaction, which is the cost of 1 unit of gas, denominated in Gwei \(1 ETH = 1,000,000,000 Gwei\).

For example, when you simply send ETH from one account to another, this cost 21,000 gas. If you were to set a gas price of 1 Gwei, this transaction would cost 0.000021 ETH.

### Store of Value

Ether, the native currency of the Ethereum network, derives its value from a myriad of different factors. It is used within the Ethereum network to perform a range of functions, including:

used to pay Ethereum transaction fees \(in the form of ‘gas’\) used as collateral for a wide range of open finance applications \(MakerDAO, Compound\) can be lent or borrowed \(Dharma\) accepted as payment at certain retailers and service providers used to as a medium of exchange to purchase Ethereum-based tokens \(via ICOs or exchanges\), crypto-collectibles, in-game items, and other non-fungible tokens \(NFTs\) earned as a reward for completing bounties \(Gitcoin, Bounties Network\) Furthermore, in Ethereum 2.0 \(Serenity\), users will be able to become a validator and help secure the network by providing computational resources and locking up 32 Ether per validator. Due to this, it is expected that Proof of Stake will lock a substantial amount of the circulating supply of Ether. There are also discussions around introducing a ‘fee-burn’ model where a percentage of Ether used to pay transaction fees would be ‘burned’ and thus reduce the circulating supply of Ether.

In addition to utility value, Ether also has speculative value. This is value that is derived from speculative activities \(such as trading and investing\) which currently accounts for most of the value behind all crypto-assets. As observed in 2017, crypto-assets can attract substantial speculative interest, with some assets increasing in value by 1000x over just a few months. This speculative interest often brings fresh capital into the ecosystem that can be reinvested into various verticals, but it can be damaging to the short-term market sentiment of all crypto-assets.

> Can’t tokens on Ethereum be used instead of Ether?

Theoretically, yes. Practically, no. The concept of using another asset to secure the Ethereum network is called ‘economic abstraction’ \(a good primer can be found [here](https://docs.ethhub.io/questions-about-ethereum/is-ether-needed-for-transaction-fees). This would involve miners / validators accepting tokens other than Ether in exchange for adding valid transactions to new blocks.

It is highly unlikely that the Ethereum protocol will ever implement economic abstraction as it could potentially reduce the security of the blockchain by compromising the value of Ether.

> How does valuable Ether help to secure the network?

In Proof of Work systems, miners compete with each other to find a block and thus be rewarded for their work \(in the form of the native crypto-asset of the protocol\). As the price of the asset increases, it naturally brings with it more miners, which then increases the network difficulty. As the network difficulty increases, it becomes increasingly difficult for miners to find a block which results in large scale mining operations \(commonly referred to as “mining farms”\) being one of the only profitable ways to mine on a Proof of Work network \(once it reaches a certain size\). Miners can also join ‘mining pools’ in order to increase their chances of finding a block and thus increase their rewards.

It would currently cost an individual or group a large amount of money to successfully attack or take control of either the Bitcoin or Ethereum PoW blockchains.

When Ethereum transitions to Proof of stake under Ethereum 2.0, it is expected that users will be able to stake 32 Ether per validator and receive rewards for their work in the form of additional Ether \(at a dynamic issuance rate , discussed later in this essay\).

Under Proof of Stake, the cost of attacking Ethereum will be tied to the cost of Ether. Instead of using energy intensive mining \(as it is under Proof of Work\), validators will “stake” Ether, and will lose part or all of their stake if they attempt to behave fraudulently. The more validators with staked Ether securing the network, the more Ether an attacker would need to purchase in order to carry out an attack. Such an attack would likely rapidly increase the price of Ether and thus make it prohibitively more expensive for the attacker.

### Medium of Exchange

In order for something to function as money within an economy, it needs to act as a good medium of exchange \(MoE\), unit of account \(UoA\) and store of value \(SoV\). Ether is used as a medium of exchange within the Ethereum economy for a wide range of apps, with dApp providers accepting it in exchange for fungible / non-fungible tokens, or other services. It is also used as a unit of account by various parties \(including companies that have raised Ether via ICOs\). Finally, Ether has historically been used as a store of value, with investors and speculators purchasing Ether to hold for investment purposes, given its relative scarcity, predictable supply growth, and inherent utility.

An object \(physical or digital\) must typically exhibit five distinct attributes in order to be considered money: portability, durability, divisibility, fungibility and established history \(see the [Lindy effect](https://en.wikipedia.org/wiki/Lindy_effect)\). Ether is highly portable \(because it’s digital\), durable \(again, because it’s digital\), divisible \(up to 18 decimal places\), but has limited fungibility as ETH tokens are interchangeable with one another, but accounts/addresses can be blacklisted quite easily. Privacy protocols such as zk-SNARKs will eventually improve this property for Ethereum.

Ethereum has been in operation since 2015 and continues to build a strong established history. The Ethereum network \(and Ether\) have functioned as expected for 99.99% of its life. The other 0.01% includes surviving The DAO, multiple large hacks of smart contracts, multiple protocol-level exploits, the Shanghai DoS attacks, constant negative remarks from the wider crypto community and multiple bear markets \(including a recent 94% drop in price\).

On top of this, Ether has additional properties such as being censorship-resistant, permission-less, pseudonymous and interoperable with other crypto-networks.

The supply scheme of crypto-assets is hotly debated among various parties \(especially those in the Bitcoin community\) and there are currently two main approaches: a capped supply \(like Bitcoin\) or a low, predictable and hard to change issuance rate \(like what is planned for Ethereum 2.0\).

In Ethereum 2.0 \(with Sharding and Proof of Stake implemented\), while a low inflation rate will always guarantee the validators are rewarded for securing the network, it suffers from the fact that it may dilute the value of Ether for those that are not validators. Though, this is offset by Ether being taken out of the circulating supply through staking, various open finance applications, fee burning, and people simply losing access to their Ether.

## Resources

* [Wikipedia](https://en.wikipedia.org/wiki/Ether)
* [Why Ether is Valuable](https://medium.com/ethhub/why-ether-is-valuable-2b4e39e01eb3)
* [Why Ether is Valuable](https://medium.com/ethhub/why-ether-is-valuable-2b4e39e01eb3)

