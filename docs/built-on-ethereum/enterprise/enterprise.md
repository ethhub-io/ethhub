# Enterprise

**What Ethereum offers to Enterprises**

Ethereum offers tools which empower developers to build collaboratively and confidently. These tools enables businesses to create, test, and deploy  enterprise-grade blockchain solutions in a matter of minutes. Some of them are:

* Blockchain for business platforms: [Kaleido](https://kaleido.io/), [Quorum](https://www.jpmorgan.com/global/Quorum), [Pantheon](https://pegasys.tech/)
* Infrastructure and Ethereum API access: [Infura](https://infura.io/)
* Wallet and identity platforms: [MetaMask](https://metamask.io/) and [uPort](https://www.uport.me/)
* Developer tools, frameworks and testnets: [Truffle](https://truffleframework.com/) and [Rinkeby](https://www.rinkeby.io/)
* Training resources: [ConsenSys Academy](https://consensys.net/academy/)

For management and ongoing maintenance of Enterprise Ethereum solutions: Established support providers such as [ConsenSys Solutions](http://consensys.net/solutions/) and top-tier IT consulting firms exist in every market across the globe.<br/>
Ethereum's architectural specifications effectively satisfy enterprise-grade requirements for privacy, security, performance, scalability, and interoperability.
To read [more](https://consensys.net/enterprise-ethereum/best-blockchain-for-business/)

**Enterprise Ethereum Alliance (EEA)**

Industry leaders are now realizing the true potential of blockchain and ethereum. EEA is a member-driven standards organization whose charter is to develop open blockchain specifications that drive harmonization and interoperability for businesses and consumers worldwide.

EEA has more than 200 members now with big names like microsoft, JPM etc. Many of the EEA members are going through and researching into ethereum to support to fit it into their use case. You can see the list of all the members [here](https://entethalliance.org/members/).

Below is the list of some of the EEA members and organizations who are using, building enterprise based solutions. 

## JPM

### Summary
JPM is working on blockchain solutions for business. It launched **Quorum**, an open source blockchain platform that combines the innovation of the public Ethereum community with enhancements to support enterprise needs. Quorum help alleviate major banking issues such as settlement times, risk exposure, and system breakdowns. Since it is a permissioned network, no need for POW/POS and instead it has it's own alternative consensus mechanisms which in turn gives higher perfomance due to faster blocktimes, transaction finality, and on-demand block creation.<br/>

JPM is also working on their own coin (**JPM Coin**), built on quorum that enables the instantaneous transfer of payments between institutional accounts.

Besides quorum, JPM has developed a privacy feature for ethereum-based blockchains, obscuring not only how much money is being sent but who is sending it.
It is an extension to the **Zether protocol** which not only conceals the account balances and the transfer amounts but the sender may also hide herself and the 
transactions recipients in a larger group of parties.

### Resources

* https://www.goquorum.com/
* https://github.com/jpmorganchase/quorum
* https://github.com/jpmorganchase/anonymous-zether

## Microsoft

### Summary
Microsoft along with Enterprise Ethereum Allaince (EEA) launched a token-building-kit to help businesses design and create the right sort of crypto tokens for their particular needs. According to microsoft, "a business person can create a token visually using a design tool that does not involve writing any code whatsoever, and allows them to then say to developers, 'I want one of these.'"

Recently they also released a suite of tools allowing clients to build ethereum-based apps on its cloud computing platform Azure. The new Azure Blockchain Development Kit for Ethereum will help developers create and deploy ethereum-based apps on Azure Blockchain Service or the ethereum blockchain. It was released as an extension of it's very powerful Visual Studio Code.

Microsoft is also working with starbucks to harness this Azure Blockchain Service in tracking coffee shipments from across the world, bringing "digital, 
real-time traceability" to its supply chains.


### Resources

* https://docs.microsoft.com/en-us/azure/blockchain/workbench/
* https://news.microsoft.com/transform/starbucks-turns-to-technology-to-brew-up-a-more-personal-connection-with-its-customers/


## Ernest and Young (EY)

### Summary
EY is rolling out free software designed to help corporate clients use the ethereum blockchain. Recently they announced a protocol, internally code-named **Nightfall**, which has been developed over the last year by a team of over 200 blockchain developers. The protocol is created for such use cases as supply chains, food tracing, transactions between branches of a company and public finance. It takes advantage of Zero Knowledge Proofs to allow private txs on a shared ledger.

Unlike other enterprise blockchain platforms, Nightfall is supposed to run on top of public ethereum network not private. EY has already released the code with no permissive copyright license. 

### Resources

* https://github.com/EYBlockchain/nightfall
* https://www.ey.com/en_gl/blockchain


## Deloitte

### Summary
Deloitte has a dedicated team (EMEA blockchain lab) exploring blockchain capabilities. Recently it partenered with Institute of Banking (IoB), Bank of Ireland, AIB and Ulster Bank to develop an Ethereum-based tool which facilitate wide range of staff-related data management processes. It is currently in beta test mode and a full rollout can be expected by summer 2020.

The new platform is a first in the European financial services industry and will support the verification, tracking, direct access to, and management of, regulatory and other professional designations, education qualifications and lifelong learning credentials.

### Resources

* https://cointelegraph.com/news/deloitte-completes-joint-pilot-digitizing-supply-chain-management-on-multiple-dlts
* https://www2.deloitte.com/ca/en/pages/technology/solutions/deloitte-digital-blockchain.html

## MetLife

### Summary
MetLife is utilizing the live public Ethereum blockchain to add transparency and efficiency to the life insurance claims process. MetLife's Singapore-based incubator LumenLab is collaborating with Singapore Press Holdings (SPH) and NTUC Income (Income) on a platform of smart contracts known as **Lifechain** to help loved ones quickly determine if the deceased was protected with a policy and automatically file a claim. This move by metlife can destroy the life insurance industry worth $ 2.7trillion.

If a family choose to participate, Lifechain will encrypt the deceased's National Registration Identity Card (NRIC) number (which is included in the Death Certificate) using a hashing algorithm and place it onto the blockchain. This will trigger a search on NTUC’s end for a matching life insurance policy. If a match is found, "SPH will inform family members within one working day, while 'Lifechain' will send an automatic notification to Income via email to initiate the claims process." 

This is not MetLife's first experimentation with blockchain. In fact, the core smart contract platform that constitutes Lifechain is very closely related to what was built for the company’s first successful pilot, a mobile app called **Vitana**, that utilized Ethereum to pay out claims to expectant mothers who contracted gestational diabetes.

### Resources

* http://www.vitana.sg/
* https://www.forbes.com/sites/stevenehrlich/2019/06/19/metlife-plans-to-disrupt-2-7-trillion-life-insurance-industry-using-ethereum-blockchain/#205ac2fb2770


## Google

### Summary
Google announced a parternship with **Chainlink** to build hybrid blockchain/cloud applications utilizing the Ethereum blockchain. The blog posted by Google describes that the team is working on applications of making internet-hosted data available inside an immutable public blockchain: placing BigQuery data available on-chain using a Chainlink oracle smart contract.

BigQuery allows large swathes of data from multiple blockchains to be correlated and analyzed. The datasets have been used to develop processes such as profit sharing, characterizing network participants, and detecting software vulnerabilities and malware.

Chainlink will act as the "middleware" between smart contracts and Google's real-world data, and provide a secure on and off ramp for the outside information they need. At a high level, Ethereum Dapps request data from Chainlink, which in turn retrieves data from a web service built with Google App Engine and BigQuery.

Chainlink partenering with google opens up the gate for innumerable applications. 

### Resources

* https://cloud.google.com/blog/products/data-analytics/building-hybrid-blockchain-cloud-applications-with-ethereum-and-google-cloud

## AXA

### Summary
AXA, the insurance giant and the world’s second biggest financial company has launched an insurance product that utilizes smart contracts on ethereum's public blockchain called **Fizzy**.

When you buy flight delay insurance on the fizzy platform, purchase is recorded on ethereum blockchain, making the insurance contract equally tamperproof. This smart contract is connected to global air traffic databases, so as soon as a delay of more than two hours is observed, compensation is triggered automatically. 

In this way, AXA has delegated the compensation decision to an independent network.

### Resources

* https://fizzy.axa/en-gb/
* https://www.axa.com/en/newsroom/news/axa-goes-blockchain-with-fizzy


## Fnality International

### Summary
Fnality (Formerly known as Utility Settlement Coin (USC)), the newly rechristened U.K.-based project is developing blockchain versions of five major fiat currencies: the U.S. dollar, the Canadian dollar, the British pound, the Japanese yen and the euro. It has $63.2 million in fresh funding from 14 banks. Fnality's tech partner, Clearmatics, is building these systems on a private version of ethereum called **Autonity**. 

Fnality's complex roadmap will see things begin to come to fruition in 2020. Aside from UBS and Barclays, its shareholders include Banco Santander, BNY Mellon, CIBC, Commerzbank, Credit Suisse, ING, KBC Group, Lloyds Banking Group, MUFG Bank, Nasdaq, Sumitomo Mitsui Banking Corporation, and State Street.

### Resources

* https://www.coindesk.com/fnality-utility-settlement-coin-central-bank-token-blockchain
* https://www.clearmatics.com/about/


## Hyperledger

### Summary
Hyperledger is an umbrella organization – cast in the image of the Linux Foundation – for open source blockchain development, comprising a number of protocols designed specifically for enterprises.<br/>

Hyperledger has many projects backed by big organizations such as 'Fabric' backed by **IBM** and 'Sawtooth' backed by **Intel Corporation**. Both Intel and IBM worked on these projects first and then presented them to hyperledger for acceptance into the Incubator. That resulted into these projects growing at a tremendous rate and now are among the top frameworks for enterprise blockchain networks. Fabric supports EVM based smart contracts, it also has a web3 provider which can be used to develop dApps using web3.js.

Sawtooth also supports Ethereum through **Seth**, Sawtooth's Ethereum-compatible Transaction Processor. It implements a Ethereum Virtual Machine (EVM) so Seth can run Ethereum Dapps written in Solidity.

### Resources

* https://www.hyperledger.org/blog/2018/10/26/hyperledger-fabric-now-supports-ethereum
* https://www.hyperledger.org/blog/2017/08/22/hello-world-meet-seth-sawtooth-ethereum
* https://sawtooth.hyperledger.org/docs/seth/releases/latest/introduction.html
* https://hyperledger-fabric.readthedocs.io/en/release-1.4/


## Axoni

### Summary
Axoni announced **AxLang**, a new programming language that supports functional programming and enables formal verification of smart contracts for Ethereum-compatible networks.

Solidity has some limitations such as inability to use techniques like formal verification to prove the correctness of smart contract code prior to deploying the contracts on the live network. AxLang goal is to maximize security while enabling broad adoption as much as possible. It is designed to support both public Ethereum as well as private Ethereum projects.

### Resources

* https://medium.com/axoni/axlang-formally-verifiable-smart-contracts-for-the-ethereum-ecosystem-6201203be4e8
* https://axoni.com/axlang/


## Depository Trust & Clearing Corporation (DTCC)

### Summary
DTCC records for most of the world’s securities, representing some $48 trillion in assets—from stocks and bonds to mutual funds and derivatives. In a few months DTCC will begin the largest live implementation of blockchain. Records for about 50,000 accounts in DTCC’s Trade Information Warehouse, where information on $10 trillion worth of credit derivatives is stored, will move to a customised digital ledger called **AxCore**. 

AxCore protocol is originally derived from the public ethereum blockchain, and the DTCC’s system uses the same Solidity smart contract language that powers its applications. However, AxCore has been modified to include a modular consensus mechanism that lets it tailor services to the specific needs of the DTCC, as well as submit real-time reports to both regulators and other counterparties.

And, unlike ethereum, the DTCC implementation of AxCore does not include a token – though both Axoni and Palatnick (DTCC’s chief technology architect) confirmed the system is still powered by a form of "gas," implying a parallel to the way transaction fees are paid on the ethereum blockchain.


### Resources

* http://www.forbesindia.com/article/cross-border/blockchain-goes-to-work/53903/1
* https://www.coindesk.com/dtcc-milestone-11-trillion-derivatives-gets-closer-blockchain
* http://www.dtcc.com/blockchain


## Foxconn

### Summary
Foxconn – best known for manufacturing Apple’s iPhone launched a Shanghai startup called **Chained Finance** with a Chinese peer-to-peer lender. Chained will soon connect Foxconn and its many small suppliers (and their suppliers' suppliers) on an Ethereum-based blockchain that will use its own token and smart contracts to make payments and provide financing in near real time, eliminating a daisy chain of paperwork. 

### Resources

* https://www.coindesk.com/foxconn-wants-take-global-supply-chain-blockchain
* http://www.forbesindia.com/article/cross-border/blockchain-goes-to-work/53903/1


## Kaleido

### Summary
The Kaleido Blockchain Business Cloud is the full-stack platform for building and running cross-cloud, hybrid enterprise ecosystems.
It brings the dramatic simplicity of SaaS combined with the performance, security, global reach and cloud scale in an enterprise platform that goes way beyond today’s quick start scripts and templates and other Blockchain-as-a-Service offerings.

Kaleido has deep partnerships with industry leaders like ConsenSys, Microsoft Azure, Amazon Web Services and more to bring you enterprise blockchain’s easy button for your modern business network.

Kaleido provides services such as:
* **B2B**: [App2App Messaging](https://marketplace.kaleido.io/service/app2app-messaging)
* **Blockchain First**: [Token Explorer](https://marketplace.kaleido.io/service/token-explorer), [Token Swap](https://marketplace.kaleido.io/service/token-swap), [On-Chain Registry](https://marketplace.kaleido.io/service/identity-registry), [EthFirewall](https://marketplace.kaleido.io/service/ethfirewall)
* **Middleware**: [Event Streams](https://marketplace.kaleido.io/service/event-streams-and-data-sync), [REST API Gateway](https://marketplace.kaleido.io/service/rest-api-gateway)


### Resources

* https://kaleido.io/
* https://marketplace.kaleido.io/


## Pegasys

### Summary
PegaSys (Protocol Engineering Groups and Systems) is a 50-person team dedicated to enterprise grade blockchain at ConsenSys. It is building Ethereum tech for the public-chain community and leading enterprises focused on privacy, permissioning, scalability, and other features to make Ethereum production-ready.

Pegasys develop open-source software, and are researching next-generation solutions like sidechains and sharding.

Some of the great solutions developed by pegasys are:
* **Pantheon**: An Apache 2.0 licensed Ethereum client written in Java. Pantheon is public chain compatible, with a more modular architecture and roadmap to add privacy, permissioning, and new consensus algorithms.
* **Hobbits (In progress)**: Hobbits is a lightweight wire protocol for ETH 2.0 network testing purposes.

### Resources

* https://pegasys.tech/
* https://pegasys.tech/solutions/
* https://github.com/deltap2p/hobbits


## Enterprise Ethereum Projects

**Project i2i: Blockchain Payments in the Philippines**

_Problem Statement_

The Philippines is a rapidly emerging economy with a population of over 100 million. However, two-thirds of the population remains unbanked. 70 million Filipinos have severely limited access to both the domestic and global financial ecosystems. This poses a significant problem when up to 10% of the Philippines' GDP is made up of international remittances sent from overseas workers to family members across the country. 

_Solution_

UnionBank of the Philippines, one of the largest banking institutions in the country, sought to tackle this challenge by partnering with ConsenSys Solutions, Kaleido, Amazon AWS, ConsenSys Diligence, Microsoft Azure, and seven rural Philippine banks to create an inter-rural bank payment platform using Enterprise Ethereum. <br/>

Project i2i implemented Enterprise Ethereum to create a decentralized, cost-efficient, real-time inter-rural bank payment platform that operates autonomously outside of existing payment infrastructures and intermediaries such as the Philippines' PhilPass and SWIFT. The Project i2i platform works to connect rural banks as well as national commercial banks to the central bank, helping remote banks integrate with the domestic financial system while also improving banking access for local citizens.

The commercial launch of the i2i platform is scheduled for 2019, in partnership with 130 rural banks. Project i2i has received clearance and support from the central bank of the Philippines to operate as the country's first Ethereum-based payment network for domestic funds transfers. UnionBank and ConsenSys Solutions are now working toward expanding the platform to include international funds transfer.

Case study can be downloaded from [here](https://consensys.net/enterprise-ethereum/use-cases/banking-and-finance/project-i2i/)

**Project Khokha: Blockchain for Central Banking in South Africa**

_Problem Statement_

Central banks need an innovative way to increase the resiliency of interbank payment systems while maintaining or reducing the overall cost of those systems. SARB created a simulation to assess if the performance, scale, and confidentiality of payments were possible utilizing blockchain technology.

_Solution_

In consortium with seven commercial banks, SARB partnered with ConsenSys Solutions and Adhara, to build a proof-of-concept grounded in real-world performance, confidentiality requirements, and diverse bank hardware on the blockchain—without a single point of failure. By harnessing a permissioned blockchain network, the Istanbul Byzantine Fault Tolerance consensus mechanism, Pedersen commitments, and range proofs, Project Khoka was able to replicate interbank clearing and 
settlements in less than two hours.<br/>

The project achieved the transaction performance target at 70,000 transactions in less than two hours, privacy while meeting required transaction volumes.

Project Khokha was recognized by the Central Bank Publication as the "Best Distributed Ledger Initiative" of 2018.

Case study can be downloaded from [here](https://consensys.net/enterprise-ethereum/use-cases/banking-and-finance/project-khokha/)

**Project Ubin: Blockchain for Banking in Singapore**

_Problem Statement_

Singaporean financial institutions are recognized for their efficiency. Their public policy is exported as a blueprint for other central systems around the world. Recently, the Monetary Authority of Singapore (MAS) began exploring the potentials of distributed ledger technology in regards to finance and banking applications.

_Solution_

MAS launched a three-phase exercise in partnership with a consortium of international banks, distributed ledger technologies, and blockchain providers.

Phase 1 consisted of a research and feasibility study around the potential applications of blockchain technology.

The study explored:

* Benefits and pitfalls of tokenizing central bank currency
* Optimizing payment settlements between participating local banks
* Steps to enable cross-border transactions
* Effective methods of digitizing payments

Phase 2 focused on how to use blockchain platforms and tokenization in the daily settlement and clearing process to enable RTGS. During this phase, MAS partnered with ConsenSys Solutions and JP Morgan's Quorum enterprise blockchain platform. Together, they successfully demonstrated how a tokenized Singaporean dollar could function as a means of daily inter-bank settlement.

Phase 3 explored the potentials of a tokenized national currency and realizing cross-border payments through blockchain technology.

Project Ubin's results prove that inter-bank transactions, cross-border remittances, and tokenized securities can be settled with distributed ledger technology with full settlement finality and transaction privacy.

Case study can be downloaded from [here](https://consensys.net/enterprise-ethereum/use-cases/banking-and-finance/project-ubin/)
