# State Channels

## What Are State Channels?

State channels are a very broad and simple way to think about blockchain interactions which could occur on the blockchain, but instead get conducted off of the blockchain, without significantly increasing the risk of any participant. The most well known example of this strategy is the idea of payment channels in Bitcoin, which allow for instant fee-less payments to be sent directly between two parties. 

State channels are very similar to the concept of payment channels in Bitcoin’s Lightning Network, but instead of only supporting payments, they also support general ‘state updates.’ For example, moves conducted in a game of Chess could be updated in a state channel and only broadcasted to the Ethereum network once the game is finished. This magnifies the number of computation developers can move off-chain.

## How do State Channels work?

State channels work by “locking up” some portion of blockchain state into a multisig contract, controlled by a defined set of participants. The state that is “locked up” is called a state deposit. For instance, this might be an amount of ether or an ERC20 token, but could also be a cryptokitty or an ENS domain name.

After the state deposit is locked, channel participants use off-chain messaging to exchange and sign valid ethereum transactions without deploying them to chain. These are transactions that could be put on chain anytime, but are not.

A basic breakdown:

![](../.gitbook/assets/state-channels.png)

1. Part of the blockchain state is locked via multisignature or some sort of smart contract, so that a specific set of participants must completely agree with each other to update it.

2. Participants update the state amongst themselves by constructing and signing transactions that could be submitted to the blockchain, but instead are merely held onto for now. Each new update “trumps” previous updates.

3. Finally, participants submit the state back to the blockchain, which closes the state channel and unlocks the state again (usually in a different configuration than it started with).

## What are the differences between State Channels and Plasma?
