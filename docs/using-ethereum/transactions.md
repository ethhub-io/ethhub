title: Ethereum Transactions - EthHub
description: Explanation of Ethereum transactions including gas and the fee market.

# Transactions

## Gas

### Summary

Understanding 'gas' is fundamental to understanding how the Ethereum network functions.

The EVM - the Ethereum Virtual Machine \(EVM\) running on each Ethereum node - is an emulation of a computer system. One example of a regular, non-blockchain virtual machine is the VirtualBox software, which allows you to emulate computer systems \(guests\) on your physical hardware \(hosts\). Any operation in the EVM consumes CPU cycles, disk access, memory, of the hosting machine \(which carries a cost\). This cost is paid via Ethereum 'gas'.

In order to prevent "overload" of the host, each operation on the EVM consumes a certain amount of gas. Accessing memory or writing to disk have differing costs with each EVM operator setting an upper limit to the gas consumed during execution of a contract. So, if a malicious operator crafted a smart contract that went into an infinite loop, each loop would consume some gas and eventually run into the limit, at which point the EVM would abort the execution of this contract. Essentially, the larger, more complex the contract and the more operations it performs, the more expensive it is to run it.

This process creates a fee market using gas prices where users decide how much they are willing to pay for each unit of gas. Due to the gas block limit, the fee market almost always determines what order transactions are mined in because miners looking to profit will select the transactions with the highest fees.

There are many key components to a transaction that are important to understand:

| Term | Description |
| :--- | :--- |
| Gas | Unit for how much computation work is done. |
| Gas Price | How much you’re willing to pay per gas for work \(in gwei\) |
| Tx Cost | Gas used \* Gas Price |
| Gas Limit | Max gas you’ll pay for a certain tx |
| Gas Block Limit | Max gas allowed in a block |

## Fee Market

### Summary

The Ethereum gas block limit means that there is a limit to how many computations can occur per block. This creates a fee market for gas where miners will accept higher paying transactions first. Users that want their transactions to be included first can pay a higher gas price than those who aren't in a rush. Key concepts to understand about the fee market are:

| Term | Description |
| :--- | :--- |
| Gas Price | How much a user is willing to pay per gas for work \(in gwei\) |
| Safe Low | A price that will be mined in a reasonable time \(&lt;50 blocks\) |
| Standard Gas Price | The average gas price being paid by the network |
| Fast Gas Price | A price that will be mined within the next few blocks |

## Signing Transactions on Ethereum

### Interacting with Smart Contracts via Etherscan and MetaMask
1. Navigate to the Etherscan page for the Contract Address
2. If the code and ABI have been uploaded to Etherscan, you should be able to access the 'Write Contract' tab
3. Click the connect with MetaMask button
4. Follow the documentation provided by the Contract's author to complete your transaction.

### Interacting with Smart Contracts via MyCrypto
1. Navigate to **[MyCrypto](https://mycrypto.com/).** *Verify the SSL (little green lock next to URL) to avoid phishing sites.* 
2. Click the **'Contracts'** tab
3. Enter the Ethereum address of your desired contract in the **'Contract Address'** field
Enter the **'ABI / JSON Interface'** provided by the contract author into the **'Contract ABI'** filed.
*The ABI allows MyCrypto to display named functions that are invokable for the provided contract address. This code can sometimes be found on the Etherscan page for the contract address under the 'Code' tab.*
4. Click **'Access'**
5. Follow the contract documentation provided by the contract author to use the desired contract function in the **'Read / Write Contract'** dropdown.
6. Follow the MyCrypto prompts to access your wallet in order to sign and submit your transaction.

#### Important notes
* If you are experiencing troubles, be sure that you are using the 'Ethereum' (mainnet) from the dropdown in the top right hand corner
* It never hurts to cross reference the average gas limit and gas price on either [Etherscan](https://etherscan.io/) or [EthGasStation](https://ethgasstation.info/)

### How To Make An Offline Transaction via MyCrypto
To learn how to generate, sign, and broadcast a transaction locally and offline via MyCrypto, see [this guide](https://support.mycrypto.com/offline/making-offline-transaction-on-mycrypto.html). 

## Signing & Verifying Messages on Ethereum

Ethereum private keys can be used to sign messages. Signatures can be used to verify that a given user owns an Ethereum address.

To learn how to sign and verify signatures via MyCrypto, see [this guide](https://support.mycrypto.com/addresses/signing-and-verifying-messages.html). 



## Resources

* [How does Ethereum work, anyway?](https://medium.com/@preethikasireddy/how-does-ethereum-work-anyway-22d1df506369)
* [EthGasStation](https://ethgasstation.info/)

