# Gas

Understanding gas is fundamental to understand how the Ethereum network functions.   
  
The EVM - the Ethereum Virtual Machine running on each Ethereum node - is a mini-computer contained in a box. Somewhat like a VirtualBox contains a whole computer inside another computer. And, similarly to a VirtualBox, any operation in the EVM actually consumes CPU cycles, disk access, memory,... of the hosting machine.

In order to prevent "overload" of the host, each operation on the EVM carries a cost - consumes a certain amount of gas. To access memory is cheap. To write to disk is more expensive,... Each EVM operator sets an upper limit to the gas consumed during execution of a contract. So, if a malicious operator crafted a smart contract that went into an infinite loop, each loop would consume some gas and eventually run into the limit, at which point the EVM would abort the execution of this contract.

Essentially the larger and the more complex the contract and the more operation it performs, the more expensive it is to run it. Note that expensive is literally that - you need to pay Ether for execution.

This creates a fee market using gas price where users decide how much they are willing to pay for each unit of gas. Due to the gas block limit, the [fee market](fee-market.md) almost always determines what order transactions are mined in because miners looking to profit will select the transactions with the highest fees.  
  
There are many key components to a transaction that are important to understand:

| Term | Description |
| :--- | :--- |
| Gas | Unit for how much computation work is done. |
| Gas Price | How much you’re willing to pay per gas for work \(in gwei\) |
| Tx Cost | Gas used \* Gas Price |
| Gas Limit | Max gas you’ll pay for a certain tx |
| Gas Block Limit | Max gas allowed in a block |

