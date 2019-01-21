# Staking Logistics

## Why would I want to stake my Ether?

For staking your ETH and attesting to correct blocks, you will be rewarded with ETH through a network wide interest rate as well as receive a portion of network transaction fees. Details can be found [here](https://docs.ethhub.io/ethereum-roadmap/serenity-phases/eth-2.0-economics).

## What are the minimum requirements to stake?

* A minimum of 32 ETH per validator
* Computer
* Internet connection

## What software do I need to run to stake?

There are two main types of software to be aware of when considering staking on Ethereum:

* Beacon nodes: This is the hub for your validators. 
  * Stores canonical state, handles peers and incoming sync, propogates blocks and attestations.
  * Has a gRPC server that clients can connect to and provides a public API.
* Validator clients: Talks to your beacon node and signs blocks. You can have multiple of these at 32 ETH each.
  * Stores important secrets such as RANDAO reveal, proof of custody for shared data and BLS private key.
  * Can swap underlying beacon nodes efficiently
  * Tracks shared state execution data and data blobs the validator has signed.

This means that there are three possible combinations of software to run:

1. Beacon node only
2. Beacon node + validator client
3. Beacon node + multiple validator clients

## What are the hardware requirements to run this software?

Still TBD. Ideally we can get minimum requirements for all three setups mentioned above.

## What happens if I lose my internet connection while staking?

The key to being a validator is making sure you are only voting for blocks and therefore securing the network. Therefore, there is a slight penalty if your validator client goes offline at any point. There are two scenarios where this can happen:

1. If blocks are finalizing and you're offline, you can lose x% of your deposit over a year where x=current\_interest
   * For example, if the current interest rate is 5%, you would lose 0.0137% of your deposit every day, but gain that for every day you're online.
2. If blocks aren't finalizing \(&gt;33% of validators are offline\) and you're offline, you can lose 60% in 18 days. 

If at any point your deposit drops below 16 ETH, you will be removed from the validator set entirely.

## How long is my Ether locked up if I stake?

There is a withdraw queue that you are placed into when wanting to withdraw ETH from your validator. If there is no queue, then the minimum withdraw time is 18 hours and adjusts dynamically depending on how many people are withdrawing at that time.

## Resources

* [Beacon and Validator explanations](https://twitter.com/terenc3t/status/1070738081337106432)
* [Some details around staking from Vitalik](https://www.reddit.com/r/ethereum/comments/a41u9k/_/ebbm03t/?context=1)

