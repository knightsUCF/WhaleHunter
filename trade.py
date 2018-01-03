#!/usr/bin/python3
import user
import bittrex
import feed

bittrex = bittrex.Bittrex(user.bittrex_public_key, user.bittrex_private_key)
feed = feed.Feed()


class Trade():


    def __init__(self):
        self.btc_balance = user.starting_btc_balance



    def open(self, broker, pair):
        print('btc balance: ', self.btc_balance)
        self.last_price = feed.get_last_x_record(broker, pair, 'price', 0)
        print('opening trade at', self.last_price)
        self.units = self.btc_balance / self.last_price
        print('\nBought ', self.units, 'units of ', pair)
        # query the broker api for 'success', then: state.set_trade_queue = x



    def close(self, broker, pair): # sell altcoin into bitcoin
        self.last_price = feed.get_last_x_record(broker, pair, 'price', 0)
        print('\n Sold ', self.units, ' at ', self.last_price)
        self.btc_balance = self.units * self.last_price
        print('\n New BTC balance: ', self.btc_balance)









    


