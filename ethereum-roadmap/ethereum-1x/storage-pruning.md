# Storage Pruning group
The questions to be answered are:
* What do we absolutely have to keep to comply with the Ethereum protocol?
* Do we always need to keep all the blocks? (maybe not, if we use backward sync, for example)
* Do we need to keep receipts, or just logs, how much (in Gb), or for how long?
* Do we need to always download the entire header chain or can we compress it (with STARK proofs for example)?
* Can we improve snapshot sync procedures (fast sync, warp sync) so that they prevent invalid state transitions (with Validity Proofs, for example)? 
