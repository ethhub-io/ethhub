title: Plasma - EthHub

description: Plasma a layer 2 scaling solution for Ethereum.

# Plasma

## What is Plasma?

Plasma is a layer-2 scaling solution that was originally proposed by Joseph Poon and Vitalik Buterin in their paper [Plasma: Scalable Autonomous Smart Contracts](https://plasma.io/plasma.pdf). It is a framework for building scalable applications.

Plasma uses a combination of smart contracts and cryptographic verification. Together, these enable fast and cheap transactions by offloading these transactions from the main Ethereum blockchain into a "side" chain (sometimes referred as child or plasma chains). These side chains periodically report back to the main chain and use it to settle any disputes (almost like a higher court).

**Why it is needed**

According to Vitalik Buterin,<br/> 
*it is a "bad idea" to build sophisticated features into the base layer of the blockchain, it would create a high level of governance overhead as the platform would have to continually discuss, implement and coordinate newly discovered technical improvements. The time intensive task to add a new feature into the base protocol might cause Ethereum to stagnate. We should not only be relying on changes to the base protocol to continue progressing Ethereum. I do think that as blockchains become more and more mature, layer 1 will necessarily stabilize, and layer 2 will take on more and more of the burden of ongoing innovation and change.*

## How does Plasma work?

The Plasma structure is built through the use of smart contracts and Merkle trees, enabling the creation of an unlimited number of child chains - which are, essentially, smaller copies of the parent Ethereum blockchain. Each chain is designed to work in a singular way, serving different needs by coexisting and operating independently. On top of each child chain, more chains can be created and this is what builds a tree-like structure.

Deposits and withdrawals of Plasma chain funds with state transitions is enabled by fraud proofs. This ensures enforceable state and exchangeability. It also allows the processing of a greater number of transactions with less data loading on the basic platform. Any user can send funds to another, including those from a different set of participants. These fund transfers can be paid and withdrawn in the native platform coin.

### Fraud Proofs

The communication between the child chains and the root chain is secured by fraud proofs. Each child chain has its own mechanisms for validating blocks and a particular fraud-proof implementation, which can be built on top of different consensus algorithms. The most common are Proof of Work, Proof of Stake, and Proof of Authority.

The fraud proofs ensure that in case of malicious activity, users are able to report dishonest nodes, protect their funds and exit the transaction (which involves an interaction with the main chain). In other words, fraud proofs are used as a mechanism through which a Plasma child chain files a complaint to its parent chain or to the root chain.

These proofs use an interactive funds-withdrawal protocol. In order to withdraw a certain amount of funds, an exit time is needed. The exiting party must confirm the outputs via UTXO model requesting a withdrawal. Network participants can then submit a bonded proof that has to be confirmed and tested if any funds have been spent. If the event appears to be wrong, it is treated as fraudulent, and the confirmation is cancelled. With time, another bonded round allows the withdrawal to happen, bonding to state before a committed timestamp. An incorrect Plasma chain can be quickly exited by participants. In case of attack, participants can quickly exit and save their costs, ensuring security within the system.

**Example**

If Alice keeps 1 ETH in a Plasma chain, for instance, it gets recorded into a block, whereas the consensus is met due to fraud proofs. Further commitments are enforced and submitted on the base chain, and her funds are held in its smart contract:

![](https://i.imgur.com/RLsoIkv.jpg)

![](https://i.imgur.com/NbvA4eM.jpg)

## Plasma: Pros and Cons
Undoubtedly, plasma is a good solution for scalability issues but Plasma does have some drawbacks. Each new plasma iteration reveals a new research problem that needs to be addressed, leading to multiple Plasma variants that navigate deployment trade-offs in different ways. We will compare these different variants in detail below but let's first compare the pros and cons of plasma and it's variants.

| Pros | Cons |
| :--- | :--- |
| Plasma will help the Ethereum blockchain scale by taking operations off-chain | Plasma requires a centralized component in order to operate as the off-chain component is managed by authorities |
| Lower fees and faster operations also enables computationally intensive applications to run on a blockchain | Long waiting periods(7-14 days) for users who wish to withdraw their funds |
| Eliminating significant amount of unnecessary data in the main chain which also reduces the processing bandwidth of nodes | Poor experience for users who don’t have a large number of assets and don’t want to wait weeks to access them |
| It is compatible with various on-chain scaling solutions such as sharding, varying block sizes, etc. | New security risks/challenges (primarly for exits) that would need to be addressed to maintain immutability. |

Many plasma variants have their own set of drawbacks such as:
* Plasma MVP has time constraints, is a less than ideal user experience, and is vulnerable to network congestion.
* Plasma Cash relies on non-fungible tokens (NFTs) to function which requires heavy transaction histories. You will have to keep track of the value and have to be constantly collecting proofs of non-inclusion, and so when you transfer ownership of the NFT you have to transfer its history as well.

## Exploring popular plasma flavours

There isn’t any single project called "Plasma". Instead, there are lots of different projects that use the tools provided by the Plasma framework/specification.

Currently there are four main distinct versions of the protocol:

* **Plasma Cash** <br/>
Plasma Cash is a Plasma design primarily built for storing and transferring non-fungible tokens. It is highly scalable because users only ever need to keep track of their own tokens. <br/>
It uses Sparse Merkle Trees (SMT) for non inclusion proofs and hence can only be used for NFTs since SMTs uses indexing.
Each block has a ‘slot’ for each coin (unique deposit). When a coin is spent, a transaction proof is recorded in that coin’s respective slot in the block. <br/>
_Note: Coin defragmentation research to support FTs is going on currently_

* **Plasma Debit** <br/>
Plasma Debit is like Plasma Cash, except every token is a payment channel between the user and the chain operator. It’s sort of like a big Lightning Network hub, but the channels can be transferred just like a Plasma Cash token. Transactions are super fast and you only need to keep track of your own channels.

* **Plasma Prime** <br/>
Plasma Prime is a fancy new design that makes use of RSA accumulators to solve the problem of large history proofs in Plasma Cash.

* **MVP (Minimum Viable Plasma)**<br/>
Plasma MVP is a design for an extremely simple UTXO-based Plasma chain. The basic Plasma MVP specification enables high-throughput payment transactions, but does not support more complicated constructions like scripts or smart contracts.

Plasma MVP relies on confirmation signatures because withdrawals are processed in order based on the position of the output being withdrawn. 

Users need to sign a signature before making a transaction, wait to see the transaction included in a valid block, and then sign another signature. These second signatures must also be included within a plasma block, reducing block space available for more transactions!

_Note: Confirmation signatures make for pretty bad user experience. **More Viable Plasma**, also known as **MoreVP**, is an extension to Minimal Viable Plasma that removes the need for confirmation signatures. MoreVP modifies the process through which users can withdraw their funds. The ordering of each withdrawal becomes based on the position of the youngest input to the transaction that created an output._

### Comparing different models of plasma

| Plasma Design Component | Plasma MVP | Plasma Cash | Plasma Debit |
| :--- | :--- | :--- | :--- |
| Data Structure | Binary Merkle tree | Sparse Merkle Tree | Sparse Merkle tree |
| Consensus | Any (PoW,PoA,PoS) | Any (PoW,PoA,PoS) | Single or few operators preferred over because of payment channel structure |
| Deposits | UTXOs representation, support for ETH, ERC20 | Unique Coin ID for each deposit, NFTs only | Accounts with unique coin IDs for each deposit, NFTs and FTs only |
| Fees | Plasma transaction fees to validators and gas fees when exiting/withdrawing to rootchain or other chains | Same as MVP | Users pay via operator-led payment channel instead of directly to other users |
| Signatures | Tx signature before block inclusion, confirmation signature post-inclusion | Confirmation signatures to avoid griefing | No confirmation signatures |
| Exits/Withdrawals | Proof of unspent UTXO required to exit, priority based on how old UTXO is | Proof of coin’s latest two transactions, proof of block inclusion, no priority | Proof of coin’s latest two transactions, proof that fraction of coin hasn’t been previously spent, proof of block inclusion, no exit priority |

Let's compare pros, cons and use cases for each model now

| Type | Plasma MVP | Plasma Cash | Plasma Debit |
| :--- | :--- | :--- | :--- |
| Pros | Scalable, all signatures sent to operator in PoA, High fungibility | Very scalable, watchers or users themselves need to only keep track of their own coins not all coins on the chain | Very scalable, watchers or users themselves need to only keep track of their own coins, Enables transactions with NFTs and FTs, Efficient balance updates don’t need to be included in blocks as agreement can be made between operator and coinholder (similar to channels) |
| Cons | Watchers or users themselves are required to watch and challenge invalid exits, Potential for honest bond slashing if operator withholds blocks and user attempts to re-submit transaction | Coin proofs can be massive, Coins are in fixed denomination, Watchers or users themselves are required to watch and challenge invalid txs with their own coins | Heavy reliance on operator, can be hedged by creating a set of rotating operators, Coin proofs can be massive, Requires operator to lock up significant funds in advance to fund payment channels, Tx size constrained by initial coin deposit size, Enabling decentralized exchange on Debit is non-trivial |
| Use Cases | Low-trust use cases (PoA), Exchanges, securities, P2P payments, recurring/bill payments, gaming | Collectibles, Asset management (real estate, art) | Use cases with high-trust of operators, ewallet or service providers, Gaming, Asset Management, P2P payments |

## Resources

* [Plasma Group](https://plasma.group/)
* [What is Ethereum Plasma](https://www.binance.vision/blockchain/what-is-ethereum-plasma)
* [The State of Plasma](https://media.consensys.net/the-state-of-plasma-1-6b48c1e4b295)
* [How Plasma Work](https://medium.com/applicature/what-is-plasma-and-how-does-it-work-15641c95825f)
* [Learn Plasma](https://www.learnplasma.org/en/learn/framework.html)
* [Comparing plasma models](https://www.learnplasma.org/en/learn/compare.html)
