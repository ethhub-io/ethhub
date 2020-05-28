title: Ethereum 2.0 Economics - EthHub

description: A deep dive on the economics in Ethereum 2.0 including staking rewards and issuance rate.

# Eth 2.0 Economics

## Introduction

The Ethereum 2.0 upgrade will bring with it a switch from Proof of Work to Proof of Stake. This means instead of miners competing for a block reward, validators will be paid to perform assigned rules and secure the network. It's vitally important to get the economics of staking right so that the network stays healthy and secure.

If the incentive to stake is too low, the network will not get the minimum amount of validators needed to maintain consistent cross-shard communication. If the incentive is too high, the network is overpaying for security and inflating at a rate that is detrimental to the economics of the network as a whole.

There are a few considerations when it comes to how many validators the network "needs". According to the latest spec, for phase 0 there is a 16,384 validator count requirement for the chain to begin. For phase 1+ the recommended minimum validators per committee is 128. In order for all shards to crosslink (learn eachothers state) on every slot, for 64 shards that would be 262,144 validators and 8,388,608 total ETH staked.

## Terms

NOTE: Some of these are taken from [https://github.com/ethereum/eth2.0-specs/blob/master/specs/phase0/beacon-chain.md](https://github.com/ethereum/eth2.0-specs/blob/master/specs/phase0/beacon-chain.md)

* **Validator** - a participant in the Ethereum 2.0 consensus. You can become one by depositing 32 ETH into the deposit contract.
* **Committee** - a \(pseudo-\) randomly sampled subset of active validators, chosen to perform duties for a given slot on a selected shard.
* **Issuance Rate** - The annualized rate at which ETH supply grows.
* **Return Rate** - The annualized rate at which validators are rewarded \(in ETH\).

## Staking Rewards

In order to incentivize those that have ETH to stake in the network, validators will be rewarded for performing their assigned duties. Every 6 minutes, a validator is assigned a duty and is rewarded if it is performed. This reward is a sliding scale based on total network stake. So if total ETH staked is very low, the return rate per validator increases, but as stake rises, total annual issuance increases to fund those validators, while they individually will receive less rewards. The current [suggested payouts](https://github.com/ethereum/eth2.0-specs/pull/971) are as follows:

| ETH validating | Max annual issuance | Max annual network issuance % | Max annual return rate  (for validators) |
| :--- | :--- | :--- | :--- |
| 1,000,000 | 181,019 | 0.17% | 18.10% |
| 3,000,000 | 313,534 | 0.30% | 10.45% |
| 10,000,000 | 572,433 | 0.54% | 5.72% |
| 30,000,000 | 991,483 | 0.94% | 3.30% |
| 100,000,000 | 1,810,193 | 1.71% | 1.81% |

[According to Vitalik Buterin](https://www.reddit.com/r/ethtrader/comments/bffp0n/higher_pos_rewards_proposed/elen71t?utm_source=share&utm_medium=web2x), these are maximum numbers and there are many factors that can decrease the total issuance amounts. They are:

* Validators going offline. Combining the individual and collective penalties, every 1% of validators offline cuts total issuance by around 3%, and if more than 33% ever go offline at once, this will lead to finality leaking which will incur extra penalties for offline validators.

* Validators getting slashed. Probably will happen infrequently in practice.

* Transaction fees being burned due to [EIP 1559](https://medium.com/@TrustlessState/eip-1559-the-final-puzzle-piece-to-ethereums-monetary-policy-58802ab28a27) (estimate ~10k ETH/year initially while usage is still low, ramping up to hopefully hundreds of thousands of ETH/year eventually)

## Staking Costs and Risks

Validating and earning rewards is not a free lunch. There are many things to consider for one to become a validator. These factors will be considered by every validator when contemplating if the staking rewards are "worth it". They are:

* Computing cost
	* Users will need to run a validators client at a minimum and likely a beacon node as well. This requires computing resources.
	* Beacon Node: capable of running on a raspberry pi 4 in phase 0, will want to run 1 of these.
	* Validator client: lightweight and 1000s of validators can run on one client.
	* Rough estimates on costs are $120/year for a beacon node and validator client.

* Capital acquisition and lockup
	* The user must acquire the necessary 32 Ether and send a one-way transaction to the deposit contract.
	* Stakers can't directly sell staked Ether while it's staked. 
	* For phase 0, funds will be locked on the beacon chain until phase 1. It is possible to stop validating, but after submitting an exit you cannot resume or withdraw until after phase 1.

* Code Risk
	* By staking your ETH, you are trusting the staking software you are running on to perform its duties accurately. However, with block explorers and validator dashboards, it will be easy to see if anything is going wrong. It is the implementors role to create functional software that can work reliably. 
	* There is also a risk of network-wide flaws, however these can mostly be solved socially through hard forks if needed.

* General uptime and maintenance cost
	* Users can stay net-positive in earnings if they are online >50% of the time (assuming normal network conditions). However, you should not stake if you're not able to commit to strong uptime in some form.
	* If greater than 1/3rd of the network goes offline at once, finality cannot be reached. If this continues for over 4 epochs (25 minutes), all offline validators will incur finality leak penalties.  
	* If a user wishes to distribute their validators among multiple setups, maintenance cost and worry of the infrastructure comes into play.

* Security risk
	* Beyond failures in the client code, stakers are responsible for the security environment of their validator clients \(internet connection, operating system, hardware, etc.\). If their validator client gets hacked due to a security failure, leading to forced downtime and/or misbehavior, there's currently no way to recover funds.
	* This risk is similar to the risk of getting Ether stolen from a wallet due to a hacked laptop or smartphone. With decentralized autonomy comes responsibility.

A recommended read for those interested in validating is: [8 Things Every Validator Should Know Before Staking](https://medium.com/chainsafe-systems/8-things-every-eth2-validator-should-know-before-staking-94df41701487).
## Competition

A very important factor in determining if staking ETH is worth it is comparing the net reward versus competition.

**Decentralized Finance**  
Decentralized finance applications such as [Compound Finance](https://compound.finance/), [Dharma](https://dharma.io/) and [Maker](https://makerdao.com/). These applications offer ways for users to lock up ETH and gain a reward. Trying to understand what these offerings are or will be is something that should be considered.

**Other Investment Vehicles**  
More traditional investment alternatives such as bonds, certificates of deposit, savings account, etc. can be considered competition to staking as well. While not as directly influential to the decent as DeFi apps, they need to be considered.

## Resources
* [ETH2 Staking Calculator](https://docs.google.com/spreadsheets/d/15tmPOvOgi3wKxJw7KQJKoUe-uonbYR6HF7u83LR5Mj4/edit#gid=1446566120)
* [8 Things Every Validator Should Know Before Staking](https://medium.com/chainsafe-systems/8-things-every-eth2-validator-should-know-before-staking-94df41701487)
