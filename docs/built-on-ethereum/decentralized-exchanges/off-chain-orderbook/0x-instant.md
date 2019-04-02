# 0x Instant

## Summary

0x Instant is a new product from the 0x core team that offers a convenient way for people to get access to a wide variety of tokens and other crypto-assets in just a few taps. Developers can integrate the free, open source library into their applications or websites in order to both offer seamless access to crypto-assets, as well as gain a new source of revenue, with just a few lines of code.

## Affliate Fees

As an end host of 0x Instant, you can charge users a fee on all trades made through Instant with the `affiliateFee` option. Simply specify an ethereum address and feePercentage \(up to 5%\), and a percentage of each transaction will be deposited into the specified address \(denominated in ETH\).

Example: 3% of transaction volume \(in ETH\) will de deposited into 0x50ff5828a216170cf224389f1c5b0301a5d0a230

```markup
<head>
    ...
    <script src="https://instant.0xproject.com/instant.js"></script>
    ...
</head>
```

```javascript
zeroExInstant.render(
    {
        orderSource: 'https://api.relayer.com/sra/v2/',
        affiliateInfo: {
            feeRecipient: '0x50ff5828a216170cf224389f1c5b0301a5d0a230',
            feePercentage: 0.03,
        },
    },
    'body',
);
```

## Important Links

* [Website](https://0x.org/instant)
* [Getting Started](https://0x.org/wiki#Get-Started-With-Instant)

