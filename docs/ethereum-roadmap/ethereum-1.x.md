title: Ethereum 1.x
description: Ethereum 1.x is an effort to improve performance and storage of the current Ethereum mainnet.

# Ethereum 1.x

## Summary

A group of Ethereum core developers and friends talked at Devcon IV and realized that they all share similar view - that Ethereum mainnet, if left unchanged, would become very hard or impossible to use due to severe performance degradation, and increased storage requirements.

* Performance degradation mostly due to the large \(and increasing\) state.
* Increased storage requirements mostly due to keeping blocks, event logs \(receipts\), and state history \(currently prunable in major clients\).

## Pre-History

#### October 2017, Devcon3 in Cancun

Vitalik Buterin presents ["Modest proposal for Ethereum 2.0"](https://www.youtube.com/watch?v=hAhUfCjjkXc), suggesting that Layer 1 of Ethereum 1.0 should stay “safe and conservative”, and most of the innovation go into Layer 2 and into shards.

#### May 2018, EDCON in Toronto

Vitalik Buterin gives a talk [“So you want to become Casper validator?”](https://www.youtube.com/watch?v=VqOlOMAqC08), signaling that Casper FFG validators may be running on laptops and rollout is getting close.

#### June 2018

Pivot in Casper research from Casper FFG to full Casper and merging with sharding, due to challenges of implementing Casper FFG as a contract, and due to large overlap with Sharding research, as discussed at the [Core Dev Meeting 40](https://youtu.be/8-AZys80RrU?t=1819).

### October-November 2018, Devcon IV in Prague

It becomes apparent that Serenity \(full Casper + Sharding\) is not going to functionally supersede Ethereum 1.0 for another 3-5 years.

## Main Objectives

* Develop, formalize, and implement set of measures, deployable on the Ethereum 1.0 mainnet, within the next 2 years, to ensure that the chain stays viable and usable. That mainly means curbing the state growth or limiting the state size.
* Emphasize focus on these measures and de-emphasize introduction of specific “features”. This is one of the places where eWASM engine comes in. Current computational pre-compiles are seen as features requiring case-by-case work. Introduction of eWASM engine would first enable “pre-compile” factory, where more pre-compiles are introduced faster. Later it would enable any contracts written in eWASM, obviating need in pre-compiles altogether.

## Working groups
* State rent
* eWASM
* Storage pruning
* Simulation and emulation

## State Rent

#### Proposal framework

Since State rent is a potentially higher impact change \(and therefore more controversial, unpopular\) than any other changes within Ethereum 1x, it requires a clear logical framework for designing, evaluating, and comparing proposals. This framework attempts to ensure, as much as possible, that the change plan eventually chosen is likely close to the best available. It defines the path of reasoning from “What is the problem \(what happens if we do nothing\)?” to “How exactly we are doing it”. [Current location of the proposal framework document](https://github.com/ledgerwatch/eth_state/blob/master/State_size_growth_management.pdf) \(Work in progress\)

#### Reasoning questions

* Why is state a valuable resource and to whom? \(can this value be replicated\)
* Why state size needs to be managed? \(effect on system performance + possible partial mitigations\)
* How can state size be managed? \(feedforward vs feedback control\)
* What metrics need to be regulated? \(state size, state growth, or both\)
* Do metrics need to be in-state or off-state?
* What parameters \(control inputs\) do we use? \(cost of state expansion, charge per size unit per block\)
* Can controlled system weaken or evade control? \(dark rent, miner rebates\)

#### Current proposals

* Introduce rent on all accounts \(contracts and non-contracts\), existing and newly created ones, with the ability to restore evicted contracts. [Current location](https://github.com/ledgerwatch/eth_state/blob/master/State_rent.pdf)
* Introduce fund lock-up when state is expanded \(creation of accounts, adding store items\), which is partially released when the state is cleared. Apply rent only on the pre-existing state. [Current location](https://github.com/ledgerwatch/eth_state/blob/master/State_Rent_2.pdf)
* Increase the cost of state expansion in “short term”, to enable block gas limit increase before state rent is implemented
* Do nothing

#### Challenges inherent to most proposals

* How will existing dapps be affected. Will they become too expensive/cumbersome to use? Will they need to be optimised/rewritten completely?
* Denomination of the extra state expansion charge or rent - should it be priced in gas, ETH, and how should be the price be determined \(feedback loop on the state size?\). Will volatility of ETH price affect those charges too much? Will miners help users evade charges?

#### Classes of contracts and impacts

Part of the state rent research is to identify main classes of contracts that are likely to be affected by the changes in the protocol, and provide guidelines on what they can do about it. Likely important classes:

* ERC20 token contracts and applications managing them \(DAI, Augur\)
* On-chain order books \(DEXs\)
* ENS
* Non-fungible token contracts
* Multi-signature wallets
* Gaming contracts
* Gambling contracts

#### Resources

* [State Rent Proposal](https://ethereum-magicians.org/t/state-rent-proposal-version-2-rushed/2494)

## eWASM

#### Main unresolved questions

* Gas metering
* Memory allocation
* Interaction with the rest of EVM state \(e.g. contract storage, balances\)
* Interpreter/compiler guarantees on compilation time and runtime

#### Gas metering

Two main approaches:

* Injection. Wasm bytecode gets pre-processed. An extra register is added to serve as a gas counter. It gets incremented at certain points \(jumps, calls\) and out-of-gas check is performed. Pro: generic. Con: performance overhead.
* Automatic upper bound estimation. Static analysis is performed on the bytecode, and, for some subset of codes, upper bound of executed instructions \(virtual gas\) can be calculated. Pro: no performance overhead. Con: only subset of codes

Current approach for the 1st phase \(pre-compiles\) is upper-bound based.

#### Memory allocation

Wasm semantics dictates that Wasm execution has a linear memory \(only one in the current version of the spec\) that can be grown on demand. Will that linear memory be allocated every time the engine is called, and then torn down at the end of the execution? If yes, how more efficient is this compared to the current EVM model \(which does this allocation and tearing down at each CALL opcode\).

#### Interaction with the rest of EVM state

Was proposed via external functions, for example \(name made up\):

`function_SLOAD(storage_index: uint256)`

Alternative approach is not to have Ewasm code access EVM state, but only exchange input/output when called. This, of course, makes maintaining large persistent data structures difficult.

#### Interpreter/compiler guarantees

Initially, this problem has been brought up in the context of JITs \(Just In Time\) compilers. JIT compilers were one of the reasons why WebAssembly was a big performance improvement over JavaScript.

JIT compilers might be problematic in an adversarial environment, because it is usually possible to find a program that takes an unusually long time to compile, and algorithms that decide what to compile “just in time” can be targeted too.

AOT \(Ahead of Time\) compilers can be used for Core Dev-controlled pre-compiles \(Phase 1\). For Phase 2, the plan was to initially use very straightforward interpreters, and then develop AOT compilers with necessary guarantees. The idea of first introducing interpreters is to make sure eWASM is there, giving people more motivation to work on the compilers \(which is harder than interpreter\)

## Storage Pruning

#### The questions to be answered are:

* What do we absolutely have to keep to comply with the Ethereum protocol?
* Do we always need to keep all the blocks? \(maybe not, if we use backward sync, for example\)
* Do we need to keep receipts, or just logs, how much \(in Gb\), or for how long?
* Do we need to always download the entire header chain or can we compress it \(with STARK proofs for example\)?
* Can we improve snapshot sync procedures \(fast sync, warp sync\) so that they prevent invalid state transitions \(with Validity Proofs, for example\)? 

## Simulation and Emulation

**Simulation** handles models of the software agents \(in our case Ethereum client software instances\), coarse enough to be performant, and fine enough to capture the important facets of the agents.

**Emulation** handles the actual software agents \(in our case the actual implementations of Ethereum like geth and parity\), placed into the virtual environments with lots of freedom to change parameters of virtual machines and the network connecting them.

Potential questions that simulation may be able to answer:

* Will uncle rate become much less of an indicator of the network congestion if most of the Ethereum nodes propagate blocks straight after verifying Proof Of Work \(instead of fully processing the block as they used to do\)?

Potential questions that emulations may be able to answer:

* What is the function that describes the relationship between the rate of success for snapshot synchornisations \(fast sync, warp sync\) and things like prevailing bandwidth and state history pruning threshold?

## Deliverables

#### Measures requiring hard-forks:

* State rent \(or state growth limiting\)
* Ewasm

#### Measures likely not requiring hard-forks, but requiring client code coordination on the network protocol:

* Storage pruning

Simulation and Emulation group produces data for making projections, benchmarks, and parameter calibrations for other groups.





