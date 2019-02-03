title: Ethereum Development
description: Ethereum’s primary artifact is the smart contract, written in the programming language Solidity

# Development

## Summary

Ethereum is a blockchain, first-and-foremost. Its primary artifact is the smart contract, written in the programming language Solidity, a language with syntax similar to JavaScript. Currently Vyper is being developed to offer another choice when developing smart contracts, with syntax similar to Python.

## Patterns

### Data modelling

[Augur-style](https://sourcegraph.com/github.com/AugurProject/augur-core@master/-/blob/source/contracts/trading/Order.sol) data encapsulation.

### Characteristics

* `library` defined for a named entity. e.g. `Order`
* `struct Data {}` within the library is the abstract data type to be passed around. e.g. `Order.Data`
* function `create` which returns an instance of `Data`. 
* other related types \(such as enum's and constants\) are also encapsulated by this library. e.g. `Order.Types`
* pure helper functions that compute higher-level information on this entity. e.g. `getOrderId` which computes the ID from the hash of the data

### Example

```text
library Order {
  struct Data {
        // Contracts
        IOrders orders;
        IMarket market;
        IAugur augur;

        // Order
        bytes32 id;
        address creator;
        uint256 outcome;
        Order.Types orderType;
        uint256 amount;
        uint256 price;
        uint256 sharesEscrowed;
        uint256 moneyEscrowed;
        bytes32 betterOrderId;
        bytes32 worseOrderId;
    }

  enum Types {
    Bid, Ask
  }

  function create(IController _controller, address _creator, uint256 _outcome, Order.Types _type, uint256 _attoshares, uint256 _price, IMarket _market, bytes32 _betterOrderId, bytes32 _worseOrderId) internal view returns (Data) {
        require(_outcome < _market.getNumberOfOutcomes());
        require(_price < _market.getNumTicks());
        require(_attoshares > 0);

        IOrders _orders = IOrders(_controller.lookup("Orders"));
        IAugur _augur = _controller.getAugur();

        return Data({
            orders: _orders,
            market: _market,
            augur: _augur,
            id: 0,
            creator: _creator,
            outcome: _outcome,
            orderType: _type,
            amount: _attoshares,
            price: _price,
            sharesEscrowed: 0,
            moneyEscrowed: 0,
            betterOrderId: _betterOrderId,
            worseOrderId: _worseOrderId
        });
    }

  function getOrderId(Order.Data _orderData) internal view returns (bytes32) {
        if (_orderData.id == bytes32(0)) {
            bytes32 _orderId = _orderData.orders.getOrderId(_orderData.orderType, _orderData.market, _orderData.amount, _orderData.price, _orderData.creator, block.number, _orderData.outcome, _orderData.moneyEscrowed, _orderData.sharesEscrowed);
            require(_orderData.orders.getAmount(_orderId) == 0);
            _orderData.id = _orderId;
        }
        return _orderData.id;
    }
}
```

## Testing

Not only does Test-Driven Development make your codebase stellar, it's extremely useful when interacting with a new language with different semantics. And surprisingly, it's actually not so hard in Ethereum development to get started with it!

The Truffle framework makes it very easy to test contracts with Solidity and JS. Beware:

* while you can test contracts in Solidity, I highly advise you don't. The tooling is _very_ nascent, and Solidity itself has very few libraries already - you won't be able to load test data \(fixtures\) from files for example, since Solidity doesn't have an FS API like JS/Node does.
* for unit testing simple functions, Solidity comes in handy. However you might find using Remix IDE just as quick for accomplishing this to start with \(although you won't reap the benefits of having a test later when your code breaks ;\)\).

### Running a persistent test blockchain

A persistent chain is often useful when you want to test a frontend UI, and you need to persist the data you've transacted onto a blockchain. You can use Ganache \(née testrpc\) CLI to do this:

`ganache-cli -d --db ./ganache --gasPrice 1 --gasLimit 10000000 --networkId 123 -u 0 -u 1`

This will persist data to `./ganache` and most importantly set the network ID \(otherwise this is generated from system time on startup, and is not 'persistent' otherwise\).

#### Connecting MetaMask with your test blockchain wallets

When you run Ganache CLI, it will list private keys on first launch in hex form. You can import these into Metamask and then access your 100 ETH issued by default.

#### Gas

You will probably encounter issues with gas. Note that contracts cannot be bigger than 24,000 bytes, and transactions no bigger than 32kb \([source](https://ethereum.stackexchange.com/questions/47539/how-big-could-be-contract-size)\).

Contract creations take gas, which you can estimate with `estimateGas`. Gas is the internal Ethereum unit for pricing computation, and is converted at a fixed rate to Ether \(set by clients\), termed the **gasPrice**. It is measured in the smallest unit, which is gwei. The **gasLimit** is the maximum amount of gas that can be used in one setting.

An example of some gas arithmetic:

```text
estimateGas(YourContract)
=> 286056

# if we run a test blockchain with a gas price of 2 (2 units for 1 gwei)
ganache-cli --gasLimit 100000000000 --gasPrice 2

then the minimum amount to send with the transaction is:
286056 * 2 = 572,112 gwei
0.000572112 ETH
```

You might be tempted to set `gasLimit` to something like `1000000000000000`. This will break Metamask, as it can't encode that value into 53 bits for BigNumber \([see here](https://github.com/ethereumjs/ethereumjs-vm/issues/114)\).

#### Gas Units

| Unit | Amount per ETH |
| :---: | :---: |
| ETH | 1 |
| Finney | 1,000 |
| Szabo | 1,000,000 |
| Gwei | 1,000,000,000 |
| Mwei | 1,000,000,000,000 |
| Kwei | 1,000,000,000,000,000 |
| Wei | 1,000,000,000,000,000,000 |

### Debugging

Testing is important, but you will never ascertain as much information as to the execution of a contract as by using the official debugger tooling, the Remix IDE \([demo](https://remix.ethereum.org/), [docs](https://remix.readthedocs.io/en/latest/)\).

Remix is a big of a hack piece put together, but it works very well once you're using it correctly. It can run Solidity in a JavaScript VM, an injected Web3 provider \(e.g. Metamask\) or connect to your local Ganache / other setup on `http://localhost:8545`.

### Using Remix like a pro

Remix is a web app, so it doesn't have access to your file system \(whether you access it from remix.ethereum.org or as an Electron desktop app\). While you can copy-paste code in, it's much better to install `remixd`, which will expose a local folder to Remix.

1. Install it globally and save the dep - `npm install -g -S remixd`
2. Add this to your `package.json`.

   ```javascript
   {
     "scripts": {
       "remix": "remixd -s .",
      }
   }
   ```

   1. Run `yarn remix`

`remixd` knows to look into `node_modules` for imported contracts \(e.g. SafeMath\) from packages like OpenZeppelin, so we run it in our project root `.` rather than in `./contracts` as you might assume.

### Unit testing

Unit testing is for testing individual functions of your contracts.

### Integration testing

Integration testing generally requires multiple interactions from various users/contracts. Since this requires the use of multiple addresses, it is unsuitable to accomplish in Solidity as above.

#### Exposing contracts

You may encounter difficulty testing contracts due to the \(in\)visibility of methods/types, the lack of insertion point for validating data being returned, and so on. It is possible to test not the contract itself, but a wrapped contract for testing purposes only.

```text
contract Market {
  uint[] private orders;
  function doSomething() {}
}
```

How would we access `Market.orders` here?

```text
contract MarketForTesting is Market {
  function getOrdersCount() public returns (uint8) { return orders.length; }
}
```

#### Testing return values

When you call a method on a contract, and it updates state \(i.e. is not `view`/`pure`\), it must be transacted upon the network. In such case, the Web3 interfaces do not give you the return value of the method. This can be frustrating if you're trying to test such a value, so you can do something like so:;

```javascript
async function txWithReturnValue(method, ...args) {
  let [retval, tx] = await Promise.all([
    method.call(...args),
    method.sendTransaction(...args)
  ]);
  return retval;
}

await txWithReturnValue(Contract.method, 1, "0x123", { from: "0x12312", value: 2 });
```

#### Testing with various 'users'

You will want to test the contract's interaction from the POV of multiple users with different addresses \(whether it be human or other contracts\). This is quite easy to achieve.

Whenever you transact with a contract in calling a method, you have the option to specify the `from` address of who will be funding the tx. Below is a Truffle test which combines this with access to `accounts`, which is the same output as web3.personal.getListAccounts:

```javascript
const MyContract = artifacts.require("./MyContract.sol");

contract('MyContract', async (accounts) => {
  it('tests with various users', async () => {
    let instance = await MyContract.new();
    for(let i = 0; i < 5; i++) {
      let from = accounts[i];
      console.log(`Submitting tx from addr: ${from}`);
      let txid = await instance.yourMethod.sendTransaction(arg1, arg2, { from, });
    }
  })
})
```

### Resources

* [Ethereum Developer Tools List](https://github.com/ConsenSys/ethereum-developer-tools-list)

