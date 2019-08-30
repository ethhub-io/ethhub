title: Interacting with Clients - EthHub

description: This page provides information and resources to help you programmatically interface with an ethereum client.

# Interacting with an Ethereum Client: JSON-RPC

JSON-RPC is the primary protocol used by Ethereum and bitcoin. is a lightweight data-interchange format. It is easy for humans to read and write. It is easy for machines to parse and generate. While it is transport agnostic, most ethereum clients today implement one or all of the following: HTTP, IPC and websockets.

## Ethereum JSON-RPC Specification

There exists a specification for ethereum JSON-RPC that is expected to be implemented by all client developers. The OpenRPC document can be found [here](https://github.com/etclabscore/ethereum-json-rpc-specification/blob/master/openrpc.json).

Within the above linked repo you will also find generated code for making RPC calls to any ethereum client. 
