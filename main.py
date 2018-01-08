#!/usr/bin/python3

import log
import feed
import strategy
import broker

feed = feed.Feed()
strategy = strategy.Strategy()



def run():
    log.general('Initializing...\n')
    while True:
        try:
            log.general('Downloading feed data\n')
            feed.get_bittrex_tape()
            feed.get_binance_tape()
            feed.get_bitx_tape()
            feed.get_bitgrail_tape()
            feed.get_kucoin_tape()
            feed.get_mercatox()
            feed.get_bitflip()
            print('Seeking trade opportunity\n')
            strategy.seek()
        except KeyboardInterrupt:
            pass


run()




'''
all_coin_data = broker.get_data_for_all_coins('bittrex')
print(all_coin_data)
'''

'''
import sys
import gui
import feed
import strategy
from multiprocessing import Process



feed = feed.Feed()
strategy = strategy.Strategy()
gui = gui.GUI()



def run():

    feed_process = Process(target = feed.run)
    feed_process.start()

    strategy_process = Process(target = strategy.run)
    strategy_process.start()

    gui_process = Process(target = gui.run)
    gui_process.start()



run()
'''
