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
* **Interest** - The annualized rate at which validators are rewarded \(in ETH\).

## Validator Economic Incentive

There are many things that a user will consider when wanting to become a validator. In the base case, some users may believe in the Ethereum network so much that they would stake at a loss if need be. A good example of this is the 12,000 Ethereum nodes running today. However, in the simplest case we can break down the thought process as follows:

Total Incentive to Stake = Validator Rewards + Network Fees - Cost to run a Validator

\*One factor discussed later that validators will consider as well is competition.

## Staking Rewards

In order to incentivize those that have ETH to stake in the network, there must be some type of reward. It's unlikely that many people would stake their ETH for no reward. Serenity accomplishes this by paying validators a reward for every block they successfully propose. In the [latest spec](https://github.com/ethereum/eth2.0-specs/blob/master/specs/core/0_beacon-chain.md) this is a sliding scale based on total network stake. So if total ETH stake is low, the interest rate goes up and as stake rises, it starts to fall.

We can calculate this scale using the spec. There are a lot of variables in doing this. First up are the **constants**:

| **Constant** | Value |
| :--- | :--- |
| ETH stake | 32 |
| Shards | 1024 |
| Slot time \(in seconds\) | 6 |
| Epoch Length \(in slots\) | 64 |
| Base Reward Quotient | 1024 |

From here we can start to calculate the **outputs** using a single **assumption** which is **total network stake.** \(Let's assume 10,000,000 in the example\)

| **Output** | Calculation |
| :--- | :--- |
| Network Validators | 10000000/32 = 312,500 |
| Validators/Shard | 10000000/\(32\*1024\) = 305 |
| Epoch/year | 31536000/\(6\*64\) = 82125 |
| Reward Quotient | 1024\*INT\(SQRT\(10000000\)\) = 3,237,888 |
| Reward/epoch | 10000000/3237888 = 3.088 |
| Generated ETH/Year | 82125\*3.088 = 253638 |
| Validator Interest/Year | 253638/10000000 = 2.54% |
| Issuance Rate/Year | 253638/104000000 = 0.24% |

So here we can see that with 10,000,000 total network stake, validators are gaining 2.54% a year and the network is inflating at 0.24% a year. We can now take these formulas and generate the sliding scale:

| Total Network Stake | Validator Interest | Network Issuance |
| :--- | :--- | :--- |
| 1,000,000 | 8.02% | 0.08% |
| 2,000,000 | 5.67% | 0.11% |
| 3,000,000 | 4.63% | 0.13% |
| 5,000,000 | 3.59% | 0.17% |
| 10,000,000 | 2.54% | 0.24% |
| 20,000,000 | 1.79% | 0.34% |
| 30,000,000 | 1.46% | 0.42% |
| 50,000,000 | 1.13% | 0.55% |
| 100,000,000 | 0.80% | 0.77% |

## Fees

Validators earn a cut of the transaction fees that people pay to use the network. This is one area that needs more research but currently, the Ethereum network is paying about 600 ETH a day in fees. At current rate that's 219,000 ETH a year. How this will scale up as we add shards and throughput to the network will be important because it goes into the reward calculation.

## Staking Costs and Risks

Validating and earning rewards is not a free lunch. There are many things to consider for one to become a validator. These factors will be considered by every validator when contemplating if the staking rewards are "worth it". They are:

* Computing cost
  * Users will need to run validators clients at a minimum and likely a beacon node as well. This requires computing resources. The specifics around how much as far as HDD, [bandwidth and more are still being figured out](https://github.com/ethereum/eth2.0-specs/issues/251#issuecomment-445438093).
    * Beacon Node: similar to running geth/parity today
    * Validator client: lightweight and need one per 32 ETH stake
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

A very important factor in determining if staking ETH is worth it is comparing the net reward versus competition. We should assume that stakers do not necessarily care about securing the Ethereum network but rather they are motivated by profit. There are many different categories of competition to consider:

**Decentralized Finance**  
Decentralized finance applications such as [Compound Finance](https://compound.finance/), [Dharma](https://dharma.io/) and [Maker](https://makerdao.com/). These applications offer ways for users to lock up ETH and gain a reward \(interest\). Trying to understand what these offerings are or will be is something that should be considered.

**Other Investment Vehicles**  
More traditional investment alternatives such as bonds, certificates of deposit, savings account, etc. can be considered competition to staking as well. While not as directly influential to the decent as DeFi apps, they need to be considered.

**Alternative Staking Coins**  
There is over [500 alternative PoS coins](https://masternodes.online/), with a reward structure. Why stake ETH, when one can earn more, with potentially less infrastructure and risk, on another coin?

## Spreadsheet Examples

* Basic: Click [here](https://docs.google.com/spreadsheets/d/1SZBJsTHBFmRlo6aLZ0ex_bnTO3MqQrsZK9yLWqL4r68/edit?usp=sharing) to see calculations of network and personal staking variables given the latest spec.
* Advanced: Building on the above, this [sheet](https://docs.google.com/spreadsheets/d/1rfuWnfg42mBcaHEPr-b0gvXofHfl3fC7ldmKQ8JjfMU/edit?usp=sharing) analyzes the financial return when utilizing different validator architectures.

