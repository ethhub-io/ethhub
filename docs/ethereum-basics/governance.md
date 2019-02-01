# Governance

## Summary

Blockchains are distributed systems. They are essentially consensus protocols, which means that different nodes in the network \(e.g. computers on the internet\) have to be running compatible software.

**“Node operators”** are the owners and managers of nodes that run the protocol. Most node operators don’t want to write much software, and it’s a technical challenge for anyone to independently write compatible implementations of any consensus protocol even if they have a specification. As a result, node operators rely on software repositories \(usually hosted on Microsoft/Github servers\) to provide them with the software they choose to run.

**“Core developers”** of a blockchain are software developers who work on the software that implement that protocol. Developers have processes that are supposed to assure the quality of the software they release, and are generally very interested in maintaining the legitimacy of their software repositories because they want to see people using their software \(as opposed to someone else’s\).

## Critical Components of Governance

**1. Incentives**

Each group in the system has their own incentives. Those incentives are not always 100% aligned with all other groups in the system. Groups will propose changes over time which are advantageous for them. Organisms are biased towards their own survival. This commonly manifests in changes to the reward structure, monetary policy, or balances of power.

**2. Mechanisms for Coordination**

Since it’s unlikely all groups have 100% incentive alignment at all times, the ability for each group to coordinate around their common incentives is critical for them to affect change. If one group can coordinate better than another, it creates power imbalances in their favor.

In practice, a major factor is how much coordination can be done on-chain vs. off-chain, where on-chain coordination makes coordinating easier. In some new blockchains \(such as Tezos or Polkadot\), on-chain coordination allows the rules or even the ledger history itself to be changed.

## On-Chain Governance

Current governance systems in Bitcoin and Ethereum are informal. They were designed using a decentralized ethos, first promulgated by Satoshi Nakamoto in his original paper. Improvement proposals to make changes to the blockchain are submitted by developers and a core group, consisting mostly of developers, is responsible for coordinating and achieving consensus between stakeholders. The stakeholders in this case are miners \(who operate nodes\), developers \(who are responsible for core blockchain algorithms\) and users \(who use and invest in various coins\).

### What is on-chain governance?

On-chain governance is a system for managing and implementing changes to cryptocurrency blockchains. In this type of governance, rules for instituting changes are encoded into the blockchain protocol. Developers propose changes through code updates and each node votes on whether to accept or reject the proposed change.

### How does it work?

Unlike informal governance systems, which use a combination of offline coordination and online code modifications to effect changes, on-chain governance systems solely work online. Changes to a blockchain are proposed through code updates. Subsequently, nodes can vote to accept or decline the change. Not all nodes have equal voting power. Nodes with greater holdings of coins have more votes as compared to nodes that have a relatively lesser number of holdings.

If the change is accepted, it is included in the blockchain and baselined. In some instances of on-chain governance implementation, the updated code may be rolled back to its version before a baseline, if the proposed change is unsuccessful.

### Pros

* It is a decentralized form of governance
* Quicker turnaround times for changes 
* Possibility of a hard fork is reduced significantly

### Cons

* Low-voter turnout
* Tends towards plutocracy \(users with greater stakes can manipulate votes\)

## Off-Chain Governance

### What is off-chain governance?

Off-chain governance looks and behaves a lot similar to politics in the existing world. Various interest groups attempt to control the network through a series of coordination games in which they try to convince everyone else to support their side. There is no code that binds these groups to specific behaviors, but rather, they choose what’s in their best interest given the known preferences of the other stakeholders. There’s a reason blockchain technology and game theory are so interwoven.

### How does it work?

Improvement proposals to make changes to the blockchain are submitted by developers and a core group, consisting mostly of developers, is responsible for coordinating and achieving consensus between stakeholders. The stakeholders in this case are miners \(who operate nodes\), developers \(who are responsible for core blockchain algorithms\) and users \(who use and invest in various coins\).

The various stakeholders signal their approval or disapproval for an improvement proposal through private and community discourse. Then, the core developers get a sense for whether or not node operators and miners will agree to upgrade their software. Ideally, all sides agree and the code changes are made smoothly. Everything is announced beforehand and stakeholders have time to update.

In the case of disagreement, stakeholders have two options. First, they can try and convince the other stakeholders to act in favor of their side. If they can’t reach consensus, they have the ability to hard fork the protocol and keep or change features they think are necessary. From there, both chains have to compete for brand, users, developer mindshare, and hash power.

## Resources

* [Why on-chain governance?](https://medium.com/polkadot-network/why-on-chain-governance-82ecf28f314c)
* [On-chain governance explained](https://www.investopedia.com/terms/o/onchain-governance.asp)
* [Off-chain governance explained](https://education.district0x.io/general-topics/what-is-governance/off-chain-governance/)




