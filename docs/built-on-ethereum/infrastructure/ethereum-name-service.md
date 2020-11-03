title: Ethereum Name Service (ENS) - EthHub

description: Ethereum Name Service (ENS) is a decentralized domain name provider. It allows users to buy and manage .eth domains without a centralized domain registrar.

# Ethereum Name Service \(ENS\)

## Description

Ethereum Name Service \(ENS\) is a decentralized domain name provider. It allows anyone to buy and manage `.eth` domains without relying on a centralized domain registrar.

The owner of a domain can map it to any string value. One example is creating a human-readable name for his Ethereum wallet by resolving a personal domain to it. The owner can also create and manage subdomains.

Each domain has an owner, resolver, and time-to-live record and is stored in the ENS registry. Resolvers are smart contracts that can provide any information about given domain. Owner of the domain can choose a resolver and transfer the ownership of the domain as well as its subdomains.

## History
### Launch
The ENS launched on May 4th, 2017 with a temporary registrar contract featuring a Vickrey auction design for registering domains. 
#### Vickrey Auction Process Explained
1. First, someone looking to register an ENS domain was required to make a minimum bid of at least 0.01 ETH which opened an auction for the desired name. This started a 3-day timer for other people to place bids on the name. During this period, the details of bids were obscured: nobody could tell how much you bid, or even what name you were bidding on.
2. After the three day auction finished, a two day “reveal” period would begin. During this period, everyone who made a bid must have revealed the details of their bid — if they didn’t, they lost their entire bid. If your bid was not the highest, you were refunded your bid, minus a 0.5% fee which was burned.
3. At the end of the two day reveal period, the winner was the person who revealed the highest bid, but they only had to pay the amount of the second-highest bidder. This amount was locked up in the contract as a deposit until the permanent registrar came. The winner was required to send a “finalise” transaction to receive a refund of any extra funds, and to be assigned control of the name in ENS.
### Upgrade to Permenant Registrar
At 00:00 UTC May 4th, 2019, the ENS was upgraded to a permanent registrar contract which did away with the Vickrey auction system in lieu of instant registration for ENS domains seven characters or longer. The new registrar requires domain holders to pay $5/year paid in Ether to main. Domains registered before this update are required to migrate to the new registrar but are not required to pay this yearly fee until after May 4, 2020.

## Registering an ENS domain
Registering a domain on the ENS will cost you $5/year paid in Ether. See [here](https://medium.com/the-ethereum-name-service/step-by-step-guide-to-registering-a-eth-name-on-the-new-ens-registrar-c07d3ab9d6a6) for a step-by-step guide to registering an ENS domain. 

### Registering ENS domain names shorter than 7 characters
With the May 4th, 2019 update to the permenant registrar, ENS intends to start opening up registrations of names shorter than 7 characters.

This will start with a preregistration process, during which owners of existing DNS domains can claim the corresponding ENS name for their project. After that, an auction process will start in which anyone can bid on the newly available names, and then finally open the rest up for instant registration. See [here](https://discuss.ens.domains/t/short-name-auction-reservation-process-proposed-process/836) for more information.

## ENS-supported Software
### Mobile Wallets
* [Alphawallet](https://alphawallet.com/)
* [Argent](https://www.argent.xyz/)
* [Cipher](https://www.cipherbrowser.com/)
* [Imtoken](https://token.im/)
* [Leth](https://www.inzhoop.com/)
* [Pandax](https://www.pandax.tech/)
* [Status](https://status.im/)
### Desktop Wallets
* [Metamask](https://metamask.io/)
* [MyCrypto](https://mycrypto.com/)
* [MyEtherWallet](https://myetherwallet.com/)
* [Opera](https://www.opera.com/)
### Apps
* [Aragon](https://aragon.one/)
* [Bitfinex](https://www.bitfinex.com/)
* [Enjinx](https://enjinx.io/)
* [Etherscan](https://etherscan.io/)
* [Portal](https://www.portal.network/)
* [Swarm](https://github.com/ethersphere/swarm)
* [Totem](https://totem.network/)
* [Universallogin](https://universallogin.io/)
## Important links

* Website: [https://ens.domains](https://ens.domains)
* Github: [https://github.com/ensdomains](https://github.com/ensdomains)
* ENS Registrar: [https://manager.ens.domains](https://manager.ens.domains)

