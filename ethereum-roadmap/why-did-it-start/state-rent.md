# State Rent

## Proposal framework

Since State rent is a potentially higher impact change \(and therefore more controversial, unpopular\) than any other changes within Ethereum 1x, it requires a clear logical framework for designing, evaluating, and comparing proposals. This framework attempts to ensure, as much as possible, that the change plan eventually chosen is likely close to the best available. It defines the path of reasoning from “What is the problem \(what happens if we do nothing\)?” to “How exactly we are doing it”. [Current location of the proposal framework document](https://github.com/ledgerwatch/eth_state/blob/master/State_size_growth_management.pdf) \(Work in progress\)

## Reasoning questions

* Why is state a valuable resource and to whom? \(can this value be replicated\)
* Why state size needs to be managed? \(effect on system performance + possible partial mitigations\)
* How can state size be managed? \(feedforward vs feedback control\)
* What metrics need to be regulated? \(state size, state growth, or both\)
* Do metrics need to be in-state or off-state?
* What parameters \(control inputs\) do we use? \(cost of state expansion, charge per size unit per block\)
* Can controlled system weaken or evade control? \(dark rent, miner rebates\)

## Current proposals

* Introduce rent on all accounts \(contracts and non-contracts\), existing and newly created ones, with the ability to restore evicted contracts. [Current location](https://github.com/ledgerwatch/eth_state/blob/master/State_rent.pdf)
* Introduce fund lock-up when state is expanded \(creation of accounts, adding store items\), which is partially released when the state is cleared. Apply rent only on the pre-existing state. [Current location](https://github.com/ledgerwatch/eth_state/blob/master/State_Rent_2.pdf)
* Increase the cost of state expansion in “short term”, to enable block gas limit increase before state rent is implemented
* Do nothing

## Challenges inherent to most proposals

* How will existing dapps be affected. Will they become too expensive/cumbersome to use? Will they need to be optimised/rewritten completely?
* Denomination of the extra state expansion charge or rent - should it be priced in gas, ETH, and how should be the price be determined \(feedback loop on the state size?\). Will volatility of ETH price affect those charges too much? Will miners help users evade charges?

## Classes of contracts and impacts

Part of the state rent research is to identify main classes of contracts that are likely to be affected by the changes in the protocol, and provide guidelines on what they can do about it. Likely important classes:

* ERC20 token contracts and applications managing them \(DAI, Augur\)
* On-chain order books \(DEXs\)
* ENS
* Non-fungible token contracts
* Multi-signature wallets
* Gaming contracts
* Gambling contracts

## Resources

* [State Rent Proposal](https://ethereum-magicians.org/t/state-rent-proposal-version-2-rushed/2494)
