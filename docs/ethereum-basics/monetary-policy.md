title: Ethereum’s Monetary Policy - EthHub

description: A description of Ethereum’s monetary (issuance) policy in the past, present and future.

# Monetary Policy

### Summary

Ethereum's Monetary Policy is defined by the rewards that are paid out by the protocol at any given time. Ethereum's current yearly network issuance is approximately 4.5% with 2 Ether per block and an additional 1.75 Ether per uncle block \(plus fees\) being rewarded to miners.

As with any cryptocurrency, Ethereum's Monetary Policy is decided upon by a wide range of stakeholders within the ecosystem - including:

* Developers
* Community members
* Ecosystem spokes/projects
* Miners and other network participants

As Ethereum is a decentralized network, the Monetary Policy can only be successfully modified if there is overwhelming consensus from the aforementioned stakeholders. Ethereum follows an [off-chain governance](governance.md) process meaning that any and all decisions on changes to the network happen extra-protocol.

That said, due to natural incentives Ether's issuance is unlikely to ever increase unless the security of the network is at risk. And the upcoming Ethereum 2.0 proof of stake transition will progressively allow for a drastic reduction of Ether issuance while maintaining the same level of network security.

## Important Events

### Genesis Block

As part of the Ethereum genesis block, initial contributors to Ethereum sale were allocated 60,000,000 Ether. Another 12,000,000 Ether was given to the development fund which was distributed among early contributors and the Ethereum Foundation.

### Historical Issuance Impacts

**Block Reward Reductions**  
Every block produced on the Ethereum network has an associated block reward which incentivizes miners to support the network. On top of the base block reward, miners that find an [uncle block](../using-ethereum/mining.md) receive ~75% of the current block reward. This results in a growing supply of Ether across time. The history of the block reward are as follows:

* Block 0 to Block 4,369,999: 5 Ether
* Block 4,370,000 to 7,280,000: 3 Ether \(changed via [EIP-649](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-649.md)\)
* Block 7,280,000 to now: 2 Ether \(changed via [EIP-1234](https://github.com/ethereum/EIPs/blob/master/EIPS/eip-1234.md)\)

**Other Events**  
Issuance rate is also impacted by the speed of blocks. There have been a few other events in Ethereum's history which has impacted the issuance rate. Some planned and some not planned.

* The Homestead fork in March 2016 saw a decrease in block times and therefore a temporary increase in issuance rate.
* In late 2016, the network was under DDoS attack. This increased the uncle rate, therefore causing a temporary rise in issuance rate.
* In mid 2017, a mechanism called the difficulty bomb \(or "Ethereum Ice Age"\) started to kick in. This meant that the difficulty of mining a block rose, therefore slowing down blocks. This resulted in a dramatic decrease in issuance rate.
* In late 2017, the Byzantium fork was released which delayed the difficulty bomb and also reduced block rewards from 5 to 3.

### Proof of Stake Impact

According to the current [Eth 2.0 spec](https://github.com/ethereum/eth2.0-specs), issuance rate will be greatly reduced as a part of Proof of Stake. There will be a sliding scale between total amount of Ether at stake and annual interest earned by stakers. The current spec would produce the following annual interest and inflation numbers based on total network stake:

| ETH validating | Max annual issuance | Max annual network issuance % | Max annual return rate  (for validators) |
| :--- | :--- | :--- | :--- |
| 1,000,000 | 181,019 | 0.17% | 18.10% |
| 3,000,000 | 313,534 | 0.30% | 10.45% |
| 10,000,000 | 572,433 | 0.54% | 5.72% |
| 30,000,000 | 991,483 | 0.94% | 3.30% |
| 100,000,000 | 1,810,193 | 1.71% | 1.81% |
| 134,217,728 | 2,097,152 | 1.98% | 1.56% |

### Historical and Future Supply Forecast

There are two majors upcoming factors when it comes to Ethereum's issuance rate and supply curve. They are:

* [Serenity Phase 0](https://github.com/ethhub-io/ethhub/tree/master/ethereum-roadmap/serenity-phases): Slight bump in issuance due to Beacon Chain launch.
* [Serenity Phase 2](https://github.com/ethhub-io/ethhub/tree/master/ethereum-roadmap/serenity-phases): Strong drop in issuance due to the PoW chain fading away.

![](/assets/images/issuance_graph.png)

