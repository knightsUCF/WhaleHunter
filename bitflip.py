#!/usr/bin/python3

import api
api = api.API()


def get_tape():
    response = api.get('https://api.bitflip.cc/method/market.getRates')
    return response[1]
