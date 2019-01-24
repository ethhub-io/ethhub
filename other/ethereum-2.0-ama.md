# Ethereum 2.0 Research Team Reddit AMA

## Questions and Answers

**Q: When, as in period of time, do you think Ethereum will be able to solve scalabily issues?**

A: In phase 1 (about 2020 by my estimate) we will have shard data. Those shards, even without an EVM, can be used as the data availability layer for TrueBit (and other alternative execution engines). Phase 2 (about 2021) is when we will have scalable L1 execution. [Justin Drake]

**Follow up Q: ELI5 execution engines**

Follow up A: An execution engine is a way to compute state assuming consensus on data. The execution engine for the EVM is "naive re-execution". There are more fancy execution engines such as TrueBit and SNARK/STARK-based validity proofs. [Justin Drake]

**Q: Are economists being consulted to help decide the issuance rate of a full POS system? Stated more broadly, who is helping/advising the ETH 2.0 team on the effects certain issuance decisions will have on the network and community (both in the short and long term)?**

A: Personally at this point the feedback I'm most interested in is actually feedback from potential stakers. The main question basically being, are there any other tweaks we can make to the economics that, given a fixed level of reward, will (i) encourage more people to validate, and (ii) encourage many small solo validators or smaller pools, as opposed to a few large pools. [Vitalik Buterin]

**Q: Considering that Yoichi is not working anymore in the Foundation, what are your plans on formal verification of ETH 2.0 specs?**

A: I'd say that formal verification of the spec will make sense when the spec is more mature and stable, maybe mid 2019. Anyone interested in doing formal verification of the ETH 2.0 specs in a few months, please send a grant proposal. [Justin Drake]

**Q: What is the best response to a developer who is hesitant about building on ethereum today, given that it will be "replaced" by ETH 2.0 over the next few years?**

A: I expect that once the state and execution model for Serenity solidifies (see https://ethresear.ch/t/a-minimal-state-execution-proposal/4445 for one minimal proposal) we'll start working with the developer community on modifications to high-level languages (Solidity, Vyper, etc) and best practices. Hopefully at that point it will become clearer how to build applications in such a way that they could be redeployed as-is on the 2.0 chain. At least that's my hope. [Vitalik Buterin]

A2: Building on Ethereum 1.0 today is great for learning and prototyping. It's also great for assembling a culturally-aligned team consistent with the philosophy of the Ethereum community (which may be different than the philosophy of the Bitcoin, Ripple, Bitcoin Cash, EOS, Tether, etc. communities). [Justin Drake]

**Q: Can we run multiple validator clients on a single machine assuming we've got multiple 32 Eth deposits?**

A: Yep! There's nothing preventing you from using one machine to run multiple validators. The only hard limit you'll face is that the number of shards you are assigned to validate increases linearly with the number of validator slots you have, so if you have thousands of ETH a laptop will not suffice and you'll need something more powerful. [Vitalik Buterin]

A2: Short answer: Yes.

Long answer: You will need to register a validator for every 32 ETH. In phase 0 (just the beacon chain, no shards) you can likely handle thousands of validators on a single machine.

After phase 1 the number of validators that can be operated on a single machine depends on how resourceful your machine is. A mainstream laptop should comfortably handle one validator, and likely handle 2-10 validators at max capacity.

The computational resources scales linearly with the number of validators until you reach ~1,000 validators. At that point there are scalability advantages in being a super-node, i.e. a full node for every shard. [Justin Drake]

**Follow up Q: How much importance are the devs placing on being able to run setups at home wrt keeping Ethereum decentralised and being able to move ETH in and out of staking pools?**

Follow up A: It's definitely a goal I care about. The alternative to staking at home is staking on AWS or staking through a pool, and both are risks for decentralization.

Concrete ways we try to be friendly to staking at home:

* Relatively forgiving penalties for being offline, so you earn a net profit as long as you're online more than ~50-67% of the time
* Keeping the cost of validating the beacon chain low
* The anti-correlation penalty scheme, which more heavily penalizes validators that misbehave at the same time as many other validators (which is more likely if you're on the same pool or VPS or whatever). [Vitalik Buterin]

**Q: How can I help / get involved? I fell in love with Ethereum not too long ago. I’ve been reading Zcash’s BLS12-381 Elliptic Curves and for the past few days these are all thats been on my mind. I love this project now and just found ethresear.ch. I really wanna help in any way possible! Thanks again for all your hard work. I can’t stop reading these posts.**

A: For researchers a good way to contribute and gain visibility is to post quality content on ethresear.ch. If you are a developer consider joining one of the numerous ETH2.0 implementation teams. [Justin Drake]

A2: Hi! The best way to get involved is to find something that captures your interest and to dig in. Because Ethereum is a radically open platform, the research and development is also generally very open and very accessible.

* Keep reading. Follow your interests down all the little paths and begin to build a mental model of the ecosystem.
* https://ethresear.ch/ is a great place to follow and begin to contribute to research discussions.
* https://gitter.im/ethereum/sharding is where a lot of the day to day conversation about Serenity is happening (developers chatting from various projects)
* https://github.com/ethereum/eth2.0-specs Read the spec! but not only read it, be an active reader. If you find an error, typo, bug, etc, submit a PR. Also check out the issues and PRs in the spec repo. We are constantly discussing changes, fixes, updates and anyone can contribute.
* If you are a dev, open up one of the eth2.0 client projects and pick a "good first issue". These allow you to touch the codebase, contribute a bit, get the lay of the land, and provide the foundation to tackle bigger issues from there.

^ Those are Serenity specific suggestions, but beyond that, just find projects you are interested in and begin contributing. There is so much to do and project leads are always excited to have helping hands. This stuff doesn't build itself :) [Danny Ryan]

A3: If you're interested in Cryptography especially, you can also check out another BLS - Boneh–Lynn–Shacham signature spec for Serenity and help to review it: https://github.com/ethereum/eth2.0-specs/blob/master/specs/bls_signature.md :)

For research, as Justin and Danny said, ethresear.ch is the sanctuary. And first, you can take a look the various topics on Ethereum Sharding Research Compendium to see which area you're most interested in.

* For implementation, there are multiple topics:
  * Consensus layer - implement the spec!
  * P2P layer design and implementation - see https://github.com/ethresearch/p2p [Hsiao-Wei Wang]

**Q: From my limited understanding of Eth 2.0 specs, I gather that shards will be mostly independent, with cross-shard communication being slow and requiring multiple steps. As a consequence, smart contracts will only be able to interact lively with assets from within their deployed shard, and will have to go through slow cross-shard communication to interact with assets outside.**

**Given this topology, are we not aiming to improve scalability at the cost of sacrificing user experience (slow response of smart contracts in non-obvious ways)?**

**For instance if I want to play cryptokitties, I will need to make sure to interact with the contract that is deployed on the shard where my eth address resides, and not with any of the other contracts that reside on other shards. Then, if I want to interact with the kitties of someone else who resides on a different shard, my experience will be much slower and cumbersome than if that person would reside in my shard (or at least this is how I understand the system will work, please correct me if I am wrong). Given that the end goal is to scale to a very large number of shards, then the likelihood to have to go cross-shard increases exponentially with time, and thus the user experience gets progressively worse and worse.**

A: Cross-shard communication will definitely be slow at base layer, however there are higher-level mechanisms that can be used to implement fast cross-shard communication on top of a base layer that allows any cross-shard communication at all even if slow. See https://ethresear.ch/t/a-layer-2-computing-model-using-optimistic-state-roots/4481 for an example of how this could be done.

In general, I expect a lot of the long-run innovation in improving the smart contract development experience to happen at higher levels in this way; I write about why this is a good idea at length here: https://vitalik.ca/general/2018/08/26/layer_1.html [Vitalik Buterin]

**Q: What happens to all the contracts currently running?**

A: It is somewhat speculative at this point. My best guess is that Ethereum 1.0 contracts will stay running as-is for a long time (say, 10+ years) without any migration to Ethereum 2.0. This can be made sustainable by doing two things:

1. Lower the inflation (e.g. reduce it by 20x, bringing the PoW security to a blockchain such as Ethereum Classic). Completely removing inflation—relying on transaction fees only—would also be possible (see below for security argument).

2. Use Ethereum 2.0 to regularly finalise Ethereum 1.0, counter-balancing the reduced security and preventing long-range 51% attacks. This requires Ethereum 1.0 nodes to be beacon chain light clients, which should take years to happen.

If the community gets tired of Ethereum 1.0 a bomb mechanism (e.g. difficulty bomb, issuance bomb, gas bomb, etc.) can gracefully kill it. Another possibility is for Ethereum 1.0 to become a contract on Ethereum 2.0. I don't see this as a practical solution, but I'm open to being convinced otherwise :) [Justin Drake]

A follow up: I'll add that if any specific user wants to migrate their application to the 2.0 chain, then they should be able to just take their existing high-level code (Solidity or Vyper), make relatively few changes and redeploy. The main difference between the eth1 and eth2 systems that users will need to worry about is likely to be rent (or equivalents like gas-payment-extended bounded TTLs). [Vitalik Buterin]

**Q: Is there a worry that shards will become “gentrified” until full shard interoperability? Basically, will one shard capture all the defi apps because they can't directly communicate with each other on separate shards?**

A: I would say if that happens, that will create a large incentive for someone to create a defi dapp that can interact with the other defi dapps through asynchronous cross-shard transactions and launch it on a cheaper shard. [Vitalik Buterin]

A2: At the start in times of low usage, the economic load-balancing might result in over and under utilized shards.

Overtime as usage increases, I expect the economic benefits of deploying and interacting on particular shards will become more tangible and result in a more economically rational distribution across shards.

Observing the emergent behavior is going to be super fascinating :) [Danny Ryan]

**Q: Can we run the same validator on multiple machines - in order to avoid penalties if one machine was compromised ? If yes - what happens when we run a validator on 3 machines, one goes temporary offline, one is compromised, one is OK?**

A: For small amounts of ETH I'd recommend just running on one machine; unless many other validators get penalized at the same time as you, the penalties are not too large. If you do want to decentralize your validator, then we have recently made progress toward validation being more multi-party-computation friendly, which would allow you to run a validator as a 2-of-3. In that case, as long as two of the three sub-nodes are functioning correctly you'll be fine. [Vitalik Buterin]

A2: Yes! Ethereum 2.0 is friendly to n-of-m schemes thanks to BLS signatures. For example, with a 2-of-3 scheme you have can three computers, each with a share of the validator private key, such that two need to be online at any given time. This improves security as well, because an attacker now needs to compromise two of the BLS key shares. [Justin Drake]

**Q: Is there tech from any competitors such as Dfinity (or any others) that is worth adopting into Ethereum 2.0, or is the work all other dapp/smart contract platforms doing not relevant/good enough for ETH 2.0?**

A: Part of the job of the research team is to absorb good ideas from research papers and other blockchain projects. I keep a keen eye on technically interesting projects such as Dfinity, Coda, Zcash, etc.

Competitors definitely also have good ideas, and learning from each other is part of the game :) [Justin Drake]

**Q: Do we need to run a full node to also earn from network fees or would the validator client handle this?**

A: Depends what you mean by "full node". The design of the sharding system is such that no one needs to run a node that verifies all of the data of all of the shards. A validator client validates the beacon chain and the specific shards that you get assigned to validate, and that is sufficient to earn network fees. [Vitalik Buterin]

A2: The validator client should abstract the necessary tasks to get revenue from the different revenue streams. (This includes being a full node for the beacon chain and one shard at any given time, but that's a technicality you don't have to worry about.) [Justin Drake]

**Q: Very interested to hear about the efforts currently underway at the EF and strategic partners/OEMs to design and manufacture the VDF hardware.**

**It's also the thing that scares me the most about the proposed design;i can see how they would really increase the security of the random sample selection process in addition to RANDAO but manufacturing hw is a costly, difficult endeavor often subject to unforeseen issues and delays.**

**On that note is an economic incentive structure for running a VDF node being considered?**

A: **Very interested to hear about the efforts currently underway at the EF and strategic partners/OEMs to design and manufacture the VDF hardware.**

We're working our way with various partners, including Synopsys, AWS, TSMC, GUC, etc. VDF announcements to come in February :)

**manufacturing hw is a costly, difficult endeavor often subject to unforeseen issues and delays.**

Right. The good news is that Ethereum 2.0 can launch just fine without VDFs, so we're not betting Ethereum 2.0 on the success of VDFs. The current plan is to have VDF hardware ready in 2020, but 2021 would also be acceptable.

From a financial perspective, we may share the total costs (estimated at $15m) with Filecoin and other projects interested in VDFs. We are already sharing costs with Filecoin on viability studies.

**On that note is an economic incentive structure for running a VDF node being considered?**

Short answer: yes, of course :)

Long answer: the ethresear.ch post provides a bit of clarity on that.

**highly specialized hw always connected providing a crucial function to the network it would be a prime target for potential adversaries to disrupt or compromise**

Right. The good news is that we only need one VDF evaluator to be online for normal operation, and even if everyone goes down it's not a huge deal. The main negative consequence is that dApps relying on unbiasable randomness will have to wait longer than expected for the random numbers to arrive. [Justin Drake]

**Q: zk-STARKs are powerful and I have been reading Eli’s and the others paper on it. Are recursive zk-STARKs ever doable? I know Coda is planning on using Recursive zk-SNARKs to shrink chains but the lack of transparency is worrying.**

A: I don't see what fundamentally prevents them from happening. Recursive [any zero knowledge proof schemme] just means using the ZKP mechanism to make a ZKP of the ZKP's own verification procedure. The main challenge in practice is just that these verification procedures themselves have a high cost (eg. there's 50-500 kB worth of hashes in a STARK to verify), and this cost multiplied by the ZKP's overhead is quite a big number. ZK SNARK verification is in contrast much more "concise". [Vitalik Buterin]

A2: **Are recursive zk-STARKs ever doable?**

In theory yes, but as I understand recursive zk-STARKs won't make sense from a performance standpoint for most applications, at least in the medium term. [Justin Drake]

**Q: What’s the final scalability limit of Ethereum post Serenity? Gas limits per block? Blocks per second?**

A: The current design has a fixed number of shards, at most one block per 6-second slot, and fixed block sizes. This means that the data bandwidth is capped. The gas limit on the other hand will likely be floating, just like Ethereum 1.0. [Justin Drake]

A follow up: Though in the current phase 1 spec that's sitting around in draft mode the block size is so far fixed to 16 kB, as keeping it fixed makes the code for proofs of custody, data availability proofs, etc much simpler.

If we want to bump up capacity later increasing the shard count may well be the simpler way to do it. [Vitalik Buterin]

**Q: Why should anyone move to the Beacon Chain? How exactly do you envision the move to happen?**

A: **Why should anyone move to the beacon chain.**

Specifically, only validator balances exist in the Beacon Chain. User balances and state exist in the shard chains.

Validators will move to the beacon chain to seek profit by providing security and resources to network. Note there is a new proposal to have the beacon chain finalize the PoW chain during the transition period so the validators would be able to provide security both to the new shards and the existing chain.

Users will move to the shard chains to participate in the new scalable, sharded landscape. We envision economic activity to begin to move over as the system stabilizes and begins to show clear economic benefits to the users. It is important to note that a user could choose to not move until the eth1.0 state is rolled into a shard.

**How exactly do you envision the move to happen?**

At first, this will just be a single directional deposit for validators only to begin validation. Once the state execution layer is in the new 1024 shards, users will be able to transfer eth directly to the shards from the PoW chain. In the long term, the plan is to roll the PoW state into one of the shards. The current most favorable strategy from our perspective is to fork the PoW state root into a contract along with an EVM interpreter. Users could then execute txs on the existing eth1.0 state by call the contract along with the merkle witnesses of the state they need to access. This option is nice because it allows us to cleanly deprecate eth1.0 support in the long term. [Danny Ryan]

A2: Moving to the beacon chain is done by sending ETH to a so-called "deposit contract" on Ethereum 1.0. People would send ETH to the beacon chain to become an Ethereum 2.0 validator and gain financial rewards. [Justin Drake]

**Q: How much funds does Ethereum foundation have and are these enough for finishing Eth 2.0?**

A: The EF has tens of millions of dollars in fiat, and a bunch of ETH. More than enough to finish ETH 2.0 :) [Justin Drake]

**Q: How is the status of a possibly fixed eth supply at some point in the future? Do you think it's likely?**

A: I don't know about fixed ETH supply, but we may get to a point of decreasing ETH supply. Indeed, we are looking into transaction fee schemes that burn ETH, and burnt ETH may outweigh minted ETH. [Justin Drake]

**Q: Have you looked into hyraxZK. They are zk-SNARKs that do not require a trusted setup. Any thoughts on them being used in the future as the sizes are still very small. The only thing is they wouldnt be Quantum-Resistant but the proof size won’t be similar to a zk-STARK. I wonder what they can be used for offchain as well, especially in networking by producing a zk proof of incoming packets that acts as Natural DDOS Protection. Just some thoughts.**

A: Have not looked into Hyrax specifically, but I am totally not surprised that things like it exist. I'm definitely very happy with the progress the general-purpose ZKP space has accomplished in the last few years; the very concept of general-purpose ZKP is pretty godlike compared to what I imagined was possible with cryptography as a child.

Our general instinct is to find ways to make it possible to get the benefits of many different ZKP schemes with different tradeoffs in ethereum. The simplest way to do this would be to encourage the development of such tech as application-layer or network-layer addons so that it we do not need an agreement at consensus layer about a single ZKP scheme that everyone uses. [Vitalik Buterin]

**Q: V said that there are no fundamental problems left to solve. Is this true for only phase 0? If so, how confident are you about the other phases?**

A: Personally I am confident in all of the current fundamental technologies for all the phases outlined so far (Casper FFG and CBC, sharding, erasure coded data availability proofs, proofs of custody, receipt-based async transactions, layer 2 for acceleration, abstraction, rent, "stateless client" verification). There is definitely still a lot of room around the edges for optimization though. [Vitalik Buterin]

**Q: Why was Hybrid Casper ditched when it looks like the Beacon Chain kind of has nothing to do with the PoW chain? or Why not re-instate Hybrid Casper considering its testing is/was finalized?**

A: Honestly hybrid Casper is a bit of a dead end. Actually implementing/testing it across all the clients would require setting up a lot of infrastructure that we would then need to throw away. The design was highly inefficient because of its "implemented-in-EVM" nature, and it turned out that we could not really benefit from the ease-of-implementability of being done in EVM because we would need to write a lot of special-purpose code to make verification of signatures parallelizable. So we chose the route that would be somewhat more painful in the short term, but significantly lower headache to actually get to a stable sharded system overall. [Vitalik Buterin]

A2: I wrote up some notes on the deprecation of EIP 1011 here https://notes.ethereum.org/s/rJDrKoBOQ [Danny Ryan]

**Q: 1. Since it is a one way transfer to the beacon chain, my understanding is that there will be two tokens: ETH1.0 and ETH2.0. Right?

2. Will The beacon chain allow tokens to be send. I.e. will exchanges be able to list the token before phase 2?

3. My feeling is that from a risk/reward perspective, stakers will expect returns more in the area of emerging market debt (+20%) esp. in the beginning. But all discussion I saw was ~2%. Any comments on this?

4. Gutfeeling: how much "unsolved computer science problems" for phase 1, 2 and 3 roughly? I understood for phase zero it has arrived at 0.

5. Will we consider some kind of tax baked into the system to ensure sustainability of core developments and infrastructure?

A: **Will The beacon chain allow tokens to be send. I.e. will exchanges be able to list the token before phase 2?**

ETH in the beacon chain would not be transferable (anywhere!) until phase 2. That will make exchanges harder, although we may see a futures' market. My guess is that we will see 1 ETH ~ 1 BETH at pretty much all times :) [Justin Drake]

**My feeling is that from a risk/reward perspective, stakers will expect returns more in the area of emerging market debt (+20%) esp. in the beginning. But all discussion I saw was ~2%. Any comments on this?**

The reward/penalty constants are certainly not yet finalized and could use more community debate and input. That said, the rate does scale depending on the number of validators participating. If the fair market rate is really 20%, then a lower number of validators will show up. If the fair rate is 2%, then a ton of validators will show up. The economics of staking will find the natural equilibrium. That said the main risk here is if we set the target rate too low and the equilibrium lands at a low participation rate (and thus low security of the network).

Although ~2% (@ 10M eth validating) is not set in stone, the idea for a low rate is that a huge amount of ETH is already being held as a speculative asset. Any marginal rate of return on top of this already intended long-term hodling is a gain for the hodler. [Danny Ryan]

**Q: How would you (and or service providers) ensure the eth on the Beacon Chain is the same as that on the PoW chain and vice versa?**

A: Arbitrage is always possible in one direction by buying 1 BETH for 1 ETH. A key design goal of Ethereum 2.0 is full fungibility for ETH tokens between the Ethereum 1.0 chain, the beacon chain, and the shards. Two-way transfers between the beacon chain and the shards, as well as between shards, should come in phase 2. [Justin Drake]

**Follow up point: If you wait until phase 2 for two-way flow, you privilege the very few stakers able and willing to wait an undetermined number of years for access to their money.**

**This will be great for those few (probably north of 25% interest rates!) but not very great for security.**

Follow up A: y**ou privilege the very few stakers able and willing to wait an undetermined number of years for access to their money**

The ultimate loyalty test :)

**probably north of 25% interest rates!) but not very great for security.**

We do have a minimum amount at stake to launch phase 0, around 214 * 32 ETH = 524,288 ETH. So we're effectively capping the interest rate (will be less than 25%) and setting a minimum security level. [Justin Drake]

**Q: For how long is the 32eth locked up when running a validator client? What happens if the machine I'm using gets destroyed or stolen during the lock up period? Can you switch machines?**

A: **For how long is the 32eth locked up when running a validator client?**

At least as long as you are a validator. Withdrawal times should be a few days/weeks/months depending on how many other validators are trying to withdraw.

**What happens if the machine I'm using gets destroyed or stolen during the lock up period? Can you switch machines?**

You can switch machines. You need a copy of your private keys in case your machine gets destroyed or stolen.

Another thing is the withdrawal key used for withdrawals only. Keep that one in cold storage ideally. [Justin Drake]

**Q: Contributing to Ethereum 2.0? Are there any projects which are some sort of "under water", like only few people working on it.**

A: I feel at this point there are enough implementation teams, at least compared to some of the other issues that are underaddressed. Off the top of my head:

* Solidity being compile-able to E-WASM
* Vyper being compile-able to E-WASM
* Thinking about research problems related to phase 2, particularly around account abstraction, asynchronous contract programming models, etc
* Privacy, eg. see https://ethereum-magicians.org/t/meta-we-should-value-privacy-more/2475
* Improving the state of decentralized messaging and file storage [Vitalik Buterin]

Follow up A: A few more things good to work on:

* liibp2p implementations in various languages
* Doing security reviews of the spec
* prototyping account and state execution in eWASM
* a lot of work in cross client testing coming up in the next couple of months [Danny Ryan]

**Q: We have experienced consecutive delays with Constantinople due to bugs found late in the process on a comparatively low risk / simple upgrade.**

**What work is being done to mitigate this on Phase 0 and 1 given how much more complex these implementations will be? (I.e. What testing, third party audits, other considerations are being taken to ensure seamless implementation/integration?**

A: As the phase 0 spec is moving into a more stable place, we are beginning to look into explicitly bringing in third party audits, academics, and formal analysis. In addition to this, we are currently laying down the foundations of cross client testing and fuzzing akin to eth1.0. You're correct in that the consensus/system layer of eth2.0 is much more complex than the single PoW chain so we are constantly trying to reduce complexity and simplify. This is a major engineering effort that will require many parties other than our research team to plan, build, test, execute, and maintain. I think it is a major strength that so many independent teams with a diverse set of expertise have stepped up to contribute.

Note, one of the design goals in the [spec readme](https://github.com/ethereum/eth2.0-specs/blob/master/README.md) -- "to minimize complexity, even at the cost of some losses in efficiency"

We're excited to see new efforts like the "Ethereum Cat Herders" and scheduled release cycles emerging in 1.0 and plan to incorporate any best practices and efforts into the 2.0 process. DePM (decentralized project management) is hard, but we continue to learn and continue to get better. [Danny Ryan]




## Resources:

* [Source](https://old.reddit.com/r/ethereum/comments/ajc9ip/ama_we_are_the_eth_20_research_team/)
