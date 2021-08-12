---
title: Ethereum’s Monetary Policy - EthHub

description: A description of Ethereum’s monetary policy in the past, present and future.
---

# Monetary Policy

## Deflationary Ether (aka Ultrasound Money)

Ethereum's Monetary Policy has two distinct components with opposite effects. The first component is *issuance* and the second is *fee burning*. Issuance refers to the new Ether that is minted by the protocol on every block in order to reward proof-of-work miners and proof-of-stake validators for the security they provide to the Ethereum network. Therefore, issuance has an inflationary effect, as it increases the total supply of Ether. On the other hand, fee burning refers to the burning of most of the Ether that users pay via transaction fees for using Ethereum. Therefore, fee burning has a deflationary effect, as it decreases the total supply of Ether.

The goal of Ethereum's monetary policy has always been to reduce issuance to the minimum necessary to secure the network. This is commonly referred to as Minimum Necessary Issuance and was the pillar of Ethereum's monetary policy for several years. During that time, inflation was solely dictated by issuance, so the two terms were indistinguishable from each other. In order to minimize inflation, issuance has only gone down to the estimated minimun necessary to guarantee the network's security, and never increased throughout Ethereum's history. Nevertheless, with issuance as the only instrument for monetary policy, and limited by the need to pay for network security, inflation could only be reduced, but never eliminated.

In the last two years, though, an Ethereum improvement porposal (EIP-1559) was researched, developed and recently launched to improve Ethereum's fee market. This EIP included a fee-burning mechanism, which gave Ethereum's monetary policy an instrument to offset issuance and potentially reverse inflation. Since then, the new goal of Ethereum's monetary policy has become to turn Ether into a deflationary asset. And, in fact, early fee burning data suggests that Ether will become net deflationary as soon as the proof-of-work network is removed and replaced by the proof-of-stake network, a move that was planned many years ago to drastically reduce issuance without sacrificing security (see The Merge below).

Ethereum's monetary policy is strongly supported and enforced by a wide range of stakeholders within the ecosystem - including:

* Developers
* Community members
* Ecosystem spokes/projects
* Validators and other network participants

As Ethereum is a decentralized network, the Monetary Policy cannot be successfully modified unless there is overwhelming consensus from the aforementioned stakeholders. Ethereum follows an [off-chain governance](governance.md) process meaning that any and all decisions on changes to the network happen extra-protocol.

## Important Events

### Genesis Block

As part of the Ethereum genesis block, initial contributors to Ethereum sale were allocated 60,000,000 Ether. Another 12,000,000 Ether was given to the development fund which was distributed among early contributors and the Ethereum Foundation.

### Historical Issuance Impacts

**Block Reward Reductions**  
Every block produced on the Ethereum network has an associated block reward which incentivizes miners to support the network. On top of the base block reward, miners that find an [uncle block](../using-ethereum/mining.md) receive ~75% of the current block reward. This results in a growing supply of Ether across time. The history of the block reward are as follows:

* Block 0 to Block 4,369,999: 5 Ether
* Block 4,370,000 to 7,280,000: 3 Ether \(changed via [EIP-649](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-649.md)\)
* Block 7,280,000 to now: 2 Ether \(changed via [EIP-1234](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1234.md)\)

**Beacon Chain Launch**  
The Beacon Chain proof-of-stake network was launched in December 2020. Issuance on the Beacon Chain follows a sliding scale between total amount of Ether at stake and annual interest earned by stakers (or validators), as follows:

| ETH validating | Max annual issuance | Max annual network issuance % | Max annual return rate  (for validators) |
| :--- | :--- | :--- | :--- |
| 1,000,000 | 181,019 | 0.17% | 18.10% |
| 3,000,000 | 313,534 | 0.30% | 10.45% |
| 10,000,000 | 572,433 | 0.54% | 5.72% |
| 30,000,000 | 991,483 | 0.94% | 3.30% |
| 100,000,000 | 1,810,193 | 1.71% | 1.81% |

The Beacon Chain launch had the effect of a slight bump in issuance.

**Other Events**  
Issuance rate is also impacted by the speed of blocks. There have been a few other events in Ethereum's history which has impacted the issuance rate. Some planned and some not planned.

* The Homestead fork in March 2016 saw a decrease in block times and therefore a temporary increase in issuance rate.
* In late 2016, the network was under DDoS attack. This increased the uncle rate, therefore causing a temporary rise in issuance rate.
* In mid 2017, a mechanism called the difficulty bomb \(or "Ethereum Ice Age"\) started to kick in. This meant that the difficulty of mining a block rose, therefore slowing down blocks. This resulted in a dramatic decrease in issuance rate.
* In late 2017, the Byzantium fork was released which delayed the difficulty bomb and also reduced block rewards from 5 to 3.
* In early 2019, after a few months of difficulty bomb activation, the bomb was reset and block rewards were reduced from 3 to 2 in the Constantinople fork.
* In early 2020, the Muir Glacier fork reset the difficulty bomb.

### Historical, Current and Future Supply Forecast

Ether's yearly inflation rate currently hovers around 3%. This is calculated by subtracting burned fees from issuance. Ethereum's current yearly network issuance is approximately 4.6%, with 2 Ether per block and an additional 1.75 Ether per uncle block (plus fees) being rewarded to miners in the proof-of-work network, and ~1,130 Ether per day awarded to validators in the Beacon Chain proof-of-stake network. Meanwhile, the burned fees currently oscillate in the 4,000 to 6,000 Ether range, depending on gas prices. This amounts to a yearly reduction of Ether's supply by 1.5-1.6%.

There is one last major upgrade that will affect Ethereum's issuance rate and supply curve:

* [The Merge](https://github.com/ethereum/EIPs/pull/3675): The proof-of-work network and all associated rewards will be removed and effectively replaced by the Beacon Chain through the migration of Ethereum's execution layer from the proof-of-work chain to the (now executable) Beacon Chain. This means that the only rewards on chain will go to proof-of-stake validators, which translates into a ~90% reduction in issuance.

![](/assets/images/issuance_graph.png)

## Resources
* [Ethereum issuance reduction process explained](https://twitter.com/sassal0x/status/1086023932514189312)
