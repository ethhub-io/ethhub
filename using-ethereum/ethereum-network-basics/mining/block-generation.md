# Block Generation

## Block structure

![Diagram of an Ethereum block](https://i.stack.imgur.com/eOwjD.png) A block consists a header, which includes information identifying the block and linking it to the rest of the chain, and a body of transactions. Miners select these transactions to be included in their block from the pending transaction pool based on their own criteria \(most commonly by the highest fees paid\).

## Block times

The Ethereum network is designed to produce a block every 12 seconds. Block times will vary based upon how long it takes miners to generate a hash that meets the required mining difficulty at that moment. 12 seconds was chosen as a time that is as fast as possible, but is at the same time substantially longer than network latency. A 2013 paper by Decker and Wattenhofer in Zurich measured Bitcoin network latency and determined that 12.6 seconds is the time it takes for a new block to propagate to 95% of nodes. The goal of the 12 second design is to allow the network to propagate blocks as fast as possible without causing miners to find a significant number of stale blocks.

## Etherscan example explained

All of the following examples are based on [this block](https://etherscan.io/block/6969122).

### Height:

This number current number of blocks that exist in the Ethereum blockchain

_Example: 6969122_

### TimeStamp:

The UNIX timestamp for when the block was collated

_Example: 29 secs ago \(Dec-28-2018 05:01:54 PM +UTC\)_

### Transactions:

The transactions included in the block

_Example: 43 transactions and 91 contract Internal Transactions in this Block_

### Hash:

The hash of the block itself

_Example: 0xa6312ebbcea717972344bc598c415cb08e434c01b94d1c2a9b5415624d2c2b81_

### Parent Hash:

The hash of the block from which this block was generated, also known as its parent block.

_Example: 0xa48e2ad13de011f127b345a81a91933d221f5a60d45852e7d7c2b5a07fda9fe2_

### Sha3Uncles:

A SHA3 hash of the uncle block data included the block

_Example: 0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347_

### Mined By:

The address of who mined the block and received the block reward

_Example: 0x5a0b54d5dc17e0aadc383d2db43b0a0d3e029c4c \(SparkPool\) in 2 secs_

### Difficulty:

A number that represents the difficulty required to mine this block

_Example: 2,511,265,102,818,605_

### Total Difficulty:

A number that represents the total mining difficulty of the chain up until this block

_Example: 8,470,035,190,867,378,349,872_

### Size:

The size of the block file in bytes

_Example: 13160 bytes_

### Gas Used:

The total amount of gas used by all the transactions included in this block

_Example: 7,997,769 \(99.97%\)_

### Gas Limit:

The total limit of the amount of gas that could have been used by all transactions included in this block

_Example: 8,000,029_

### Nonce:

A hash of the generated proof-of-work. This value will be null when a block is pending

_Example: 0x1510f53c063f9669_

### Block Reward:

The total amount of Ether \(ETH\) given to the address which mined this block. This value includes the total block reward issued by the protocol combined with the fees/gas paid by all the transactions included in this block

_Example: 3.032755182184797136 Ether \(3 + 0.032755182184797136\)_

### Uncles Reward:

The total amount of Ether \(ETH\) awarded to the uncle blocks included in this block

_Example: 0_

### Extra Data:

This is an optional 32-byte value that can be used for storing information on the blockchain. This field is commonly used by mining pools to "tag" blocks that are mined by their pool.

_Example: sparkpool-eth-cn-hz2 \(Hex:0x737061726b706f6f6c2d6574682d636e2d687a32\)_

## Resources

* [https://github.com/ethereum/wiki/wiki/Design-Rationale](https://github.com/ethereum/wiki/wiki/Design-Rationale)
* [https://ethereum.stackexchange.com/questions/268/ethereum-block-architecture](https://ethereum.stackexchange.com/questions/268/ethereum-block-architecture)
* [https://github.com/ethereum/wiki/wiki/JSON-RPC](https://github.com/ethereum/wiki/wiki/JSON-RPC)
* [https://ethereum.stackexchange.com/questions/10548/what-does-every-field-in-block-means](https://ethereum.stackexchange.com/questions/10548/what-does-every-field-in-block-means)

