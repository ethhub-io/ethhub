title: Ethereum 2.0 Researches Reddit AMA - EthHub
description: All questions and answers from the Ethereum 2.0 researchers AMA done on Reddit.

# Ethereum 2.0 Reddit AMA

## Questions and Answers

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

## Resources:

* [Source](https://old.reddit.com/r/ethereum/comments/ajc9ip/ama_we_are_the_eth_20_research_team/)

