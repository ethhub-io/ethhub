# Parity
Parity is an implementation of the Ethereum protocol written in Rust, a systems programming language.

It is developed and actively maintained by a third party.

The Github repository is located [here](https://github.com/paritytech/parity-ethereum)

## Requirements
Full node:
 - Multi-core CPU
 - 4GB RAM
 - SSD drive and at least 100GB free space
 - A decent DSL connection is required

Computers using HDD are advised to run a Light Node.

Light node:
 - Single-core CPU
 - 512MB RAM
 - 128MB free space on HDD

## Setup
 - [Download parity from the official Github releases page](https://github.com/paritytech/parity-ethereum/releases/tag/v2.0.6)
 - If on Linux, make the parity binary executable with `chmod +x ./parity`

For running a compiled binary downloaded from the official Github releases page, no system dependencies are required.

## Running
By default, the parity client syncs the Ethereum Blockchain completely from a snapshot downloaded from peers and includes features such as auto-updating.

To disable downloading a snapshot from peers, use `--no-warp`; this saves a few GB of storage but takes longer to sync.

If you wish to run a light node, simply specify the command line option `--light` to the program.

Syncing can be faster by disregarding ancient blocks with `--no-ancient-blocks`; costing only 20GB.

The default sync with warp enabled occupies 82GB of storage when completed.

For a complete pruning archive, with complete state saved, run parity with `--pruning archive` (over 1TB disk space will be used).

## Using

Many commands are available with the parity client.
 - **parity account new**: asks for a password and yields an address
 - **parity account list**: lists local addresses
 - **parity snapshot --at BLOCKNUMBER FILEPATH**: save snapshot at BLOCKNUMBER to FILEPATH
 - **parity restore FILEPATH**: restore Blockchain from snapshot located at FILEPATH
