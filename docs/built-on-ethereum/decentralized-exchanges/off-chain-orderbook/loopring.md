title: Loopring - Ethhub

description: Loopring is an open protocol for building scalable and secure orderbook-based DEXes on Ethereum.

# Loopring

## Description

Loopring is an open protocol for building high-performance, non-custodial orderbook exchanges on Ethereum. Loopring is the first zkRollup DEX protocol with on-chain data availability.

## Architecture

Loopring v3 uses a zkRollup construction to achieve scalable exchanges without sacrificing Ethereum security guarantees. It performs all computations off-chain, batches and proves these updates in a zkSNARK proof, and then submits it to Ethereum to verify.

Additionally, Loopring enforces on-chain data availability, meaning in conjunction with the Merkle root, other state transition data is also kept on Ethereum, as opposed to an off-chain consortium. As a result, the only assumption needed in order be certain one can always access their own funds, is that Ethereum will continue to exist.

* [Loopring 3.0 Design Doc](https://github.com/Loopring/protocols/blob/master/packages/loopring_v3/DESIGN.md)

While previous versions of Loopring were able to settle 2-3 trades per second on Ethereum, v3 raises throughput to 1,400 tps, with the commensurate reduction in settlement costs, currently well below one US cent per transaction. 

## Components

Loopring Protocol is an assembly of Ethereum [smart contracts](https://github.com/Loopring/protocols/tree/master/packages/loopring_v3), and [zkSNARK circuits](https://medium.com/loopring-protocol/loopring-open-sources-its-zksnark-circuit-code-53c934b67ce5). These form the core of the v3 protocol. To run the protocol, a Relayer (or group of relayers) operates the off-chain components, including order hosting & proof generation. 


## Resources

* [Website](https://loopring.org) 
* [GitHub](https://github.com/Loopring)
* [Twitter](https://twitter.com/loopringorg)
* [Loopring 3.0 Overview](https://medium.com/loopring-protocol/loopring-3-0-overview-from-a-to-zksnarks-2c542e6c07b0)
* [zkSNARK Trusted Setup MPC](https://loopring.org/#/post/loopring-starts-trusted-setup-multi-party-computation-ceremony)
* [Security Audit Report](https://loopring.org/#/post/secbit-delivers-a-security-audit-report-for-loopring-protocol-3-0)
