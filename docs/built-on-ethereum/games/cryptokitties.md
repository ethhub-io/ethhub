# CryptoKitties

![An example of a CryptoKitty](https://www.cryptokitties.co/images/kitty-eth.svg)

## Summary

CryptoKitties is a game built on Ethereum that allows users to collect and breed cryptographically unique creatures called CryptoKitties. Each kitty exists on the Ethereum blockchain as an ERC721 non-fungible token. Each ERC721 kitty has a unique ID, genes that defines its appearance and rarity, a generation that affects the kitty's rarity, and a cooldown that determines how long the cat must wait before it can breed again. For a small fee, players can breed two kitties together to create a new ERC721 kitty. The new kitten's traits are randomly determined through the combination of the traits of its parents and an on-chain random number oracle, although its generation will always be greater than that of its parents.

### Generation

The game began with the creation of 50,000 Generation 0 kitties. The smart contract does not allow any more Generation 0 kitties to be created beyond 50,000. Whenever two kitties breed, the generation of their offspring is equal to the highest generation of either parent plus one. For example, if two Generation 0 kitties breed, they create a Generation 1 kitty. If a Generation 0 and a Generation 8 kitty breed, they create a Generation 9 kitty. This mechanic of increasing a kitty's generation with each breed preserves the rarity of lower gneeration Cryptokitties, preventing users from flooding the marketplace and destroying the value of all kitties.

### Genes

Each kitty has 48 genes, spanning twelve different gene categories. Within each category, each kitty has a dominant gene, a hidden-1 gene, a hidden-2 gene, and a hidden-3 gene. The dominant genes are the genes that determine a kitty's appearance. When breeding two kitty's together, the offspring is likely to get the dominant gene of either parent for each category, but has a small chance of getting one of the parent's hidden-1 genes, an even smaller chance of getting one of the parent's hidden-2 genes, and a very small chance of getting one of the parent's hidden-3 genes. When two parent's have genes that match up in a certain way, then there is a small chance of that gene "mewtating" into a higher-tier gene that neither parent had originally had. The community has created calculators for determining the probabilities of the genes of a given offspring, such as [KittyCalc](https://kittycalc.co), and the community has created trait charts that demonstrate the mewtation process, which can be found at [KittyHelper](https://kittyhelper.co/tools/traits/) and at [KittyFyi](https://www.kitty.fyi/trait-charts).

For a more detailed explanation, see the section labeled [Genes](https://guide.cryptokitties.co/guide/cat-features/genes) under the CryptoKitties Guide below.

### Cooldown

Each cat has a cooldown that determines how long a user must wait before they can breed the cat again. A kitty's initial cooldown is determined by its generation. The higher the generation, the worse the cooldown the kitty is born with. Cooldowns range from 1 minute to 1 week. Each time that a kitty breeds, its cooldown increases, to a maximum of one week. The kitty's offspring will not be born until the cooldown has completed.

## History

### Gods Unchained crossover

On January 10th, 2019, a partnership between CryptoKitties and the trading card game [Gods Unchained](https://docs.ethhub.io/built-on-ethereum/games/gods-unchained) was [announced](https://medium.com/@fuelgames/cryptokitties-x-gods-unchained-7f69c80b5e5b). The partnership was significant because it featured extensibility for the first time between two blockchain games. Extensibility is the ability to use an NFT from one game in another game. Between Jan. 10th to Jan. 28th, 2019, Cryptokitties users were able to convert any Cryptokitty into a Gods Unchained statue for a small fee. The Cryptokitty statue is purely used for aesthetic purposes in the Gods Unchained game, allowing a Gods Unchained user to decorate their board while playing a match but having no in-game effect on the game's mechanics. However, each statue's appearance differed depending on the on-chain genes that the Cryptokitty had, meaning that certain kitty's with rarer genes could create rarer statues. This demonstrates how one blockchain game can make use of the information contained within the ERC-721 tokens of another blockchain game, opening up an entire universe of possibilities for interoperability and cross-game collaboration. Noteably, the statue-creation process did not destroy the Cryptokitty that was used, meaning that a user could take a single NFT token and use its unique information in a variety of different games and different contexts, while still retaining its value in the original blockchain game.

The event also provided the ability for Crypokitty's users to create, buy, or win Gods Unchained-themed Cryptokitties, including creating one of 3,992 TallyThePurrocious fancy cats, buying one of 380 Aeoncat special edition cats, or winning the one and only Hyppurrion exclusive cat. Details can be found on the [Cryptokitties Gods Unchained page](https://www.cryptokitties.co/gods-unchained).

### Decentraland crossover

CryptoKitties are accessible in Picture Frames as part of the [Decentraland](https://docs.ethhub.io/built-on-ethereum/collectibles/decentraland/) Scene builder. The partnership was announced in December of 2017 and are ready to go with Decentraland's expected launch during the Summer 2019.

## Resources

* [Website](https://www.cryptokitties.co/)
* [Twitter](https://twitter.com/cryptokitties)
* [CryptoKitties Guide](https://guide.cryptokitties.co/guide/)
* [Cryptokitties API](https://docs.api.cryptokitties.co/)
* [KittyHelper](https://kittyhelper.co/)
* [Kitty.fyi](https://www.kitty.fyi/getting-started)
* [KittyCalc](https://kittycalc.co)
* [KittyBounties](https://kittybounties.com/)
* [Heaven.Cat](https://heaven.cat/)
* [CryptoKitties Analytics](https://www.curiousgiraffe.io/cryptokitties/)
* [LocalKitty](https://localkitty.co/)
* [CryptoKitties Russian Guide](https://blog.kotobaza.co/)
* [KittyRace](https://kittyrace.com/)
