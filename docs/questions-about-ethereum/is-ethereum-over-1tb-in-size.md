---
title: Is Ethereum over 1TB in size? - EthHub

description: Yes, the Ethereum blockchain size has not exceeded 1TB in size.
---

# Is Ethereum over 1TB in size?

## Answer

Yes. Please check [here](https://etherscan.io/chartsync/chaindefault) for the latest size.

## Explanation

As Afri Schoedon points out in [his article](https://dev.to/5chdn/the-ethereum-blockchain-size-will-not-exceed-1tb-anytime-soon-58a), the Ethereum state is what is bloated, not the chain.

So what sync mode should you run to get a full Ethereum blockchain with all necessary security? Both Parity and Geth offer options which synchronize a full node starting at the genesis block and executing all transactions. The modes are:

* parity --no-warp
* geth --syncmode full

These are full nodes because they:

* Sync the full chain from genesis block
* Replay all transactions
* Execute all contracts
* Recompute the state of each block
* Keep all historical blocks on disk
* Keep the most recent state and prunes ancient states

When running the full node described above, you are able to rebuild any historical information you want using just your node.

There is often much confusion around if a state pruned Ethereum node \(above\) is a full node and the answer is yes.

Pruning ancient state is fine as it is not necessary to most users. If you are looking to run a block explorer or do deep analysis on the blockchain, then you could [run an archive node](https://docs.ethhub.io/using-ethereum/running-an-ethereum-node#archive-nodes) with no pruning so you don't have to always recompute the pruned state.

Also note that you can run both Geth and Parity by default \(warp and fast sync enabled\) and you'll be able to serve the network as a full node after initial sync.

