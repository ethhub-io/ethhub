title: State Channels - EthHub
description: State channels are a layer 2 scaling solution for Ethereum.

# State Channels

## What Are State Channels?

State channels are a very broad and simple way to think about blockchain interactions which could occur on the blockchain, but instead get conducted off of the blockchain, without significantly increasing the risk of any participant. The most well known example of this strategy is the idea of payment channels in Bitcoin, which allow for instant fee-less payments to be sent directly between two parties.

State channels are very similar to the concept of payment channels in Bitcoin’s Lightning Network, but instead of only supporting payments, they also support general ‘state updates.’ For example, moves conducted in a game of Chess could be updated in a state channel and only broadcasted to the Ethereum network once the game is finished. This allows ethereum applications to "move" transactions off-chain, increasing the usefulness of the network as a whole.

## How do State Channels work?

State channels work by “locking up” some portion of blockchain state into a multisig contract, controlled by a defined set of participants. The state that is “locked up” is called a state deposit. For instance, this might be an amount of ether or an ERC20 token, but could also be a cryptokitty or an ENS domain name.

After the state deposit is locked, channel participants use off-chain messaging to exchange and sign valid ethereum transactions without deploying them to chain. These are transactions that could be put on chain anytime, but are not.

A basic breakdown:

![](/assets/images/state_chans.png)

1. Part of the blockchain state is locked via multisignature or some sort of smart contract, so that a specific set of participants must completely agree with each other to update it.
2. Participants update the state amongst themselves by constructing and signing transactions that could be submitted to the blockchain, but instead are merely held onto for now. Each new update “trumps” previous updates.
3. Finally, participants submit the state back to the blockchain, which closes the state channel and unlocks the state again \(usually in a different configuration than it started with\).

Since all exchanged transactions are equally valid as far as the blockchain is concerned, state channels need a mechanism to ensure that the latest off-chain state \(i.e., the latest move in our chess game\) is the one that ultimately gets settled on the main chain. Thus, if a party attempts to unilaterally close a channel, other parties in the channel have a period of time — a "dispute window" — in which they have an opportunity to submit a more recent state, thereby proving that fraud was attempted. Once an infraction is proven, the contract handles the resolution process, which typically involves punishing the guilty party by slashing their deposited funds \(though one could also simply update to the valid state and proceed accordingly\).

If the “state” being updated between participants was a digital currency balance, then we would have a payment channel. Steps 1 and 3, which open and close the channel, involve blockchain operations. But in step 2 an unlimited number of updates can be rapidly made without the need to involve the blockchain at all — and this is where the power of state channels comes into play, because only steps 1 and 3 need to be published to the network, pay fees, or wait for confirmations. In fact, with careful planning and design, state channels can remain open almost indefinitely, and be used as part of larger hub and spoke systems to power an entire economy or ecosystem.

## Difference between State Channels and Sidechains

### State Channel pros

* State channels have strong privacy properties: This is because everything is happening “inside” a channel between participants, rather than broadcast publicly and recorded on-chain. Only the opening and closing transactions must be public. Whereas in sidechains every transaction is published on the sidechain which is received by every participant on the sidechain irrespective of the fact that you are not interacting with all of the participants on the sidechain.
* State channels have instant finality, meaning that as soon as both parties sign a state update, it can be considered final. Both parties have a very high guarantee that, if necessary, they can “enforce” that state on-chain. 

### State Channel cons

* State Channels need 100% availability of all the participants involved: As we have discussed above that if anyone the participants goes unavailable, then this could prove costly to him. The participants can use a third party service to represent him if he goes unavailable \(see, for instance, [http://hackingdistributed.com/2018/05/22/pisa/](http://hackingdistributed.com/2018/05/22/pisa/)\), but the possibility of the representative getting attacked or bribed makes it a problem for state channels. Whereas in sidechains you don’t have to be available all the time you are on the sidechain.
* State channels are best used for applications with a defined set of participants: This is because the state deposit contract\(the contract used to lock the state\) must always know the participants/entities \(i.e. addresses\) that are part of a given channel. We can add and remove people, but it requires a change to the contract each time. Whereas in sidechains there is no such limitation on the movement of the participants.
* State Channels are particularly useful where participants are going to be exchanging many state updates over a long period of time: This is because there is an initial cost to creating a channel in deploying the state deposit contract. But once it is deployed, the cost per state update inside that channel is extremely low.

### Sidechain pros

* Sidechains are permanent. You don’t have create your own sidechain for specific purpose if there is one present: Sidechains are created and maintained once made. We don’t close sidechains, rather we lock the assets on sidechain to move back to the mainchain. This can be helpful in the way that anyone who is doing a specific task off blockchain/mainchain \(for eg. transacting in dogecoin\) will come to the same sidechain. So, you don’t have to create separate chains for every new participant. Whereas in state channels, an on-chain operation is required to add a participant to an existing channel. But projects such as Raiden network, and more generally the technique of meta-channels, offer a partial solution to this. They create a mesh of participants so you don’t have to create a new channel for every new participant you interact with. You can interact with participants indirectly creating a channel between you and recipient through some other participant who is common to both: you and the recipient.
* Sidechains allow cryptocurrencies to interact with one another: They add flexibility and allow developers to experiment with Beta releases of Altcoins or software updates before pushing them on to the main chain. Traditional banking functions like issuing and tracking ownership of shares can be tested on sidechains before moving them onto main chains.

### Sidechain cons

* Sidechains do not benefit from the security of the main-chain. A user interacting on a side-chain must trust the security properties of that sidechain, because if it compromised or malevolent, a user has no guarantee of withdrawal to the main-chain. In contrast, participants in a state channel can always return to the main-chain so long as they follow the protocol.
* Sidechains need a lot of initial investment to start off: To create a sidechain we need to have enough miners so that the network is safe from attackers. Also, we have to make sure that they are up and running. Whereas there is no blockchain involved in state channels. So, no such requirement is needed.
* A Federation is needed for sidechains: This adds another layer between the mainchain and the sidechain. This could prove as another weak point for the attackers to attack by bribing or attacking the federation. Whereas in state channel we just need a smart contract to do this for us.

## Resources

* [State Channels - an explanation](https://www.jeffcoleman.ca/state-channels/)
* [Making Sense of Ethereum's Layer 2 Scaling Solutions \(Josh Stark\)](https://medium.com/l4-media/making-sense-of-ethereums-layer-2-scaling-solutions-state-channels-plasma-and-truebit-22cb40dcc2f4)
* [Generalized State Channels on Ethereum \(Jeff Coleman, Liam Horne, and Xuanji Li\)](https://www.counterfactual.com/statechannels/)
* [State Channel Applications \(Liam Horne\)](https://medium.com/statechannels/state-channel-applications-1f170e7d542e)

