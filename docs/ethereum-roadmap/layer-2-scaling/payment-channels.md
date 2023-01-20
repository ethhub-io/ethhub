---
title: Payment Channels - EthHub

description: Payment channels are a layer 2 scaling solution for Ethereum.
---

# Payment Channels

## Summary

Payment Channels are one implementation of State Channel technology. Payment channels allow for practically unlimited, bidirectional transfers between two participants, as long as the net sum of their transfers does not exceed the deposited tokens. These transfers can be performed instantaneously and without any involvement of the actual blockchain itself, except for an initial one-time on-chain creation and an eventual closing of the channel.

## Kchannels

Kchannels is a new payment channel platform for Ethereum. It is non-custodial and trust-minimized, and its primary focus is on great UX.  It's avaiable on Mainnet and a number of testnets as well as on the Xdai Chain.

Kchannels uses a powerful channel design:
* a channel can hold multiple assets (and transfer multiple assets in a transaction)
* an unattended channel can receive transactions
* fast and easy deposits/withdrawals at an open channel
* most users only need a single channel--ever--for all their needs!

Kchannels provides the standard payment channel features (fast transactions, low fees, and privacy), and it also has the following features:
* minimal infrastructure requirements
* immediate transaction finality (unique in the L2 space)
* no special token
* no network
* no capital required to maintain channels
* high scalability

## The Raiden Network

The Raiden Network is an off-chain scaling solution for performing ERC20-compliant token transfers on the Ethereum blockchain. It is Ethereum's version of Bitcoin's Lightning Network, enabling near-instant, low-fee, scalable, and privacy-preserving payments.

The Raiden Network allows secure transfers of tokens between participants without the need for global consensus. This is achieved using digitally signed and hash-locked transfers, called balance proofs, fully collateralized by previously setup on-chain deposits. This concept, illustrated below, is known as payment channel technology.

![](/docs/assets/images/payment_chans.png)

The true strength of Raiden lies in its network protocol. Since opening and closing a payment channel between two peers still requires on-chain transactions, creating channels between all possible peers becomes infeasible. As it turns out, however, you do not need a direct payment channel between a payer and a payee if there exists at least one route through a network of channels that connects the two parties, as shown in figure 2. This network and its associated protocol for routing and interlocking channel transfers is called the Raiden Network.

In addition, payment channel transfers, in contrast to on-chain transactions, do not require any fees. Intermediaries within the greater network, however, will want to charge fees on a low percentage basis for providing their own channels to the network, leading to complex routing and a competitive channel fee market. The Raiden protocol aims to facilitate this market by using both protocol-level features and optional auxiliary services.

## Resources

* [Kchannels](https://docs.kchannels.io)
* [Raiden Network](https://raiden.network/101.html)

