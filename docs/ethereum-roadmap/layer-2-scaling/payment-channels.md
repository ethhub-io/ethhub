title: Payment Channels - EthHub

description: Payment channels are a layer 2 scaling solution for Ethereum.

# Payment Channels

## Summary

Payment Channels are one implementation of State Channel technology. Payment channels allow for practically unlimited, bidirectional transfers between two participants, as long as the net sum of their transfers does not exceed the deposited tokens. These transfers can be performed instantaneously and without any involvement of the actual blockchain itself, except for an initial one-time on-chain creation and an eventual closing of the channel.

## The Raiden Network

The Raiden Network is an off-chain scaling solution for performing ERC20-compliant token transfers on the Ethereum blockchain. It is Ethereum's version of Bitcoin's Lightning Network, enabling near-instant, low-fee, scalable, and privacy-preserving payments.

The Raiden Network allows secure transfers of tokens between participants without the need for global consensus. This is achieved using digitally signed and hash-locked transfers, called balance proofs, fully collateralized by previously setup on-chain deposits. This concept, illustrated below, is known as payment channel technology.

![](/assets/images/payment_chans.png)

The true strength of Raiden lies in its network protocol. Since opening and closing a payment channel between two peers still requires on-chain transactions, creating channels between all possible peers becomes infeasible. As it turns out, however, you do not need a direct payment channel between a payer and a payee if there exists at least one route through a network of channels that connects the two parties, as shown in figure 2. This network and its associated protocol for routing and interlocking channel transfers is called the Raiden Network.

In addition, payment channel transfers, in contrast to on-chain transactions, do not require any fees. Intermediaries within the greater network, however, will want to charge fees on a low percentage basis for providing their own channels to the network, leading to complex routing and a competitive channel fee market. The Raiden protocol aims to facilitate this market by using both protocol-level features and optional auxiliary services.

## Resources

* [Raiden Network](https://raiden.network/101.html)

