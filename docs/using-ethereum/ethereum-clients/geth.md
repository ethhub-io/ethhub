---
title: Geth - EthHub

description: Geth is the Golang implementation of the Ethereum protocol. It is fast, open source software that is actively maintained.
---

# Geth

## Summary

Geth is the Golang implementation of the Ethereum protocol. It is fast, open source software that is actively maintained.

## Requirements

Minimum:

* CPU with 2+ cores
* 4GB RAM
* 320GB free storage space to sync the Mainnet
* 8 MBit/sec download Internet service

Recommended:

* Fast CPU with 4+ cores
* 16GB+ RAM
* Fast SSD with at least 500GB free space
* 25+ MBit/sec download Internet service

For light nodes, the requirements are much lower, as you will only be storing block headers and receive small state updates.

## Setup

* [Download Geth from the official page](https://geth.ethereum.org/downloads/)
* Extract the compressed archive with your tool of choice

There are no system dependencies if using an officially released geth binary, which ships for most architectures and operating systems.

## Running

The first step in running an Ethereum node is synchronizing the Blockchian.

There are a few options you can use to specify the sync mode of the geth client:

* --syncmode "fast"
* --syncmode "full"
* --syncmode "light"

By default, geth will run in --syncmode "fast", this is the recommended option for running a complete Ethereum node.

When using "fast" synchronization, the node will initially download blocks until it reaches the tip of the Blockchain without performing extensive validation steps. Once your node is in sync with the rest of the network, the node will validate transactions exactly like a full node.

When using "full" synchronization, the node validates every transaction from downloaded blocks until it reaches the tip of the Blockchain. This is not advised, as it doesn't provide any benefits and can result in the node taking multiple days, or even weeks, to synchronize completely. Once the node is in sync, it will continue full validation of new transactions.

When using "light" synchronization, the node only downloads a few recent block headers, making it a very quick sync. The drawback to this method is that the node is unable to perform reliable validation, as it doesn't have complete records of the Blockchain.

If running on a device with low bandwidth or memory, the light node can be advantageous. The light node gets updated by full nodes once in a while with information on changes pertaining to relevant parts of the Blockchain.

When offering services to users which might require complete records, the fast sync options are the best to use.

A fast sync node can operate in light mode.

## Using

In the folder extracted from the downloaded archive, the geth program can be run with the desired sync mode and other options.

```bash
./geth --syncmode "option"
```

When using a light client, beware that it can take up to 10 minutes after the node's initialization before it starts receiving updates from the network. From then on, it is actively subscribed to updates by the full nodes.

You can expect it to take anywhere from 3 to 12 hours to fast sync your Ethereum node depending on your hardware and whether your connection to the Internet is a bottleneck.

A few interesting commands which will enhance your geth experience:

* **./geth account new**: create an account, yields the address and location of the keystore file
* **./geth account list**: list all accounts located in the keystore folder
* **./geth --cache VALUE**: increase the amount of memory allocated to geth, default 1024 \(MB\)
* **./geth --maxpeers VALUE**: set maximum number of full node peers, default 25
* **./geth --lightpeers VALUE**:  set maximum number of light node peers, default 100
* **./geth export FILEPATH**: export a copy of the Blockchain data to FILEPATH
* **./geth import FILEPATH**: import Blockchain data from FILEPATH

## Resources
* [Github](https://github.com/ethereum/go-ethereum)
