# A Graphical Guide to Compound

## Summary
The Compound protocol is a series of smart contracts that allows users to earn interest on their Ethereum assets. What makes the protocol unique is that there isn’t a direct counterparty that you have to negotiate with, instead a user only needs to supply their assets and they will immediately begin earning interest. There is no hassle of having to discuss a rate or a period of time your assets are required to be locked up for. Users can also borrow different assets from the protocol against the ones that they have supplied. The supply and borrow rates for each asset are dynamically calculated based on the supply and borrow demand of the protocol.

In addition, the list of assets that can be supplied and borrowed on Compound can be found [here](https://compound.finance/markets).

![coin stack](/docs/assets/images/compound_guide/coin_stack.jpg)

Lastly, this guide is meant to give a basic understanding of what the Compound protocol is. I recommend [this article](https://medium.com/compound-finance/the-compound-guide-to-supplying-borrowing-crypto-assets-94821f2950a0) if you are interested in how to use Compound website specifically.


## Supplying Assets and Receiving cTokens   
When anyone supplies an asset to the Compound protocol they are then given the corresponding cToken for their deposit. For example if someone locks up Dai they will receive an amount of cDai in return. cTokens are a deposit split that shows that you have added liquidity to the protocol and can be used to reclaim the underlying asset that was supplied plus the accrued interest, which is accrued for each block that is mined while the asset is locked in the protocol.

![comp supply](/docs/assets/images/compound_guide/comp_supply.png)

It is important to note that the amount of cTokens a user receives isn’t a 1 to 1 ratio to the token that was added. For example, if you supplied 100 Dai to the protocol you wouldn’t receive 100 cDai. The reason for this is that the cDai has an ever improving redemption rate based on the interest rate set by the protocol. Let’s say that for every 1 Dai you supply the protocol gives you 9 cDai. As time passes your Dai is earning interest, but your wallet will still only hold 9 cDai. However, when you go to redeem your cDai for Dai the rate will have improved, let’s say to 8 cDai for 1 Dai based on the interest accrued. As a result, your interest is paid to you in an ever improving exchange rate between the cToken and the underlying asset. 

![cToken Redeem](/docs/assets/images/compound_guide/cToken_redeem.png)

If you would like a more detailed example, the one below is from [Compound’s website](https://compound.finance/ctokens). 

_Let’s say you supply 1,000 DAI to the Compound protocol, when the exchange rate is 0.020070; you would receive 49,825.61 cDAI (1,000/0.020070)._

_A few months later, you decide it’s time to withdraw your DAI from the protocol; the exchange rate is now 0.021591:_

_Your 49,825.61 cDAI is now equal to 1,075.78 DAI (49,825.61 * 0.021591)_

_You could withdraw 1,075.78 DAI, which would redeem all 49,825.61 cDAI_

_Or, you could withdraw a portion, such as your original 1,000 DAI, which would redeem 46,315.59 cDAI (keeping 3,510.01 cDAI in your wallet)_


## The Utility of cTokens 

cTokens makes it easier for both users and developers to interact with the Compound protocol. cTokens are [ERC20 tokens](https://docs.ethhub.io/guides/a-straightforward-guide-erc20-tokens/), which is the defacto token standard on Ethereum. Almost all developers are already familiar with the ERC20 standard and most users have wallets that support ERC20 tokens. 

Having Compound’s balances tokenized allows for a greater amount of compossibility. Since these tokens can be easily transferred like any other token, they can be created with one address, sent to a cold storage address that has never been touched, and securely earn interest. They can also be sold on an exchange or even potentially used as collateral for a loan on a different platform. 

![cToken uses](/docs/assets/images/compound_guide/cToken_uses.png)

In addition, cTokens can also be incorporated into other financial products. One of the most interesting integrations is the ETH 20 MA Crossover Yield Set II from TokenSets. This set rebalances between cUSDC and Eth based on the 20 Day simple moving average of Ether’s price. Therefore, by using cUSDC, when the set rebalances away from Eth not only has it moved to a stable position, it will also be earning interest for you until the next rebalance. 

## Borrowing Assets
Once users have locked up assets and hold cTokens, they are then able to borrow different assets from the protocol. For example a user that has locked Dai to create cDai, can then use that cDai as collateral to borrow BAT. Borrowing in most cases allows users to be able to either short or long an asset. It is important to note that there are certain collateral ratios for each asset based on the quality of the collateral. If the price of the asset you borrowed versus the one that you supplied diverges too far, then you have the possibility of having a portion of your collateral liquidated.

![comp borrow](/docs/assets/images/compound_guide/comp_borrow.png)

Another thing to point out is that the rate to borrow an asset from the protocol is usually higher than the rate for supplying an asset. The reason behind this is that since the protocol pools liquidity not all the funds that have been supplied will be borrowed, yet all funds added earn interest. As a result the borrow rate must be higher than the supply rate to make sure that all users that are supplying assets are given a rate even if their assets aren’t currently being borrowed. 

## Governance with Comp Tokens
Previously, the upgradability of the protocol’s smart contracts was solely controlled by Compound Labs. However, with their recent upgrade and release of their governance token Comp, the upgrades are now controlled by a governance contract that makes changes based on votes from Comp token holders. This governance upgrade can be thought of as if a single key controlled the protocol, but that key was broken into small pieces and distributed to different people across the internet. Now if a change is to be made, then enough Comp token holders need to come together and “reforge” the key to push the change. In addition, in order to counteract voter apathy, Comp token holders are able to delegate their voting power to another address which can vote on their behalf.

Specific details on how voting works from the [Compound FAQ](https://medium.com/compound-finance/faq-1a2636713b69). 

_Any address with more than 100,000 COMP delegated to it may propose governance actions, which are executable code. When a proposal is created, the community can submit their votes during a 3 day voting period. If a majority, and at least 400,000 votes are cast for the proposal, it is queued in a Timelock contract, and can be implemented after a 2 day waiting period._

![comp voting](/docs/assets/images/compound_guide/comp_voting.png)

## Liquidity Mining
In the past, the main method of governance token distribution was by having an ICO. Recently however, many defi projects have been shifting to a new method called liquidity mining. Liquidity mining is a process where users lock up assets into a protocol and over time are rewarded with governance tokens. Users can now lock up liquidity into Compound and based on the amount that they have either supplied or borrowed are given a certain amount of Comp tokens. The main idea behind this is that it rewards people that are using the protocol, rather than having an ICO which rewards speculators. Currently, the distribution of Comp through liquidity mining is going to last a little over 4 years.

Additional details can be found [here](https://medium.com/compound-finance/expanding-compound-governance-ce13fcd4fe36)

_4,229,949 COMP will be placed into a Reservoir contract, which transfers 0.50 COMP per Ethereum block (~2,880 per day) into the protocol for distribution._ 

![liqu mining](/docs/assets/images/compound_guide/liqu_mining.png)

## Conclusion
The Compound protocol creates a simple way for users to earn interest on their assets without having to negotiate with a counterparty. Future users won’t even know that they are using the protocol, they will simply add funds and the apps they are interacting with will then pass them onto Compound. With no counterparty to negotiate with and no hard time lock requirements, Compound makes it seamless to earn interest on your Ethereum assets.

## Resources

* [Compound Docs](https://compound.finance/docs)
* [Compound FAQ](https://medium.com/compound-finance/faq-1a2636713b69)
* [Compound cTokens](https://compound.finance/ctokens)
* [Expanding Compound Governance](https://medium.com/compound-finance/expanding-compound-governance-ce13fcd4fe36)

