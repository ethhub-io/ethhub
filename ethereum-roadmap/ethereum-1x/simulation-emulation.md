# Simulation and Emulation Group

**Simulation** handles models of the software agents \(in our case Ethereum client software instances\), coarse enough to be performant, and fine enough to capture the important facets of the agents.

**Emulation** handles the actual software agents \(in our case the actual implementations of Ethereum like geth and parity\), placed into the virtual environments with lots of freedom to change parameters of virtual machines and the network connecting them.

Potential questions that simulation may be able to answer:

* Will uncle rate become much less of an indicator of the network congestion if most of the Ethereum nodes propagate blocks straight after verifying Proof Of Work \(instead of fully processing the block as they used to do\)?

Potential questions that emulations may be able to answer:

* What is the function that describes the relationship between the rate of success for snapshot synchornisations \(fast sync, warp sync\) and things like prevailing bandwidth and state history pruning threshold?

