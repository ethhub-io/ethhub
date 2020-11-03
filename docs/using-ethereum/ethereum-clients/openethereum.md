---
title: OpenEthereum - EthHub

description: OpenEthereum is an implementation of the Ethereum protocol written in Rust, a systems programming language.
---

# OpenEthereum

## Summary

OpenEthereum is an implementation of the Ethereum protocol written in Rust, a systems programming language. It is developed and actively maintained by OpenEthereum DAO.

## Requirements

Full node:

* Multi-core CPU
* 4GB RAM
* SSD drive and at least 100GB free space
* A decent DSL connection is required

Computers using HDD are advised to run a Light Node.

Light node:

* Single-core CPU
* 512MB RAM
* 128MB free space on HDD

## Setup

* [Download OpenEthereum from the official Github releases page](https://github.com/OpenEthereum/open-ethereum/releases)
* If on Linux, make the OpenEthereum binary executable with `chmod +x ./OpenEthereum`

For running a compiled binary downloaded from the official Github releases page, no system dependencies are required.

## Running

By default, the OpenEthereum client syncs the Ethereum Blockchain completely from a snapshot downloaded from peers and includes features such as auto-updating.

To disable downloading a snapshot from peers, use `--no-warp`; this saves a few GB of storage but takes longer to sync.

If you wish to run a light node, simply specify the command line option `--light` to the program.

Syncing can be faster by disregarding ancient blocks with `--no-ancient-blocks`; costing only 20GB.

The default sync with warp enabled occupies ~82GB of storage when completed \(as of 15/10/2018\).

For a complete pruning archive, with complete state saved, run OpenEthereum with `--pruning archive` \(over 1TB disk space will be used\).

## Using

Many commands are available with the OpenEthereum client.

* **OpenEthereum account new**: asks for a password and yields an address
* **OpenEthereum account list**: lists local addresses
* **OpenEthereum snapshot --at BLOCKNUMBER FILEPATH**: save snapshot at BLOCKNUMBER to FILEPATH
* **OpenEthereum restore FILEPATH**: restore Blockchain from snapshot located at FILEPATH

## Resources
* [Github](https://github.com/OpenEthereum/open-ethereum)
