---
title: Ethereum 1.x - EthHub

description: Ethereum 1.x is an effort to improve performance and storage of the current Ethereum mainnet.
---

# Ethereum 1.x

## Summary

Ethereum 1.x is a codename for a comprehensive set of upgrades to the Ethereum mainnet intended for near-term adoption. <br/>
Ethereum 2.0 (Serenity) won't be fully rolled out for another 2-3 years with Phase 0 and Phase 1 due within 1-2 and Phase 2 due sometime in 2022. Ethereum 2.0 is being deployed as a separate blockchain so it does not supersede ETH 1.0 which means the chain needs to be sustainable for another 5-10 years.

Eth1.x is a result of a group of Ethereum core developers and friends discussing the current challenges of Ethereum at Devcon IV and realising that they all share a similar view - that the Ethereum mainnet, if left unchanged, would become very hard or impossible to use due to severe performance degradation and increased storage requirements.

* Performance degradation mostly due to the large \(and increasing\) state size.
* Increased storage requirements mostly due to keeping blocks, event logs \(receipts\), and state history \(currently prunable in major clients\).
<br/>

The 1.x set of improvements will introduce major, breaking changes to the mainnet, while 2.0 (aka Serenity) undergoes prototyping and development in parallel. The plan for 1.x encompasses three primary goals: (1) mainnet scalability boost by increasing the tx/s throughput (achieved with client optimizations that will enable raising the block gas limit substantially); (2) ensure that operating a full node will be sustainable by reducing and capping the disk space requirements with “storage rent”; (3) improved developer experience with VM upgrades including eWASM.

## Pre-History of Ethereum 1.x

#### October 2017, Devcon3 in Cancun

Vitalik Buterin presents ["Modest proposal for Ethereum 2.0"](https://www.youtube.com/watch?v=hAhUfCjjkXc), suggesting that Layer 1 of Ethereum 1.0 should stay “safe and conservative”, and most of the innovation go into Layer 2 and into shards.

#### May 2018, EDCON in Toronto

Vitalik Buterin gives a talk [“So you want to become Casper validator?”](https://www.youtube.com/watch?v=VqOlOMAqC08), signaling that Casper FFG validators may be running on laptops and rollout is getting close.

#### June 2018

Casper FFG research is merged with sharding due to challenges of implementing Casper FFG as a contract, and due to large overlap with Sharding research, as discussed at the [Core Dev Meeting 40](https://youtu.be/8-AZys80RrU?t=1819).

#### October-November 2018, Devcon IV in Prague

It becomes apparent that Serenity \(full Casper + Sharding\) is not going to functionally supersede Ethereum 1.0 for another 3-5 years.

## Main Objectives

* Develop, formalize, and implement set of measures, deployable on the Ethereum 1.0 mainnet, within the next 2 years, to ensure that the chain stays viable and usable. That mainly means curbing the state growth or limiting the state size.
* Emphasize focus on these measures and de-emphasize introduction of specific “features”. This is one of the places where eWASM engine comes in. Current computational pre-compiles are seen as features requiring case-by-case work. Introduction of eWASM engine would first enable “pre-compile” factory, where more pre-compiles are introduced faster. Later it would enable any contracts written in eWASM, obviating the need for pre-compiles altogether.


## Working groups
* State rent (now called as state fees because it might not be just rent)
* eWASM
* Storage pruning
* Simulation and Emulation

### State Rent

#### Proposal framework

Since State rent is a potentially higher impact change \(and therefore more controversial, possibly unpopular\) than any other changes within Ethereum 1.x, it requires a clear logical framework for designing, evaluating, and comparing proposals. This framework attempts to ensure, as much as possible, that the change plan eventually chosen is likely close to the best available. It defines the path of reasoning from “What is the problem \(what happens if we do nothing\)?” to “How exactly we are doing it”. [Current location of the proposal framework document](https://github.com/ledgerwatch/eth_state/blob/master/State_size_growth_management.pdf) \(Work in progress\)

Alexey explains the idea of state rent - "to charge people not once when they start using storage and then paying them back a certain amount if they free it up again, but actually charging people by the day or by the block based on the storage that they're using, and if they decide that they don’t need these things anymore they can just withdraw their Ether or they just leave it and then it will be garbage collected by the rent".

#### Reasoning questions

* Why is state a valuable resource and to whom? \(can this value be replicated\)
* Why state size needs to be managed? \(effect on system performance + possible partial mitigations\)
* How can state size be managed? \(feedforward vs feedback control\)
* What metrics need to be regulated? \(state size, state growth, or both\)
* Do metrics need to be in-state or off-state?
* What parameters \(control inputs\) do we use? \(cost of state expansion, charge per size unit per block\)
* Can controlled system weaken or evade control? \(dark rent, miner rebates\)
* How can we get active contracts that are using lots of storage to pay a rent that more accurately represents the cost of storing that data permanently on-chain over a period of time? \(Linear cross-contract storage could be a solution here\)
* How can we clear the state of abandoned contracts that are not being used anymore? \(This problem is not addressed in any such proposal as abandoned contracts represent only 6% of the state\)
* How about keeping rent simple and maximally effective at the protocol level and completely deleting anything which runs out of funds? \(Bad Idea, Users forget about some application they are involved in all the time\)
* Moving portions of the smart contracts data off chain? \(A subprotocol is needed for the delivery\)


*"Say you have a smart contract now and it uses storage so it has to pay rent. So it has to have funds or someone needs to pay funds on behalf of it. So what happens if no one pays?"*

Under all three of the current proposals, when the smart contract exhausts its balance and the rent balance, they are considered two separate things. So when both of these balances are empty, an eviction happens. <br/>
Eviction, under the current proposals, doesn’t just happen automatically - somebody actually has to 'poke' the contract. Poking means that somebody has to create a transaction which touches it to access it in some way.<br/>
For non contracts, eviction means just removing from the state as it doesn't have any information at all but for contracts, there's storage, so eviction doesn't completely remove it from a state but it leaves a so-called stub which is essentially the commitment to the entire state of the contract before the eviction, and this stub, unfortunately has an effect that it does not completely remove it from the state so it has to still dangle there, but this stub is what allows us to restore it later on.

Let's take an **example**, "if you had a multisig wallet with lots of tokens in it and then you've forgotten to pay the rent, the multisig is "gone" but you would still be able to use the recovery mechanism to rebuild the storage of this contract in another contract and simply use a special code to restore it from the stub - then the contract comes "back to life". You can also top up the rent and then keep using the contract or you can move the things elsewhere." <br/>
The stub is expected to be a 32 byte hash which is a commitment to what the contract looked like before it was evicted.

*How is this different from stateless contracts?*

The difference is that in stateless contracts we assume that when the contract is represented as a stub it’s still accessible by the normal operations. In this proposal, when the contract is in hibernation state (ie when it’s a stub) it’s not accessible by anything. It’s basically invisible to the Ethereum Virtual Machine\([EVM](https://github.com/ethereum/wiki/wiki/Ethereum-Virtual-Machine-(EVM)-Awesome-List)\) with the exception of this special opcode, which it’s restored to, and only that opcode can see that stub - nothing else can.

*Is this the best solution?*

This is not a perfect solution as if we find that there are lots of little contracts having the hash stubs and then the state is still not small enough.

Watch the whole [talk](https://epicenter.tv/episode/274/) where Alexey explains state rent and more about Eth 1.x.

#### Current proposals
There are currently three proposals being worked upon: <br/> 
* Introduce rent on all accounts \(contracts and non-contracts\), existing and newly created ones, with the ability to restore evicted contracts. [Current location](https://github.com/ledgerwatch/eth_state/blob/master/State_rent.pdf)
* Introduce fund lock-up when state is expanded \(creation of accounts, adding store items\), which is partially released when the state is cleared. Apply rent only on the pre-existing state. [Current location](https://github.com/ledgerwatch/eth_state/blob/master/State_Rent_2.pdf)
* Increase the cost of state expansion in “short term”, to enable block gas limit increase before state rent is implemented

#### Challenges inherent to most proposals

* How will existing dApps be affected? Will they become too expensive/cumbersome to use? Will they need to be optimized/rewritten completely?
* Denomination of the extra state expansion charge or rent - should it be priced in gas, ETH, and how should be the price be determined \(feedback loop on the state size?\). Will volatility of ETH price affect those charges too much? Will miners help users evade charges?

#### Classes of contracts and impacts

Part of the state rent research is to identify main classes of contracts that are likely to be affected by the changes in the protocol, and provide guidelines on what they can do about it. Likely important classes:

* ERC20 token contracts and applications managing them \(DAI, Augur\)
* On-chain order books \(DEXs\)
* Ethereum Name Service [ENS](https://ens.domains/)
* Non-fungible token contracts
* Multi-signature wallets
* Gaming contracts
* Gambling contracts

#### Resources

* [State Fees Proposal](https://ethereum-magicians.org/t/state-rent-proposal-version-2-rushed/2494)
* [Alexey explains State Fees](https://epicenter.tv/episode/274/)

### eWASM

Enhancement to the Ethereum protocol is currently hindered by the inflexibility of the Ethereum Virtual Machine\([EVM](https://github.com/ethereum/wiki/wiki/Ethereum-Virtual-Machine-(EVM)-Awesome-List)\) architecture. The method of extending the execution layer has been the introduction of special “precompile” contracts. The use of WebAssembly as a virtual machine specification for executing high-performance “precompile” contracts promises to streamline the process of introducing such contracts.

eWASM is a subset of Wasm, Wasm has a couple of features which are non-deterministic, we need to eliminate them by validating contract while deploying. If contract uses non-deterministic features then it's rejected.

The current proposal is to use an even smaller subset of eWASM \(only allowing precompiles to be written as eWASM\).

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

Wasm semantics dictates that its execution has a linear memory \(only one in the current version of the spec\) that can be grown on demand. Will that linear memory be allocated every time the engine is called and then torn down at the end of the execution? If yes, how much more efficient is this compared to the current EVM model \(which does this allocation and tearing down at each CALL opcode\).

#### Interaction with the rest of EVM state

This was proposed via external functions, for example \(name made up\):

`function_SLOAD(storage_index: uint256)`

The alternative approach is not to have eWASM code access EVM state, but only exchange input/output when called. This, of course, makes maintaining large persistent data structures difficult.

#### Interpreter/compiler guarantees

Initially, this problem was brought up in the context of JITs \(Just In Time\) compilers. JIT compilers were one of the reasons why WebAssembly was a big performance improvement over JavaScript.

JIT compilers might be problematic in an adversarial environment because it is usually possible to find a program that takes an unusually long time to compile, and algorithms that decide what to compile “just in time” can be targeted too.

AOT \(Ahead of Time\) compilers can be used for Core Dev-controlled pre-compiles \(Phase 1\). For Phase 2, the plan was to initially use very straightforward interpreters, and then develop AOT compilers with necessary guarantees. The idea of first introducing interpreters is to make sure eWASM is there, giving people more motivation to work on the compilers \(which is harder than interpreter\)

#### Resources

[eWASM Proposal](https://ethereum-magicians.org/t/eWASM-working-group-proposal-for-eth-1-x/2033) <br/>
[eWASM Design](https://github.com/eWASM/design)

### Storage Pruning

Ethereum 1.0 has a storage scaling issue. Yes, the rate of growth itself is implicitly limited by the block gas limit, but there is no limit on the total amount of data accumulated over time. <br/>
Also known as Chain Pruning, this group is not related to state directly instead it is concerned with the growing size of logs, blocks, data, etc. <br/>
"If Ethereum were to grow at its current rate, 91 GB would be added per year to storage", according to the core team.<br/>
Storage Pruning is necessary and seeks to place a cap on Ethereum's data storage growth. Part of the proposal includes the deletion of historical blocks, logs, and indexes. 

#### The questions to be answered are:

* What do we absolutely need to keep to comply with the Ethereum protocol?
* Do we always need to keep all the blocks? \(maybe not, if we use backward sync, for example\)
* Do we need to keep receipts, or just logs, how much \(in Gigabytes\), or for how long?
* Do we need to always download the entire header chain or can we compress it \(with STARK proofs for example\)?
* Can we improve snapshot sync procedures \(fast sync, warp sync\) so that they prevent invalid state transitions \(with Validity Proofs, for example\)? 

#### How to handle removal of history

The first challenge to solve with regard to pruning historical chain segments is to ensure that we can prove the past even though we've deleted the past. There are two possible approaches for this:

##### Maintain a Merkle (or other cryptographic) proof of deleted chain segments 

Light clients work exactly like this and that's why are able to sync in a couple of minutes. Instead of having to go through all the headers from genesis, light clients are hard coded (or fed from the config file) a trusted checkpoint, which they start syncing from. This mechanism has two issues however:

* To keep sync fast, we constantly have to update the hard coded snapshots or the config file. This works for mainnet with an active maintenance schedule, but does not scale for private Ethereum networks.
* If no release is made, sync currently takes longer. If however the full nodes would start deleting old headers themselves, old checkpoints would become useless, forcing devs to constantly issue new releases and users to constantly pull new releases. It just doesn't scale.

##### Maintain the header chain indefinitely

It solve all of the issues that the Merkle proof mechanism has, you can always fast sync based on the header chain with only the genesis. The downside is that opposed to the Merkle proof, which is 32 bytes for arbitrary history, keeping the headers available indefinitely means indefinite chain growth.


#### Garbage Collection

If we agree on an N month/block retention policy, whenever the chain progresses, each client would delete bodies and receipts older than HEAD-N. This has an implication on the RPC APIs too however. We need to introduce the concept of a "virtual genesis block" (open for better names) which define the point of history before which the APIs cannot return data (or return that they don't maintain it any more).

#### Block/Receipt Archives

Archiving historical chain segments so they remain available for later reconstruction if need be is the hardest part of this proposal. So where to store these archives, internally or externally:

* Extra-protocol storage means hosting the data files on classical external servers, mirrored and replicated according to our security needs: FTP, S3, CDNs, etc. These could be archived by major players (Ethereum Foundation, Consensys, Parity Technologies, Internet Archive, etc). Access to these could boil down to dumb web requests.

* Intra-protocol storage means hosting the data files within some of the nodes in the Ethereum network itself: Swarm/devp2p, IPFS/libp2p, BitTorrent, etc. The archives would still be run by the same major players, but running an archive would be approachable to anyone, thus closer to the ethos of decentralization.

Since the whole point of Ethereum is decentralization, the only option we have is intra-protocol. However there are many methods by which we can store the archives in a decentralized way. Some of them are listed here:

* [Swarm](https://swarm.ethereum.org/) \(but not production ready\)
* [IPFS](https://ipfs.io/) \(accessing is easy, hosting is hard\)
* [BitTorrent](https://www.bittorrent.com/)
* LES/PIP

**Broken Invariants**

Pruning historical chain segments breaks a few important invariants within the Ethereum ecosystem:

* DApps will no longer be able to access events past the retention policy.
* Nodes will have no way of knowing if a transaction was already deleted, or never existed in the first place.
* It will be harder for nodes to do a full sync, a full sync on Ethereum mainnet with current Geth takes about 5 days, 4 days out of which is the last 2.7M blocks. If we bump the transaction throughput to 10x, apart from very special users, nobody will be able to do a full sync, nor will want to really.

#### Resources

[Pruning Proposal](https://gist.github.com/karalabe/60be7bef184c8ec286fc7ee2b35b0b5b)

### Simulation and Emulation

What are the tools that we can use to support the other groups like State Rent and the chain pruning group, to run some test scenarios and try to predict what problems that we’re going to face in the future?

Simulation and Emulation group produces data for making projections, benchmarks, and parameter calibrations for other groups.

The working group is tasked with developing three setups:
* A simulation framework that, when a dataset is entered, produces an output to estimate properties of proposed changes (such as uncle rate reduction and gas limit increases). Currently [Wittgenstein](https://github.com/ConsenSys/wittgenstein) is suggested.
* An emulation framework that alters environment conditions to test properties of launched changes
* A testnet that launches these changes together on the same network

**Simulation** handles models of the software agents \(in our case Ethereum client software instances\), coarse enough to be performant, and fine enough to capture the important facets of the agents. <br/>

**Emulation** handles the actual software agents \(in our case the actual implementations of Ethereum like geth and parity\), placed into the virtual environments with lots of freedom to change parameters of virtual machines and the network connecting them.

Potential questions that simulation may be able to answer:

* Will uncle rate become much less of an indicator of the network congestion if most of the Ethereum nodes propagate blocks straight after verifying Proof Of Work \(instead of fully processing the block as they used to do\)?

Potential questions that emulations may be able to answer:

* What is the function that describes the relationship between the rate of success for snapshot synchronizations \(fast sync, warp sync\) and things like prevailing bandwidth and state history pruning threshold?

Developers are in the process of collecting datasets for simulation and finalizing parameters for simulation \(one of which might be uncle rate\).

**Properties to test**

* Block propagation, to reduce uncle rate
* If yes, raise gas block limit
* If yes, consider increasing cost of storage wrt compute
* Determining what the next bottleneck is
 (a) Assume compute time is reduced
 (b) Assume bandwidth limit results in many uncles

**Dataset Preparation**

Datasets are being collected [here](https://drive.google.com/drive/folders/1cJRMKxhGBzXMxNBcPi011Mg5e2Dw1JU1) from various sources like [WhiteBlock](https://whiteblock.io/), [Etherscan](https://etherscan.io/) etc.

#### Resources

[Simulation Proposal](https://docs.google.com/document/d/1pIW6Uac5Qanx_L5Y_G4Ucrx_gjITkBgzQKmlBQbW3Cg/edit)

## Deliverables

#### Measures requiring hard-forks:

* State rent \(or state growth limiting\)
* eWASM

#### Measures likely not requiring hard-forks, but requiring cross client code coordination on the network protocol:

* Storage pruning

## Resources
* [Ethereum 1x Definition (part 1)](https://ledgerwatch.github.io/Ethereum_1x_Definition_part_1)
* [Ethereum 1x Definition (part 2)](https://ledgerwatch.github.io/Ethereum_1x_Definition_part_2)
* [Ethereum 1x Definition (part 3)](https://ledgerwatch.github.io/Ethereum_1x_Definition_part_3)
