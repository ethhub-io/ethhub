title: The Dai Card

description: The Dai Card is a Dai payment channel solution created by Connext

# The Dai Card

## Summary

[Dai Card](https://daicard.io) is a Dai payment channel solution created by [Connext](https://connext.network/). The Dai Card uses  payment channel hubs - a L2 solution built on top of Ethereum - to allow for instant and micro-fee transactions for users and developers.

![](/docs/assets/images/daicard_splash.png)

## How to Use the Dai Card

### Getting Funds

There are multiple ways to get funds onto your Dai Card. The first is to directly send funds (i.e. "deposit") to the Dai Card's address. You can deposit either ETH or Dai. If you deposit ETH, it will be instantly and automatically swapped into Dai at the current Eth-Dai price.

Note: the beta version of the Dai Card imposes a $30 limit and will refund any deposits above this amount.

![](/docs/assets/images/daicard_deposit.png)

You can also request funds from someone else who is already using a Dai Card. This can be done by clicking the request button and entering in how much you’d like to request. A link will be generated and can be sent to the person you want to request from. The first transaction that is sent to your Card will take some extra time to execute. This is because, in the background, an onchain transaction is being done to set up your Card.

![](/docs/assets/images/daicard_request.png)

### Sending Funds

There are two different ways to send funds. If the receiver already has a Dai Card and you know their address, then it’s best to just use the simple send functionality.

If the receiver has never used a Dai Card before, you can use a Link payment instead. Link payments generate an unspent payment object which can be "claimed" by the recipient that produces the correct secret. Note that the link generated here contains the secret to redeem funds in plaintext, so you should be careful with it.

![](/docs/assets/images/daicard_send.png)

### Settings

It’s possible to backup your Card's seed and restore it in any browser, at any time. 

You can also restore this seed in other wallets such as Metamask, MyCrypto or TrustWallet. However, this will not give you access to the channel funds themselves, only the signing key used to control those funds.

![](/docs/assets/images/daicard_settings.png)

## FAQ

**When I deposit ETH into a Card and I receive Dai, is the ETH being automatically sold to Connext?**

A: Yes. Connext's payment channel hub automatically swaps any ETH for Dai that you deposit at market price. The swapped ETH then goes into the hub's collateral reserves, which is used either when users "cash out" in Eth or when more Dai needs to be bought by the Connext team.

Since it's much easier for most users to get access to Eth than Dai (and to off-ramp to fiat from Eth), Connext expects that this will make it simpler to use Dai for everyday payments.

**If I deposit 1 ETH into a channel can I later withdraw 1 ETH from that channel? For example, if the price of ETH goes up while my ETH is in a channel and I then withdraw it, do I get the value of the ETH at the time of withdraw or at the time of deposit?**

A: No. You are swapping into Dai when you use the Card. Users have the benefit of being protected from volatility but, obviously, this means that you wouldn’t see the upside of an Eth bull run. Since you're not meant to hold large amounts of value in your Card anyway (only daily spending cash), the upside that you would miss out on should be minimal.

**Is the Dai Card noncustodial?**

A: The concept of custodial is more nuanced for channels:

In Connext's payment channel hub system, your funds are *always your own* since you can exit the system at any time by sending your latest channel state to the payment channel contract. This can be done regardless of the status of the hub - i.e. it is completely uncensorable. Note, this assumes that you have access to your channel state - the Connext team is still working on making sure that this will always be the case.

A *payment* itself can be custodial. This means that for the brief moment that a payment is "in-flight", it can be intercepted and/or censored by the hub. Obviously, if this happened and you knew about it, you would exit the system so your financial risk is constrained by the size of the payment itself.

Payments can also be noncustodial using more complex mechanisms (such as lightning-style HTLCs or, in Connext's case, a dispute-based system called "threads).

Connext's system is live with custodial payments for now. The noncustodial payment code is in the hub and client codebase as part of the launch, but the team is still working on making sure that the user experience of noncustodial payments is seamless, and so they have kept it deactivated for the initial launch. They plan to reactivate it within the first couple of weeks of going live.

For a more in-depth breakdown of the current trust assumptions in the system and how the team plans to address them, please see Connext's Dai Card launch post [here](https://medium.com/@arjunbhuptani/introducing-the-dai-card-fc46520078d3).

**What is the difference between this approach and Sidechain/Plasma approaches like xDai?**

A: The primary difference between channels and sidechains are that channels are a solution that scale up the existing blockchain whereas sidechains shift load out onto other chains. Because channelized systems can be built on top of any underlying chain, they are theoretically better for widespread horizontal infrastructure that aims to serve ALL users whereas sidechain/plasma based solutions are better for application-specific use cases. Think of the difference between the Visa network and Uber.

At scale, sidechains and plasma suffer from the same scalability problems as the base chain, which would require creating further sub-chains or using channels to solve. Moving into and out of sidechains/plasma systems can be more difficult since it involves moving value across different chains, rather than within the base chain. In the event of a mass exit from the system (because the chain went down), it is also sometimes unclear how all users could move their value back onto the base chain. However, sidechains/plasma are *much* more flexible once within the system, do not require significant collateral lockuup to run, and do not require counterparties to be online/available.

Channels, on the other hand, are easier to get into and out of. They are also *much* cheaper to run/scale and funds can always be exited onto the base chain no matter the circumstances. The downsides of channel networks are that they require intermediaries to hold collateral in order to ensure that a transaction will be completed and that they require that those intermediaries (and counterparties) to be available when a transaction occurs. Note that the availability requirements can be improved with better conditional payment functionality.

**Does Connext have to put reserves in the channel itself? Can this run or cap out?**

A: Yes. The ChannelManager contract (0xdfa6edae2ec0cf1d4a60542422724a48195a5071) has Eth and Dai reserves in it. All channels are automatically collateralized based on the reserves in this contract. If it runs out, channels would stop being collateralized and this would interrupt payments.

**If a channel stops being collateralized, how will users be alerted that payments are currently interrupted (e.g. does the UI show an alert and grey’s out the SEND button)? How long might outages last, on average?**

A: The most noticeable instance of this occurring will be when a Card receives its first payment. For a standard payment, the sender's UI will state that the receiver's Card is still being set up and whill show a progress indicator. For a link payment, the redeem payment screen will state that the Card is being set up and will show a similar progress indicator. In both of these cases, collateralization of the channel occurs in the background and takes ~30-40s (block time + 2 block confirmations) to complete.

Aside from these instances, *most* payments should be instant. Connext is still working on better ways to optmistically allocate collateral to channels so users can expect the user experience around this to improve with time.

## Resources

* [DeFi Pulse](https://defipulse.com/connext)
* [Website](https://connext.network/)


