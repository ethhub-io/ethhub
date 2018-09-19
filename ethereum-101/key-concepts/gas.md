# Gas

Understanding gas is fundamental to understand how the Ethereum network functions.   
  
Every transaction on the Ethereum network requires computation power to execute. The measurement of how much computation power is required is called gas. Computational resources aren't free, therefore users requesting a transaction to be executed must pay for it.   
  
There is a limit to how much gas can be computed in any single block. This creates a fee market using gas price, where users decide how much they are willing to pay for each unit of gas. Due to the gas block limit, the [fee market](fee-market.md) determines what order transactions are mined in.  
  
There are many key components to a transaction that are important to understand:

| Term | Description |
| :--- | :--- |
| Gas | Unit for how much computation work is done. |
| Gas Price | How much you’re willing to pay per gas for work \(in gwei\) |
| Tx Cost | Gas used \* Gas Price |
| Gas Limit | Max gas you’ll pay for a certain tx |
| Gas Block Limit | Max gas allowed in a block |

