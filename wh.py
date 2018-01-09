#!/usr/bin/python3

import log
import argparse
import feed
import strategy
import broker


feed = feed.Feed()
strategy = strategy.Strategy()



def menu():
    log.general('Starting\n')
    parser = argparse.ArgumentParser()
    parser.add_argument("echo", help="live, demo, feed")
    args = parser.parse_args() # print (args.echo) # example of how to grab echo
    if args.echo == 'live':
        print('Live mode selected')
    if args.echo == 'demo':
        print('Demo mode selected')
    if args.echo == 'feed':
        print('Feed mode selected')
        while True:
            try:
                log.general('Downloading feed data\n')
                # feed.get_bittrex_tape()
                # feed.get_binance_tape()
                feed.get_bitx_tape()
            except KeyboardInterrupt:
                pass
    if args.echo == 'test':
        print('Test mode selected')
        print('Testing bitx tape')
        feed.get_bitx_tape()
    '''
    while True:
        try:
            log.general('Downloading feed data\n')
            feed.get_bittrex_tape()
            feed.get_binance_tape()
            feed.get_bitx_tape()
            feed.get_bitgrail_tape()
            feed.get_kucoin_tape()
            feed.get_mercatox_tape()
            feed.get_bitflip_tape()
            print('Seeking trade opportunity\n')
            strategy.seek()
        except KeyboardInterrupt:
            pass
            '''


def run():
    menu()



run()






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
