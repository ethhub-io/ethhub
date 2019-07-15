title: Ethereum 2.0 Researches Reddit AMA - EthHub
description: All questions and answers from the Ethereum 2.0 researchers AMA done on Reddit.

# Ethereum 2.0 Reddit AMA

## Part 1

**Q: When, as in period of time, do you think Ethereum will be able to solve scalability issues?**

A: In phase 1 \(about 2020 by my estimate\) we will have shard data. Those shards, even without an EVM, can be used as the data availability layer for TrueBit \(and other alternative execution engines\). Phase 2 \(about 2021\) is when we will have scalable L1 execution. \[Justin Drake\]

**Follow up Q: ELI5 execution engines**

Follow up A: An execution engine is a way to compute state assuming consensus on data. The execution engine for the EVM is "naive re-execution". There are more fancy execution engines such as TrueBit and SNARK/STARK-based validity proofs. \[Justin Drake\]

**Q: Are economists being consulted to help decide the issuance rate of a full POS system? Stated more broadly, who is helping/advising the ETH 2.0 team on the effects certain issuance decisions will have on the network and community \(both in the short and long term\)?**

A: Personally at this point the feedback I'm most interested in is actually feedback from potential stakers. The main question basically being, are there any other tweaks we can make to the economics that, given a fixed level of reward, will \(i\) encourage more people to validate, and \(ii\) encourage many small solo validators or smaller pools, as opposed to a few large pools. \[Vitalik Buterin\]

**Q: Considering that Yoichi is not working anymore in the Foundation, what are your plans on formal verification of ETH 2.0 specs?**

A: I'd say that formal verification of the spec will make sense when the spec is more mature and stable, maybe mid 2019. Anyone interested in doing formal verification of the ETH 2.0 specs in a few months, please send a grant proposal. \[Justin Drake\]

**Q: What is the best response to a developer who is hesitant about building on ethereum today, given that it will be "replaced" by ETH 2.0 over the next few years?**

A: I expect that once the state and execution model for Serenity solidifies \(see [https://ethresear.ch/t/a-minimal-state-execution-proposal/4445](https://ethresear.ch/t/a-minimal-state-execution-proposal/4445) for one minimal proposal\) we'll start working with the developer community on modifications to high-level languages \(Solidity, Vyper, etc\) and best practices. Hopefully at that point it will become clearer how to build applications in such a way that they could be redeployed as-is on the 2.0 chain. At least that's my hope. \[Vitalik Buterin\]

A2: Building on Ethereum 1.0 today is great for learning and prototyping. It's also great for assembling a culturally-aligned team consistent with the philosophy of the Ethereum community \(which may be different than the philosophy of the Bitcoin, Ripple, Bitcoin Cash, EOS, Tether, etc. communities\). \[Justin Drake\]

**Q: Can we run multiple validator clients on a single machine assuming we've got multiple 32 Eth deposits?**

A: Yep! There's nothing preventing you from using one machine to run multiple validators. The only hard limit you'll face is that the number of shards you are assigned to validate increases linearly with the number of validator slots you have, so if you have thousands of ETH a laptop will not suffice and you'll need something more powerful. \[Vitalik Buterin\]

A2: Short answer: Yes.

Long answer: You will need to register a validator for every 32 ETH. In phase 0 \(just the beacon chain, no shards\) you can likely handle thousands of validators on a single machine.

After phase 1 the number of validators that can be operated on a single machine depends on how resourceful your machine is. A mainstream laptop should comfortably handle one validator, and likely handle 2-10 validators at max capacity.

The computational resources scales linearly with the number of validators until you reach ~1,000 validators. At that point there are scalability advantages in being a super-node, i.e. a full node for every shard. \[Justin Drake\]

**Follow up Q: How much importance are the devs placing on being able to run setups at home wrt keeping Ethereum decentralised and being able to move ETH in and out of staking pools?**

Follow up A: It's definitely a goal I care about. The alternative to staking at home is staking on AWS or staking through a pool, and both are risks for decentralization.

Concrete ways we try to be friendly to staking at home:

* Relatively forgiving penalties for being offline, so you earn a net profit as long as you're online more than ~50-67% of the time
* Keeping the cost of validating the beacon chain low
* The anti-correlation penalty scheme, which more heavily penalizes validators that misbehave at the same time as many other validators \(which is more likely if you're on the same pool or VPS or whatever\). \[Vitalik Buterin\]

**Q: How can I help / get involved? I fell in love with Ethereum not too long ago. I’ve been reading Zcash’s BLS12-381 Elliptic Curves and for the past few days these are all thats been on my mind. I love this project now and just found ethresear.ch. I really wanna help in any way possible! Thanks again for all your hard work. I can’t stop reading these posts.**

A: For researchers a good way to contribute and gain visibility is to post quality content on ethresear.ch. If you are a developer consider joining one of the numerous ETH2.0 implementation teams. \[Justin Drake\]

A2: Hi! The best way to get involved is to find something that captures your interest and to dig in. Because Ethereum is a radically open platform, the research and development is also generally very open and very accessible.

* Keep reading. Follow your interests down all the little paths and begin to build a mental model of the ecosystem.
* [https://ethresear.ch/](https://ethresear.ch/) is a great place to follow and begin to contribute to research discussions.
* [https://gitter.im/ethereum/sharding](https://gitter.im/ethereum/sharding) is where a lot of the day to day conversation about Serenity is happening \(developers chatting from various projects\)
* [https://github.com/ethereum/eth2.0-specs](https://github.com/ethereum/eth2.0-specs) Read the spec! but not only read it, be an active reader. If you find an error, typo, bug, etc, submit a PR. Also check out the issues and PRs in the spec repo. We are constantly discussing changes, fixes, updates and anyone can contribute.
* If you are a dev, open up one of the eth2.0 client projects and pick a "good first issue". These allow you to touch the codebase, contribute a bit, get the lay of the land, and provide the foundation to tackle bigger issues from there.

^ Those are Serenity specific suggestions, but beyond that, just find projects you are interested in and begin contributing. There is so much to do and project leads are always excited to have helping hands. This stuff doesn't build itself :\) \[Danny Ryan\]

A3: If you're interested in Cryptography especially, you can also check out another BLS - Boneh–Lynn–Shacham signature spec for Serenity and help to review it: [https://github.com/ethereum/eth2.0-specs/blob/master/specs/bls\_signature.md](https://github.com/ethereum/eth2.0-specs/blob/master/specs/bls_signature.md) :\)

For research, as Justin and Danny said, ethresear.ch is the sanctuary. And first, you can take a look the various topics on Ethereum Sharding Research Compendium to see which area you're most interested in.

* For implementation, there are multiple topics:
  * Consensus layer - implement the spec!
  * P2P layer design and implementation - see [https://github.com/ethresearch/p2p](https://github.com/ethresearch/p2p) \[Hsiao-Wei Wang\]

**Q: From my limited understanding of Eth 2.0 specs, I gather that shards will be mostly independent, with cross-shard communication being slow and requiring multiple steps. As a consequence, smart contracts will only be able to interact lively with assets from within their deployed shard, and will have to go through slow cross-shard communication to interact with assets outside.**

**Given this topology, are we not aiming to improve scalability at the cost of sacrificing user experience \(slow response of smart contracts in non-obvious ways\)?**

**For instance if I want to play cryptokitties, I will need to make sure to interact with the contract that is deployed on the shard where my eth address resides, and not with any of the other contracts that reside on other shards. Then, if I want to interact with the kitties of someone else who resides on a different shard, my experience will be much slower and cumbersome than if that person would reside in my shard \(or at least this is how I understand the system will work, please correct me if I am wrong\). Given that the end goal is to scale to a very large number of shards, then the likelihood to have to go cross-shard increases exponentially with time, and thus the user experience gets progressively worse and worse.**

A: Cross-shard communication will definitely be slow at base layer, however there are higher-level mechanisms that can be used to implement fast cross-shard communication on top of a base layer that allows any cross-shard communication at all even if slow. See [https://ethresear.ch/t/a-layer-2-computing-model-using-optimistic-state-roots/4481](https://ethresear.ch/t/a-layer-2-computing-model-using-optimistic-state-roots/4481) for an example of how this could be done.

In general, I expect a lot of the long-run innovation in improving the smart contract development experience to happen at higher levels in this way; I write about why this is a good idea at length here: [https://vitalik.ca/general/2018/08/26/layer\_1.html](https://vitalik.ca/general/2018/08/26/layer_1.html) \[Vitalik Buterin\]

**Q: What happens to all the contracts currently running?**

A: It is somewhat speculative at this point. My best guess is that Ethereum 1.0 contracts will stay running as-is for a long time \(say, 10+ years\) without any migration to Ethereum 2.0. This can be made sustainable by doing two things:

1. Lower the inflation \(e.g. reduce it by 20x, bringing the PoW security to a blockchain such as Ethereum Classic\). Completely removing inflation—relying on transaction fees only—would also be possible \(see below for security argument\).
2. Use Ethereum 2.0 to regularly finalise Ethereum 1.0, counter-balancing the reduced security and preventing long-range 51% attacks. This requires Ethereum 1.0 nodes to be beacon chain light clients, which should take years to happen.

If the community gets tired of Ethereum 1.0 a bomb mechanism \(e.g. difficulty bomb, issuance bomb, gas bomb, etc.\) can gracefully kill it. Another possibility is for Ethereum 1.0 to become a contract on Ethereum 2.0. I don't see this as a practical solution, but I'm open to being convinced otherwise :\) \[Justin Drake\]

A follow up: I'll add that if any specific user wants to migrate their application to the 2.0 chain, then they should be able to just take their existing high-level code \(Solidity or Vyper\), make relatively few changes and redeploy. The main difference between the eth1 and eth2 systems that users will need to worry about is likely to be rent \(or equivalents like gas-payment-extended bounded TTLs\). \[Vitalik Buterin\]

**Q: Is there a worry that shards will become “gentrified” until full shard interoperability? Basically, will one shard capture all the defi apps because they can't directly communicate with each other on separate shards?**

A: I would say if that happens, that will create a large incentive for someone to create a defi dapp that can interact with the other defi dapps through asynchronous cross-shard transactions and launch it on a cheaper shard. \[Vitalik Buterin\]

A2: At the start in times of low usage, the economic load-balancing might result in over and under utilized shards.

Overtime as usage increases, I expect the economic benefits of deploying and interacting on particular shards will become more tangible and result in a more economically rational distribution across shards.

Observing the emergent behavior is going to be super fascinating :\) \[Danny Ryan\]

**Q: Can we run the same validator on multiple machines - in order to avoid penalties if one machine was compromised ? If yes - what happens when we run a validator on 3 machines, one goes temporary offline, one is compromised, one is OK?**

A: For small amounts of ETH I'd recommend just running on one machine; unless many other validators get penalized at the same time as you, the penalties are not too large. If you do want to decentralize your validator, then we have recently made progress toward validation being more multi-party-computation friendly, which would allow you to run a validator as a 2-of-3. In that case, as long as two of the three sub-nodes are functioning correctly you'll be fine. \[Vitalik Buterin\]

A2: Yes! Ethereum 2.0 is friendly to n-of-m schemes thanks to BLS signatures. For example, with a 2-of-3 scheme you have can three computers, each with a share of the validator private key, such that two need to be online at any given time. This improves security as well, because an attacker now needs to compromise two of the BLS key shares. \[Justin Drake\]

**Q: Is there tech from any competitors such as Dfinity \(or any others\) that is worth adopting into Ethereum 2.0, or is the work all other dapp/smart contract platforms doing not relevant/good enough for ETH 2.0?**

A: Part of the job of the research team is to absorb good ideas from research papers and other blockchain projects. I keep a keen eye on technically interesting projects such as Dfinity, Coda, Zcash, etc.

Competitors definitely also have good ideas, and learning from each other is part of the game :\) \[Justin Drake\]

**Q: Do we need to run a full node to also earn from network fees or would the validator client handle this?**

A: Depends what you mean by "full node". The design of the sharding system is such that no one needs to run a node that verifies all of the data of all of the shards. A validator client validates the beacon chain and the specific shards that you get assigned to validate, and that is sufficient to earn network fees. \[Vitalik Buterin\]

A2: The validator client should abstract the necessary tasks to get revenue from the different revenue streams. \(This includes being a full node for the beacon chain and one shard at any given time, but that's a technicality you don't have to worry about.\) \[Justin Drake\]

**Q: Very interested to hear about the efforts currently underway at the EF and strategic partners/OEMs to design and manufacture the VDF hardware.**

**It's also the thing that scares me the most about the proposed design;i can see how they would really increase the security of the random sample selection process in addition to RANDAO but manufacturing hw is a costly, difficult endeavor often subject to unforeseen issues and delays.**

**On that note is an economic incentive structure for running a VDF node being considered?**

A: **Very interested to hear about the efforts currently underway at the EF and strategic partners/OEMs to design and manufacture the VDF hardware.**

We're working our way with various partners, including Synopsys, AWS, TSMC, GUC, etc. VDF announcements to come in February :\)

**manufacturing hw is a costly, difficult endeavor often subject to unforeseen issues and delays.**

Right. The good news is that Ethereum 2.0 can launch just fine without VDFs, so we're not betting Ethereum 2.0 on the success of VDFs. The current plan is to have VDF hardware ready in 2020, but 2021 would also be acceptable.

From a financial perspective, we may share the total costs \(estimated at $15m\) with Filecoin and other projects interested in VDFs. We are already sharing costs with Filecoin on viability studies.

**On that note is an economic incentive structure for running a VDF node being considered?**

Short answer: yes, of course :\)

Long answer: the ethresear.ch post provides a bit of clarity on that.

**highly specialized hw always connected providing a crucial function to the network it would be a prime target for potential adversaries to disrupt or compromise**

Right. The good news is that we only need one VDF evaluator to be online for normal operation, and even if everyone goes down it's not a huge deal. The main negative consequence is that dApps relying on unbiasable randomness will have to wait longer than expected for the random numbers to arrive. \[Justin Drake\]

**Q: zk-STARKs are powerful and I have been reading Eli’s and the others paper on it. Are recursive zk-STARKs ever doable? I know Coda is planning on using Recursive zk-SNARKs to shrink chains but the lack of transparency is worrying.**

A: I don't see what fundamentally prevents them from happening. Recursive \[any zero knowledge proof schemme\] just means using the ZKP mechanism to make a ZKP of the ZKP's own verification procedure. The main challenge in practice is just that these verification procedures themselves have a high cost \(eg. there's 50-500 kB worth of hashes in a STARK to verify\), and this cost multiplied by the ZKP's overhead is quite a big number. ZK SNARK verification is in contrast much more "concise". \[Vitalik Buterin\]

A2: **Are recursive zk-STARKs ever doable?**

In theory yes, but as I understand recursive zk-STARKs won't make sense from a performance standpoint for most applications, at least in the medium term. \[Justin Drake\]

**Q: What’s the final scalability limit of Ethereum post Serenity? Gas limits per block? Blocks per second?**

A: The current design has a fixed number of shards, at most one block per 6-second slot, and fixed block sizes. This means that the data bandwidth is capped. The gas limit on the other hand will likely be floating, just like Ethereum 1.0. \[Justin Drake\]

A follow up: Though in the current phase 1 spec that's sitting around in draft mode the block size is so far fixed to 16 kB, as keeping it fixed makes the code for proofs of custody, data availability proofs, etc much simpler.

If we want to bump up capacity later increasing the shard count may well be the simpler way to do it. \[Vitalik Buterin\]

**Q: Why should anyone move to the Beacon Chain? How exactly do you envision the move to happen?**

A: **Why should anyone move to the beacon chain.**

Specifically, only validator balances exist in the Beacon Chain. User balances and state exist in the shard chains.

Validators will move to the beacon chain to seek profit by providing security and resources to network. Note there is a new proposal to have the beacon chain finalize the PoW chain during the transition period so the validators would be able to provide security both to the new shards and the existing chain.

Users will move to the shard chains to participate in the new scalable, sharded landscape. We envision economic activity to begin to move over as the system stabilizes and begins to show clear economic benefits to the users. It is important to note that a user could choose to not move until the eth1.0 state is rolled into a shard.

**How exactly do you envision the move to happen?**

At first, this will just be a single directional deposit for validators only to begin validation. Once the state execution layer is in the new 1024 shards, users will be able to transfer eth directly to the shards from the PoW chain. In the long term, the plan is to roll the PoW state into one of the shards. The current most favorable strategy from our perspective is to fork the PoW state root into a contract along with an EVM interpreter. Users could then execute txs on the existing eth1.0 state by call the contract along with the merkle witnesses of the state they need to access. This option is nice because it allows us to cleanly deprecate eth1.0 support in the long term. \[Danny Ryan\]

A2: Moving to the beacon chain is done by sending ETH to a so-called "deposit contract" on Ethereum 1.0. People would send ETH to the beacon chain to become an Ethereum 2.0 validator and gain financial rewards. \[Justin Drake\]

**Q: How much funds does Ethereum foundation have and are these enough for finishing Eth 2.0?**

A: The EF has tens of millions of dollars in fiat, and a bunch of ETH. More than enough to finish ETH 2.0 :\) \[Justin Drake\]

**Q: How is the status of a possibly fixed eth supply at some point in the future? Do you think it's likely?**

A: I don't know about fixed ETH supply, but we may get to a point of decreasing ETH supply. Indeed, we are looking into transaction fee schemes that burn ETH, and burnt ETH may outweigh minted ETH. \[Justin Drake\]

**Q: Have you looked into hyraxZK. They are zk-SNARKs that do not require a trusted setup. Any thoughts on them being used in the future as the sizes are still very small. The only thing is they wouldnt be Quantum-Resistant but the proof size won’t be similar to a zk-STARK. I wonder what they can be used for offchain as well, especially in networking by producing a zk proof of incoming packets that acts as Natural DDOS Protection. Just some thoughts.**

A: Have not looked into Hyrax specifically, but I am totally not surprised that things like it exist. I'm definitely very happy with the progress the general-purpose ZKP space has accomplished in the last few years; the very concept of general-purpose ZKP is pretty godlike compared to what I imagined was possible with cryptography as a child.

Our general instinct is to find ways to make it possible to get the benefits of many different ZKP schemes with different tradeoffs in ethereum. The simplest way to do this would be to encourage the development of such tech as application-layer or network-layer addons so that it we do not need an agreement at consensus layer about a single ZKP scheme that everyone uses. \[Vitalik Buterin\]

**Q: V said that there are no fundamental problems left to solve. Is this true for only phase 0? If so, how confident are you about the other phases?**

A: Personally I am confident in all of the current fundamental technologies for all the phases outlined so far \(Casper FFG and CBC, sharding, erasure coded data availability proofs, proofs of custody, receipt-based async transactions, layer 2 for acceleration, abstraction, rent, "stateless client" verification\). There is definitely still a lot of room around the edges for optimization though. \[Vitalik Buterin\]

**Q: Why was Hybrid Casper ditched when it looks like the Beacon Chain kind of has nothing to do with the PoW chain? or Why not re-instate Hybrid Casper considering its testing is/was finalized?**

A: Honestly hybrid Casper is a bit of a dead end. Actually implementing/testing it across all the clients would require setting up a lot of infrastructure that we would then need to throw away. The design was highly inefficient because of its "implemented-in-EVM" nature, and it turned out that we could not really benefit from the ease-of-implementability of being done in EVM because we would need to write a lot of special-purpose code to make verification of signatures parallelizable. So we chose the route that would be somewhat more painful in the short term, but significantly lower headache to actually get to a stable sharded system overall. \[Vitalik Buterin\]

A2: I wrote up some notes on the deprecation of EIP 1011 here [https://notes.ethereum.org/s/rJDrKoBOQ](https://notes.ethereum.org/s/rJDrKoBOQ) \[Danny Ryan\]

**Q: 1. Since it is a one way transfer to the beacon chain, my understanding is that there will be two tokens: ETH1.0 and ETH2.0. Right?**

1. Will The beacon chain allow tokens to be send. I.e. will exchanges be able to list the token before phase 2?
2. My feeling is that from a risk/reward perspective, stakers will expect returns more in the area of emerging market debt \(+20%\) esp. in the beginning. But all discussion I saw was ~2%. Any comments on this?
3. Gutfeeling: how much "unsolved computer science problems" for phase 1, 2 and 3 roughly? I understood for phase zero it has arrived at 0.
4. Will we consider some kind of tax baked into the system to ensure sustainability of core developments and infrastructure?

A: **Will The beacon chain allow tokens to be send. I.e. will exchanges be able to list the token before phase 2?**

ETH in the beacon chain would not be transferable \(anywhere!\) until phase 2. That will make exchanges harder, although we may see a futures' market. My guess is that we will see 1 ETH ~ 1 BETH at pretty much all times :\) \[Justin Drake\]

**My feeling is that from a risk/reward perspective, stakers will expect returns more in the area of emerging market debt \(+20%\) esp. in the beginning. But all discussion I saw was ~2%. Any comments on this?**

The reward/penalty constants are certainly not yet finalized and could use more community debate and input. That said, the rate does scale depending on the number of validators participating. If the fair market rate is really 20%, then a lower number of validators will show up. If the fair rate is 2%, then a ton of validators will show up. The economics of staking will find the natural equilibrium. That said the main risk here is if we set the target rate too low and the equilibrium lands at a low participation rate \(and thus low security of the network\).

Although ~2% \(@ 10M eth validating\) is not set in stone, the idea for a low rate is that a huge amount of ETH is already being held as a speculative asset. Any marginal rate of return on top of this already intended long-term hodling is a gain for the hodler. \[Danny Ryan\]

**Q: How would you \(and or service providers\) ensure the eth on the Beacon Chain is the same as that on the PoW chain and vice versa?**

A: Arbitrage is always possible in one direction by buying 1 BETH for 1 ETH. A key design goal of Ethereum 2.0 is full fungibility for ETH tokens between the Ethereum 1.0 chain, the beacon chain, and the shards. Two-way transfers between the beacon chain and the shards, as well as between shards, should come in phase 2. \[Justin Drake\]

**Follow up point: If you wait until phase 2 for two-way flow, you privilege the very few stakers able and willing to wait an undetermined number of years for access to their money.**

**This will be great for those few \(probably north of 25% interest rates!\) but not very great for security.**

Follow up A: y**ou privilege the very few stakers able and willing to wait an undetermined number of years for access to their money**

The ultimate loyalty test :\)

**probably north of 25% interest rates!\) but not very great for security.**

We do have a minimum amount at stake to launch phase 0, around 214 \* 32 ETH = 524,288 ETH. So we're effectively capping the interest rate \(will be less than 25%\) and setting a minimum security level. \[Justin Drake\]

**Q: For how long is the 32eth locked up when running a validator client? What happens if the machine I'm using gets destroyed or stolen during the lock up period? Can you switch machines?**

A: **For how long is the 32eth locked up when running a validator client?**

At least as long as you are a validator. Withdrawal times should be a few days/weeks/months depending on how many other validators are trying to withdraw.

**What happens if the machine I'm using gets destroyed or stolen during the lock up period? Can you switch machines?**

You can switch machines. You need a copy of your private keys in case your machine gets destroyed or stolen.

Another thing is the withdrawal key used for withdrawals only. Keep that one in cold storage ideally. \[Justin Drake\]

**Q: Contributing to Ethereum 2.0? Are there any projects which are some sort of "under water", like only few people working on it.**

A: I feel at this point there are enough implementation teams, at least compared to some of the other issues that are underaddressed. Off the top of my head:

* Solidity being compile-able to E-WASM
* Vyper being compile-able to E-WASM
* Thinking about research problems related to phase 2, particularly around account abstraction, asynchronous contract programming models, etc
* Privacy, eg. see [https://ethereum-magicians.org/t/meta-we-should-value-privacy-more/2475](https://ethereum-magicians.org/t/meta-we-should-value-privacy-more/2475)
* Improving the state of decentralized messaging and file storage \[Vitalik Buterin\]

Follow up A: A few more things good to work on:

* liibp2p implementations in various languages
* Doing security reviews of the spec
* prototyping account and state execution in eWASM
* a lot of work in cross client testing coming up in the next couple of months \[Danny Ryan\]

**Q: We have experienced consecutive delays with Constantinople due to bugs found late in the process on a comparatively low risk / simple upgrade.**

**What work is being done to mitigate this on Phase 0 and 1 given how much more complex these implementations will be? \(I.e. What testing, third party audits, other considerations are being taken to ensure seamless implementation/integration?**

A: As the phase 0 spec is moving into a more stable place, we are beginning to look into explicitly bringing in third party audits, academics, and formal analysis. In addition to this, we are currently laying down the foundations of cross client testing and fuzzing akin to eth1.0. You're correct in that the consensus/system layer of eth2.0 is much more complex than the single PoW chain so we are constantly trying to reduce complexity and simplify. This is a major engineering effort that will require many parties other than our research team to plan, build, test, execute, and maintain. I think it is a major strength that so many independent teams with a diverse set of expertise have stepped up to contribute.

Note, one of the design goals in the [spec readme](https://github.com/ethereum/eth2.0-specs/blob/master/README.md) -- "to minimize complexity, even at the cost of some losses in efficiency"

We're excited to see new efforts like the "Ethereum Cat Herders" and scheduled release cycles emerging in 1.0 and plan to incorporate any best practices and efforts into the 2.0 process. DePM \(decentralized project management\) is hard, but we continue to learn and continue to get better. \[Danny Ryan\]

**Q: How difficult will it be for 1.0 contracts to work on Serenity? Should developers expect to rewrite their contracts to account for state rent and cross-shard communication?**

A: Solidity can already compile to WASM and I believe it is in Vyper's roadmap to do so as well. These naive compilations might be inefficient \(e.g. keeping 256 bit types in the 64bit wasm machine\) so some amount of rewrite or utilization of optimizers might be called for.

Beyond that, there are some unknowns that might change the approach to certain contract programming modesl. For example, storage fees might call for a new ERC20 contract design in which user balances are stored in separate child contracts so that users become responsible for managing their own storage fees related to their coins. \[Danny Ryan\]

**Q: What is the latest view on how the "upgrade" to Ethereum 2.0 will happen? Can you take us through the different phases/hardforks that will in the end enable the full PoS/sharded/WASM blockchain, and what each will enable?**

A: Eth2.0 is broadly divided into three phases -- Phase 0, 1, and 2.

* Phase 0 - The Beacon Chain
  * This phase is the launch of the core system level functionality of the new PoS chain \(the beacon chain\).
  * Validators can submit deposits, join the validator set, and build/finalize the core chain.
  * At this point the chain will have Casper finality, an RNG, shuffling into the various validator roles, and simulate crosslinking in the \(currently\) non-existent shard chains.
* Phase 1 - Shard Chains \(data\)
  * This phase is the launch of the shard chains, but only as a blockchain of data. \(Execution and state comes in phase 2\).
  * At this point, validators will additionally build these data chains and finalize the each shard back into the beacon chain via "crosslinks" and attest the availability of the data. These crosslinks were already being created in Phase 0, but had a stub for the shard hash being finalized. In this phase, that hash becomes "unstubbed".
  * Shard data chains begin to have some utility for applications that need a high availability data store.
* Phase 2 - Shard Chains \(state and execution\)
  * This phase is the launch of state and execution of state \(eWASM\) on the shard chains.
  * This is when users and applications will begin to migrate to Serenity and use it to it's full potential.
  * Cross shard txs will be available at this point, and users can begin developing any number of "layer 2" execution engines on top.

The above \(especially phase 2\) might be divided into sub-forks, and there will be a fork during/after phase 2 to bring in the eth1.0 state/evm into a contract. \[Danny Ryan\]

**Q: I'm quoting James' article:**

**"This means there will be little reason to migrate smart contract code or users until Phase 4 is released, potentially in the mid-2020s". Does this mean, ETH2.0 wont be usable before 2025?**

**"ETH2.0 designers do not know what the cross-shard communication system will look like." If you're so unsure about the features of ETH2.0, why is it being developed at all? What will be the advantages in daily use compared to EHT1.X? Why should anyone wait till "the mid-2020s" to use ETH2.0?**

A: 2025 sounds... unlikely!

I publicly made the prediction \(since July 2018\) that phases 0, 1, 2 will come in 2019, 2020, 2021 respectively. Scaling from shards will come in phase 1 and phase 2.

On the topic of timelines, for phase 0 specifically, ideally the spec should be close to final in Q1, cross-client testnets in Q2, security audits in Q3, mainnet launch in Q4.

As a rule of thumb, launching in December is hard because of the holiday season. So November 2019 and January 2020 would be my two best guesses for phase 0. \[Justin Drake\]

A2: I answered a related question here [https://www.reddit.com/r/ethereum/comments/ajc9ip/ama\_we\_are\_the\_eth\_20\_research\_team/eeufhqb](https://www.reddit.com/r/ethereum/comments/ajc9ip/ama_we_are_the_eth_20_research_team/eeufhqb) \[Danny Ryan\]

**Q:** [https://hackernoon.com/what-to-expect-when-eths-expecting-80cb4951afcd](https://hackernoon.com/what-to-expect-when-eths-expecting-80cb4951afcd)

**From the article above, this is what I understand as the timeline of Ethereum 2.0:**

**Phase 0 will be available in year 2020**

**Phase 1 will be available in 2022**

**Phase 2 will be available in 2023/24**

**Given the above timeline, is it fair to say that DAPP's have to wait at least 4 years before they can run their smart contracts on top of Ethereum 2.0?**

A: Hi! That article is written by an independent engineer that has been following development so it is not necessarily our 1-to-1 opinion. That said, I'm only seeing the following in the article -- "Which is to say, while ETH2.0 may launch this year, don’t expect ETH2.0 to support asset transfer or smart contracts until at least 2020."

I agree that assets and smart contracts won't be available in eth2.0 in 2019. At the latest, I expect phase 2 to launch in 2021, but we are building a complex system and can't say for sure what unexpected challenges might arise between now and then.

Waiting until 2023/24 is entirely out of the question for phase 2 imo. \[Danny Ryan\]

**Q: With eWASM will we be able to write contracts in Rust and/or any language that compiles to WASM in addition to Solidity? Where can one find out more about that and/or potentially help out? Thanks :\)**

A: Yes you will be able to write contracts in any language that compiles to WASM :\) I expect specific toolkits/frameworks to spring up in the languages people are particularly interested in \(e.g. Rust, go, typescript, etc\) to aid in writing contracts in these languages.

[https://github.com/ewasm/design](https://github.com/ewasm/design) is a great place to get started. The eWASM team has compiled a ton of info here to understand the project from a high level.

[https://gitter.im/ewasm/Lobby](https://gitter.im/ewasm/Lobby) The eWASM team and broader community congregate in this gitter room and I'm sure would be willing to provide more guidance and answer any questions you have. \[Danny Ryan\]

**Q: Hi guys, Would you like to implement an optional decentralized identity layer in the future? like an option to use DID's or something. so the user can use zero knowledge proofs for Dapps that requires some proof of credentials of the user. Greetz**

A: Decentralized identity systems are definitely very interesting, but imo out-of-scope for blockchain base layers. The good news is that it's a Turing-complete platform, so anyone can build one on top of ethereum \(1.0 or 2.0\), and yes that are teams working on different approaches to it already. \[Vitalik Buterin\]

**Q: What is the one thing on eth 2.0 dev that keeps you up at night?**

A: In my mind the Ethereum 2.0 abstract design is a remarkably elegant/slick/simple design. I worry that we botch the spec with poor taste in some of the implementation details, or bugs that we miss. \[Justin Drake\]

**Q: How will the Eth1.0/PoW chain eventually be migrated over?**

A: See the bottom of this post [https://www.reddit.com/r/ethereum/comments/ajc9ip/ama\_we\_are\_the\_eth\_20\_research\_team/eeucd4f](https://www.reddit.com/r/ethereum/comments/ajc9ip/ama_we_are_the_eth_20_research_team/eeucd4f)

tldr, fork into a stateless contract on a shard \[Danny Ryan\]

A2: See [https://www.reddit.com/r/ethereum/comments/ajc9ip/ama\_we\_are\_the\_eth\_20\_research\_team/eeub9sp/](https://www.reddit.com/r/ethereum/comments/ajc9ip/ama_we_are_the_eth_20_research_team/eeub9sp/) \[Justin Drake\]

**Q: What are the current incentives for a person to run their own beacon node?**

A: It is a similar set of incentives as why you would run an eth1.0 node -- mining, run applications \(block explorer, wallet services, dapp portal, etc\), hobbyists wanting direct connection to the network, etc.

* If you are a validator, you will receive rewards for operating a node and signing consensus messages.
* If you run some sort of application, it can be beneficial to run a beacon chain to directly sync the shards you need.
* You also might serve light clients and applications as a business. I fully expect some some entities to experiment with this model.
* If you are a hobbyist, you might just like running the protocol directly for self-sovereignty :\) \[Danny Ryan\]

A2: Financial rewards through ETH inflation. I think Eric Conner has a spreadsheet somewhere. See [https://twitter.com/econoar/status/1070713152864583682](https://twitter.com/econoar/status/1070713152864583682) for example here—numbers presented here likely on the low side. \[Justin Drake\]

**Q: How do the researchers and developers feel about the complexity of ETH 2.0?**

A: We're definitely trying hard to bring the complexity down! Examples of complexity decreases that we've made in the last ~3 months include:

* Switching FFG from the "per-block finalization" model to a simpler epoch-based model
* Moving shard committee calculation outside the state
* Replacing the RANDAO hash onion construction with a simpler BLS construction \(and same with the hash onion for proofs of custody\)
* Storing validator state change slots in the validator record, making each validator's state transition process much more understandable
* Making shard blocks fixed size rather than variable size \(which allows removing a lot of boilerplate for handling transitions\)

That said we recognize that there's still a way to go, and many features of eth2 don't feel neat and clean the way eg. Nakamoto PoW does. I personally hope a medium-term switch to Casper CBC \(see [https://vitalik.ca/general/2018/12/05/cbc\_casper.html](https://vitalik.ca/general/2018/12/05/cbc_casper.html)\) can mitigate some of that. \[Vitalik Buterin\]

**Q: Is there any work being done on reducing the size of the blockchain as it grows?**

A: You mean the current chain or the 2.0 chain? Since this AMA is primarily about on the 2.0 chain I'll focus on that. The beacon chain state size is bounded, and there are no objects that hang around forever; even validator records disappear once either their balance drops too low or the validators exit voluntarily and then the withdrawal and exit waiting periods pass. On the shard chains, we're looking at ongoing storage maintenance fees for every byte of storage, "hibernating" accounts that do not pay up \(at which point their users are responsible for storing and maintaining the data needed to revive those accounts if they need them\). \[Vitalik Buterin\]

A2: If you are talking about the Ethereum 1.0 chain size there are a number of workgroups in place and some of them deal with decreasing the chain state or slowing down chain state growth.

See:

* [https://ethereum-magicians.org/t/meta-ring-to-discuss-and-coordinate-all-ethereum-1x-efforts/2048](https://ethereum-magicians.org/t/meta-ring-to-discuss-and-coordinate-all-ethereum-1x-efforts/2048)
* [https://ethereum-magicians.org/t/ethereum-1-dot-x-a-half-baked-roadmap-for-mainnet-improvements/1995](https://ethereum-magicians.org/t/ethereum-1-dot-x-a-half-baked-roadmap-for-mainnet-improvements/1995)
* [https://ethereum-magicians.org/t/state-rent-proposal-version-2-rushed/2494](https://ethereum-magicians.org/t/state-rent-proposal-version-2-rushed/2494) \[Hudson Jameson\]

**Q: Inter-shard transactions - how do downstream shards protect themselves against kiting exploits \(A-&gt;B B-&gt;C C-&gt;D where the transfer A-&gt;B is later challenged\)?? I can imagine kiting tumblers that might make this a computationally intractable challenge.**

A: There isn't really a concept of "challenging transfers" in the current spec, and if you mean plain old fraud proofs then the answer is that if a block that was confirmed into a history turns out to be invalid then the entire history from that point on is invalid and should get discarded. \[Vitalik Buterin\]

**Q: If I deploy a contract in ETH 2.0 will it randomly be assigned to a shard?**

A: No. You specify the shard you want. You'll chose based on proximity to contracts of interest, and gas prices. \(Each shard will have a separate gas market.\) \[Justin Drake\]

A follow-up: Though initial choice is not necessarily irreversible; contracts could be designed to be yanked \([https://ethresear.ch/t/cross-shard-contract-yanking/1450](https://ethresear.ch/t/cross-shard-contract-yanking/1450)\) from one shard to another, and I expect a lot of applications will take advantage of this feature.

**Q: Will there be a software implementation of VDF for those who are unable to obtain the ASIC?**

**Also, will participants in the RANDAO/VDF mix earn rewards in a similar fashion to validators \(if at all\)?**

A: **Will there be a software implementation of VDF for those who are unable to obtain the ASIC?**

A software implementation of the VDF would likely be useless for production. The current estimate is that a CPU implementation would be 1,000 to 10,000 times slower than the ASIC. A software implementation would be useful for testing though.

**will participants in the RANDAO/VDF mix earn rewards in a similar fashion to validators \(if at all\)?**

There will be a small incentive for validators to also be VDF evaluators. Other than that we're mostly drawing from external incentives \(e.g. as a large ETH holder you have an incentive that Ethereum stays healthy\).

The good news is that we only need one VDF evaluator to do its job. There will be thousands of VDF rigs given for free to the community. \[Justin Drake\]

**Q: Do Quantum Computers pose a permanent threat to ownerless legacy addresses with significant funds and can they cause collisions with old contracts?**

A: One of the features of Ethereum 2.0 is "abstraction", which means that users can specify whatever signature scheme they want. I expect quantum-secure signature schemes to gradually become more popular. Burn addresses can easily be made quantum-secure.

**Do Quantum Computers pose a permanent threat to ownerless legacy addresses with significant funds**

Yes, definitely a threat. Ownerless legacy address could be a systemic risk for blockchains such as Ethereum and Bitcoin. Would be interesting to guestimate how much ETH is at risk.

**Q: ERC20/721 standards' design sucks. Is there any idea or plan to convert current tokens to ERC-1155 like, efficient format? \(Code isn't Law. Seriously.\)**

A: I'm hoping that Ethereum 2.0 standards \(such as token standards\) can learn from the mistakes of Ethereum 1.0 and evolve. Starting from scratch is a unique opportunity in Ethereum's lifetime. \[Justin Drake\]

A follow-up: Agree! There's a lot from ERC20 that I dislike, the main two things being:

* It being a pull system vs a push system, requiring the whole approve/transferFrom mess to use tokens to pay for things in smart contracts
* Handling of ETH being so different from handling of tokens

Definitely would like to see both issues resolved in 2.0. The other big things I want to "get right this time" is \(i\) multisig wallets and \(ii\) not having the "ether used to pay for gas to withdraw funds from a mixer contract being a deanonymization vector" issue that makes privacy hard at the moment.

**Q: How soon will staking pools be live when Ethereum staking goes live?**

A: At the consensus layer we are trying hard to be friendly to decentralised staking pools. Hopefully we will see those soon after the launch of phase 0. The research and implementation work that Dfinity is doing regarding BLS Distributed Key Generation \(DKG\) will likely help decentralised pools.

Centralised staking pools—unlike centralised mining pools—are somewhat awkward because you have to trust the operator to behave properly with your funds. \[Justin Drake\]

**Q: If we want to bring our smart contracts to a new chain, could we pre-determine the corresponding starting/ending hex values for the old smart contracts? Kind of reminds me of CREATE2...**

A: Yes, Eth2.0 will have a CREATE2 equivalent for deploying contracts.

As for existing contracts, the entire eth1.0 state will be rolled into a contract on a shard and these existing contracts will be callable via calling into this 1.0 contract targeting the existing contract address. \[Danny Ryan\]

**Q: Are there any courses or subjects in uni that one should take to help in becoming a researcher?**

A: I'd say you need to be a good self-learner. Math, cryptography, computer science, programming, economics, networking are all relevant. \[Justin Drake\]

**Q: Of proposed ways to tackle state rent problem, which one is your favorite? What do you think about resulting complexity from user point of view?**

A: As far as base protocol goes, either option here: [https://ethresear.ch/t/a-minimal-state-execution-proposal/4445](https://ethresear.ch/t/a-minimal-state-execution-proposal/4445)

The complexity is actually not so much in the rent itself, it's in how it changes the developer experience. The general approach is that application storage will need to be more "modular" and explicitly broken down into chunks associated with specific users, possibly with a fixed amount of "global" storage, plus some short-term storage not assigned to any user that goes away after some fixed amount of time, eg. 6 months. \[Vitalik Buterin\]

**Q: Question for Justin Drake and other VDF researchers: Would using Chainlink and TEEs \(Intel SGX\) be a viable method of generating secure randomness for the VDF function of Eth 2.0? Could this be used in lieu of specialized hardware? If so, I imagine this could be a substantial time and cost saving measure in the quest for Serenity.**

A: TEEs can be used to generate randomness using delay. Unfortunately TEEs is trusted hardware. We need a trustless solution :\) \[Justin Drake\]

A follow-up: Though I would add that trusted hardware could be a great thing for individual validators to use to increase their security. \[Vitalik Buterin\]

**Q: What computer science problems still need to be solved prior to the release of Phase 1?**

A: For phase 0 we need locally-computable shuffles. For phase 1 we want a custody scheme that is friendly to decentralised pools. Please message me if that sounds like your cup of tea :\) \[Justin Drake\]

**Q: What happens to the beacon chain in the event of a controversial hardfork on the Eth 1.0 chain? Will two beacon chains form? If not, what mechanism will the beacon chain use to determine which Eth 1.0 chain is the main chain? How will this affect the transition of the Eth 1.0 chain onto a Eth 2.0 shard?**

**What safeguards are in place to ensure that malicious participants do not create unnecessary volatility between ETH & BETH during the year long transition from phase 0 to phase 2? It is my view that this trading pair must remain stable for a successful transition to take place.**

A: **If not, what mechanism will the beacon chain use to determine which Eth 1.0 chain is the main chain?**

By default the beacon chain validators will just use the voting mechanism that's specified in the spec, and whichever chain a majority of the validators support is the chain that the beacon chain will go with. That said, if we want to facilitate a peaceful split, there is a fork versioning feature built in to the beacon chain to make replay protection very easy... \[Vitalik Buterin\]

**Q: Why are you not doing "proper" research and submit publications to conferences?**

A: Not really an answer to your question, but Ethresear.ch \([https://scholar.google.co.uk/scholar?hl=en&as\_sdt=0%2C5&q="ethresear.ch"&btnG=&oq="et](https://scholar.google.co.uk/scholar?hl=en&as_sdt=0%2C5&q="ethresear.ch"&btnG=&oq="et)\) does get cited :\) \[Justin Drake\]

A follow-up: As does the Casper FFG paper! \[Vitalik Buterin\]

**Q: Let's say that I have some ethereum locked on a time locked contract, will be available after the 2.0 transition? This question can be expanded to all 1.0 contract functionality after the POS transition**

A: The Ethereum 1.0 will live on, even after Ethereum 2.0 is fully deployed. See [https://old.reddit.com/r/ethereum/comments/ajc9ip/ama\_we\_are\_the\_eth\_20\_research\_team/eeub9sp/](https://old.reddit.com/r/ethereum/comments/ajc9ip/ama_we_are_the_eth_20_research_team/eeub9sp/). \[Justin Drake\]

**Q: Thoughts on this tweet?** [https://twitter.com/zaoyang/status/1088001513459511296?s=21](https://twitter.com/zaoyang/status/1088001513459511296?s=21)

A: Eth 2.0 is not really trying to maintain backwards compatibility; almost every part of the design is significantly altered, and old contracts will have to explicitly migrate over to the new system and in some cases rewrite eg. to adapt to rent. \[Vitalik Buterin\]

**Q: What's your vision for Eth 3.0?**

A: STARKs, STARKs and lots of STARKs. Hopefully some nice way to achieve 2 second average block times. Extremely effective cross-shard communication, either at base layer or through a variety of easy-to-use layer 2 systems. \[Vitalik Buterin\]

A2: See [https://twitter.com/drakefjustin/status/1072593728253104128](https://twitter.com/drakefjustin/status/1072593728253104128) \[Justin Drake\]

**Q: In the future how will a really popular DAPP operate? Will it be possible for a single DAPP to operate across multiple shards? If not how will it operate properly with the TX/sec limits on a single shard? Will L2 solutions be the only option?**

A: A dApp would have to get really big to consume all the resources in a given shard to justify spreading itself over multiple shards. For example, Uber does less than 20 rides per second. A similarly popular decentralised equivalent would likely fit on a single shard, especially when fancy L2 infrastructure is involved \(e.g. state channels, plasma, SNARKs/STARKs\). \[Justin Drake\]

**Q: What is your take on the current state of finding consensus on randomness, in particular the current VDF construction. While certainly clever, I wouldn't say it is very elegant. Do you think this is due to theoretical constraints or do do you see potential for a 'nicer' way?**

**More general, are there any theoretical problems in this space, relevant to Ethereum 2.0 or not, that are just interesting to think about? \(starting my PhD soon and looking for inspiration if it wasn't obvious\)**

A: **I wouldn't say it is very elegant**

I'd say VDFs are a super elegant thin layer on top of RANDAO :\)

Is it the hardware you don't like? If so, would you agree that proof-of-work is an elegant solution? Then think of VDFs as being "proof-of-work 2.0": much better randomness at much lower cost. It's a paradigm shift from massively-parallel work to inherently-sequential work.

**Do you think this is due to theoretical constraints or do do you see potential for a 'nicer' way?**

I'm not aware of any unbiasable randomness schemes that only have strong liveness, other than VDFs :\)

**are there any theoretical problems in this space, relevant to Ethereum 2.0 or not, that are just interesting to think about? \(starting my PhD soon and looking for inspiration if it wasn't obvious\)**

We will have an academic "VDF day" at Stanford on Feb 3 to work on open problems. Will you be nearby? \[Justin Drake\]

**Q: Shouldn't the smart contract stated in \(4\) have the ability of sending just 16 ETH for something as RocketPool v2 work \(while some consider this to be "centralization" I think it will help a lot the average user and mitigate the risk of the average user\)?**

A: You can send between 1 ETH and 32 ETH to the Ethereum 1.0 deposit contract at any time. A minimum balance of 32 ETH on the beacon chain is required for activation as a validator. \[Justin Drake\]

**Q: I see a lot of people talking about nodes running in cloud. Shouldn't ETH find a way to actually discourage this? If everybody is running nodes in cloud that means we have possible single point of failure, which is against what I think we are trying to achieve and what enterprise customers are looking to eliminate.**

A: "Partial slashing" and the quadratic leak during times of no-finality actually financially encourage diverse validator setups. Your potential losses are much smaller when your slashable message or validator down-time are discorrelated.

Diversity in setup includes -- node software, validation software, local server vs cloud provider \(and which cloud if using cloud\), geographic region, etc.

If a ton of validators all run on AWS and AWS goes down, these validators will suffer large penalty leaks. To guard against this, I should setup my validation node locally or on a less used cloud provider. \[Danny Ryan\]

A2: We do have a way! It's called "partial slashing" and the idea is that, if something goes wrong, the more people did something wrong the more everyone gets penalised. So there is an incentive to avoid correlation with other validators, and hence avoid centralisation. \[Justin Drake\]

**Q: Can you foresee ever having to move Eth 1.0 to Eth 2.0 in order to avoid losing it forever?**

A: The current plan is to incorporate the eth1.0 state into a contract on a shard in eth2.0. Note that this will just be a state root and an EVM interpreter along with eth balances. Users will be able to call into this contract by providing merkle witnesses of the required state. \[Danny Ryan\]

**Q: I'm a new developer looking into Ethereum, where would you officially recommend I look to develop with an eye toward future proofing?**

A: A key consideration to future proof your contract code for Ethereum 2.0 is sustainable storage. It's known as "storage rent" and "storage maintenance fees". \[Justin Drake\]

**Q: What do you guys think of the Avalanche consensus mechanism and could it play a role in the ETH roadmap further into the future?**

A: Avalanche is interesting to me because it's a fresh approach. Looking forward to seeing how it plays out with Bitcoin Cash. Successes there can be ported to Ethereum via L2 infrastructure. \[Justin Drake\]

**Q: Is sharding smart contracts theoretically possible? How would one go about that?**

A: Here's a trivial example: the Ethereum Name Service \(ENS\) can be sharded across n shards according to the first log\_2\(n\) bits in the domain name hash. \[Justin Drake\]

**Q: How does eth 2.0 balance security across shards holding different amounts of notional value in them? For example if there is a decentralized finance shard holding a very high % of eth + other tokens, would the stakers/validators responsible for that shard have incentives to behave badly?**

A: The key security guarantee of sharding comes from frequently shuffling validators into randomly-sampled committees \(known as "crosslink committees"\). The hope is that this fast shuffling resists bribing attacks, in both the "honest majority" and the "slowly-adaptive rational majority" security models. \[Justin Drake\]

**Follow-up Q: It still seems like an inefficiency where you'd be over-securing shards with low notional value + under-securing shards with high notional value. Am I thinking about this wrong?**

A: Every shard gets security with the same notional value. Value \(validator collateral\) gets spread evenly across shards. \[Justin Drake\]

**Follow-up Q: Ah think we are speaking past each other a bit, let me try to clarify my concern --&gt; It seems likely you will have wildly varying ratios of \(value sitting atop a particular shard / validator collateral securing that shard\).**

**So for example a defi shard with 90% of value in eth economy sitting in it only gets 1/1024th of the validator collateral securing it.**

**And an empty or unused shard would get same 1/1024th of total validator collateral securing it.**

**This seems inefficient to me. Depending on how the distribution of value shakes out across shards, potentially materially inefficient?**

A: **This seems inefficient to me. Depending on how the distribution of value shakes out across shards, potentially materially inefficient?**

Oh I see! Interesting point. We consider every shard equal, and provide high security for all shards. The breakdown of even a single shard \(namely, an unavailable or invalid crosslink\) would likely be catastrophic for the whole system. \[Justin Drake\]

**Q: Will the Beacon Chain require its own nodes? Is this basically a brand new chain that has only one connection to ethereum: Proof of Burn?**

A: The beacon chain is a new system level chain that houses the validators and manages their responsibilities and rewards/penalties. In many ways this is akin to the FFG contract and sharding contract proposals that were previously deprecated but the organization breaks clean from the EVM to allow for a radically new design and increased efficiency.

A node in the future can run the PoW chain and/or the beacon chain. If they run the beacon chain, they can then sync whatever shard chains they want.

The connection at first is just an economic connection -- use the existing economics and community to seed validation in the beacon chain. Beyond that, we expect the beacon chain to be used to finalize the pow chain in the short to medium term.

In the end, there are a number of proposals to either fork the eth1.0 state into eth2.0. \[Danny Ryan\]

**Q: How does Eth 2.0 account for DDOS attacks? If people run nodes at home on consumer hardware with a normal internet connection they can be taken offline easily with DDOS attacks or am I interpreting this wrong?**

A: It is the responsibility of a validator to remain online to fulfill their responsibilities and gain rewards. A validator can remain profitable if they generally remain online greater than 50-67% of the time.

A validator's inactivity penalties are also minimized if their being offline is dis-correlated from other validators. This incentivizes to utilize different node and validation software from the majority so that in the case of a ddos attack vector against a particular node implementation, your offline losses are minimized.

The validator's protocol level identity and it's node's network identity are completely decoupled. This allows for a validator to create any type of obfuscated network setup that serves their purposes. I expect many tools and best practices to arise for home validators in the coming months. \[Danny Ryan\]

**Q: What are your thoughts on formal verification of smart contracts? Will this be possible with Ethereum 2.0?**

A: Formal verification of smart contracts is awesome and super valuable IMO. Formal verification will be possible in eth2.0. I believe the WASM semantics are already available in K which will provide some good opportunities for contract verification. Opening up more languages by using WASM will also allow for utilization of more restricted languages that are more amenable to FV. \[Danny Ryan\]

**Q: What are some good cypherpunk books that you would recommend to people getting interested in this space? \(Or just good book recommendations in general\)**

A: I don't read many books nowadays. I mostly consume academic papers, whitepapers, podcasts, videos, blog posts, Reddit, Twitter, etc. I did enjoy "Zero to One" by Peter Thiel when I was an entrepreneur. \[Justin Drake\]

\*\*Q: How do you prevent single shard corruption attacks? Basically will there be resharding? If so, how is resharding done?

**How are you solving the fast state syncing problem if nodes need to be reshuffled around shards?**

A: **How do you prevent single shard corruption attacks?**

By randomly shuffling validators across shards.

**Basically will there be resharding? If so, how is resharding done?**

Right now crosslink committees are shuffled every epoch \(6.4 minutes\) and shard proposer committees are shuffled every ~9 days. Crosslink committees are critical, hence why there are shuffled fast. See this answer also. \[Justin Drake\]

**Q: You said in a comment some days ago that there are basically no unsolved problems of Serenity Phase 0 left. Which problems of Phase 1 and 2 are still left to be solved?**

A: The short answer is there are no big fundamental problems for phases 0, 1, 2. The more detailed answer is that for phase 0 we need locally-computable shuffles. For phase 1 we want a custody scheme that is friendly to decentralised pools. For phase 2 we need to figure out sustainable storage. \[Justin Drake\]

**Q: Before Eth 2.0 Enhancements come in, what is the best recommended approach for storing private data on Ehereum?**

A: Storing data on Ethereum is expensive per byte. Infrastructure like Filecoin may prove to be a good trustless storage solution. For privacy, just encrypt the data. \[Justin Drake\]

**Q: Will there be any zk-snarks related enhancements coming with Eth 2.0?**

A: We are hoping to have a SNARK- and STARK-friendly hash function in Ethereum 2.0 at some point. Unfortunately those likely won't be ready for phase 0.

At the application layer, WASM will ideally mean that SNARK-specific precompiles won't be necessary. \[Justin Drake\]

**Q: Is there some kind of roadmap for the migration from ETH 1.0 to ETH 2.0 in layman's terms? For true decentralization it is required to get more people on board that understand the full process.**

A: I described the three phases here [https://www.reddit.com/r/ethereum/comments/ajc9ip/ama\_we\_are\_the\_eth\_20\_research\_team/eeueuzc](https://www.reddit.com/r/ethereum/comments/ajc9ip/ama_we_are_the_eth_20_research_team/eeueuzc)

EthHub also does a great job at simply describing the path

[https://docs.ethhub.io/ethereum-roadmap/serenity-phases](https://docs.ethhub.io/ethereum-roadmap/serenity-phases) \[Danny Ryan\]

**Q: ETH token will not be transferable back after migration to ETH2.0 What will be the token ticker for the ETH2.0 chain native token?**

A: ETH—at least when Ethereum 2.0 is fully deployed. Fungibility is a key design goal. \[Justin Drake\]

**Q: Where does new client software take lists of peers with their ip addresses and ports? Is there is centralized server?**

A: This is an implementation detail. Some clients may have a hardcoded list of "bootstrap node" IPs and ports. \[Justin Drake\]

\*\*Q: Do you have any final plans in mind about the current ETH inflation?

A: Nothing final. Ultimately the community will have to make a tradeoff between low inflation and high security. See [https://github.com/ethereum/eth2.0-specs/issues/251](https://github.com/ethereum/eth2.0-specs/issues/251). \[Justin Drake\]

**Q: What are the odds that a fully sharded chain including state transitions is feasible?**

A: Very high. No fundamental problems unsolved. The tricky part is getting everything to fit together cleanly. \[Danny Ryan\]

**Q: Can I use a raspberry Pi to stake when staking is possible? And what do I do with it in the mean time?**

A: Nimbus \([https://github.com/status-im/nimbus](https://github.com/status-im/nimbus)\) is targeting resource-constrained validators :\) \[Justin Drake\]

**Q: What's your opinion of EOS \(or TRON, STEEM\) in terms of dapp platform?**

A: I tend to be critical of that class of systems. See [https://vitalik.ca/general/2017/12/17/voting.html](https://vitalik.ca/general/2017/12/17/voting.html) and [https://vitalik.ca/general/2018/03/28/plutocracy.html](https://vitalik.ca/general/2018/03/28/plutocracy.html) for reasons why. \[Vitalik Buterin\]

**Q: Any updates as far as overall inflation rate per year or per milestone/HF? Any updates as far as TPS per year or per milestone/HF?**

A: See [https://github.com/ethereum/eth2.0-specs/issues/251](https://github.com/ethereum/eth2.0-specs/issues/251) \[Justin Drake\]

**Q: Can I make a Zcash coin on ETH 2.0 for example with all or most of the advantages of Zcash?**

A: Yes, there are already a number of experiments in eth1.0 to demonstrate usage of ZKSNARKs for both privacy and scalability. Check out [miximus](https://github.com/barryWhiteHat/miximus) for privacy and [roll up](https://github.com/barryWhiteHat/roll_up) for scalability \(both by barry whitehat!\).

Usage of ZKSNARKs will be supported in eWASM state execution so I expect more privacy solutions akin to Zcash to continue to be built on eth2.0. \[Danny Ryan\]

**Q: Why is ETH 2.0 Phase 0 even needed as a "main" chain, and need Bether transform from real ether \(hence risk losing some value\), instead of doing a testnet only, because after all this is what phase 0 is, based on TestnetBEther?**

A: ETH 2.0 needs a main chain as a single point of truth for all the shards. The reason we have phases 0, 1, 2 is to break things down conceptually, and in terms of incremental releases to limit risk. \[Justin Drake\]

**Q: What work is being done to make the research behind ETH 2.0 more geographically decentralized? Are there any efforts to translate research specifications into other languages?**

A: **Are there any efforts to translate research specifications into other languages?**

Once the spec is more mature I expect the community to pick this up, somewhat similar to how Andreas's books get translated. English seems to be the a lingua franca for research and development. \[Justin Drake\]

**Q: After PoS, if a node gets hacked, can the hacker make the node to lose its stake by confirming false transactions?**

A: When your validator gets penalised it is automatically deregistered to prevent further damage. We have a mechanism called "partial slashing". The idea is that, if something goes wrong with your validator it only gets penalised a bit if not many other validators also mess up around that time.

So in the optimistic case of a lone hack you should recover most of your funds with your withdrawal key \(kept secure, e.g. in cold storage\). \[Justin Drake\]

**Q: Will contracts be able to pay for gas in Eth 2.0?**

A: That will likely be unlocked with abstraction \(which includes gas abstraction\). \[Justin Drake\]

**Q: Assuming the number of network nodes remains the same and the network graduates to full PoS... what is your expected maximum theoretical transaction throughout?**

A: Rough ballpark figures. 1024 shards \* 10 transactions per second per shard ~= 10k transactions per second. \[Justin Drake\]

**Q: What is the most updated timeline for rolling out PoS? Since Vitalik already said 'research is done', what are developers' incentives to push things forward? Are there any specific measures taken to ensure a smooth transition?**

A: I expect the beacon chain (the core PoS chain) to launch late 2019. Ideally the spec should be close to final in Q1, cross-client testnets in Q2, security audits in Q3, mainnet launch in Q4.

As a rule of thumb, launching in December is hard because of the holiday season. So November 2019 and January 2020 would be my two best guesses.

Having the Ethereum 2.0 chain finalise the Ethereum 1.0 chain will take more time. [Justin Drake]

**Q: Will it be possible with sharding to have shards with different rules and/or technology independent from the other shards/beacon chain, but still using the same base tech in terms of transacting and security? For example: private eth network run in a shard connected to main eth network from which it takes just security from validators. Private transaction with ZKsnarks shard(s). Encrypted data shards. Erc20 like coin launched on ETH 2.0, but with it's own rules and maybe own shards somehow controlled by the smart contract of that erc20.**

A: Every shard has the same data availability layer, and the option to use EVM2.0 as an execution engine. That's common base-layer infrastructure. At the application layer contracts can be powered by non-EVM2.0 execution engines (so-called alternative execution engines).

There's also a huge L2 design around state channels, plasma, cross-shard communication, etc. So at the application layer I expect lots of non-homogeneity across shards, as well as a lots of homogeneity thanks to standardisation. [Justin Drake]

**Q: Today, running full nodes isn’t that hard, but the resource requirements are slowly increasing. How much thinking is being devoted to the greater infrastructure requirements of Eth 2.0 and how they will impact node participation and decentralization?**

A: Ethereum 2.0 validation should be sustainable from a resource perspective:

* Bandwidth: fixed cost (thanks for fixes shard block sizes)
* Storage: if not fixed then sustainable (thanks to ideas such as storage maintenance fees). Note that storing shard blocks since genesis is not required.
* CPU, memory I/O: similar situation to Ethereum 1.0 (gas limit that can be voted up or down). [Justin Drake]

**Q: How ETH 2.0 differs from ETH, and why POS instead of POW.**

A: PoS enables goodies such as economic finality and sharding. It is also much cheaper (in terms of inflation cost for hodlers, as well as ecologically) than PoW. [Justin Drake]

## Part 2

**Q: What do you feel is the biggest unsolved challenge left in Eth 2.0 research which must be addressed before Phase 1 or Phase 2 could be implemented in the future?**

A: I really honestly think that there are no unsolved research challenges at this point. It's mostly "how do we make this thing more elegant and take up fewer lines of code and have fewer edge cases" on the research side. [Vitalik]

Better understanding the incentives and various actors that might arise in a stateless and highly abstracted execution model. There is really great work being led by both the EF eWASM team and the Consensys Quilt team to better understand the design space and active build prototypes to vet ideas. [Danny]

**Q: Previously, a release date of January 2020 for Phase 0 was informally articulated. Do you feel this date is realistic and achievable?**

A: Thanks for noting its informality. :) Launching early next year is my personal target, but there is a lot that needs to be done before then! We need: long-running test nets (however that is defined), formal verification of the deposit contract, and clients to be ready for prime time, but right now it looks like everything will come together in time. We also don't want to rush clients into developing buggy software just to be ready by an arbitrary date. 

If anything, I think BLS standardisation efforts are the most likely to slow us down. We (as a greater blockchain community) are trying very hard to have a standardised signature scheme for better interoperability between all the chains. There is a high degree of consensus on this already, but establishing a new standard is always a slow process. [Carl]

The client teams are doing a great job and continuing to push the envelope. I expect exciting progress to be made in the coming months, but I also expect that the last mile might be long.


Early 2020 is realistic and still the target [Danny]

**Q: Are the researchers happy with the current state of the economics of Ethereum 2.0?**

A: I don't think it's productive for us to worry about the absolute numbers at this point; the network will launch, and either the rewards will prove sufficient or they won't. The other thing worth worrying about is centralization incentives, but that's difficult to work out "in theory land"; much of the result in practice has to do with how lazy people are. [Vitalik]

**Q: My biggest worry about ETH 2.0 is that it will kill composability. Won't most dapps end up trying to build on the same shard as say MakerDAO so they can use Dai?**

A: Composability between shards is definitely unchartered territory but there are reasons to be optimistic:

The shards are designed for homogeneity (unlike, say, Polkadot or Cosmos) to facilitate cross-shard communication.

There are design patterns which abstract away the boundaries between shards. For example, one could consider shards 0 and 1 as a combined data availability substrate for an execution engine which requires more bandwidth. These design patterns will be more easily exploitable in the context of programmable execution engines.

The shards are designed to be friendly to "fast optimistic finality" thanks to shard attestations which are somewhat analogous to block confirmations in the context of Eth1. What this means that is, in practice, the shards may act as one logical blockchain thanks to quick probabilistic finality of individual shards.

The UI layer is also an opportunity to abstract away the boundary between shards. [Justin]

**Q: When can we expect the Beacon Chain to be finalizing/checkpointing the Eth1.x chain?**

A: My best guess is early 2021. See [here](https://www.reddit.com/r/ethtrader/comments/c872b7/ethereum_20_well_on_its_way_serenity_phase_zero/esnnvey/). [Justin]

**Q: Under the specs there is a " block.eth1_data " property; based on that I thought that somehow we were going to have an hybrid validation starting Jan 2020 (if all goes well) from both PoW and PoS. As stakers, what are we going to validate except the validators, staking rewards & penalties if all the traffic will still be on eth 1.0 and we're not taking part?**

A: In order for Eth2 to finalise Eth1, 2 things are needed, Eth2 must vote on Eth1 (as is implemented as you point out) and Eth1 must change its fork rule to follow the finalised blocks on Eth1. The latter requirement requires an Eth1 hardfork. It is therefore easier to just have validator finalise the things you mention for now and later on add in Eth1 finalisation.

Additionally, it is safer to launch without Eth1 finalisation in case of a Eth2 black-swan event in the early days. [Carl]

**Q: Rebuttals to the criticism that Eth 2.0 is extremely complex?**

A: It got considerably simpler over the last year. If you do a word count on the spec, it seems to be considerably smaller than the yellow paper at this point. There's a lot of things in eth2 that are much simpler than eth1. But there's definitely lingering complexity and I deeply care about minimizing it. [Vitalik]

While the research path has been somewhat tortuous and hard to follow, the end product is arguably simple and clean. Expect more educational material highlighting the simplicity of the current design. Phase 0 is about 1024 lines of code to specify (assuming SHA256 and BLS12-381 as primitives). I expect phases 1 and 2 to be 1024 lines of code combined (assuming WASM as primitive). [Justin]

**Q: Why are there so many teams building eth2.0 clients? I understand the point of client diversity but don't you think 6 clients seem to be pushing it? Supporting so many clients would also divide the resources in terms of funding. Which clients do you see as the geth and parity of eth2.0?**

A: A few notes on client diversity:

* There's more than 6 clients being developed—it's closer to 8.

* I expect consolidation—a bunch of clients may not survive 2020.

* I expect specialisation—one can focus on the browser (e.g. Lodestar), resource-constrained devices (e.g. Nimbus), the enterprise (e.g. Artemis), prototyping (e.g. Trinity), etc.

* A minimum of two production-ready clients are necessary for launch. I expect the first-mover advantage to be strong.

* All the above have, to an extent, historically happened on Eth1. [Carl]

We definitely don't want a duopoly! For me personally, the ideal would be to have no single client exceed 1/3 of the network, so any software bug in any single client would not stop the network. Though having no single client exceed 1/2 is ok too and gets us most of the same benefit (if a major client has a bug, having no finality for a while while things are being figured out may even be an improvement...)

I expect a power law distribution, and it's definitely likely that some of the clients will not survive to see significant usage on mainnet. [Vitalik]

My guess on why so many clients showed up to do the hard work is that eth2.0 is both exciting as a purely technical challenge as well as a chance to make a mark on Ethereum and the crypto space in general.


I'm pleased that there are so many great teams doing the hard work, but recently, I've been more focused on finding contributors to do value-add work outside of the core client implementation. Formal verification, academic analysis of protocols, testing, light clients, web3 interfaces and developer tooling, validator clients with great UX that plug into any underlying node, etc [Danny]

**Q: Are the Ethereum 2.0 clients eventually going to replace the 1.0 counterparts? For example, will Prism ever get merged to Geth?**

A: I expect the Eth1 clients to live a long and prosperous life :)

On Prism: "Likely not. Other than the language (Go), Prysm and Geth have very little in common." [Justin]

**Q: what happens when I stake 32 eth, and get slashed once? now that my stake is below 32 eth do i get kicked out of the validator set?**

A: Validators get kicked out when they get slashed. There is another ejection mechanism if your balance goes below 16 ETH from accumulating (non-slashing) penalties. [Justin]

You also lose some amount of ETH. The minimum being set to 1 ETH currently.

There is an additional penalty related to the number of other slashable offenses that have occurred in the recent time period. If more validators have been slashed recently, you lose more ETH. The maximum penalty occurs if ~1/3 of validators have been slashed recently, at which point you lose all ETH.

This highlights the importance of having a discorrelated validator setup from other nodes and potentially having some fault tolerance setup with yourself before you sign things. [Danny]

**Q: What are the non-slashing offences?**

A: There are micro-penalties for not voting to finalise the same blocks as other validators and the inactivity penalty (for offline validators) for when the chain is not finalising for an extended period of time. [Carl]

We have a bunch of micro-penalties for not optimally crafting attestations and penalties for being offline (search for get_attestation_deltasand get_crosslink_deltas [here](https://github.com/ethereum/eth2.0-specs/blob/dev/specs/core/0_beacon-chain.md)). [Justin]

**Q: i hear a lot of hype around staking rewards, but what are the penalties for getting slashed? does the network have different punishments for different misbehavior (offline vs. double-signing)? is the "up to 60.8% slash in 18 days" still correct?**

A: I think you are conflating two thigs here, slashing and the inactivity leak.

**Inactivity leak**

If your validator node goes offline for 18 days, and the beacon chain is not finalizing, then your balance will be reduced by "up to 60.8% slash in 18 days".

**Slashing**

If a validator behaves provably maliciously, then they are slashed by having their balance reduced. Assuming client software is written well, this should be basically impossible to happen to you. Minimum penalty is 1 ETH, but it goes up linearly in the number of people slashed at the same time as you.

See [here](https://notes.ethereum.org/9l707paQQEeI-GPzVK02lA#Why-are-the-Casper-incentives-set-the-way-they-are) for more [Carl]

Important to note that if you are offline, but the chain is still finalizing you only stand to lose approximately the same as you would have gained. The quick reduction in balance over a ~2 week period only occurs when not finalizing.

Another reason to have a discorrelated setup from the rest of the network! [Danny]

**Q:What is currently the most exciting new research development in Ethereum 2.0?**

A: The execution engine abstraction in phase 2 is quite exciting, taking account abstraction to the next level. It allows for the consensus part of execution to be an ultra thin layer of abstraction on top of data availability. Assuming WASM as a black box, it may be on the order of 256 lines of code to specify. 

There's an initial proposal from Vitalik [here](https://notes.ethereum.org/s/Bkoaj4xpN). The idea is that even the notion of a "transaction" is an application-layer detail which can be specified as WASM code. Compare this to Eth1 which "enshrines" an opinionated notion of replay protection (nonces), signatures (ECDSA), contracts, accounts (vs UTXOs), gas, storage, etc. [Justin]

I'm lately most excited about [this](https://ethresear.ch/t/layer-2-state-schemes/5691). The OVM work by Karl Floersch and co is along similar lines and also very interesting. [Vitalik]

**Q: Theres been some debate over the necessity of ASICs in Eth 2.0. I understand theres an effort to spread the cost out among various communities, but I think many people feel this might just end up being an expensive science project where the rewards dont justify the costs and if you itemised Eth 2.0, it seems like it might be the most expensive part. Are there alternatives besides relying on just Randao/Randao + ASICs (VDF)? What are the ELI5 upsides + downsides of the alternatives? I appreciate that the researchers are a tackling a difficult problem with randomness for a blockchain.**

A: It's important to stress that the VDF mechanism's safety is not critical to the safety of the Eth2 consensus; if the VDF scheme gets broken or someone makes an ASIC fast enough to predict all the outputs, all that happens is that the percentage of validators they need to corrupt a single committee drops by a few percentage points (think, from ~50% to ~33-40% plus a lot of computing power). I actually think the main value of the VDF is that it provides global trustable secure randomness to applications that need it. [Vitalik]

+1 on consensus-layer security and/or performance gains, and value-add at the application-layer. The other "promise" of VDFs is that they are a new cryptographic building block with the rather unique notion of time. They can used for proofs of space, proofs of replication, proofs of history, anti-frontrunning, expiring zk-proofs, and hopefully further applications which are hard to predict today. [Justin]

**Q: I'd like to know more about the data availability layer of Ethereum 2.0 - particularly the economic costs of long-term data storage. Part of my political platform includes integrating blockchain technology with government operations. For example, I'd like to see all of America's public records stored on a public, open source, sufficiently decentralized blockchain. Would it make sense to build something like this on top of Ethereum 2.0? Why or why not?**

A: Realistically you would want an incentivized data storage platform like Swarm, with hashes of the documents stored on the ethereum blockchain.

But I'd recommend thinking harder and trying to figure out how to answer the deeper question "how could we use blockchains as a tool to minimize opportunities for misbehavior in government?" Places to start I can think of include:

* Things like https://opencerts.io/ for all government-issued records

* Using https://ethresear.ch/t/minimal-anti-collusion-infrastructure/5413/ to do online votes, starting in low-security contexts (I think petitions would be a good place to start and underexplored)

* An internal-use stablecoin where only government agencies can hold balances but transactions are visible to and auditable by the public

* Some kind of zero-knowledge privacy-preserving sales tax collection thing

* Blockchain-based solutions for esoteric government things like spectrum auctions

* Get your country (I'm speaking generically to all readers here :D) to make an Estonian-style E-ID system that lets people make digital signatures that can be verified by anyone publicly. This is not technically a blockchain application, but it would be a tool useful in many blockchain applications [Vitalik]

**Q: I recall /u/bobthesponge once saying that almost his entire Net worth is in Ether (even his salary from the EF). Are there any other researchers on the research team that are as convinced of Ethereum's future, besides Vitalik and Justin of course? No need to call someone out. Just percentages, ie. "Over 50% of the research team is heavily (over 30% of net worth) invested in Ether financially", would be sufficient.**

A: Somewhat ingrained in our culture, the research team doesn't talk much about net worths. Having said that, the research team has a lot of fresh blood (e.g. Dankrad, Proto, Carl) which I don't expect to be crazy invested in ETH.[Justin]

I am not an eth whale, but I get paid in eth and have high exposure. [Danny]

The aforementioned Carl here, let's put it this way: financially, emotionally, and intellectually, I am heavily exposed to ETH. [Carl]

**Q: How many Eth2.0 client teams have to have a finished client for the Beacon chain to go live?**

A: I asked the same question a few days ago. At this moment, it is still an open question and will likely be until much loser to the time. Obviously having more clients is better, but that should be played off against the launch date. I am currently torn between 2 and 3. (Having > 2 would be great because otherwise there is a client guaranteed to have a majority of the validator-base.) At the end of the day, it will come down to who is ready and when. [Carl]

Two at minimum, ideally three. [Justin]

**Q: I understand that about 10 million eth is expected to provide good enough security for the network. In a hypothetical scenario, what happens in the situation where a large organization manage to secure more than 50% of the total eth staked and use it to maliciously attack the network? As i understand, the side with less total eth staked will be slashed, so won't this malicious actor be able to effectively kill the network?**

A: If a large actor were to aquire a large enough stake to take over the network they would need to buy >2/3 of the total staking supply which would drive the price up, so it's not a cheap attack in the first place. Secondly, you are not slashed if you vote for a minority chain, only if you behave provably maliciously in the eyes of 2/3 of the validators.

One of the beautiful things about PoS is that these attacks can be handled with grace. We, as a community, can go in and hard-fork out the malicious actors so they have no more voting power. The malicious actors just burnt a lot of money to temporally halt a network. In PoW, by contrast, if someone buys ASICS with 51% hash power, there is no way to remove them from the system. [Carl]

**Q:Do the client teams feel their implementations will be sufficiently robust enough, stable enough, and easy enough to use that normal nerds (like myself) can safely run their node software, stake 32 ETH on it, and not be slashed or lose ETH due to client bugs? My biggest concern is losing ETH while being a well intentioned actor. I've ran Geth, Parity, Trinity, and EthereumJ (Harmony) nodes for multiple years now and those clients have been around a lot longer than any of the ETH 2.0 clients have, but they still have issues, still have bugs, still sometimes crash.**

A: I hope so!

One key component in the incentive design is that penalties (for going offline and for being slashed) are only high if many other validators go offline at the same time. So any bug that doesn't hit every node at the same time should only cost you a minimal amount. [Vitalik]

**Q:suppose ethereum reaches 1 mllion tps, ledger size will grow 1 terabyte everyday, any solution to this? what is your projections in terms of ledger size growh and what is your solution to this**

A: The sharded eth2.0 is expected to handle ~10MB/s of data availability. This is data that is come to consensus upon in shard chains and guaranteed to be available in at least the ~2 week time frame.

This is not necessarily state size. The current approach to state and state execution is to take a "state-less" approach in which blocks must contain the merkle witnesses of the relevant state to perform the tx executions. This is reduces the amount of state any consensus node must store, but does bring up other issues about state size, who stores it, how users get it, etc. In fact, the entirety of state execution is being abstracted away such that we can experiment with multiple schemes to deal with this problem (state rent, users/dapps storing their own data, etc). Much of the state rent research that @ledgerwatch has driven in the past year or so will likely come into play. [Danny]

**Q: Lets assume you are a guy with very little cryptotech-knowledge, but you do have >32 ETHER.**

**Question #1: Would staking be made easy-to-do, so "ordinary" people can earn interest on their holdings?**

**Question #2: Does staking pose any risks of losing ETH by accident? Trying to understand if you can stake without any risks unless you "intentionally" try to harm the network (eg. if your validator node goes offline, because your internet provider has an issue and likewise)**

A: 
>Would staking be made easy-to-do, så "ordinary" people can earn interest on their holdings?

I expect a cottage industry will be setup around accessibility. Infrastructure to be built includes staking pools (centralised—think Coinbase—as well as decentralised one) as well as plug-and-play "validator in a box" solutions.

>Trying to understand if you can stake without any risks unless you "intentionally" try to harm the network

That's definitely the goal.

>eg. if your validator node goes offline, because your internet provider has an issue and likewise

Penalties should be marginal for validator nodes that go offline for short periods of time every once in a while. [Justin]

**Q: What is the current thinking around the Eth1>Eth2 migration plan?**

A: The current approach is to fold eth1 into eth2 as an execution environment. In practice, this will mean that we would need to have a hard fork on the eth1 side to rebalance some gas costs (opcodes that read storage or read accounts would see their gas costs increased to 2000-10000), and after that at some point there will be a "flag block height" from which the eth1 state root will be moved into the eth2 system (or possibly some one-time processing will be run on the eth1 state to make some optimizations, eg. replacing the patricia hex trie with a binary tree) and after that eth1 will be part of eth2, with applications being able to run as before.

I do think the likely gas cost increase of storage/account reading opcodes (basically the same opcodes whose gas costs were already increased in Tangerine Whistle; those costs will need to go up at least another order of magnitude) is something that contract devs should be aware and plan for. The reason that change will be necessary is that those opcodes greatly increase the size of a Merkle proof needed to statelessly verify a block, so currently Merkle proofs for a worst-case block are >100 MB; with those gas repricings plus trie optimization plus charging per byte of any contract being read, we could get it down to acceptable levels. [Vitalik]

**Q: Regarding Proof-of-Stake and wealth distribution (and issuance reduction), by the looks of it the majority of ETH will be held by the minority of entities, does that cause any concern since a single entity can run multiple validator nodes (and earn more rewards)?**

**It's a question from inequality perspective not security; if ETH were to take a significant role in the global economy, wouldn't this widen the gap between rich and poor by orders of magnitude (MUCH worse than the current economic system)? Basically, economic inequality on steroids.**

A: I definitely think income inequality issues from crypto are an issue! It's a big part of why I am not a single-cryptocurrency maximalist. But I still think that PoW is not better than PoS from an inequality point of view, because although PoW does distribute coins into "fresh hands", you need so much capital to become a PoW miner that PoW itself is a big rich-get-richer mechanic in practice. [Vitalik]

**Q: I know its still early but are there some rough estimates of when we might see Spec freezes for Phase 1 and 2?**

A: Phase 2 is a bit too far out to say, but my hope for phase 1 is Q3/4 of this year. [Carl]

That said, the current minimal execution design with EEs for phase 2 (once better researched and prototyped) is a super simple addition on top of phase 1 [Danny]

**Q: Please ELI5 ("explain like I'm five") why the need for a second chain instead keeping on evolving the first one?**

A: Building Eth2 on Eth1 would be a bad design decision for a few reasons:

* We would be constrained by the Eth1 gas limit, which would severely affect performance (e.g. 1024 shards and 32 ETH to validate would not be possible).

* We would be mixing the consensus and application layers. This means the consensus layer is subject to the application-layer DoS vectors (e.g. high gas prices). It would also mean "enshrining" application-layer contracts, which is far from ideal from a governance standpoint which should be as neutral as possible with regards to deployed contracts (i.e. The DAO interventions should be the exception, not the norm).

* We would be constrained by the EVM, which is notoriously hard to safely program complex contracts in.

* Eth1 does not have support for BLS12-381.

* We would be subject to the Eth1 block time Poisson distribution (as opposed to the regular—and shorter—slots durations in Eth2).

The list goes on :) [Justin]

**Q: I am considering to stake during phase 0, but i am a bit concerned about the inactivity leak. I want to know how to stop/pause being a validator if I change my mind? I am asking this as there may be certain situations in which I think I will be offline for a while, and I do not want my balance to slowly leak out due to that.**

A: You will only suffer large penalties if you are offline at the same time that >1/3 of other validators are offline. Otherwise the penalties for being offline will be tiny, to the point where you will be net-profitable (not including computer costs etc) as long as you are online more than ~50-67% of the time. The incentives are deliberately designed to be forgiving to avoid discouraging amateur setups to promote decentralization. [Vitalik]

The closest to a "pause" button is to first exit (which can take as little as half an hour, but may take days/weeks since there's a queuing mechanism) and later re-activate. [Justin]

**Q: 1024 shards, 131,000+ validator slots... what happens if there aren't enough validator slots filled by the time sharding goes live?**

A: With 1024 shards, and 128 validators in a committee, a minimum of 131,072 validators are needed to crosslink every shard every slot. If there are fewer validators than this, then shards are skipped to ensure the 128/committee validator number. [Carl]

The system can naturally handle as low as ~64 validators. In this case, security is obviously insanely degraded, but the protocol can technically move forward. [Danny]

Technically the system can "move forward" with one validator :D

But yes, below the 131,072 validator (4.1M ETH) level the properties of the system progressively degrade as the number of validators goes lower and lower. [Vitalik]

**Q: if i understand finalization correctly, the more validators you have the longer it takes to finalize. how is eth2 addressing this issue without pounding the network with tons of messages being sent between all the validators?**

A: Correct. I wrote an article about this fundamental tradeoff here: https://medium.com/@VitalikButerin/parametrizing-casper-the-decentralization-finality-time-overhead-tradeoff-3f2011672735

We managed to get a couple orders of magnitude more favorable tradeoff curve than other projects through BLS signature aggregation, which reduces the marginal cost of a signature to 1 bit of data and 1 ECADD (~0.001 traditional signature verifications) of computation. [Vitalik]

In Eth2, more validators should not lead to (significantly) longer finalization times. By making use of BLS signature aggregation and by grouping the validators into committees, we're able to support hundreds of thousands (and hopefully into the millions) of validators. [Carl]

**Q: Has the EF given any thought to maybe issuing "official" NFTs (i.e. collectibles) to initial stakers upon the launch of Beacon Chain as an "extra incentive"? What's your opinion on this?**

I'd say this would be the remit of the community, not the EF. Note that the Eth2 designers avoided giving early validators a special reward (e.g. giving the first 16,384 validators a 1 ETH bounty) to avoid distorting the economic experiment. We want to learn whether or not the basic incentivises are sufficient to incentivise participation. [Justin]

I actually like the idea of an NFT. The deposit contract is readable in such a way that proofs can be made to a separate contract to generate NFTs. Been talking to Austin Griffith about this. He/burner-wallet might take the charge. I don't think an NFT would hinder our ability to understand the pure incentivizes here. It's at best a trophy and of little economic value imo. [Danny]

**Q: How is the work on evaluating the feasibility of producing dedicated VDF hardware coming along?**

A: At this point there's reasonably high confidence that VDFs (including building hardware) are viable. A few updates:

* A team of 3 ex-Intel people (Simon, Sean, Kelly from Supranational) is dedicated to the hardware aspects.

* The Rivest timelock challenge (open for 20 years, designed to last 35 years) was cracked in a few months using an FPGA (see here, and here). There's also code on Github.

* Work by Erdinc Ozturk has improved the state-of-the-art circuit depth for the modular exponentiation in VDFs. The ePrint paper was submitted a few days ago and should be published soon.

* A prominent complexity theorist (Ryan Williams from MIT) is working on circuit depth lower bounds for modular multiplication.

* Significant progress was made by Ligero on the RSA ceremony. We are planning for a ceremony with unprecedented scale (1024 participants) in 2020.

* New research papers keep flowing in—see http://vdfresearch.org

* The $100K FPGA competition is starting in a few weeks. We have relevant corporate sponsors for the FPGA and ASIC competitions.

* In addition to the Ethereum Foundation and Protocol Labs (i.e. Filecoin), a new blockchain project (to be announced with the FPGA competition) is helping with funding. $900K was raised in the latest round of funding. [Justin]

**Q: Is there a chance for obligatory anonymity of future validator withdrawals? Force every withdrawal to go to a shielded pool - like zcash does with mining rewards. I fear without the obligatory anonymity here just using a mixer/etc is going to be treated as extremely suspicious - forcing stakers would add plausible deniability.**

A: I definitely support moving toward more and more privacy being a default over time! I'd say validator _deposits_ are more important to mix than withdrawals, as that way it becomes harder to locate the nodes of specific validators which seems like it would increase security and censorship resistance. [Vitalik]

**Q: What are the main incentives to run a beacon node for validators if they can just connect to high-up time beacon nodes?If there are beacon node providers with high up-time - how is this going to be decentralized?**

A: There is an anti-centralisation incentive mechanism baked in. Basically, validators get punished for going offline the more other validators are offline at the same time. So "uncorrelated downtime" should be optimised in addition to "high uptime". [Justin]

**Q: If, as a validator, I know that I'm going to be offline for a period of time, is is possible to 'pause' validating without suffering an inactivity leak?**

A: The closest to a "pause" button is to first exit (which can take as little as half an hour, but may take days/weeks since there's a queuing mechanism) and later re-activate. [Justin]

Clarification: there's a minimum ~1 day period before you can withdraw after you exit. It's safe to be offline during that time, but it does prevent you from re-entering.

If we want to, in some future version we could add a "re-enter" feature that allows immediate re-depositing without waiting to withdraw first.... there's no theoretical reason why such a thing would not be possible. [Vitalik]

**Q: Do we have clarity yet on whether currently locked-down smart contracts (eg metronomes 4 contracts by Jeff garzik) will continue to work seamless in ETH2.0 or whether these contracts will be deprecated with all ETH in them lost? And how can storage costs be added to locked-down contracts in ETH 1.x ? In other words can we all assume immutable contracts on ETH1.0 will continue to work forever (provided enough people want them to)? Thx**

A: The current plan is that eth1 will be folded into eth2 as an execution environment via the stateless client approach, in which case, yes, contracts will keep working as expected. [Vitalik]

**Q: According to this paper, it may be possible for Quantum Computers to hijack and re-sign transactions DURING BLOCKTIME by (as early as) 2027. In other words, ownership of ANY wallet that has not upgraded to a quantum secure signature scheme BEFORE THEN can no longer be trusted AT ALL (even WITHOUT previous outgoing transactions). SO THE QUESTION IS THIS: Is anyone who fails to manually upgrade their wallets before a deadline (in order to become quantum secure) guaranteed to lose their funds after the advent of Quantum Computers? For example, if someone stores a PAPER WALLET for let's say 20 years, are they going to lose their funds by that time? Can QCs just monitor the entire blockchain and automatically attempt to hijack any transaction with insecure signature scheme during one blocktime, even if the sender has no previous outgoing transactions?**

A: Even if a quantum computer gets announced as immediately usable tomorrow, it is possible to do an emergency procedure to secure the funds of everyone who has not yet publicly released their public key or a signature (ie. every standard account holder that has not signed a transaction). You do this by doing a soft fork to disallow standard transactions, and replace them with a special transaction type that uses a STARK to prove that you own the private key k such that the given address A equals to `hash(G * k)[12:]`, and then moves the funds over into a new address type that uses a quantum-secure signature scheme, eg. Winternitz signatures.

If we get more warning, then we can get people to update to Winternitz on an orderly schedule.

TLDR: we're fine. [Vitalik]

**Q: how do/will the performance bottlenecks compare between 1.x and 2.0**

A: 2.0 removes the disk I/O bottleneck for consensus participants by heavily leaning towards stateless clients. Finality greatly mitigates the sync latency bottleneck, and the requirement for consensus participants to store historical blocks. [Justin]

I'd also add that I expect light clients to be massively more viable in eth2 than in eth1. About the same order of magnitude load as a bitcoin light client to stay synced (as opposed to eth1, where light clients are not light enough in practice to run on phones...) [Vitalik]

**Q: As an ETH miner, my main concern is how to prep for ETH 2.0. Any wiki, tips, or advice on how to proceed contributing (and profiting) for Ethereum?**

A: Eth2 has no mining. You may be able to put those GPUs to good use at the application layer with protocols like Golem, or maybe protocols that incentivise GPU-accelerated SNARK proofs. [Justin]

**Q: Approximately when is ETH issuance supposed to drop dramatically? (I believe the figure I've come accross is 10x reduction in issuance, is this correct also?)**

A: When the PoW chain starts piggybacking on the PoS chain for security (this could happen during phase 1 or phase 2), it becomes safe to lower the PoW chain reward by maybe ~4x. Further reductions would happen when the PoW chain stops entirely. [Vitalik]

**Q: During Phase 0, will ETH 2.0 be transferrable between wallets? 2.0 to 2.0? If so, are there concerns exchanges will list ETH 2.0?**

A: Transfers will probably only go live in Phase 1 at which point exchanges will list ETH2.0. Having exchanges to so will help maintain price-parity between ETH and ETH2.0. [Carl]

**Q: if block reward is X eth, and it is enough to secure the block, why do we pay X+gas to miners? Will this change?**

A: In Eth2 the economic security is not a direct function of the block rewards. Instead, it is a function of the total amount at stake.

>Will this change?

Eth2 should have a partial fee burning mechanism (see EIP1559). [Justin]

**Q: As ETH 2.0 currently stands what are the odds of a uni-directional vs bi-directional 1.x to 2.0 bridge?**

A: The uni-directional Eth1 -> Eth2 bridge comes with the beacon chain. I'd say it's likely there will be a bi-directional bridge eventually (though unlikely to happen in 2020). Even better than a bi-directional bridge (based on light clients, which comes with non-negligible latency) is native integration of Eth1 into Eth2 (see here). [Justin]

**Q: Will the issuance rate be enough to incentivize validators given the competition from say DeFi products and will it be changed in the future if needed?**

A: Compound rates for ETH are ~0.02% AFAIK, so very easy to compete with. The "do you take 3% interest staking or 6% lending DAI on Compound" framing is highly misleading, because that 6% is on USD, which is very different to having 3% on ETH. But over time I do expect interest rates on ETH to slide up as more forms of staking become available (eg. channels, Plasma, Truebit, other security deposit games...). [Vitalik]

**Q: What are the research team's thoughts / plans on if there is extreme price differences between ETH 1.0 and ETH 2.0? I would think arbitrage would solve the issue but haven't thought too deeply on the subject myself. In paticular, if ETH 1.0 coins are worth significantly more causing people to not want to redeem their ETH 2.0 coins because they will instantly take a price hit versus just selling.**

A: I'm not too worried:

* Transfers and exchanges can be used to redeploy "cheap" Eth2 coins for validation.

* Large holders (e.g. the EF) can be arbitragers.

* The greater the price delta, the greater the incentive to deliver a two-way bridge ASAP. [Justin]

**Q: Is it still the plan that the frequently rotated notaries perform stateless validation of the blocks?**

- **If yes, are there any insights into how much extra network overhead will sending blocks with merkle proofs incur?**

- **If no, is there any other mechanism to prevent adversaries that can corrupt a shard quickly from applying an invalid state transition?**

A: 
> Is it still the plan that the frequently rotated notaries perform stateless validation of the blocks?

Yep!

> - If yes, are there any insights into how much extra network overhead will sending blocks with merkle proofs incur?

Looks like ~10x data (though very low computation, and we expect data to be cheaper than computation). But with techniques like https://ethresear.ch/t/layer-2-state-schemes/5691, even that could potentially be unnecessary. [Vitalik]

>Is it still the plan that the frequently rotated notaries perform stateless validation of the blocks?

Yes.

>are there any insights into how much extra network overhead will sending blocks with merkle proofs incur?

Now that execution engines are application layer, the answer is technically 0 :) For execution engines that use large Merkle trees (e.g. Eth1) the rough estimate at one point was 8x. I'm personally excited for execution engines that do Merkle path "witness compression" using SNARKs (proof creation accelerated by GPUs, FPGAs, or even ASICs). [Justin]

**Q: What is the current design to move Ether tokens on eth1 to eth2?**

A: That depends on what you mean by "Ether tokens".

* Validators can send a deposit of 32 ETH to the deposit contract which is then transferred to the beacon chain where they can begin validation.

* For people who wish to transfer their ETH from Eth1->2, that is not something that has been decided upon yet, but there will (probably) exist a dedicated bridge for this purpose (otherwise they can go through the deposit contract).

* It is still too early to know about ERC20/721 tokens. If Eth2 has an Eth1 execution engine, then it could be pretty painless, but even if not, an ERC20 token could just be transferred by copying over its state root. [Carl]

**Q: Sorry in advance if my questions are dumb but I didn't follow closely Ethereum 2.0 for couple months.**

* **Is there an approximative release date?**

* **Concerning staking, how much is needed and do we know for now the rewards?**

* **What is the main point in eth2.0 you are the most proud of?**

* **Do you feel that the Binance Chain is an enemy to Ethereum?**

A: 
>Is there an approximative release date?

January 3, 2020 at the earliest for phase 0. I'd say Q1 2020 is likely.

>Concerning staking, how much is needed and do we know for now the rewards?

32 ETH. Rewards depend on the total number of validators, individual validator performance, and the gas markets. I wouldn't be surprised if the typical validator has an annual return around 10%.

>What is the main point in eth2.0 you are the most proud of?

I'm proud to have been able to make a contribution in a beautiful piece of infrastructure I believe will radically change the world in a positive way :)

>Do you feel that the Binance Chain is an enemy to Ethereum?

No. [Justin]

**Q: When sharding is released, will there just suddenly be 1024 shards in existence, or will there be a small but growing number of shards as usage goes up? Starting with such a high number will leave a lot of unused space/capacity**

A: All 1024 shards will be launched at once. Growing the number of shards is (probably) unneeded complexity. Shards with lots of unused capacity will have lower gas prices attracting more users.

**Q: How can the average person help with eth2.0? Donations? Documentation? Are there any organized efforts underway?**

A: Educating yourself enough to feel comfortable to participate as a validator would be fantastic :) [Justin]

**Q: After the scaling issues are solved will this be an economical platform to host backend logic on? How will this compare to running your own server or going through a cloud hosting company in terms of cost and ease of use for light or heavy workloads? Personally, my highest anticipated use case is hosting multiplayer matchmaking and signaling, though I haven’t built such a system yet out of concern for difficulty and cost.**

A: It's unlikely that Eth2 on its will be used as a backend for heavy workloads, the data throughput is likely just too high. That said, it works really well as a dispute resolution layer so a centralised service can run the backend optimistically and if someone disagrees with the execution, they can contest and have it resolved on Eth2.

For lighter use-cases it probably can, but this is more in the context of a dapp. [Carl]

**Q: I was under the assumption that ETH would just update to the new ETH 2.0 chain, no need to swap coins or anything but will this transition from ETH1 to ETH2 cause a fork in the community similar to ETC Ethereum classic and ETH chain? Does the circulating supply of ETH 2.0 depend on how many people 'evolve' their ETH1 tokens to ETH2 tokens?**

A: 
>ETH would just update to the new ETH 2.0 chain

Unfortunately, it is not quite that simple. Eth2 is such a big upgrade over Eth1 that it is easier to implement as an entirely new chain than to upgrade. See [Justin's ELI5 here for more](https://old.reddit.com/r/ethereum/comments/cdg8v6/ama_we_are_the_eth_20_research_team_pt_2/ettrnlw/).

>Does the circulating supply of ETH 2.0 depend on how many people 'evolve' their ETH1 tokens to ETH2 tokens?

The large majority of it, yes. Rewards are also issued on the Eth2 chain so that increases the supply there too. Ultimately, the expectation is that all Eth1 ETH will be transferred to Eth2.

**Q: Do you think its worth laying 6 month/1 year/2 year 'ground rules' for Eth 2.0 chain assuming something unexpectedly goes wrong?**

A: My concern with doing something like this is its inflexibility. It is basically impossible to cover all the possible cases and even if we could, I'd argue that such an approach is too inflexible to handle the intricacies of exactly how something has failed. Handling it on a case-by-case basis seems like a better solution to me. [Carl]

**Q: Are there any plans to have the ETH 2.0 chain finalize blocks of the ETH 1.0 chain during Phase 0? For example like proposed with Casper, every 100th block will be validated by PoS.**

A: The integration between Eth1 and Eth2 is a roadmap orthogonal to phases 1, 2, 3 of Eth2.

>Are there any plans to have the ETH 2.0 chain finalize blocks of the ETH 1.0 chain during Phase 0?

My best guess is this will happen in 2021. See [here](https://www.reddit.com/r/ethtrader/comments/c872b7/ethereum_20_well_on_its_way_serenity_phase_zero/esnnvey/). [Justin]

**Q: What happens if you send more ETH to the deposit contract? Like 32.1 or 40?**

A: Nothing is stopping you from sending >32 Eth to the deposit contract, but you'll only receive rewards on the first 32 Eth, so it's not something I'd really recommend. [Carl]

That's fine. Your balance will reflect the deposit, and the balance in excess of 32 ETH can be transferred to another validator (phase 1) or to a shard (phase 2). [Justin]

**Q: What's the easiest set up to stake let's say 320 ETH?**

A: A laptop should be capable of handling around 10 validators so you should be able to send 10*32 Eth to the deposit contract and start validating on your 1 machine. [Carl]

A laptop should be sufficient. We'll know more in a few months when the numbers for block sizes and gas limits of shard blocks get finalized. [Vitalik]

**Q: What's your opinion on Harmony one's approach to a high scalability smart contract platform using PoS? I read you're involved in discussions with them, have you helped each other in developing code?**

A: 
>I read you're involved in discussions with them

I've had brief VDF discussions with Harmony.

>have you helped each other in developing code?

Don't think so, at least not yet.

>What's your opinion on Harmony one's approach to a high scalability smart contract platform using PoS?

I had a brief look at their whitepaper which seems to be inspired by Ethereum. So I guess my opinion is that their approach to scalability is great :) [Justin]

**Q: If Eth 2.0 introduces PoS, are there legal hurdles to be clarified upon? Could the token be considered a security token?**

A: I'm not aware of any jurisdiction that considers ETH on Eth1 a security, and since ETH on Eth2 is basically the same as ETH on Eth1 (other than the temporary technicality of two separate tokens) then ETH on Eth2 should not be a security. [Justin]

**Q: I'm planning to run a beacon node + N validators. Do you think this will will be able to be managed by a Raspberry Pi 4? I'm aware that it is being worked out to have ARM64 binaries ready soon, the question is if it seems realistic not to have a computer running at home and instead running something smaller and cleaner environmentally speaking like a Pi4.**

A: That depends on "N". I (personally) fully expect a RPi3 to be able to run at least one validator node, but we'll only know this when clients are closer to delivery. [Carl]

**Q: What are some smaller things that you guys would like an average r/ethtrader community member could help with?**

A: Educating yourself enough to feel comfortable to participate as a validator would be fantastic :) [Justin]

**Q: Is there any clarity on the transition process regarding basic aspects like whether Beacon eth can be sold on exchanges for example, and whether the PoW chain knows of the Beacon eth? Better asked, how do you ensure there is one network when there are two chains?**

A: 
>whether Beacon eth can be sold on exchanges for example

Beacon eth will be sellable on exchanges when transfers are enabled in phase 1.

>whether the PoW chain knows of the Beacon eth?

That will come later, see [here](https://www.reddit.com/r/ethtrader/comments/c872b7/ethereum_20_well_on_its_way_serenity_phase_zero/esnnvey/).

>how do you ensure there is one network when there are two chains?

The long term plan is to natively integrate Eth1 into Eth2. See [here](https://ethresear.ch/t/work-to-natively-integrate-eth1-into-eth2/5573). [Justin]

**Q: Can you explain somewhat precisely how cross sharding communication would work. As in how does shard node A talk to shard node B without going through some sort of intermediary? If they can do this talking, why can't it be used for eth to talk to say bitcoin.**

A: The intermediary is the beacon chain, or infrastructure optimistically predicting what will eventually get finalised in the beacon chain. [Justin]

**Q: How would you objectively judge the level of technological advancement of current eth and current bitcoin as far as the very limited function of sending coins from A to B is concerned?**

A: Eth1 and Bitcoin are comparable for on-chain payments. [Justin]

**Q: Presuming you agree price drives security, and presuming you agree all cryptos reside in a very competitive environment, are there any plans to address the increased issuance that the Beacon chain would bring? In addition, are there any plans to meet or maybe even surpass bitcoin's coded reduction of new supply to 2% next year. And related, what would you say to the criticisms that have already been expressed whereby if you can reduce issuance by say 10x, you can increase it too. Or asked in a more open question manner, what do you think of this process through which increases or decreases of issuance are made?**

A: It's possible Eth2 will cause net-negative issuance. The reason is that ETH gets burned via transaction fees. Pushing code to the beacon chain will also burn ETH. Finality, the penalties also burns ETH. [Justin]

**Q: Will phase 0 contain any scalability improvements? How many transactions per second will Ethereum be able to handle with Sharding?**

A: Phase 0 will allow for a light client that can give you hashes of the eth1 chain in a fairly lightweight way (but not too lightweight, you'll need ~200kb per 6 minutes to keep up with the committees, this will go down to 200kb per a few days with phase 1). This could be used to allow eg. light clients inside of browsers to work efficiently. That's a kind of scalability improvement, and an underdiscussed one imo. [Vitalik]

Phase 0's purpose is tracking validators' states and producing randomness, asking about its scalability is not really meaningful. Regarding Tx/s, the answer is not really known. As a basic calculation, if each shard has the same throughput as Eth1.x, then we'll have 16 * 1024 = 16,384 Tx/s (assuming no inter-shard Txs).

That said, the above numbers are kinda meaningless as Eth2 is designed to be used along with L2 scaling solutions like Rollups and OVM which could yield insanely high throughputs. [Carl]

**Q: Can you address points 2 - 4 in this [tweet](https://twitter.com/josephdelong/status/1148771489807835136)?**

A: The default idea for clocks in eth2 is https://ethresear.ch/t/network-adjusted-timestamps/4187.

There has not been that much work done on writing "policeman" software that would detect slashable violations by validators and penalize them, but I am not worried about this. Reasons:

* Even if no one writes the code, that just means the security model degrades to honest majority, which is not the worst

* One client implementing the code correctly is sufficient

* If a client implements the code badly, there's no consensus risk, they could just ship with badly written code that only works half the time and it would catch half the slashable violations.

I'll defer to Danny on wire protocol stuff. [Vitalik]

Point 2: "Wire protocol" => This is an implementation detail that I'm sure the implementers will agree upon soon enough :) The high-level recommendation from the research team is to use libp2p as the networking stack (dicv5 for discovery) and SSZ for serialisation. But this cannot enforced at the consensus layer, and we've already seen alternatives (e.g. clients using Whiteblock for networking, and Prysm is using protobufs in some places).

Point 3: "Clients to slash surround votes" => Not sure what this means. The spec clearly defines the slashing mechanism for surround votes. See is_slashable_attestation_data.

Point 4: "Decentralized network time protocol" => Just like Eth1, clocking is an implementation detail. It is to an extent decentralised (e.g. there are alternatives to NTP such as GPS, one can choose his/her NTP servers, one can use local clocks, etc.). It would be nice to have something even more robust but this is research territory—not required for launch of Eth2. [Justin]

**Q: Why aren't Beacon nodes rewarded? Wouldn't this allow the network to be more decentralized?**

A: Validators are rewarded. Beacon nodes that are not validators are not rewarded in protocol because the protocol can't tell who's a beacon node vs just pretending to be one (eg. via 100 fake nodes pointing to the same real node). Though non-validator nodes may be able to earn money in eth2 through incentivized light client protocols.

**Q: In regards to the recent proposal of vitalik to use the bcash chain as a short-term scaling solution until eth 2.0 launches: is eth 2.0 still on track? is there a concrete demand for an interim solution?**

A: The main motivation for proposing an interim solution (if you don't like bitcoin cash for political reasons, I also recommended ethereum classic, I think it's also a good choice) is to make it easier for the work on building these layer 2s to be able to get off the ground in parallel with finalizing the work on the eth2 layer 1 itself. In general, the ethereum community is large, so doing things in parallel is its advantage. [Vitalik]

**Q: You do not plan to work on the creation of parachain (eth 2.0.) On Polkadot?**

I don't think EF will have to drive this. Web3/Parity are on it and I believe consider it to be a top priority.

The Shasper (Parity) client is written in substrate to help facilitate this happening. [Danny]

**Q: Pretty basic but what's a realistic estimate of throughput after every is put together?**

A: Somewhere between 5000 and 500000 TPS depending on what execution environment and transaction type you're using. [Vitalik]

**Q: Could you say anything about the adoption of Ethereum Blockchain? Are there plans to create something like a B2B team actively approaching "qualified" companys?**

A: I'd say the Ethereum Foundation's primary focus is the consensus layer (research, development, education, maintenance, etc.), more so than the application layer. [Justin]


## Resources:

* [Part 1](https://old.reddit.com/r/ethereum/comments/ajc9ip/ama_we_are_the_eth_20_research_team/)
* [Part 2](https://old.reddit.com/r/ethereum/comments/ajc9ip/ama_we_are_the_eth_20_research_team/)

