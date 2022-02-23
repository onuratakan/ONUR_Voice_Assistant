#!/usr/bin/python3
# -*- coding: utf-8 -*-

from lcg import LCG

from get_crypto_price import get_crypto_price

def how_are_you(expression):
    answers = [
        """I'am fine""",
        "Not bad",
    ]
    return LCG.choice(answers)

def onur_get_crypto_price(expression, coin = "btc"):
    if len(expression.split()) > 3:
        coin  = expression.split()[-1]
    return get_crypto_price(crypto=coin)


OFFICAL_DATA = [
    [
        [
            "how are you",
        ], 
        how_are_you
    ],
    [
        [
            "get crypto price"
        ],
        onur_get_crypto_price
    ]
]