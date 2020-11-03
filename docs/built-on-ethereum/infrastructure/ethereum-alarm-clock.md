title: Ethereum Alarm Clock - EthHub

description: Ethereum Alarm Clock is a protocol that defines financial incentives for miners to include a transaction at a specified time.

# Ethereum Alarm Clock

## Description

Ethereum Alarm Clock \(EAC\) is a protocol for scheduled Ethereum transactions. The protocol defines financial incentives for miners to include a transaction at a specified time.

A user that wants to create a transaction which needs to be executed in the future can use EAC. To do so, he needs to specify a receiver \(whether it’s an account or contract\) as well as call data. He also needs to specify at which time the transaction should be executed by defining the start time and window size. Finally, a user needs to specify how big a miner reward will be. The execution of the transaction is not guaranteed due to possible network congestion, but setting a higher gas price and longer time window increases the chances of successful execution.

All EAC transactions are processed by TimeNode miners. These miners set up clients to track the transactions and execute them in a specified time. By doing so, they are eligible to claim a reward set up by the sender.

## Important links

* Website: [https://www.ethereum-alarm-clock.com](https://www.ethereum-alarm-clock.com)
* Github: [https://github.com/ethereum-alarm-clock](https://github.com/ethereum-alarm-clock)
* ChronoLogic: [https://chronologic.network](https://chronologic.network)

