#!/usr/bin/python3

import re
import time
import user
import log
import state
import trade
import broker
import feed
import gui


trade = trade.Trade()
feed = feed.Feed()



class Strategy():


    def __init__(self):
        # feed.initialize_databases('bittrex_tape.db', 'binance_tape.db')
        self.refresh_rate = 0.5
        self.mode = user.mode
        self.entry_lookback = user.entry_lookback
        self.exit_lookback = user.exit_lookback
        self.volume_spike_magnitude_coefficient = user.volume_spike_magnitude_coefficient 
        self.price_spike_magnitude_coefficient = user.price_spike_magnitude_coefficient
        self.volume_drop_magnitude_coefficient = user.volume_drop_magnitude_coefficient 
        self.price_drop_magnitude_coefficient = user.price_drop_magnitude_coefficient
    
        log.general('\nRunning strategy\n')

        self.all_coin_data = broker.get_data_for_all_coins('bittrex') # used to get all the symbols



         


        self.queue = 'free'
        self.can_trade = 'yes'



    def current_volume(self, broker, pair):
        last_volume = feed.get_last_x_record(broker, pair, 'volume', 0)
        return last_volume



    def current_price(self, broker, pair):
        last_price = feed.get_last_x_record(broker, pair, 'price', 0)
        return last_price



    def average_volume(self, broker, pair, number_of_data_points): 
        total = 0
        for i in range(number_of_data_points):
            total += feed.get_last_x_record(broker, pair,'volume', i)
        average = total / number_of_data_points
        return average 



    def average_price(self, broker, pair, number_of_data_points): 
        total = 0
        for i in range(number_of_data_points):
            total += feed.get_last_x_record(broker, pair,'price', i)
        average = total / number_of_data_points
        return average



    def spike_in_price(self, broker, pair):
        if self.current_price(broker, pair) > (self.average_price(broker, pair, self.entry_lookback) * self.price_spike_magnitude_coefficient):
            return True
        else:
            return False


    
    def spike_in_volume(self, broker, pair):
        if self.current_volume(broker, pair) > (self.average_volume(broker, pair, self.entry_lookback) * self.volume_spike_magnitude_coefficient):
            return True
        else:
            return False



    def drop_in_price(self, broker, pair):
        if self.current_price(broker, pair) < (self.average_price(broker, pair, self.exit_lookback) * self.price_drop_magnitude_coefficient):
            return True
        else:
            return False



    def drop_in_volume(self, broker, pair):
        if self.current_volume() < (self.average_volume(broker, pair, self.exit_lookback) * self.volume_drop_magnitude_coefficient):
            return True
        else:
            return False 



    def entry_conditions(self):
        for i in self.all_coin_data:
            pair_symbol = re.sub('-','',i['MarketName'])
            if self.spike_in_volume('bittrex', pair_symbol) and self.spike_in_price('bittrex', pair_symbol):
                self.current_trade_pair = pair_symbol
                return True
            else:
                return False



    def exit_conditions(self, coin):
        if self.drop_in_price('bittrex', coin):
            return True
        else:
            return False
            


    def seek(self):
        time.sleep(0.1)
        log.general('Running trade management')
        if self.queue is 'free':
            if self.entry_conditions():
                if trade.open('bittrex', self.current_trade_pair):
                    self.queue = 'busy'
        if self.queue is 'busy':
            if self.exit_conditions(self.current_trade_pair):
                trade.close('bittrex', self.current_trade_pair) # get back into bitcoin
                self.queue = 'free' # reset the queue



    def run(self):
        self.seek()
