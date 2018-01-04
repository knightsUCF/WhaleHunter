#!/usr/bin/python3

import log
import user
import json
import numpy
import bittrex
# from binance.client import Client

bittrex = bittrex.Bittrex(user.bittrex_public_key, user.bittrex_private_key)
# binance = Client(user.binance_public_key, user.binance_private_key)






def get_data_for_all_coins(broker):
    if broker == 'bittrex':
        prices = bittrex.get_market_summaries()
        response = prices['success']
        if response == False:
            error_code = 'E1: No response from broker server'
            log.error(error_code)
        results = prices['result']
        return results
    if broker == 'binance':
        return binance.get_ticker()




def get_bids():
    prices = bittrex.get_market_summaries()
    response = prices['success']
    if response == False:
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
    if response == False:
        error_code = 'E1: No response from broker server.'
        log.error(error_code)
    if response == True:
        quote = float(data['result']['Bid'])
        return quote





    
