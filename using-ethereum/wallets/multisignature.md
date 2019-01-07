# Multisignature

## Summary

Multisignature Wallets (multisig wallets) are wallets created with signatures from several private keys. Multisignatures require signatures from a majority of the original signing keys (commonly referred to as n-of-m keys) in order to interact with the wallet. Ideally, the signing keys of a multisignature wallet should be comprised of several different types of wallets in order to reduce the risk of any one key from compromising the security of the multi-signature wallet. Multisignature wallets where the keys are properly distributd also reduce the risk of losing the keys to your funds due to unforeseen circumstances. For example, if a multisignature wallet included keys stored on a hardware wallet, a mobile wallet, and a desktop wallet and your mobile phone is stolen, you could still access your multisignature wallet using the hardware and desktop wallets.

## Pros and Cons

### Pros

* Can be secured by several types of wallet keys (desktop, hardware, mobile, etc.) for added security
* Can be configured to be recovered by a portion of the original signing keys (n-of-m keys)
* Non-custodial, more private than most other methods of interacting with your funds.

### Cons

* Inconvenience of requiring access to multiple keys to interact with the wallet
 
## Wallets

* [Gnosis MultiSigWallet](https://github.com/Gnosis/MultiSigWallet) - The original Gnosis multisig wallet
* [Gnosis Safe](https://safe.gnosis.io/) - An improved version of Gnosis MultiSigWallet
* [BitGo Multi-Sig Wallet v2](https://github.com/BitGo/eth-multisig-v2)

Grid+'s hardware agent called Lattice1 also uses multisignature wallets to allow end users and merchants to securely store their funds using a combination of an arbitrary amount of smart cards or Safe Cards and your mobile phone.

## Resources
* [Grid+ Lattice1](https://blog.gridplus.io/introducing-the-grid-lattice1-bc4ff6df5321) - Enterprise-grade hardware terminal for multisig wallets
* [Consensys's ethereum-developer-tools-list](https://github.com/ConsenSys/ethereum-developer-tools-list/blob/master/EcosystemResources.md)

