title: Oracles on Ethereum - EthHub

description: Oracles refers to a number of decentralized protocols building means for smart contracts to access data from the world outside Ethereum.

# Oracles

## Summary
An oracle provides real-world off-chain data and submits this information to a blockchain to be used by smart contracts.  Typically this is a data feed provided by a third party service.

## The Oracle Problem 

Since smart contracts on Ethereum are fully self-contained and any information or access to off-chain data is restricted, certain types of smart contracts are reliant on an outside provider (an oracle) of off-chain data points.  The problem ('the oracle problem') is that you now have a decentralized smart contract with a centralized key point of failure. The issue with this is obvious to anyone who values decentralization. 


## Solutions

Solutions to the oracle problem center around ways to both validate the data being queried and also place this data on chain in both an available and non-centralized manner. Solutions to these problems include consensus based truth, schelling point oracles (e.g. prediction markets), staked reporters (skin-in-the-game), trusted execution environoments (TEEs),  and many combinations of the various game theoretic crypto-economic security measures.  


## Resources
[Decentralized Oracles](https://medium.com/fabric-ventures/decentralised-oracles-a-comprehensive-overview-d3168b9a8841)