# EthHub CFTC Response

On December 11th, 2018 the CFTC [submitted a public "Request for Input"](https://www.cftc.gov/sites/default/files/2018-12/federalregister121118.pdf) which asks for clarity and answers around Ethereum. The following is a list of all questions asked in the RFI. The following answers were developed on EthHub, an open source, community run information hub for the Ethereum community.

_**From the CFTC: In providing your responses, please be as specific as possible, and offer concrete examples where appropriate. Please provide any relevant data to support your answers where appropriate. The Commission encourages all relevant comments on related items or issues; commenters need not address every question.**_

## Purpose and Functionality

### 1. What was the impetus for developing Ether and the Ethereum Network, especially relative to Bitcoin?

The underlying impetus to develop Ethereum was to utilize aspects of the technology initially developed as part of the Bitcoin blockchain and combine it with the capabilities of a Turing complete supporting environment.

The idea was that this change would lead to a platform that could sustain not only a medium of exchange and imperative non-turing complete programmability, but also to add conditional branching (Turing completeness) to the programmability existing on bitcoin. 

Introducing conditional branching to the equation would open up a wide range of possibilities with regards to decentralized financial applications and products, more decentralized applications are possible with these new attribute.

Turing completeness:
https://medium.com/@evinsellin/what-exactly-is-turing-completeness-a08cc36b26e2
Conditional branching:
https://www.pcmag.com/encyclopedia/term/40224/conditional-branch

### 2. What are the current functionalities and capabilities of Ether and the Ethereum Network as compared to the functionalities and capabilities of Bitcoin?

The Bitcoin and Ethereum blockchains are currently both secured by a Proof of Work transaction ordering, sybil-control mechanisms and BFT consensus. However, the core difference is that Ethereum offers smart contract functionality enabled by its flexible scripting languages and the Ethereum Virtual Machine \(EVM\), which is a quasi-Turing Complete virtual machine that compiles smart contract code and enables execution of that code. These smart contracts allow the incorporation of logic based programs that can create unique conditons to the transfer and settlement of Ether transactions amongst counterparties. Because of its ability to support smart contracts Ethereum enables the development and deployment of decentralized applications that can incorporate any computational logic.

The functionality of the underlying asset Ether is actually very similar to Bitcoin. It is used to 1: incentivize security for the network as a block reward to miners peforming computationally intensive work to provide secure transaction ordering and block creation and to prevent a wide array of failures \(e.g. double spending, transaction censorship\); 2: serves as a sybil resistance mechanism \(and additional miner incentive\) in the form of network transaction fees that prevent forged identity based attacks, provides spam and denial of service attack protection, and that are ultimately paid to miners \(or staking validators in Proof of Stake\) to incentivize their work securing the network, while also creating a fee market that aids in preventing network congestion; and, 3: a vehicle for interacting with smart contracts deployed on the Ethereum blockchain.

### 3. How is the developer community currently utilizing the Ethereum Network? More specifically, what are prominent use cases or examples that demonstrate the functionalities and capabilities of the Ethereum Network?

The simplest use case of the Ethereum network is value transfer by sending Ether \(which has an attached value\) from one person to another. However, the amount of applications being built on top of the program is growing at a rapid pace. Currently, the most active applications are those related to "Decentralized Finance". As of 12/11/18, there is currently $120,000,000 worth of Ether being used in Decentralized Finance applications.

### 4. Are there any existing or developing commercial enterprises that are using Ether to power economic transactions? If so, how is Ether recorded for accounting purposes in a comprehensive set of financial statements?

The Enterprise Ethereum Alliance is a large group of commercial enterprises decidated to developing enterprise use cases and building out standards frameworks for Enterprise Ethereum. Additionally, though non-commerical, the United Nations International Children's Emergency Fund's Kazakhstan branch and Innovation Innovation Fund is piloting an effort utilizing the Ethereum blockchain to provide track and traceability for transactions between UNICEF and partners to enhance transparency and efficiency of how UNICEF deals with its implementing partners on the ground \(http://unicefstories.org/2018/09/26/project-opportunity-build-a-smart-contract-prototype-for-unicef-kazakhstan-to-track-results-for-children/\).

Currently, the Financial Accounting Standards Board classifies native cryptocurrencies, including Ether as indefinite-lived intangible assets under ASC 350 in their report titled *Financial Reporting Alert 18-9 — Classification of cryptocurrency holdings*. Ether, like other cryptocurrencies, meets the definition of an indefinite-lived intangible asset. Using the intangible-asset model results in holdings of cryptocurrencies being recorded at the cost of acquisition, subject to impairment. That is, the model should only capture declines in the value of the cryptocurrency, not increases. When Ether is purchased, the intangible asset would be measured at the price paid or consideration given to obtain the cryptocurrency. However, the question for miners in Proof of Work or validators in Ethereum's propose Proof of Stake is more complicated. Unlike a direct purchase, miners and staked validators are awarded Ether as a reward for ordering transactions and securing the network, but they incur costs of computing equipment, electricity, devops and other expenses. At issue for the miners or staked validators is whether the associated costs should be capitalized as an intangible asset or expensed.

While Ether may fit into the existing model for intangible assets and appear as such in the companies balance sheets, a simpler, and potentially better model for representing the economics associated with holding or using Ether is the fair value measurement model, with both realized and unrealized changes reflected currently in the income statement.

### 5. What data sources, analyses, calculations, variables, or other factors could be used to determine Ether’s market size, liquidity, trade volume, types of traders, ownership concentration, and/or principal ways in which the Ethereum Network is currently being used by market participants?

There are a plethora of publicly available tools, websites, and APIs that this type of information can be obtained from. Exchanges such as Coinbase gather a host of trading data and metrics for each blockchain whose native cryptocurrency they have listed. Additionally, free and open source tools such as those provided by coinmetrics.io, etherscan.io, and Santiment, or paid tools such as coinfi.com, Diar Newsletter, and other Ethereum blockchain tools and services monitor and provide metrics. These metrics include the concentration of wealth in Ethereum by wallet address, individual account information including all send and receive transactions \(and in some cases available ownership information\), daily transaction volume measured in total Ether and USD value equivalent, average block time, average block size, number of nodes connected to the network, current network transaction fees, most active addresses and smart contracts, smart contract internal transaction monitoring, amount of Ether or USD value equivalent stored or transferred by decentralized applications and associated smart contracts, subjective user activity metrics, and more market focused metrics tracking price trends, market cap, total and available supply, liquidity, etc.

### 6. How many confirmations on the Ethereum blockchain are sufficient to wait to ensure that the transaction will not end up on an invalid block?

A user must only wait 1 block confirmation for their transaction to be validated and confirmed. However, there is a risk of hash power related attacks to the network \(e.g. 51% attacks\) that could potentially result in double spends or the block a transaction was originally included in being orphaned \(abandoned in its own version of the chain that is not accepted by the network\) and thus censored by a large hashrate owning miner or group of miners attacking the network. However, because Ethereum, like Bitcoin, is probablistic by nature, the probability of such an attack decreases with every block confirmation, as the cost to aquire the hashrate necessary to attack the network increases substantially until it becomes uneconomical. Because of this, some merchants may wait a pre-selected amount of confirmations, such as 6 block confirmations for Bitcoin with its 10 minute block time or 30 for Ethereum with its 12-14 second block time in order to avoid this risk.

## Technology

### 7. How is the technology underlying Ethereum similar to and different from the technology underlying Bitcoin?

From a high level, Ethereum is similar to Bitcoin in that it uses a 'blockchain' and uses 'Proof of Work' to achieve consensus and secure the network. Both blockchains have a native digital asset - Ether \(ETH\) for Ethereum and Bitcoin \(BTC\) for Bitcoin.

The Ethereum network is a turing-complete blockchain. This means that it is capable of executing arbitrary code - known as smart contracts. The ability to run code on the Ethereum blockchain means that developers can build applications on top of it. One such application, MakerDAO, allows users to use their ETH as collateral to take out a loan denominated in a USD-pegged stablecoin \(known as DAI\). Applications are all interoperable within the confines of the Ethereum network. Ethereum acts as a common protocol for all decentralized applications built atop in the way that TCP/IP acts as a common protocol for all public web-based applications. It is not strictly limited to being used as a settlement layer as Bitcoin has become.

Ethereum 2.0 \(Serenity\) is a substantial upgrade for the Ethereum network being deployed in multiple phases. The main features in this upgrade include a move to a novel Proof of Stake system known as Casper\(for securing the network\), sharding \(for scaling the network\) and eWASM \(a new virtual machine for the network\). These upgrades and new features are developed by a decentralized network of core developers spanning 8 individual Ethereum software client teams, the non-profit Ethereum Foundation, and additional volunteer developers and researchers from around the globe.

### 8. Does the Ethereum Network face scalability challenges? If so, please describe such challenges and any potential solutions. What analyses or data sources could be used to assess concerns regarding the scalability of the underlying Ethereum Network, and in particular, concerns about the network’s ability to support the growth and adoption of additional smart contracts?

The Ethereum Network faces scalability problems similar to Bitcoin and other decentralized blockchains. Where other blockchains have traded off decentralization, trust minimization, and security in favor of throughput (transactions per second) both Ethereum and Bitcoin were created on the principle of maximum decentralization and security above all. It is a trade-off as identified in Vitalik Buterins trilemma for blockchain scalability \(https://bitcoinist.com/breaking-down-the-scalability-trilemma/\)

It's important to understand the basics of how the Ethereum blockchain functions before diving into scaling. Every transaction cost a certain amount of "gas" which is the cost, in computational power, to execute a transaction \(denominated in Ether\). Every block processed on the network has a cap on the amount of gas it can hold \(the "gas limit"\). This is because if blocks get too large, there are issues with the way they propogate across the network which increases the likelihood of an incidental fork \(chain split\) as well as storage and initial syncronization issues. Currently, the Ethereum network sits at max capacity in terms of gas used every day, though recent optimizations in the most widely used client, Parity Ethereum, now enables the gas limit to be increased safely if the mining nodes so agree.

This is how Ethereum plans to tackle the scalability issue:

'Layer 1' refers to the main Ethereum network/blockchain. 'Layer 2' refers to technologies built on top of \(or above\) the main Ethereum network/blockchain. 'Interoperability' refers to the use of other blockchains.

A decentralized network of open source developers are addressing Ethereum's Layer 1 scalability challenges by introducing a mechanism borrowed from traditional databases - 'sharding'. Sharding takes the blockchain and splits it up into multiple blockchains \(that can communicate with eachother\) so that transactions and computations can be processed in parallel, and then finalized to one larger ledger of record \(known as the beacon chain\).

An ecosystem of project teams, decentralized application teams, traditional companies, and open source developers are addressing Layer 2 scalability challenges on Ethereum through the use of multiple technologies. These technologies include sidechains \(such as Plasma\), state channels, and interoperability chains and bridges that outsource some transacting to other, compatible blockchains and utilize Ethereum strictly as a settlement layer.

### 9. Has a proof of stake consensus mechanism been tested or validated at scale? If so, what lessons or insights can be learned from the experience?

Proof of Stake \(and Proof of Work\) aren’t consensus mechanisms - they are sybil-control mechanisms. They need to be coupled with a protocol such as BFT \(byzantine fault tolerance\) to achieve consensus.

There are different types of Proof of Stake \(PoS\).

* DPoS - Delegated Proof of Stake 
* LPoS - Liquid Proof of Stake 
* Casper FFG \(friendly finality gadget\)

DPoS has inherent flaws as it tends to centralize the system over time \(to what is commonly referred to as a plutocracy\). One such example of this happening is with the EOS blockchain. The EOS system employs the use of DPoS in which stakers vote for 21 ‘block producers’ to secure the network. These block producers are voted in and out by EOS token holders based on a weighted percentage of the total tokens they own. The goal of the system is to have a sort of ‘democratic’ process in which people can use their EOS tokens to vote in “good actors” and vote out “bad actors”. Unfortunately, DPoS suffers from poor distribution of coins and small holder voter apathy, and thus is a honeypot for cartel formation \(and we’ve already seen reports about EOS block producers colluding with each other to ensure incumbency as block producers: https://cointelegraph.com/news/eos-developer-acknowledges-claims-of-collusion-and-mutual-voting-between-nodes\). Additionally, this chain relies heavily on extra-protocol social and political mechanisms to promote "honesty" including an authority generated Constitution and Block Producer Agreement which are not enforceable under any jurisdiction and are instead good faith agreements or hand shake agreements to operate in the best interest of the network.

Ethereums Proof of Stake mechanism \(known by the common name of Casper\) is fundamentally different and intends to maximize decentralization by incentivizing hundreds of thousands of validators to participate in securing the network versus a small subset of voted on delegates.

There are currently multiple projects that employ the Proof of Stake consensus mechanism. Peercoin and NXT are two blockchains in the wild that have utilized Proof of Stake. There have been many lessons learned from these deployments including potential attack vectors, such as the "nothing at stake" problem. Ethereum researchers have taken these lessons learned and incorporated them into their design requirements. For example, Casper Proof of Stake addresses the nothing at stake problem by enforcing a set of pre-defined conditions and rules that if violated by a malicious party will result in the "slashing" of their staked Ether as a penalty. For example, if a validator offers a differing version of the blockchain and history than the blockchain the remaining honest nodes have reached consensus on, that validator is slashed a portion of their staked Ether as a punitive measure. This discourages attacks as their stake ironically becomes something at stake. 

### 10. Relative to a proof of work consensus mechanism does proof of stake have particular vulnerabilities, challenges, or features that make it prone to manipulation? In responding consider, for example, that under a proof of stake consensus mechanism, the chance of validating a block may be proportional to staked wealth.

Ethereum's Casper Proof of Stake will function on the basis of validators, each of which will stake 32 Ether. Users are able to run multiple validators but their computing cost will increase as well \(it should be noted that there is a cost to running a validator in Casper Proof of Stake including the cost of computational resources, the cost of high availability and devops, and the opportunity cost and risk of locking value in the stacking system when that wealth could be used elsewhere\). A validator will be randomly chosen to propose a block and then a committee of users \(at least 111\) will attest that validator acted properly. If so, the block will be validated and the validator rewards. If not, the validator's deposit will be slashed and be lost. If an attacker gained 51% of all Ether they could attempt to attack the network but mechanisms in place make it likely that they will still be slashed. At current Ether price, this attacker would be risking $4,300,000,000 to do so and if caught could lose it all. The cost to aquire 51% of the Bitcoin has rate is much less.

As noted previously Casper Proof of Stake addresses the "nothing at stake" problem suffered by previous Proof of Stake based blockchains by enforcing a set of pre-defined conditions and rules that if violated by a malicious party will result in the "slashing" of their staked Ether as a penalty.

Additionally, Ethereum enjoyed the benefit of initial Proof of Work based distribution versus other Proof of Stake Based Chains. This provides greater guarantees for wealth distribution and preventing a single entity from amassing a disproportionate ammount of Ether which could grant them a supermajority of the stake weight and thus the block validity vote.

### 11. There are reports of disagreements within the Ether community over the proposed transition to a proof of stake consensus model. Could this transition from a proof of work to a proof of stake verification process result in a fragmented or diminished Ether market if the disagreements are not resolved?

The roadmap and community consensus is very clear when it comes to the switch to proof of stake. There are active conversations occuring about the logistics and mechanisms of the proof of stake transition but wanting to stay on proof of work is not something actively discussed. At any point, a user can attempt to fork or stay on the current proof of work chain but the incentive will be very little once proof of stake is live because the users of the network see many positive network effects from the updated proof of stake version of Ethereum. These include: scalability by also enabling sharding which requires the transition to Proof of Stake, a more solidified monetary policy, the ability to work as a validator securing the network and earn by using your stake as collateral for remaining an honest party, and a greater ecosystem of decentralized applicatiosn that can take advantage of both the economic state and scalable state of Ethereum.

It is worth mentioning that Ethereum has only seen one contentious fork in its lifetime following the "DAO hack" and subsequent recovery effort. This was driven partially by a split in the community based on values, which is a natural progression in blockchains /(see Bitcoin Cash, Bitcoin Cash ABC, Bitcoin Cash SV, Bitcoin Diamond, which are all community values driven forks of Bitcoin/). It was also driven by greedy opportunists who seized an opportunity to take advantage of business relationships with exchanges and brand confusion to get the minority fork \(now known as Ethereum Classic\) added to the Poloniex exchange, and subsequently valued in the market, despite the majority of Ethereum participants opting to follow the forked Ethereum chain, that valued the intent of code and practicality over the 'code is law' idealogy.

### 12. What capability does the Ethereum Network have to support the continued development and increasing use of smart contracts?

Ethereum currently supports the most active and largest ecosystem of developers globally. In addition to the core protocol developers and the massive ecosystem of decentralized application developers building and testing on Ethereum, there are currently 8 client teams developing individual client implementations for Ethereum which makes the network more decentralized, robust, and secure. A network with a reliance on a single client implementation becomes a single point of attack or failure \(see CVE-2018-17144, the Bitcoin Core client bug that represented a High risk vulnerability affecting Bitcoin's security and monetary policy, present in 95% of Bitcoin nodes due to the reliance mostly on the single client implementation).

Additionally one only needs to visit sites such as edX or Udemy to view the incredible amount of solidity and vyper smart contracting courses enthusiasts have developed, or to Indeed to see the increasing number of positions related to Ethereum and smart contract development.

## Governance

### 13. How is the governance of the Ethereum Network similar to and different from the governance of the Bitcoin network?

The ethereum governance process, at least in regarsd to software updates and development is similar to Bitcoin's in that it uses a public Github repo to track development from proposal to implementation. In Bitcoin, this is referred to as the Bitcoin Improvement Proposal or BIP process, and in Ethereum it is the EIP process. Where the two differ is in the openness to feature additions, layer 1 improvements, and the way in which those upadtes are discussed, weighed, and proposed. Ethereum seeks to be an inclusive forum for all stakeholders, which would be defined as anyone who believes they would like to contribute to the governance or development of the Ethereum network \(Ether holding not required!). Therefore there are several different layers of governance in Ethereum. Ethereum utilizes rough consensus to gauge the greater community feedback and acceptance of proposals, various tools are also used for signal measurement such as coinvotes, polling, surveys, and general sentiment guaging attempts across a multitude of social media platforms. There is not a central governing body for Ethereum, but rather an approach similar to the IETF in which various forums and working groups have been designed to review, discuss, and guage general community sentiment for each proposal. These forums inform consensus amongst the core developers to inform whether changes should enter the EIP process for technical review, or if further discussions and consensus is needed. Ultimately, these processes are simply to guide development and improvements to the nework, as the decision whether or not to approve or accept the updates and changes lies with the thousands of collective users running nodes on the network. Nodes may choose to run or not to run code they agree or don't agree with. That is the noderunners prerogative as the protocol's rules enforcers. If nodes choose not to update, the chain will continue without the added features or changes and is considered rejected by the community. If the nodes choose to update with no contention then the changes are considered accepted by the community. If the nodes are split by their beliefs and values, two chains may emerge if the differences cannot be reconciled. This is a natural expression of free will and decentralization in blockchains, as the communities are allowed to split and run the coded rules that support their interests. Finally, the market provides the final validation of these changes as the market and its participants will determine the value of each resulting blockchain, and it's associated currency, if any.

### 14. In light of Ether’s origins as an outgrowth from the Ethereum Classic blockchain, are there potential issues that could make Ether’s underlying blockchain vulnerable to future hard forks or splintering?

Ether was not an outgrowth of the Ethereum Classic blockchain. Ether, the cryptocurrency, was born out of the genesis block of the Frontier blockchain, the first iteration of the mainnnet Ethereum blockchain. In March 2016, the Ethereum blockchain hard forked again to add additional features and optimizations to the Homestead chain, the next iteration of the Ethereum blockchain. In July of 2016, following the exploit of a vulnerability smart contract called "The DAO" which resulted in substantial loss of Ether to a hacker, the EThereum blockchain was hard forked again to include an "irregular state transition" that recovered the stolen Ether and returned it to the initial owners \(it should be noted that the history of the blockchain remains 100% in tact and no transactions were censored or removed. Funds were moved via irregular state transtion from the hacked DAO child contracts and remaining DAO child contracts to a recovery contract that users could claim their Ether back from to undo the damages caused by the hacker\). Most in the Ethereum community elected to support the hard forked chain by upgrading their nodes. This chain became the chain we knew under the ticker ETH. A minority elected to remain on the unchanged chain in which the hacker thief retained all of the stolen Ether under the ideological belief in 'code is law.' This chain was expected by the community to disappear over time like the old Frontier chain since only a small minority of nodes were supporting it still, and it had not received support from any exchanges, and thus had no value in the market. In a surprise, Poloniex listed the Ethereum Classic chain \(the minority chain\) and it gained a small share in the greater cryptocurrency market. It has continued on to this day under the ticker ETC building its own support from a small group of likeminded developers and community members operating the network under the ethos of 'code is law.'

As for predicting future hard forks or chain splits, each hard fork carries with it the possibility that the cast off, minority chain gains value in the market if listed by an exchange and raises some support because of it. Blockchains are not insulated or isolated from politics. Bitcoin is inherrently political and relies on social contracts to ensure its system remains unchanged, which is what drove the Bitcoin Cash community away, and subsequently split that community into Bitcoin Cash ABC and Bitcoin SV. It is likely Ethereum may endure another contentious issue that could result in community members opting to go their separate ways by running the code that promotes their interests, but this is not something to be feared. This is the beauty of decentralization and the freedom to choose the rules that support your values, interests, or beliefs best.

## Markets, Oversight and Regulation

### 15. Are there protections or impediments that would prevent market participants or other actors from intentionally disrupting the normal function of the Ethereum Network in an attempt to distort or disrupt the Ether market?

Yes, Ethereum's byzantine fault tolerant consensus prevents against many consensus based attacks such as the well known 51% attack, while Proof of Work and Proof of Stake provide sybil resistance and protection from double spends. Additionally, there is a substantial economic cost to attacking the network in Proof of Work or Proof of Stake. Additionally, smart contract coding principles and standards are growing by the day to ensure better quality, flaw free contracts that operate as intended. Formal verification of contracts is becoming a norm as well as multiple audits before release to production. These measures have already supported a higher level of security and reliability of smart contracts deployed today.

### 16. What impediments or risks exist to the reliable conversion of Ether to legal tender? How do these impediments or risks impact regulatory considerations for Commission registrants with respect to participating in any transactions in Ether, including the ability to obtain or demonstrate possession or control or otherwise hold Ether as collateral or on behalf of customers?

Currently offramps to legal tender from Ether are mostly supported by centralized exchanges such as Coinbase or Gemini. These centralized exchanges present a systemic risk to all cryptocurrencies as they maintain custody of customers cryptocurrencies. These centralized exchanges become a single point of attack or failure, and also lack many of the controls traditional financial institutions managing custody are required to implement. These entities are often unaudited (both for financials and IT Controls), unlicensed, and under-/uninisured. Customers are at significant risk by relying on these central entities to provide custody not only due to the possibility of attacks, but also due to their propensity to act as fractional reserves, making it impossible to determine solvency.

### 17. How would the introduction of derivative contracts on Ether potentially change or modify the incentive structures that underlie a proof of stake consensus model?

Answer:

### 18. Given the evolving nature of the Ether cash markets underlying potential Ether derivative contracts, what are the commercial risk management needs for a derivative contract on Ether?

Answer:

### 19. Please list any potential impacts on Ether and the Ethereum Network that may arise from the listing or trading of derivative contracts on Ether.

Answer:

### 20. Are there any types of trader or intermediary conduct that has occurred in the international Ether derivative markets that raise market risks or challenges and should be monitored closely by trading venues or regulators?

The off-shore exchange BitMex, incorporated in the Seychelles, has engaged in market manipulation through its proprietary trading desk that has direct advantages over customer traders. Additionally, BitMex introduced a perpetual swap product that allows customers to purchase ETHUSD perpetual swap contracts and take long or short positions. Bitcoin Quanto ETH/USD contract has a fixed Bitcoin multiplier regardless of the USD price of ETH. This allows the trader to go long or short the ETH/USD exchange rate without ever touching ETH or USD. This product disproportionately reduces the risk of either a long or short side play. Additionally, BitMex offers unchecked leverage up to 50x on the ETH/USD perpetual swap.

### 21. What other factors could impact the Commission’s ability to properly oversee or monitor trading in derivative contracts on Ether as well as the underlying Ether cash markets?

Privacy is one of the core features being worked on by multiple teams. The technology is expected to have profound effects on both the privacy of Ethereum and the scalability of the network.

Privacy technology on Ethereum already has working implementations being deployed to the Ethereum main network \([https://medium.com/aztec-protocol/confidential-transactions-have-arrived-a-dive-into-the-aztec-protocol-a1794c00c009](https://medium.com/aztec-protocol/confidential-transactions-have-arrived-a-dive-into-the-aztec-protocol-a1794c00c009)\).

This privacy technology may impede the Commission's ability to monitor, audit or oversee trading activity in the future.

### 22. Are there any emerging best practices for monitoring the Ethereum Network and public blockchains more broadly?

Due to the transparency of blockchains, there are multiple services that provide monitoring, visualization and analytical tools for Ethereum and related applications that are built on top.

* [https://aleth.io/](https://aleth.io/)
* [https://etherscan.io/](https://etherscan.io/)
* [https://www.kaggle.com/bigquery/ethereum-blockchain](https://www.kaggle.com/bigquery/ethereum-blockchain)
* [https://observeth.net/main](https://observeth.net/main)
* [https://www.ethtective.com/](https://www.ethtective.com/)
* [https://mkr.tools](https://mkr.tools)

## Cyber Security and Custody

### 23. Are there security issues peculiar to the Ethereum Network or Ethereum- supported smart contracts that need to be addressed?

Smart contracts, like any piece of code, suffer from the possibility of having vulnerabilities or bugs. The security of smart contracts is paramount because they tend to interact with different financial apps and handle value transfer \(such as the transfer of ETH or tokens\)

Independent auditing and smart contract security firms exist such as Zeppelin or Trail of Bits. These firms provide contract auditing and fuzzing services. Additionally, formal verification services have emerged to formally verify smart contract code. Runtime Verification is one of the leading providers of these services for Ethereum smart contracts.

### 24. Are there any best practices for the construction and security of Ethereum wallets, including, but not limited to, the number of keys required to sign a transaction and how access to the keys should be segregated?

Best practices exist in the ecosystem for building wallets and writing smart contracts.

[https://consensys.github.io/smart-contract-best-practices/](https://consensys.github.io/smart-contract-best-practices/)

Additional standards and best practices, inclding token standards such as ERC-20 or ERC-721 are located within the Ethereum Github Repository located at https://github.com/ethereum/EIPs

### 25. Are there any best practices for conducting an independent audit of Ether deposits?

Many firms conducting audits utilize tools or forensics services such as Chainalysis to audit and provide track and trace for transactions from deposit/source to destination. Transactions may be independently audited by any party with a simple block explorer synced to the Ethereum main net, such as https://etherscan.io. Additionally, private sector CPA firms including PwC, Deloitte, EY, and Accenture now provide full service forensics for cryptocurencies and blockchains.
