title: ERC20 - The Token Standard - EthHub

description: ERC20 allows the implementation of a standard API to ensure the interoperability between tokens

# ERC20

## Summary

ERC20 allows the implementation of a standard API to ensure the interoperability between tokens. It offers basic functionalities to transfer tokens, obtain account balances, get the total supply of tokens, and allow token approvals.

To define an ERC20 token you need:

* The address of the contract
* The number of tokens available

However, there are other optional values for additional information such as:

* Name, for example “Augur Token”
* Symbol, such as “REP”
* Decimals, or how much you can divide the token. You can chose from 0 to 18 decimal values

ERC20 defines two types of events, `Transfer()`, triggered when tokens are transferred and `Approve()`, used for every successful call of the `approve()` method. This token may also include functions such as `allowance()`, `approve()`, and `transferFrom()` to offer advanced functionalities and authorize some other Ethereum address to utilise your tokens on your behalf. This other Ethereum address could be a smart contract designed to handle tokens or just another account.

## Resources

* [Github](https://github.com/ethereum/EIPs/issues/20)
* [Wiki](https://theethereum.wiki/w/index.php/ERC20_Token_Standard)

