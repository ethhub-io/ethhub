# ExcitePrice

## Summary

ExcitePrice is a non-custodial decentralized trading platform that allows traders to use “Events” which are contracts between the trader and ExcitePrice to speculate on cryptocurrency prices. Events give traders multiplied exposure (similar to leverage) to cryptocurrencies without having to hold the underlying asset. ExcitePrice is an Ethereum dapp and runs on a smart contract system. Excite Price currently allows users to open short and long positions on BTC, ETH, EOS, Tron, Cardano and Bitcoin Cash.

## Event Types Information

ExcitePrice is a limited loss trading platform, meaning the maximum a trader can lose on any event is 100% of what they put in. This means traders will never owe any debts to ExcitePrice, and because the platform is non-custodial there is no concept of a negative account balance.

The events are designed to be interactive and specialized to suit different trading strategies and opportunities. Each type of event has a name and defined details. The following will explain the different types of events that are currently available on ExcitePrice.

Before describing the different types of events, it's important to understand specific terms commonly used on the platform, as well as have an understanding how multiplier works in general.

Terminology

Long: betting the price of the underlying asset will increase.

Short: betting the price of the underlying asset will decrease.

Entry Price: the price of the asset at the time a trader enters an event.

Exit Price: the price of the asset at the time a trader exits a position or the position is automatically closed.

Maximum Upside Potential: the maximum percentage gain a trader can make on an event.

Upside: the formula by which a trader’s gains are measured.

Downside: the formula by which a trader’s losses are measured.

Multiplier: increased exposure to price swings, allows a trader to simulate trading with more money.

Liquidation Price: the underlying asset's price at which the trader’s position will be closed and his money will be lost.

Exposure Events: contracts between the trader and ExcitePrice.

Event Types
ExcitePrice has four available event types, namely Simple Match, Perpetual, High Roller, and Super High Roller. Each event offers a different type of trading opportunity, with different payouts, risk metrics, etc. The following will describe in detail how each of these events work:

1. Simple Match
The Simple Match event is the most basic event offered by ExcitePrice. This event is great for traders trying out the platform for the first time. The event enables traders to go long or short with multiplier. The payout is capped at 50% profit, and the upside is discounted by 50%. This event does not have a liquidation price and carries a fixed contract duration. Once you enter the event it will stay open until the expiration, when the exit price is determined.

For example, a trader enters long BTC with $1000, when Bitcoin is $8,000 with multiplier of 100X. The trader has entered into a 1-hour market, meaning that in one hour the platform will get the new price of Bitcoin and determine if the trader will earn or lose money. In our example, an hour goes by and Bitcoin increases to a new price of $8,100. This means, Bitcoin has appreciated by 1.25%. The trader’s position in this case would increase in value from $1000, to $1500, a 50% gain. If you apply the traders 100X multiplier to a 1.25% increase it would mean a gain of 125%, however because the Simple Match event has Maximum Upside Potential capped at 50%, the trader would be given a 50% return.

Maximum Upside Potential: 50%

Upside = (multiplier * price change) * 50%

Downside = (multiplier * price change)

Liquidation Price: None.

2. Perpetual
The Perpetual event is a basic event, similar to the Simple Match, but has a cap of 100% and no upside discount. Instead, there is an established liquidation price, which is set at 50% above the bankruptcy price. This event is great for traders who are looking to trade without restrictions on expiration times and like control over when they can close out their positions.

For example, a trader could enter an event long, with $1000 when Bitcoin is $8,000 with multiplier of 1000X. At the time the trader enters this position, his liquidation price will be $7,996. This means that if Bitcoin hits or goes lower than $7,996 the trader will lose his $1000 entirely.

However, if the price of Bitcoin appreciates by 0.05% (+0.05% * 1000 multiplier = +50%), the trader’s position will increase to $1500. At which point he may either decide to close the position or keep it open. If the trader closes the position, his $500 profit will be realized, and he will receive back a total of $1500.

If the trader keeps the position open and the price of Bitcoin jumps up 1%, the trader’s position will automatically close itself and pay double what he originally traded with, so in this example, the trader would realize a $1000 profit, receiving back a total of $2000.

Maximum Upside Potential: 100%

Upside = (multiplier * price change)

Downside = (multiplier * price change)

Liquidation Price: 50% above bankruptcy price.

3. High Roller
The High Roller event is a slightly riskier event than either the Simple Match or Perpetual, however it does have a higher potential upside of 300%. The risk comes from a 6X multiplier attached to the downside. This means that if the price of your asset falls by -1% the system calculates the percentage decrease as if it was a -6% decrease. This event does not have a liquidation price and is fixed to specific contract durations. This event is better suited for traders looking to enter short term risky trades without there being much potential for downside.

For example, a trader goes $1000 long for 2 minutes with multiplier of 10X, when the price of Bitcoin is $8,000. If the price of Bitcoin decreases by 1%, then the trader will lose twice the potential upside (3 * 2 = 6X). This means that the trader will lose 60% instead of losing just 10%. If the price of Bitcoin goes up by 1% then the trader would still make 10%, meaning he would gain $100. The maximum potential returns the trader can earn in a High Roller Event is 300%. So if the price appreciates in this case by 30% then the trader’s position will automatically close giving him a profit of $3,000 and will receive back $4000.

Maximum Upside Potential: 300%

Upside = (multiplier * price change)

Downside = (price change * 6) * multiplier

Liquidation Price: None.

Super High Roller
The Super High Roller is highest risk highest return event offered by ExcitePrice. The potential upside of the event is 500%. Like the normal High Roller, this event has a 6X multiplier attached to the downside, and like the perpetual this event also has a liquidation price, and like the Simple Match the upside is discounted at 50%. This event can be offered as either perpetual or as a fixed contract duration.

Maximum Upside Potential: 500%

Upside = (multiplier * price change) * 50%

Downside = (price change * 6) * multiplier

Liquidation Price: 50% above bankruptcy price.

## Resources

* [Website](https://exciteprice.com/home)
* [Twitter](https://twitter.com/ExcitePrice)
