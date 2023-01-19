# Deciphering a Transaction on Etherscan

## Summary

If you have started to dip your toe into the Ethereum world, chances are you have seen or been redirected to Etherscan. Etherscan is a block explorer, which allows users to view information about transactions that have been submitted to the blockchain, verify contract code, and visualize network data. This guide will focus on explaining the information that is displayed for different types of transactions on Etherscan.

## Components of an Ethereum Transaction on Etherscan

* **Transaction Hash:** A unique identifier that can be used to locate a specific transaction.
* **Status:** The current state of a transaction (Success, Failed, or Pending). 
* **Block:** The block number that the transaction was included in. 
* **Timestamp:** The time that the block was mined in UTC.
* **From:** The account that originally sent the transaction.
* **To:** The account that the transaction is addressed to.
* **Value:** The amount of Ether included in the transaction.
* **Transaction Fee:** The amount of Ether paid to the miner for processing the transaction, which is calculated by multiplying the amount of gas used by the gas price.
* **Gas Limit:** The upper limit of how much computational work and storage the sender is willing to expend on the transaction.
* **Gas Used by Transaction:** The amount of computational work and storage used in the transaction.
* **Gas Price:** The amount of Ether per unit of gas the user is willing to pay for the transaction, commonly denoted in a subunit of Ether known as Gwei. 1 Gwei = 1x10^-9 Ether.
* **Nonce:** The count of transactions sent out of the account. The number is initialized at 0 and is incremented by 1 for each transaction sent.
* **Input Data:** Information that is passed to a smart contract when a transaction is sent to its address. However, if the transaction is creating a contract, the contract’s bytecode is placed in the input data field.

*I recommend checking out this [article](https://blockgeeks.com/guides/ethereum-gas/) if you are not very familiar with how gas is used in Ethereum.*

## Gas and Ethereum Transactions

Reading data from the blockchain has no cost, however, when you want to change data recorded in the chain you are required to submit a transaction. In short, gas is a way of measuring the amount of computation and storage required to execute a change.

Transactions in Bitcoin are rather straightforward, you have an amount of BTC and you create a transaction that sends it to another address. With the complexity of smart contracts, Ethereum transactions can have a large range of effects. In order to make sure that a user appropriately pays for the complexity of their transaction, gas is used to measure how much computational work and storage is needed in order to execute it. 

When submitting a transaction, a user will specify a gas limit, which is the highest amount of gas the transaction is allowed to expend. The transaction will fail if it exceeds the limit. The gas price is the amount of Ether the user is willing to pay per unit of gas (most commonly expressed in Gwei. 1 Gwei = 1x10^-9 Ether). For transactions where not all of the gas is used, the remaining Ether is refunded back to the account that created the transaction.

## “Out of Gas” Error Message

There are a number of reasons why an Ethereum transaction might fail. The most common issue is that the transaction ran out of gas when the miner attempted to execute it. This will be apparent when you see a message that says “Warning! Error encountered during contract execution [Out of gas]” on Etherscan. This means that the transaction surpassed the gas limit that was specified when the transaction was created. 

Please use caution when setting the gas limit for a transaction that will be sent to a contract. If the limit is set too high the transaction might burn up all the Ether in your account. When a transaction runs out of gas, the proposed transaction fails, but the Ether that was dedicated to paying for gas is still given to the miner.

## Externally Owned Accounts (EOA) vs Contract Accounts

There are two different types of accounts in Ethereum. The first are externally owned accounts (EOA), which are derived from a private key and able to generate transactions to poke the Ethereum network to do something. The second kind are contract accounts, which are able to store and execute code only when prompted by a transaction from an EOA. There are three different types of transactions between these accounts: an EOA sending Ether to another EOA, an EOA creating a contract, or an EOA sending a transaction to a contract.

## Transferring Ether Between Two Externally Owned Accounts (EOA)

In the random transaction below, we can see that one externally owned account (EOA) is sending Ether to another EOA. We know this because the data input is empty, the To address isn’t labeled as a contract address, and the value field is filled out.

![](/docs/assets/images/etherscan_guide/EOA_to_EOA_tx.png)

When moving Ether, we are telling the Ethereum network please decrease my balance x amount and increase the other account’s balance by that amount. If the transaction is valid, then the global state of Ethereum updates the balances. In terms of gas considerations, a standard transfer of Ether from one EOA to another EOA costs 21,000 gas, which we can see is the amount used.

![](/docs/assets/images/etherscan_guide/EOA_to_EOA_diagram.png)

## Transferring ERC20 Tokens

One of the biggest differences between transferring ERC20 tokens versus transferring Ether is that the transaction is addressed to the Token’s contract address rather than the account we want to send the tokens to. In the random transaction below, the input data field includes the function we would like to call (in this case transfer). In addition, the inputs for the function, which includes the recipient's address along with the amount of tokens we want to send formatted in [hexadecimal](https://en.wikipedia.org/wiki/Hexadecimal). Etherscan marks the To account as the DAI contract address and added a field called Tokens Transferred to display the input data in a more human readable format.

![](/docs/assets/images/etherscan_guide/token_transfer_tx.png)

Typically, the value field is left empty for token transfers because we only need to update to the contract’s balances. Lastly, the gas cost for transferring ERC20 tokens can vary depending on how to contract was implemented.

![](/docs/assets/images/etherscan_guide/token_transfer_diagram.png)

## An Externally Owned Account (EOA) Creating a Contract

Below is the transaction that created the Ethhub contract wallet. The most notable difference for contract creation transactions is that the input data contains the bytecode for the contract’s logic. We can see that the contract’s address is displayed in the To field with “Created” next to it. 

![](/docs/assets/images/etherscan_guide/ethhub_creation_tx.png)

## Transferring Ether from an Externally Owned Account (EOA) to a Contract Account

If you are sending Ether to a contract address, the gas cost can vary from the standard 21,000 gas. 

![](/docs/assets/images/etherscan_guide/Eth_to_EthHub_tx.png)

Viewing the transaction above we can see that someone made an Ether deposit to the Ethhub contract wallet, which required 22,511 gas. This is because the contract wallet also emits a Deposit event when receiving Ether, which bumps the gas cost over 21,000. 

![](/docs/assets/images/etherscan_guide/Eth_EOA_to_contract_diagram.png)

That is why it is important to know what kind of account you are sending to before you assume that the gas cost will be 21,000 gas or else the transaction might run out of gas. In addition, there can be harmful side effects to sending a transaction to a contract that you aren’t familiar with because contracts are able to forward messages to other contracts. Meaning that calling a function or simply depositing Ether to a malicious contract could execute code that might yield a negative result. 

Please always make sure that you trust the contract that you are about to submit a transaction to and set a reasonable gas limit.

## Resources

* [Etherscan](https://etherscan.io/)
* [What is Ethereum Gas?](https://blockgeeks.com/guides/ethereum-gas/)
* [Transactions in Ethereum](https://medium.com/@kctheservant/transactions-in-ethereum-e85a73068f74)
