# Running a Node

#### What is a light node?
The light node listens to full nodes it is connected to and only receives relevant Blockchain data periodically. Light nodes are useful for low capacity devices, such as embeded devices or mobile phones, which can't afford to store multiple dozen Gigabytes of data.

#### What is a full node?
Full nodes are responsible for maintaining the balance of the Blockchain. They receive new transactions and blocks, all while participating in their validation. Considering their validative responsibilities, they are required to hold more precise records of the Blockchain when compared to light nodes, which are only there to listen to full nodes.

#### What are the simplest commands for running a light node and full node? 
Light node:
 - **geth**: --syncmode "light"
 - **parity**: --light

Full node:
 - **geth**: --syncmode "fast"

The parity default settings are the best for full nodes.

#### Table of node settings

Parity

Client / Mode                     | Block Number   | Disk Space | CLI flags                |
==================================|================|============|==========================|
parity light                      | 5_600_000      |  89M       | --light                  |
parity warp pruning fast -ancient | 5_600_000      |  20G       | --no-ancient-blocks      |
parity warp pruning fast          | 5_600_000      |  82G       |                          |
parity pruning fast               | 5_600_000      |  78G       | --no-warp                |
parity pruning fast fatdb trace   | 5_600_000      | 108G       | --fat-db on --tracing on |
parity pruning archive            | 5_600_000      | 1.1T       | --pruning archive        |

Geth

Client / Mode                     | Block Number   | Disk Space  | CLI flags                          |
==================================|================|=============|====================================|
geth light                        | 5_600_000      |  1G         | --syncmode "light"                 |
geth fast                         | 5_600_000      |  100G       |                                    |
geth archive full                 | 5_600_000      |  850G       | --gcmode=archive --syncmode "full" |

#### Node Benchmarks
