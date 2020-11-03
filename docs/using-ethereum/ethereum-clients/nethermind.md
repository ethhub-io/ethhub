---
title: Nethermind - EthHub

description: Nethermind is the .NET Core implementation of the Ethereum protocol. It is fast, open source software that is actively maintained.
---

# Nethermind

## Summary

Ethereum Client built on .NET Core, perfect for enterprise-grade systems and benefiting from a huge pool of developers. Extend it, customise it - the sky’s the limit.

## Requirements

[Hardware Requirements](https://nethermind.readthedocs.io/en/latest/hardware_requirements.html)


## Setup

* [Download Nethermind from the official page](http://downloads.nethermind.io/)
* [Follow the instructions](https://nethermind.readthedocs.io/en/latest/start.html)

## Running

There are two methods to run the Nethermind client.

* Nethermind.Launcher
* Nethermind.Runner

Nethermind ships with a set of default configuration files located in the configs folder. These config files are used by Nethermind.Launcher. You can customize them following the documentation [here](https://nethermind.readthedocs.io/en/latest/configuration.html). It is recommended to not overwrite the default configs as they will be replaced when upgrading. Instead, copy the one that closest meets your needs and save it to a known location.

### Nethermind.Launcher
Nethermind.Launcher is an interactive prompt that allows you to choose the network which then calls Nethermind.Runner with the appropriate config file. This is the quickest way to get up and running.

### Nethermind.Runner
This is the actual client binary similar to the `geth` binary and supports both cli options or a JSON configuration file.

By default Nethermind will use the binary's location as its home and will create keystore, database, etc in that home location. You can overwrite this behavior with a custom configuration file or via the command line options.

`Nethermind.Runner --config <path_to_config>`

## Using

Nethermind.Launcher can be used as a [CLI](https://nethermind.readthedocs.io/en/latest/cli.html) tool similar to that of the geth cli. If you have enabled WebSockets and/or [JSON RPC](https://nethermind.readthedocs.io/en/latest/jsonrpc.html) then most RPC endpoints have been implimented and can be accessed in the same manner as geth.

## Resources
* [Website](https://nethermind.io/client)
* [Github](https://github.com/NethermindEth/nethermind)
* [Read The Docs](https://nethermind.readthedocs.io/en/latest/index.html)
