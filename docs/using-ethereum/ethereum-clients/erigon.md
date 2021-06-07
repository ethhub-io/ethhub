---
title: Erigon - EthHub

description: Erigon - Ethereum implementation on the efficiency frontier
---

# Erigon

## Summary

Erigon is a completely re-architected implementation of Ethereum. Currently written in Golang, with other implementations to follow.

Erigon's biggest selling points are:
* Full Database / Data Model redesign
    * Full Archive Node in 1.2TB (as of 2021-06-01)
* Staged Sync
    * Full Archive Node in less than 3 Days on NVMe (as of 2021-06-01)
* More Modular Design
    * Core/Execution
    * Peering (sentry) (coming soon)
    * JSON-RPC Server (rpcdaemon)
* Selective Pruning with Storage-Mode:
```
--storage-mode value
    * h - write history to the DB
    * r - write receipts to the DB
    * t - write tx lookup index to the DB
    * c - write call traces index to the DB,
    * e - write TEVM translated code to the DB
```

## Requirements

Minimum:

* CPU with 2+ cores
* 16GB RAM
* Storage:
    * Full Prune (`--storage-mode=`): ~450GB
    * Full Archive (default or `--storage-mode=hrtc`): ~1.2TB

## Setup

* [Download and install Golang](https://golang.org/doc/install)
* Clone the [stable repository](https://github.com/ledgerwatch/erigon/tree/stable)
    * `git clone --branch stable https://github.com/ledgerwatch/erigon.git`
* Build erigon from source

### Linux
```bash
cd erigon
make
```
### Windows
* Install [Chocolatey](https://chocolatey.org/)
* build via Powershell:
```powershell
choco install cmake make mingw
cd erigon
./win-build.ps1
```

Binaries should be available in the build/bin folder once build is complete if successful.

## Running

At this time, Erigon only has one mode of operation and that is "Full Sync"

There are 2 primary components to be concerned with at this time.
1. erigon
    * This is the core component that is responsible for downloading blocks and processing them
    * Eventually the peering will be removed into a separate process (sentry) but for now it's all in `erigon`
2. rpcdaemon
    * This is the JSON-RPC Server that lets you query the node for data

## Using

Both `erigon` and `rpcdaemon` should be located in the `build/bin` folder after building. You can copy or move them to a new location if desired.

Running erigon can be as simple as:
```bash
./build/bin/erigon
```

Running rpcdaemon can be as simple as:
```bash
./build/bin/rpcdaemon
```

However, both erigon and rpcdaemon have many of the same flags that you might find with `geth` and you can get help with those flags via `--help`

A more complex example:
```bash
# erigon in full pruning mode, custom datadir, custom peer identity, custom port number, and listening on all interfaces
./build/bin/erigon --storage-mode= --datadir="/data/erigon/datadir" --identity="my-erigon-node" --port=30304 --private.api.addr="0.0.0.0:9090"

# rpcdaemon running in dual-mode, listening on all interfaces, on port 8544, disabling CORS, enabling all HTTP APIs, enabling WebSockets
./build/bin/rpcdaemon --datadir="/data/erigon/datadir" --private.api.addr="localhost:9090" --http.addr="0.0.0.0" --http.port=8544 --http.vhosts="*" --http.corsdomain="*" --http.api="eth,debug,net,trace,web3,erigon" --ws
```

## Resources
* [Github](https://github.com/ledgerwatch/erigon)
