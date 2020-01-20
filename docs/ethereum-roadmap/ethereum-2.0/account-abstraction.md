title:  Account Abstraction

description:  An explanation of account abstraction on the Ethereum network and the steps being made to achieve this goal.

# Account Abstraction

## Introduction

Data abstraction in computer science is the practice of information hiding.  This increases the ability of a computer system to be used at a higher level with less knowledge of the processes going on underneath.

Consider the software developer.  A high level programming language is used to create virtual interactions between objects.  The programmer does not need to know how to write the 1's and 0's that compose the machine code that runs physically in the memory and processor.  This is an example of data abstraction.

On the Ethereum network there are currently two types of accounts.  External accounts are wallets from which cryptocurrency is transacted in send and receive functions that exist outside of the EVM (Ethereum Virtual Machine).  Contract accounts are "smart contracts" that exist in the EVM.

The EVM is a virtual computer that exists on the Ethereum blockchain.  A series of OPCODES have been hard programmed into the Ethereum blockchain to be able to act as a virtual machine; memory, storage, and processing in the execution of smart contracts. 

Ethereum account abstraction has the goal of reducing from two account types down to one, a contract account.  The single account type will have the functionality to transact both coin and contract.  Developer and user will no longer need to make a distinction between account type since transacting will be moved fully into the EVM and off of the blockchain protocol.

Account abstraction is going to be an Ethereum 2.0 implementation and there is still fierce debate about the methodology in so doing. 

## Possible Implementation Methods

As described by Ethereum co-founder Vitalik Buterin

### Lazy full abstraction

* How it works: the only type of account is a contract. There is one transaction type, which has the following fields: [gas, addr, data]. Executing the transaction consists of playing a message, with msg.sender being some standard “ENTRY_POINT” address (eg. 0xff…ff), msg.to being the addr, and the gas and data being the provided values. Users are expected to store funds in contract accounts, where the code of the contract interprets the provided data as an ABI encoding of [nonce, signature, gasprice, value, data], verifies the nonce and signature, pays gas to the miner, sends a message to the desired address with the desired value, and then asks for a refund for the remaining gas.

* Pros: makes the protocol very simple. apply_tx becomes a very trivial wrapper around apply_msg.

* Cons: requires fairly complex code inside of each account to verify the nonce and signature and pay gas. Second, requires fairly complex code in the miner to determine what transactions actually are guaranteed to pay for gas. Third, it requires additional logic for the sender and the miner to create new accounts. Finally, it introduces the possibility that, with accounts constructed in a “non-standard” way, a transaction with the same hash could get included multiple times.

The miner’s problem is as follows. The miner needs to verify, in O(1) time, that a given transaction actually is guaranteed to pay for gas if the miner decides to process the transaction and try to include it in the block. In an abstraction system, this could involve asking the miner to run some code, say, with a limit of 200000 gas, but the miner would need to be sure that, after this happens, the transaction execution is in a state where the gas is paid for, and the payment cannot be reverted. Currently, the protocol handles this automatically; in full abstraction, this must all be implemented in code, and possibly in a fairly complex way.

### Remove nonce abstraction

* How it works: same as above, except a transaction also has a nonce field. A rule is added that a transaction’s nonce must equal the account nonce, and that the nonce is incremented upon a successful transaction.

* Pros: removes the possibility of a transaction appearing in multiple places.

* Cons: increases base protocol complexity slightly, and remove the possibility of alternative schemes (eg. UTXOs, parallelizable nonces)

### Standardize signature scheme

* How it works: add a byte-array field sig to the transaction. In the top-level message, add to the transaction’s return data sighash ++ sig, where sighash is the sha3 of the transaction not including the sig.

* Pros: makes signature verification much simpler.

* Cons: increases base protocol complexity slightly.

### Add BREAKPOINT opcode

* How it works: add an opcode BREAKPOINT, which has the property that if a transaction throws after a breakpoint, it only reverts up to the breakpoint.

* Pros: makes it much easier for the miner to detect if a transaction pays for gas; the miner’s code would only need to be something like “run for N steps or until a breakpoint, see that the breakpoint has been reached, and that gas has been paid for”.

* Cons: deep and fundamental change to the EVM. Historically not the best idea.

### Add PAYGAS opcode

* How it works: takes as input one argument (gasprice), immediately transfers the gasprice * tx.gas to a temporary account, and then at the end of executing the transaction refunds any unused gas.

* Pros: makes paying for gas simpler, and particularly does not require the transaction to include merkle branches to process a call to the coinbase. Avoids the overhead of a call to the coinbase.

* Cons: increases base protocol complexity. Also does not allow abstracting gas payment, eg. paying with ERC20 tokens.

### Gasprice + PANIC

* How it works: a transaction adds a parameter gasprice. At the start of execution, gasprice * startgas is subtracted. A PANIC opcode is added, which can only be called in a top-level execution context (ie. if msg.sender == ENTRY_POINT) and where (tx.gas - msg.gas) <= PANICLIMIT (eg. PANICLIMIT = 200000). If this opcode is triggered, then the entire transaction is invalid. A user account would make sure to check the signature and nonce within the limit, preventing invalid transactions from consuming gas. Miners would run transactions with a sufficient gasprice and reject those that panic.

* Pros: account code is simple, and miner code is simple, while still adding full signature and nonce abstraction

* Cons: increases base protocol complexity slightly. Also does not allow abstracting gas payment, eg. paying with ERC20 tokens. Third, does not provide flexibility in how much time signature verification can take (though Casper already enforces a limit, so the limit can be set to be the same value).
One possible variant is to simply make the transaction invalidity behavior be part of the behavior of THROW if called in a top-level context with the given amount of remaining gas.

### Combine PANIC and PAYGAS

* How it works: remove PANIC. Instead, have all exceptions have behavior equivalent to PANIC if PAYGAS has not yet been called.

* Pros: allows accounts to set their own base verification gas limit. A miner can run the algorithm of running the code for up to N gas, where N is chosen by the miner, until PAYGAS has been called. Also, removes the need for gasprice to be part of the transaction body.

* Cons: makes the output state of a message slightly more complicated, as it also needs to carry the information of whether or not a PAYGAS opcode was triggered and if so with what gasprice.

### Salt + code in transaction

* How it works: a transaction has two new fields: salt and code. If the target account of a transaction is nonempty, then these two fields must be empty [variant: are ignored]. If the target account is empty, then the last 20 bytes of sha3(salt + code) must equal the account, and if this is the case then the code is put into that position in the account code [variant: is used as init code].

* Pros: creates a standard and clean way to create new accounts.

* Cons: adds protocol complexity.

### Newly created account pays

* How it works: a transaction can be a contract creation transaction by specifying a salt and code. If the target address is empty, then it takes funds from that address to pay for gas, and then creates the contract.

* Pros: similar to existing contract creation.

* Cons: sending the first transaction from an account takes an additional step.

##  Minimally Simple Account Abstraction without Gas refunds

As described by Ethereum co-founder Vitalk Buterin:

This is an account abstraction proposal that achieves significantly greater simplicity, and greater generality, than anything proposed so far, but at a price: transactions whose gas costs are not completely static may end up overcharging gas.

The proposal is simple. Add an opcode BREAKPOINT, with the property that a function call that fails after a BREAKPOINT reverts only up to the BREAKPOINT. User account code would in general be structured as follows:

verify_nonce()
verify_signature()
send(coinbase, x)
breakpoint()
do_stuff()
do_more_stuff()

After the execution hits the BREAKPOINT opcode, the block proposer is certain that they will get compensated for including the transaction. Note that in this model, refunds for unused gas are not possible.

To add more flexibility, add another opcode, DECREASE_LIMIT, which decreases the remaining gas limit without consuming gas. This would allow for account code where the gas limit of a transaction can be determined in the “header” (ie. before the send and BREAKPOINT).

### Consequences

* apply_msg and apply_tx become identical (fee market reform 7 can be done at the per-block level), greatly reducing complexity

* The ABI would need to specify the max gas consumption of each function call, so that tight maximums can be more easily computed

* Does not require static analysis of code

* Would lead to some inefficiency in cases where gas costs truly are variable (the most common use case being CREATE2’ing a contract if and only if it does not exist yet), as the user would need to pay for the higher level of consumption even if the lower level of consumption is more frequent

* Implements full abstraction, so we would lose the tx hash uniqueness guarantee

## Security Considerations

To pay for the computing resources of nodes and miners and to incentivize the use of efficient code, there is a Gas cost associated with interactions of smart contracts.  

One of the attack vectors for the Ethereum blockchain is DoS (denial of service) by creating transactions that are computationally intensive.  The efforts seen above are intended to be able to charge the correct amount of Gas without allowing an attack vector for DoS.

## Resources

* [Abstraction in Computer Science](https://link.springer.com/article/10.1007/s11023-007-9061-7)

* [Tradeoffs in Account Abstraction Proposals](https://ethresear.ch/t/tradeoffs-in-account-abstraction-proposals/263)

* [A recap of where we are at on account abstraction](https://ethresear.ch/t/a-recap-of-where-we-are-at-on-account-abstraction/1721)

* [Maximally Simple Account Abstraction without Gas Refund](https://ethresear.ch/t/maximally-simple-account-abstraction-without-gas-refunds/5007)

* [Work to Natively Integrate Eth1 into Eth2](https://ethresear.ch/t/work-to-natively-integrate-eth1-into-eth2/5573)

* [The Ethereum Virtual Machine - How does it work?](https://medium.com/mycrypto/the-ethereum-virtual-machine-how-does-it-work-9abac2b7c9e)
