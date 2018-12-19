# ERC721

ERC721 describes a non-fungible token \(NFT\), i.e. an asset that can’t be consumed while you are making use of it. Right now ERC721 is in a draft state, however, people are already using it. Each ERC721 token is unique, they are all different and they may even have different values according to their owner. They may represent ownership over physical or digital assets, such as houses, art masterpieces, loans and, why not? Kitties.

Each NFT is identified through an `uint256` ID. They may be transferred through two different funcions:

* A safe transfer function `safeTansferFrom()` which verifies that the `msg.sender`,i.e. the user that triggered the function, is the owner of the token or an authorized user allowed to transfer the token.
* A non-secure trasfer `transferFrom()`, where there is no preliminary authorization verification. The token developer is responsible for implementing a piece of code in this function that verifies that the responsible for calling the function is authorized to do so. In this function, the user calling it must also verify that the receiver is entitle for receiving the token. If these verifications are not performed, the tokens could be lost forever.

ERC721 tokens must implement the proposed ERC165 interface. This standard allows the detection of the interfaces implemented by a contract. This is really useful, as it allows to detect the interface that a token implements and, consequently, adapt the method/code to interact with it.

Source: [https://medium.com/coinmonks/anatomy-of-an-erc-an-exhaustive-survey-8bc1a323b541](https://medium.com/coinmonks/anatomy-of-an-erc-an-exhaustive-survey-8bc1a323b541) Reference: [https://github.com/ethereum/EIPs/blob/maste%20r/EIPS/eip-721.md](https://github.com/ethereum/EIPs/blob/maste%20r/EIPS/eip-721.md)

