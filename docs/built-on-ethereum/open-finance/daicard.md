# Daicard

## Summary

[Daicard](https://daicard.io) is a Dai payment channel solution created by [Connext](https://connext.network/). Daicard uses the concept of payment hubs which is a L2 solution build on top of Ethereum, allowing for instant and micro-fee transactions.

![](/assets/images/daicard_splash.png)

## How to Use Daicard

### Getting Funds

There are multiple ways to get funds onto your Dai card. The first would be to directly deposit into your wallet. You can deposit ETH or Dai. If you deposit ETH, it will be auto collateralized into Dai.

![](/assets/images/daicard_deposit.png)

You can also request funds from someone else who is already using Daicard. This can be done by clicking the request button and entering in how much you’d like to request. A link will be generated and can be send to the person you want to request from.

![](/assets/images/daicard_request.png)

### Sending Funds

There are two different ways to send funds. If the receiver already has a Daicard, then it’s best to just use the simple send functionality.

If the receiver has never used Daicard, you can use the Link function. This will allow anyone to click this link and receive the funds, even if they’ve never used Daicard before.

![](/assets/images/daicard_send.png)

### Settings

It’s possible to backup your wallets seed and restore it in any browser, at any time.

![](/assets/images/daicard_settings.png)

## FAQ

**When I deposit ETH into a channel and I receive dai, is the ETH being automatically sold to Connext?**

A: Sort of. The hub swaps the Dai for Eth in the channel so that you now have custody over Dai and the hub now has custody over Eth instead. The hub actually just stores this in it’s collateral reserves in the contract which it then uses either for gas or when users cash out in Eth. We do expect that most users who enter with Eth will leave with Eth (and the same for Dai) so we expect it to even out. 

**If I deposit 1 ETH into a channel can I later withdraw 1 ETH from that channel? For example, if the price of ETH goes up while my ETH is in a channel and I then withdraw it, do I get the value of the ETH at the time of withdraw or at the time of deposit?**

A: You are trading into Dai when you use the card. So you have the benefit of being protected from volatility but, obviously, this means that you wouldn’t see the upside of an Eth bull run. (I guess we should make this more clear to users so that they don’t unwittingly trade their Eth away when they don’t want to). The best way to think about it might be as a decoupled swap -> pay -> swap. We can also allow for the user to hold and pay in Eth only, but we don’t currently support it to keep things simple. 

*”Connext is live in production with a custodial version of our Hubs. Noncustodial hubs are coming in late January 2019, and networked Hubs (nodes) will be shipped with V2 in mid-late 2019" So this is the beta for non-custodial, yes? Can you nutshell the difference between this approach and one that uses POA?**

A: Custodial is sort of a funny word for channels. When we say that, we mean that the payment is custodial, not your funds. Your funds are always your own and can be exited at any time even if the hub disappears. However, in a custodial hub it’s possible for the payment to be intercepted by the hub (if they choose not to route a given payment). Obviously, if this happened and you knew about it you’d exit the system so the risk is small.

Given this, noncustodial just means that it’s lightning-style multihop. The hub is not able to redeem the sender’s channel payment until they complete the receiver’s channel payment.

The noncustodial code is actually in the repo right now, but the payments are currently custodial because we’re trying to keep collateralization simple until we understand user behavior better. Hoping to activate it sometime week after next.

The primary difference between channels and sidechains are that channels are a solution that scale up the existing blockchain whereas sidechains move load onto other chains. Both have their uses but IMO channels are better for widespread horizontal infra that aims to serve ALL users and sidechains/plasma are better for app-specific use cases. Think of the difference between the Visa network and Uber.

It’s easier to get in and out of channels because they’re on the main Ethereum chain. The downside is collateral. We hope to reduce collateral burden by decentralizing ourselves into something that looks like lightning once enough demand/liquidity exists. Sidechains don’t have this restriction but also suffer from the same scalability problems as base chains when they get big. Also, it’s unclear how economic finality on sidechains works. If the sidechain goes down, all funds are gone. Igor is working on this afaik with a plasma-style exit game.

**Does connext have to put reserves in the channel itself? Can this run or cap out?**

A: Yes! The ChannelManager contract (0x083c8bc6bc6f873091b43ae66cd50abef5c35f99) has Eth and token reserves in it. All channels are automatically collateralized based on the reserves in this contract. If it runs out, channels would stop being collateralized and this would interrupt payments.

**If a channel stops being collateralized, how will users be alerted that payments are currently interrupted (e.g. does the UI show an alert and grey’s out the SEND button)? How long might outages last, on average?**

A: We definitely need to show a UI alert and grey out. Outages shouldn’t last long, realistically there’s going to be enough collateral on the contract (We would make sure that collateral would always be 2-3x volume in channels or something like that). The main “outage” would be the time it took for the hub to recollateralize - we wait 2 block confirmations and there is a signed state exchanged to confirm so like… 20s max on rinkeby? Same amount of time as deposit.

I definitely think interrupting payments is not acceptable so want to find a way to avoid it in all but the most extreme of edge cases.




