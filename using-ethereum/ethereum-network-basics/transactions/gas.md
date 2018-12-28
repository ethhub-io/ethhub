# Gas

Understanding 'gas' is fundamental to understand how the Ethereum network functions.

The EVM - the Ethereum Virtual Machine \(EVM\) running on each Ethereum node - is an emulation of a computer system. One example of a regular, non-blockchain virtual machine is the VirtualBox software, which allows you to emulate computer systems \(guests\) on your physical hardware \(hosts\). Any operation in the EVM consumes CPU cycles, disk access, memory, of the hosting machine \(which carries a cost\). This cost is paid via Ethereum 'gas'.

In order to prevent "overload" of the host, each operation on the EVM consumes a certain amount of gas. Aaccessing memory or writing to disk have differing costs with each EVM operator setting an upper limit to the gas consumed during execution of a contract. So, if a malicious operator crafted a smart contract that went into an infinite loop, each loop would consume some gas and eventually run into the limit, at which point the EVM would abort the execution of this contract. Essentially, the larger, more complex the contract and the more operations it performs, the more expensive it is to run it.

This process creates a fee market using gas prices where users decide how much they are willing to pay for each unit of gas. Due to the gas block limit, the [fee market](fee-market.md) almost always determines what order transactions are mined in because miners looking to profit will select the transactions with the highest fees.

There are many key components to a transaction that are important to understand:

| Term | Description |
| :--- | :--- |
| Gas | Unit for how much computation work is done. |
| Gas Price | How much you’re willing to pay per gas for work \(in gwei\) |
| Tx Cost | Gas used \* Gas Price |
| Gas Limit | Max gas you’ll pay for a certain tx |
| Gas Block Limit | Max gas allowed in a block |

