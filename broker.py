#!/usr/bin/python3

import log
import api
import user
import json
import numpy

# brokers
# from brokers import luno
import bitgrail
import kucoin
from brokers import mercatox
import bitflip


api = api.API()

import bittrex
bittrex = bittrex.Bittrex(user.bittrex_public_key, user.bittrex_private_key)

from binance.client import Client
binance = Client(user.binance_public_key, user.binance_private_key)

from kucoin.client import Client
kucoin = Client(user.kucoin_public_key, user.kucoin_private_key)






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
    if broker is 'luno':
        pass
    if broker is 'bitgrail':
        return bitgrail.get_tape()
    if broker is 'kucoin':
        response = api.get('https://api.kucoin.com/v1/market/open/symbols')
        return response['data']
    if broker is 'mercatox':
        pass
    if broker is 'bitflip':
        return bitflip.get_tape()



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
        


def balances(exchange):
    if exchange == 'binance':
        balances = binance.get_account()
        # pretty = api.readable(balances)
        # print(' Binance balances: ', pretty)
        return balances
    if exchange == 'kucoin':
        balances = kucoin.get_all_balances()
        pretty = api.readable(kucoin.get_all_balances())
        print('Kucoin balances: ', pretty)
        return balances



def balance(exchange, coin):
    balance = 0
    balances = 0
    if exchange == 'binance':
        balances = binance.get_account()
        for i in balances['balances']:
            if i['asset'] == coin:
                balance = i['free']
                return balance
    if exchange == 'kucoin':
        balances = kucoin.get_all_balances()
        for i in balances:
            if i['coinType'] == coin:
                balance = i['balance']
                return balance
    


def address(exchange, pair):
    if exchange == 'binance':
        print('Getting deposit address at ', exchange, ' for ', pair)
        address = binance.get_deposit_address(pair)
        return address
    if exchange == 'kucoin':
        print('Getting deposit address at ', exchange, 'for', pair)
        address = kucoin.get_deposit_address(pair)
        return address



def buy(exchange, pair, amount, kucoin_pending_order_price):
    if exchange == 'binance': # probably 'BTCX' no special characters format
        response = binance.order_market_buy(pair, amount)
        print('Buy order API response: ', response)
        return response
    if exchange == 'kucoin': # 'KCS-BTC' format
        response = kucoin.create_buy_order(pair, kucoin_pending_order_price, amount)
        return response



def withdraw(exchange, coin, amount, address):
    valid_milliseconds_window = '' # for binance
    if exchange == 'binance':
        binance.withdraw(coin, address, amount, recvWindow = valid_milliseconds_window)
    if exchange == 'kucoin':
        kucoin.create_withdrawal(coin, amount, address)

        
