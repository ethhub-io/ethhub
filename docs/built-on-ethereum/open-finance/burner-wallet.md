# Burner Wallet (xDai)

## Summary

Founded by [Austin Griffith](https://twitter.com/austingriffith), The Burner Wallet is a wallet that allows users to interact with the xDai sidechain from [POA](../bult-on-ethereum/infrastructure/poa-network.md). 

xDai is the USD-stable coin that is a representation of Dai but lives on xDai Chain, instead of Ethereum mainnet. xDai is the native coin on xDai Chain and is used as the currency and for transaction fees on the network. You can use the [TokenBridge](https://dai-bridge.poa.network/) to convert Dai from Ethereum Mainnet to xDai on xDai Chain


##How to use the Burner Wallet
First, it’s suggested at the moment to use the Burner Wallet without MetaMask. While it’s possible to use MetaMask, it is not necessary and adds some overhead. Suggested use right now would be in a mobile browser or in a private browser tab (to avoid MetaMask).

####Wallet Generation
Upon visiting [https://xdai.io](https://xdai.io) a wallet is automatically generated and your private key is stored in a cookie in your browser. There are multiple ways to backup and restore your Burner Wallet in the Advanced section.

![](/assets/images/burner_advanced.png)

* Private Key: Show private key and save it somewhere. This can be inserted into the Private Key box in the future and upon hitting create, the wallet will be restored.
* Seed Phrase: Create any string of words or phrase that you want and hit create. This will create a wallet tied to that phrase and you can reenter it and pull it up at any point. WARNING: Doing this the first time will create a NEW wallet.

####Getting xDai
As previously mentioned, xDai is a representation of Dai running on a POA sidechain. This means that you must lock up Dai on the Etheruem mainnet to be minted xDai tokens. The Burner Wallet makes this easy through the Exchange section of the page.

![](/assets/images/burner_exchange.png)

You can start with just ETH or Dai. If you start with ETH you must go ETH > Dai > xDai using this page. Once complete, you have xDai in your wallet.

####Exiting xDai
Leaving the xDai chain is just as easy as getting on but in reverse. Simply go to the Exchange page and convert from xDai to Dai and then onto ETH if you want.

####Sending and Receiving xDai
Sending and Receiving xDai is extremely easy. Simply get the address of whoever you want to send to or scan a QR code which is generated inside the wallet. Users can also request funds via the Request option which generates a link for others to drop in their browser.

## Resources

* [Website](https://xdai.io)
* [Github](https://github.com/austintgriffith/burner-wallet)
* [Introduction to Burner Wallet](https://medium.com/gitcoin/ethereum-in-emerging-economies-b235f8dac2f2)
* [Burner Wallet Video](https://youtu.be/k1Ssz1dvcpk)
* [xDai Chain Explained](https://medium.com/poa-network/poa-network-partners-with-makerdao-on-xdai-chain-the-first-ever-usd-stable-blockchain-65a078c41e6a)

