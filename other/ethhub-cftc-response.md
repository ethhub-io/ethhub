# EthHub CFTC Response

On December 11th, 2018 the CFTC [submitted a public "Request for Input"](https://www.cftc.gov/sites/default/files/2018-12/federalregister121118.pdf) which asks for clarity and answers around Ethereum. The following is a list of all questions asked in the RFI. The following answers were developed on EthHub, an open source, community run information hub for the Ethereum community.

_**From the CFTC: In providing your responses, please be as specific as possible, and offer concrete examples where appropriate. Please provide any relevant data to support your answers where appropriate. The Commission encourages all relevant comments on related items or issues; commenters need not address every question.**_

## Purpose and Functionality

### 1. What was the impetus for developing Ether and the Ethereum Network, especially relative to Bitcoin?

It's first vitally important to distinguish between Ether and Ethereum. Ethereum is an open-source, blockchain-based computing system. Leveraging smart contract \(scripting\) technology, anyone is able to build and deploy decentralized applications on top of Ethereum. This is very attractive for development because you are able to create programs that run exactly as programmed, trustlessly and with no down time.

Ether is the fundamental cryptocurrency used on the Ethereum network. It is used to compensate miners for performing transactions on the network. Ether also has many other use cases such as money, store of value and value transfer.

### 2. What are the current functionalities and capabilities of Ether and the Ethereum Network as compared to the functionalities and capabilities of Bitcoin?

Bitcoin and Ethereum are currently both secured by a Proof of Work blockchain. However, the core difference is that Ethereum has smart contract functionality that allows for the development and deployment of decentralized applications.

The functionality of the underlying asset Ether is actually very similar to Bitcoin.

### 3. How is the developer community currently utilizing the Ethereum Network? More specifically, what are prominent use cases or examples that demonstrate the functionalities and capabilities of the Ethereum Network?

The simplest use case of the Ethereum network is value transfer by sending Ether \(which has an attached value\) from one person to another. However, the amount of applications being built on top of the program is growing at a rapid pace. Currently, the most active applications are those related to "Decentralized Finance". As of 12/11/18, there is currently $120,000,000 worth of Ether being used in Decentralized Finance applications.

### 4. Are there any existing or developing commercial enterprises that are using Ether to power economic transactions? If so, how is Ether recorded for accounting purposes in a comprehensive set of financial statements?

The Enterprise Ethereum Alliance is a large group of commercial enterprises decidated to building out standards for Enterprise Ethereum.

### 5. What data sources, analyses, calculations, variables, or other factors could be used to determine Ether’s market size, liquidity, trade volume, types of traders, ownership concentration, and/or principal ways in which the Ethereum Network is currently being used by market participants?

Answer:

### 6. How many confirmations on the Ethereum blockchain are sufficient to wait to ensure that the transaction will not end up on an invalid block?

A user must only wait 1 block confirmation for their transaction to be valid. There is a risk of hash power related attacks to the network and this risk goes down every confirmation that occurs. Some merchants may wait a pre-selected amount of confirmations \(such as 6\) in order to avoid this risk.

## Technology

### 7. How is the technology underlying Ethereum similar to and different from the technology underlying Bitcoin?

From a high level, Ethereum is similar to Bitcoin in that it uses a 'blockchain' and uses 'Proof of Work' to achieve consensus and secure the network. Both blockchains have a native digital asset - ETH for Ethereum and BTC for Bitcoin.

The Ethereum network is a turing-complete blockchain. This means that it is capable of executing arbitrary code - known as smart contracts. The ability to run code on the Ethereum blockchain means that developers can build applications on top of it. One such application, MakerDAO, allows users to use their ETH as collateral to take out a loan in a USD-pegged stablecoin \(known as DAI\). Applications are all interoperable within the confines of the Ethereum network.

Ethereum 2.0 \(Serenity\) is a substantial upgrade for the Ethereum network being deployed in multiple phases. The main features in this upgrade include a move to Proof of Stake \(for securing the network\), sharding \(for scaling the network\) and eWASM \(a new virtual machine for the network\).

### 8. Does the Ethereum Network face scalability challenges? If so, please describe such challenges and any potential solutions. What analyses or data sources could be used to assess concerns regarding the scalability of the underlying Ethereum Network, and in particular, concerns about the network’s ability to support the growth and adoption of additional smart contracts?

The Ethereum Network faces scalability problems similar to Bitcoin and other blockchains.

It's important to understand the basics of how the Ethereum blockchain functions before diving into scaling. Every transaction cost a certain amount of "gas" which is the cost, in computational power, to execute a transaction. Every block processed on the network has a cap on the amount of gas it can hold. This is because if blocks get too large, there are issues with storage and network latency. Currently, the Ethereum network sits at max capacity in terms of gas used every day.

This is how Ethereum plans to tackle the scalability issue:

'Layer 1' refers to the main Ethereum network/blockchain. 'Layer 2' refers to technologies built on top \(or above\) of the main Ethereum network/blockchain. 'Interoperability' refers to the use of other blockchains.

Ethereum is tackling layer 1 scalability challenges by introducing a mechanism borrowed from traditional databases - 'sharding'. Sharding takes the blockchain and splits it up into multiple blockchains \(that can communicate with eachother\) so that transactions and computations can be processed in parallel.

Ethereum is tackling layer 2 scalability challenges through the use of multiple different technologies. These technologies include sidechains \(such as Plasma\), state channels, and interoperability.

### 9. Has a proof of stake consensus mechanism been tested or validated at scale? If so, what lessons or insights can be learned from the experience?

Proof of Stake \(and Proof of Work\) aren’t consensus mechanisms - they are sybil-control mechanisms. They need to be coupled with a protocol such as BFT \(byzantine fault tolerance\) to achieve consensus.

There are different types of Proof of Stake \(PoS\).

DPoS - Delegated Proof of Stake LPoS - Liquid Proof of Stake Casper FFG \(friendly finality gadget\). DPOS is widely varied when used by different projects, the largest example of DPOS is used in the EOS blockchain, but active community members have voiced their concern over its decentralization factor. 

DPoS has inherent flaws as it tends to centralize the system over time \(what is commonly referred to as “cartels”\). 

There are currently multiple projects that employ the Proof of Stake consensus mechanism.

Ethereums Proof of Stake mechanism \(codenamed Casper FFG and Casper CBC\) is fundamentally different and intends to maximize decentralization by requiring 100’s of thousands of validators to secure the network.

### 10. Relative to a proof of work consensus mechanism does proof of stake have particular vulnerabilities, challenges, or features that make it prone to manipulation? In responding consider, for example, that under a proof of stake consensus mechanism, the chance of validating a block may be proportional to staked wealth.

Ethereum Proof of Stake will function on the basis of validators, each of which will stake 32 Ether. Users are able to run multiple validators but their computing cost will increase as well. A validator will be randomly chosen to propose a block and then a committee of users \(at least 111\) will vote to say if that validator acted properly. If so, the block will be validated and the validator rewards. If not, the validator's deposit will be slashed and be lost. If an attacker gained 51% of all Ether they could attempt to attack the network but mechanisms in place make it likely that they will still be slashed. At current Ether price, this attacker would be risking $4,300,000,000 to do so and if caught could lose it all. The cost to aquire 51% of the Bitcoin has rate is much less.

### 11. There are reports of disagreements within the Ether community over the proposed transition to a proof of stake consensus model. Could this transition from a proof of work to a proof of stake verification process result in a fragmented or diminished Ether market if the disagreements are not resolved?

The roadmap and community consensus is very clear when it comes to wanting to switch to proof of stake. There are active conversations occuring about the logistics and mechanisms of the proof of stake transition but wanting to stay on proof of work is not something actively discussed. At any point, a user can attempt to fork or stay on the current proof of work chain but the incentive will be very little once proof of stake is live because the users of the network gain many benefits from Eth 2.0 chain which will include proof of stake. These include: scalability, lower issuance rate, ETH holders being able to stake and earn rewards and all development power focused on the new chain.

Anyone can choose to fork the Ethereum network during the upgrade, but the chance of a competing blockchain that has removed the newest PoS upgrade, is very slim. As the upgrade is a massive improve on scaliblity, the forked chain would be subpar and therefore not have much market traction. 

### 12. What capability does the Ethereum Network have to support the continued development and increasing use of smart contracts?

Answer: The Ethereum foundation and the multiple of projects working to support and improve the Ethereum ecosystem provides a global support network of developers and cash flow. The Ethereum foundation has multiple years of runway according to Joesph Lubin, CEO of Consensys. 

This question is similar to asking - What capability does Microsoft have to support the continued development of applications on the Windows Operating System. 

## Governance

### 13. How is the governance of the Ethereum Network similar to and different from the governance of the Bitcoin network?



### 14. In light of Ether’s origins as an outgrowth from the Ethereum Classic blockchain, are there potential issues that could make Ether’s underlying blockchain vulnerable to future hard forks or splintering?



## Markets, Oversight and Regulation

### 15. Are there protections or impediments that would prevent market participants or other actors from intentionally disrupting the normal function of the Ethereum Network in an attempt to distort or disrupt the Ether market?

Answer:

### 16. What impediments or risks exist to the reliable conversion of Ether to legal tender? How do these impediments or risks impact regulatory considerations for Commission registrants with respect to participating in any transactions in Ether, including the ability to obtain or demonstrate possession or control or otherwise hold Ether as collateral or on behalf of customers?

Answer: (needs review) Potential risk of spam attacks that prevent the timely sending or recieving of Ether. 
See paper: Paavolainen, S., Elo, T., & Nikander, P. (Accepted/In press). Risks from Spam Attacks on Blockchains for Internet-of-Things Devices. In 2018 IEEE 9th Annual Information Technology, Electronics and Mobile Communication Conference (IEMCON) International: IEEE.

### 17. How would the introduction of derivative contracts on Ether potentially change or modify the incentive structures that underlie a proof of stake consensus model?

Answer:

### 18. Given the evolving nature of the Ether cash markets underlying potential Ether derivative contracts, what are the commercial risk management needs for a derivative contract on Ether?

Answer:

### 19. Please list any potential impacts on Ether and the Ethereum Network that may arise from the listing or trading of derivative contracts on Ether.

Answer:

### 20. Are there any types of trader or intermediary conduct that has occurred in the international Ether derivative markets that raise market risks or challenges and should be monitored closely by trading venues or regulators?

Answer:

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

Independent auditing and smart contract security firms exist such as Zeppelin or Trail of Bits.

### 24. Are there any best practices for the construction and security of Ethereum wallets, including, but not limited to, the number of keys required to sign a transaction and how access to the keys should be segregated?

Best practices exist in the ecosystem for building wallets and writing smart contracts.

[https://consensys.github.io/smart-contract-best-practices/](https://consensys.github.io/smart-contract-best-practices/)

### 25. Are there any best practices for conducting an independent audit of Ether deposits?

Ether deposits are upheld by the security of the Proof of Work system within the Ethereum blockchain. Where very similarily to how the bitcoin blockchain works - the underlaying functionality of the Ethereum blockchain is simply transferring balances from one account to the next. As such, whenever a user sends/deposits ether from one wallet into another, the PoW blockchain is what secures that this balance has been securely transferred and accounted for within the ledger. 

Everytime a block is confirmed, the statisitcal chance of that transaction being invalid are reduced exponentally. Refer to answer #6.

