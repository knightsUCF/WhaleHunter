#!/usr/bin/python3

import log
import user
import json
import numpy

# brokers
import bittrex
from brokers import bitx
from brokers import bitgrail
from brokers import kucoin
from brokers import mercatox
from brokers import bitflip
from binance.client import Client

bittrex = bittrex.Bittrex(user.bittrex_public_key, user.bittrex_private_key)
binance = Client(user.binance_public_key, user.binance_private_key)



def get_data_for_all_coins(broker):
    if broker is 'bittrex':
        prices = bittrex.get_market_summaries()
        response = prices['success']
        if response is False:
            error_code = 'E1: No response from broker server'
            log.error(error_code)
        results = prices['result']
        return results
    if broker is 'binance':
        return binance.get_ticker()
    if broker is 'bitx':
        pass
    if broker is 'bitgrail':
        pass
    if broker is 'kucoin':
        pass
    if broker is 'mercatox':
        pass
    if broker is 'bitflip':
        pass



def get_bids():
    prices = bittrex.get_market_summaries()
    response = prices['success']
    if response is False:
        error_code = 'E1: No response from broker server'
        log.error(error_code)
    results = prices['result']
    return results


def get_markets_summary():
    return bittrex.get_markets()



def get_coins_summary():
    return bittrex.get_currencies()



def get_tradable_markets():
    # make sure 'Notice' is None, and 'IsActive' is True, put the results in a dictionary
    pass



def quote(coin):
    bittrex_string = 'BTC-' + coin
    data = bittrex.get_ticker(bittrex_string)
    response = data['success']
    if response is False:
        error_code = 'E1: No response from broker server.'
        log.error(error_code)
    if response is True:
        quote = float(data['result']['Bid'])
        return quote
