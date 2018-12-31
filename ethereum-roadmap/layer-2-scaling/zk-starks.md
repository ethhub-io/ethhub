# ZK-STARKs (Zero-Knowledge Scalable Transparent ARguments of Knowledge)
## About
ZK-STARKs (Zero-Knowledge Scalable Transparent ARguments of Knowledge) are a type of cryptographic proof technology that enables users to share validated data or perform computations with a third party without the data or computation being revealed to the third-party, also known as a zero-knowledge proof, in a way that is publicly verifiable. In simpler terms, a zero-knowledge proof can prove something is true without having to reveal what exactly it is proving. For example, ZK-STARKs would allow Alice verify Bob's banking information using a zero-knowledge cryptographic proof instead of revealing his ID to Alice.

Prior to the creation of ZK-STARKs, ZK-SNARKs were used to create ZK proof systems, but required a trusted party or parties to initially setup the ZK proof system which introduced the vulnerability of those trusted parties compromising the privacy of the entire system. ZK-STARKs improves upon this technology by removing the need for a trusted setup.   

## Scaling benefits of using STARKs
STARKs improve two of problems of permissionless blockchains: scalability and privacy. StarkWare Industries' current ZK-STARK research is focusing on scalability first and then privacy later on.

STARKs improve scalability by allowing developers to move computations and storage off-chain. Off-chain services will be able to generate STARK proofs that attest the integrity of off-chain computations. These proofs are then placed back on chain for any interested party to validate the computation. Moving the bulk of computational work off-chain using STARKs allows existing blockchain infrastructure to scale exponentially while trustlessly maintaining computational integrity.

## Differences between ZK-SNARKs and ZK-STARKs
1. ZK-SNARKs require a trusted setup phase whereas ZK-STARKs use publicly verifiable randomness is used to create the trustlessly verifiable computation system. 
2. ZK-STARKs are more scalable in terms of computation speed and size when compared to ZK-SNARKs. 
3. ZK-SNARKs are vulnerable to attacks from quantum computers due to the cryptography it uses. ZK-STARKs are currently quantum-resistant.

## Reference Links
* [ZK-STARKs Whitepaper](https://eprint.iacr.org/2018/046.pdf)
* [libSTARK](https://github.com/elibensasson/libSTARK) - a C++ library for ZK-STARK systems
* [StarkWare Industries site](https://www.starkware.co/) - The leading researchers pioneering ZK-STARKs
* [StarkWare Industries blog](https://medium.com/@StarkWare)
* Vitalik's series on ZK-STARKs - [Part 1](https://vitalik.ca/general/2017/11/09/starks_part_1.html) [Part 2](https://vitalik.ca/general/2017/11/22/starks_part_2.html) [Part 3](https://vitalik.ca/general/2018/07/21/starks_part_3.html) 
* [STARKs presentation at Web3 Summit 2018](https://www.youtube.com/watch?v=1KSwVIZ82hs) - Eli Ben-Sasson and Avihu Levy present Stark vs. Snark & Bulletproofs 
* [Adam Luciano on ZK-STARKS](https://medium.com/coinmonks/zk-starks-create-verifiable-trust-even-against-quantum-computers-dd9c6a2bb13d) - A simple breakdown of the STARK whitepaper and differences from SNARKs
* [Zero Knowledge FM](https://www.zeroknowledge.fm/) - a podcast made for developers and people looking to learn about ZK tech 
