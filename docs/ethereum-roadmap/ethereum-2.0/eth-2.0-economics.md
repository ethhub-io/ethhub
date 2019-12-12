title: Ethereum 2.0 Economics - EthHub

description: A deep dive on the economics in Ethereum 2.0 including staking rewards and issuance rate.

# Eth 2.0 Economics

## Introduction

The Ethereum Serenity upgrade will bring with it a switch from Proof of Work to Proof of Stake. This means that rather than pay miners to secure the network, we will be paying validators to secure the network. It's vitally important to get the economics of staking right so that the network stays healthy and secure.

If the incentive to stake is too low, the network will not get the minimum amount of validators needed to keep many shards going. If the incentive is too high, the network is overpaying for security and inflating at a rate that is detrimental to the economics of the network as a whole.

There are a few considerations when it comes to how many validators the network "needs". According to the latest spec, the recommended minimum validators per committee is 111. At 1024 shards that would be 113,664 validators and 3,637,248 total ETH staked.

To achieve crosslinks on all shards within 1 epoch, the committee size would be 256. That equates to 8,388,608 total ETH at stake on the network. Having less is fine it just means crosslinks become rarer.

## Terms

NOTE: Some of these are taken from [https://github.com/ethereum/eth2.0-specs/blob/master/specs/core/0\_beacon-chain.md](https://github.com/ethereum/eth2.0-specs/blob/master/specs/core/0_beacon-chain.md)

* **Validator** - a participant in the Casper/sharding consensus system. You can become one by depositing 32 ETH into the Casper mechanism.
* **Committee** - a \(pseudo-\) randomly sampled subset of active validators. When a committee is referred to collectively, as in "this committee attests to X", this is assumed to mean "some subset of that committee that contains enough validators that the protocol recognizes it as representing the committee".
* **Issuance Rate** - The annualized rate at which ETH supply grows.
* **Issuance** - The annualized rate at which validators are rewarded \(in ETH\).

## Validator Economic Incentive

There are many things that a user will consider when wanting to become a validator. In the base case, some users may believe in the Ethereum network so much that they would stake at a loss if need be. A good example of this is the 12,000 Ethereum nodes running today. However, in the simplest case we can break down the thought process as follows:

Total Incentive to Stake = Validator Rewards + Network Fees - Cost to run a Validator

\*One factor discussed later that validators will consider as well is competition.

## Staking Rewards

In order to incentivize those that have ETH to stake in the network, there must be some type of reward. It's unlikely that many people would stake their ETH for no reward. Serenity accomplishes this by paying validators a reward for every block they successfully propose and attest. This reward is a sliding scale based on total network stake. So if total ETH stake is low, the issuance rate goes up and as stake rises, it starts to fall. The current [suggested payouts](https://github.com/ethereum/eth2.0-specs/pull/971) are as follows:

| ETH validating | Max annual issuance | Max annual network issuance % | Max annual return rate  (for validators) |
| :--- | :--- | :--- | :--- |
| 1,000,000 | 181,019 | 0.17% | 18.10% |
| 3,000,000 | 313,534 | 0.30% | 10.45% |
| 10,000,000 | 572,433 | 0.54% | 5.72% |
| 30,000,000 | 991,483 | 0.94% | 3.30% |
| 100,000,000 | 1,810,193 | 1.71% | 1.81% |

[According to Vitalik Buterin](https://www.reddit.com/r/ethtrader/comments/bffp0n/higher_pos_rewards_proposed/elen71t?utm_source=share&utm_medium=web2x), these are maximum numbers and there are many factors that can decrease the total issuance amounts. They are:

* Validators going offline. Combining the individual and collective penalties, every 1% of validators offline cuts total issuance by around 3%, and if more than 33% ever go offline at once many coins could get burned quickly.

* Validators getting slashed. Probably will happen infrequently in practice.

* Transaction fees being burned due to EIP 1559 (estimate ~10k ETH/year initially while usage is still low, ramping up to hopefully hundreds of thousands of ETH/year eventually)

* Transaction fees being burned to pay for state rent (this mechanism could possibly be folded into the gas mechanism and hence the EIP 1559 burn)

[According to Justin Drake](https://github.com/ethereum/eth2.0-specs/pull/971#issuecomment-485069932), this could result in the 30,000,000 staked figure about resulting in 0.5% network issuance and 5% staker return.

## Fees

Validators earn a cut of the transaction fees that people pay to use the network. This is one area that needs more research but currently, the Ethereum network is paying about 600 ETH a day in fees. At current rate that's 219,000 ETH a year. How this will scale up as we add shards and throughput to the network will be important because it goes into the reward calculation.

## Staking Costs and Risks

Validating and earning rewards is not a free lunch. There are many things to consider for one to become a validator. These factors will be considered by every validator when contemplating if the staking rewards are "worth it". They are:

* Computing cost
	* Users will need to run validators clients at a minimum and likely a beacon node as well. This requires computing resources.
	* Beacon Node: similar to running geth/parity today, will want to run 1 of these.
	* Validator client: lightweight and need one per 32 ETH stake.
	* Rough estimates on costs are $120/year for a beacon node and $60/year per validator client.

* Capital acquisition and lockup
	* The user must acquire the necessary 32 Ether either via purchase or mining.
	* Stakers can't directly sell staked Ether while it's staked. 
	* If the user wants to withdraw funds, there is a set amount of time they must wait to get their ETH back. However, this time has come down considerably in the latest versions of the spec. The minimum withdraw queue wait is 18 hours. This could go up if a lot of people are exiting at the same time but 18 hours will likely be the norm.

* Code Risk
	* There is some code risk involved in staking that users will take into account. This will be more of a concern early on and likely dissipate over time. It's important to distinguish between client side code risk and consensus code risk. If the network runs into a consensus code break, the network will hard fork and fix it, so that's less of a concern. However, client side code risk is more serious because it'll be hard to distinguish that from a malicious fault.

* General uptime and maintenance cost
	* Users need to make sure their validator doesn't have downtime or they risk a quadratic leak on their stake.
	* If a user has multiple validators, maintenance cost and worry of the infrastructure comes into play.

* Security risk
	* Beyond failures in the client code, stakers are responsible for the security environment of their validator clients \(internet connection, operating system, hardware, etc.\). If their validator client gets hacked due to a security failure, leading to forced downtime and/or misbehavior, there's currently no way to recover funds.
	* This risk is similar to the risk of getting Ether stolen from a wallet due to a hacked laptop or smartphone. With decentralized autonomy comes responsibility.

## Competition

A very important factor in determining if staking ETH is worth it is comparing the net reward versus competition.

**Decentralized Finance**  
Decentralized finance applications such as [Compound Finance](https://compound.finance/), [Dharma](https://dharma.io/) and [Maker](https://makerdao.com/). These applications offer ways for users to lock up ETH and gain a reward. Trying to understand what these offerings are or will be is something that should be considered.

**Other Investment Vehicles**  
More traditional investment alternatives such as bonds, certificates of deposit, savings account, etc. can be considered competition to staking as well. While not as directly influential to the decent as DeFi apps, they need to be considered.

## Resources
* [ETH2 Staking Calculator](https://docs.google.com/spreadsheets/d/15tmPOvOgi3wKxJw7KQJKoUe-uonbYR6HF7u83LR5Mj4/edit#gid=1446566120)
