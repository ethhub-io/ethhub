# Geth
Geth is the Golang implementation of the Ethereum protocol.

It is fast, open source software that is actively maintained.

You can find the Github repository [here](https://github.com/ethereum/go-ethereum)

## Requirements

Minimum:

 - CPU with 2+ cores.
 - At least 80GB free storage space.
 - 4GB RAM minimum with a SSD, 8GB+ if you have an HDD.
 - 8 MBit/sec download Internet service.

For light nodes, the requirements are much lower, as you will only be storing block headers and receive small state updates.

Recommended:

 - Fast CPU with 4+ cores.
 - 16GB+ RAM.
 - Fast SSD with at least 500GB free space.
 - 25+ MBit/sec download Internet service.

## Setup
 - [Download Geth from the official page](https://ethereum.github.io/go-ethereum/downloads/)
 - Extract the compressed archive with your tool of choice

There are no system dependencies if using an officially released geth binary, which ships for most architectures and operating systems.

## Running
The first step in running an Ethereum node is synchronizing the Blockchian.

There are a few options you can use to specify the sync mode of the geth client:
 - --syncmode "fast"
 - --syncmode "full"
 - --syncmode "light"

By default, geth will run in --syncmode "fast", this is the recommended option for running a complete Ethereum node.

When using "fast" synchronization, the node will initially download blocks until it reaches the tip of the Blockchain without performing extensive validation steps. Once your node is in sync with the rest of the network, the node will validate transactions exactly like a full node.

When using "full" synchronization, the node validates every transaction from downloaded blocks until it reaches the tip of the Blockchain. This is not advised, as it doesn't provide any benefits and can result in the node taking multiple days, or even weeks, to synchronize completely. Once the node is in sync, it will continue full validation of new transactions.

When using "light" synchronization, the node begins downloading block headers for a few million blocks prior to the current block height, making it a very quick sync. The drawback to this method is that the node is unable to perform validation, as it doesn't have complete records of the Blockchain.

If running on a device with low bandwidth or memory, the light node can be advantageous. The light node gets updated by full nodes once in a while with information on changes pertaining to relevant parts of the Blockchain.

When offering services to users which might require complete records, the fast sync options is the best.

A fast sync node can operate in light mode.

## Using
In the folder extracted from the downloaded archive, the geth program can be run with the desired sync mode and other options.

```sh
./geth --syncmode "fast"
```
