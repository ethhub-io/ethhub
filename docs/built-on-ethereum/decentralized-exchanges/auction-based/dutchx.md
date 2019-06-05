# DutchX

## Description

The DutchX is a decentrealized exchange for ERC-20 tokens based on the Dutch auction principle. DutchX uses the [Dutch auction](https://en.wikipedia.org/wiki/Dutch_auction) principle which attempts to fix issues faced by other decentralized exchanges such as front running, issues with low liquidity, and third party risk.

## How an auction works
1. Sellers deposit tokens they want to sell to the exchange and pick what token they want in return.
2. Once $1,000 threshold in deposits for the pair is reached, the auction starts at 2x the previous closing price.
3. Price of the pair starts falling according to a price decreasing function.
4. Bidders can now begin to place their bids and can immediately claim tokens bought even if auction isn't closed yet.
5. Once all sell quantity is accounted for, the auction clears and everyone who bid pays that price for their tokens. This means those who bid higher can come back and claim more tokens.

## Interface examples

Sellers:
![](/assets/images/slowtrade.png)

Buyers:
![](/assets/images/fairdex.png)

## Resources

* [Documentation](https://dutchx.readthedocs.io/en/latest/index.html)
* [GUI for Sellers](https://slow.trade)  
* [GUI for Bidders](https://fairdex.net/)   
* [Introducing the DutchX](https://blog.gnosis.pm/introducing-the-gnosis-dutch-exchange-53bd3d51f9b2)
* [Main Benefits of DutchX](https://blog.gnosis.pm/the-main-benefits-of-the-dutchx-mechanism-6fc2ef6ee8b4)
