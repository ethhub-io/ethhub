# Bskt

## Description

Bskt allows creating portfolios of tokens.

To create a Bskt portfolio, one needs to deploy a smart contract providing underlying token addresses, their weights, and the base unit of the portfolio.

Once the contract is deployed, anyone can interact with it by minting new portfolio tokens in exchange for the underlying assets. These assets can then be redeemed by the owner of portfolio tokens. Portfolio tokens are ERC20 tokens that can be traded and put into another portfolio.

In case some of the underlying tokens become untransferable (e.g. the `transfer` function was paused by the token smart contract owner), users can skip that token during redemption. Alternatively, a portfolio owner can `extract` this token from the portfolio, creating a new one without accessing the user funds.

The owner of a Bskt portfolio can also `pause` creation of the new portfolio tokens in case they want to deprecate the portfolio. An owner can’t `pause` redemption of the underlying assets.

## Important links

* Website: https://cryptofinlabs.github.io
