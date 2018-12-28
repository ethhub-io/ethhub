# Plasma

## What is Plasma?

Plasma is a layer 2 scaling solution that was originally proposed by Vitalik Buterin and Joseph Poon in the original paper ['Plasma: Scalable Autonomous Smart Contracts'](https://plasma.io/plasma.pdf). Since then, many [flavours] (https://ethresear.ch/t/plasma-world-map-the-hitchhiker-s-guide-to-the-plasma/4333) of Plasma have been proposed that come with different sets of trade-offs.

Plasma is a technique for conducting off-chain (layer 2) operations while relying on the underlying Ethereum blockchain (layer 1) to ground its security. You may also see Plasma (and similar constructs) referred to as 'child chains'.

## How does Plasma work?
In order to understand how Plasma works, let’s take a look at how the technology could be used in a real-world example.

Let’s imagine that you are creating a digital-collectibles game on Ethereum. The collectibles will be ERC 721 non-fungible tokens (like Cryptokitties), but have certain features and attributes that lets users play against each other — like Pokemon Go. These kinds of complex operations are expensive to do on-chain, so you decide to use Plasma instead for your application.

Initially, smart-contracts are created on the Ethereum main-chain. These smart contracts serve as the “root” of the Plasma child-chain. This main chain entry contains the basic rules of the child-chain, records state hashes of the child-chain, and allows users to move assets between the Ethereum main-chain and the child-chain.

After rooting the child-chain in the main chain, a child-chain is created. This child-chain features its own consensus algorithm, independently from the Ethereum main-chain. Let’s use Proof of Stake (PoS) for this example. This consensus mechanism does not rely on miners using electricity to run a hashing algorithm but rather the block producers are economically incentivized to remain truthful by a collateral that will be destroyed in case of a bad actor behaving fraudulently. This consensus algorithm generally allows for faster block-creation times than PoW.

Now that the child-chain is initialized, the basic rules of the game can be set, deploying the actual game application smart contracts on the child-chain, which contains all of the game logic and rules. The collectibles are still ERC721 tokens, created on the Ethereum main-chain, and then transferred onto the child-chain using the plasma root.

Once the child-chain is active, the block producers periodically commit a validation to the main-chain, essentailly proofing that the current state of the child-chain is valid according to the consensus rules. When a user plays this game, they are executing the application, without ever interacting with the main-chain directly.

## What are the main benefits of Plasma?

* Plasma will help the Ethereum blockchain scale by taking operations off-chain.

* Because only a much smaller number of nodes (i.e. block producers) have to process transactions, fees can be much lower and operations can be faster.

* Plasma will help to get rid of unnecessary data in the main-chain.

* Plasma is compatible with various on-chain scaling solutions such as sharding, various block sizes, etc.

## Does Plasma have drawbacks?

The main concern related to the current Plasma proposal is what would happen if everyone using a child-chain tried to exit the sidechain at the same time. In the case of a mass withdrawal, there might not be enough capacity on the Ethereum main-chain to process everyone’s transactions within the challenge period, meaning users could lose funds. Fortunately, there are many possible techniques for preventing this, e.g. by extending the challenge period in a way that is responsive to demand for withdrawals.

## Resources: 
* [Ethereum Plasma Explained] (https://medium.com/@argongroup/ethereum-plasma-explained-608720d3c60e)
* [Construction of a Plasma Chain] (https://blog.omisego.network/construction-of-a-plasma-chain-0x1-614f6ebd1612)
* [Plasma Design Comparison] (https://docs.google.com/spreadsheets/d/1Hs1-ddKwLG8xrqIXFrYUJzTEH2SjsATFXhgISG1ypzI/edit#gid=0)
* [An Introduction to Application-Specific Sidechains] (https://medium.com/loom-network/million-user-dapps-on-ethereum-an-introduction-to-application-specific-sidechains-c0fdc288c5e5)
* [Scaling Ethereum with Plasma: Georgios Konstantopoulos of Loom (Podcast)] (https://podcast.ethhub.io/scaling-ethereum-with-plasma-georgios-konstantopoulos-of-loom)
