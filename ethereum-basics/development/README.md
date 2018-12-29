# Developing on the Ethereum blockchain
Ethereum is a blockchain, first-and-foremost. Its primary artifact is the smart contract, written in the programming language, Solidity. However, you should know that the tech stack surrounding it is HUGE!

## Background
Ethereum was the first general-purpose smart contract platform that supported Turing-complete computation. However, this means its stack is more complicated than a bespoke platform. Here's a list I took from a talk [\[1\]](https://slides.com/liamzebedee/the-blockchain-tiramisu).

 * blockchain node/client software - `geth`
 * consensus engine - proof-of-stake, clique (geth, Parity), test (Ganache)
 * blockchain RPC client - web3.js
 * accounts/keys
 * debugger (Remix)
 * smart contract language and compiler - Solidity and solc
 * Smart contract artifacts (ABI's)
 * Smart contract wrappers (TypeScript)
 * API layer - encoding/decoding data (ABIEncoder, BigNumber.js, hex normalisation)
 
