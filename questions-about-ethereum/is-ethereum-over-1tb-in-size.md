# Is the Ethereum blockchain over 1TB in size?

##Answer
No. Please check [here](http://didtheethereumblockchainreach1tbyet.5chdn.co/) for the latest size.

##Explanation
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

There is often much confusion around if a pruned Ethereum node (above) is a full node and the answer is yes. A lot of confusion comes from the fact that Bitcoin nodes leave no choice and [prune blocks by default](https://bitcoin.stackexchange.com/questions/37496/how-can-i-run-bitcoind-in-pruning-mode/37497#37497), so it's often not recognized that this occurs. The node configuration above is the same as a full Bitcoin node.

Pruning ancient blocks is fine as they are not necessary to most users. If you are looking to run a block explorer or do deep analysis on the blockchain, then you could [run an archive node](https://docs.ethhub.io/using-ethereum/running-an-ethereum-node#archive-nodes) with no pruning to get them. 

Also note that you can run both Geth and Parity by default (warp and fast sync enabled) and you'll be able to serve the network as a full node after initial sync.