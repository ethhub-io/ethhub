Patterns
========

## Data modelling
[Augur-style](https://sourcegraph.com/github.com/AugurProject/augur-core@master/-/blob/source/contracts/trading/Order.sol) data encapsulation. 

### Characteristics

 * `library` defined for a named entity. e.g. `Order`
 * `struct Data {}` within the library is the abstract data type to be passed around. e.g. `Order.Data`
 * function `create` which returns an instance of `Data`. 
 * other related types (such as enum's and constants) are also encapsulated by this library. e.g. `Order.Types`
 * pure helper functions that compute higher-level information on this entity. e.g. `getOrderId` which computes the ID from the hash of the data

### Example
```sol
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
