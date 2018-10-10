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

#### Node Benchmarks
