#!/usr/bin/python3

import re
import txt
import log
import time
import user
import write
import random
import broker
import sqlite3
import datetime
from multiprocessing import Process

txt = txt.TXT()


class Feed():


    def __init__(self):
        self.initialize_databases('bittrex_tape.db', 'binance_tape.db')
        self.bittrex_refresh_rate = 1
        self.binance_refresh_rate = (random.randint(1,3))
        # log.general('\nRunning feed')



    def initialize_databases(self, name_one, name_two):
        try:
            self.bittrex_db = sqlite3.connect(name_one)
            self.binance_db = sqlite3.connect(name_two)
            self.bittrex_cursor = self.bittrex_db.cursor()
            self.binance_cursor = self.binance_db.cursor()
        except sqlite3.Error as e:
            log.error('E2: No database connection')

 

    def create_bittrex_table(self, coin):
        self.bittrex_cursor.execute('''
            CREATE TABLE IF NOT EXISTS {0}(id INTEGER PRIMARY KEY AUTOINCREMENT, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            price REAL, volume REAL)'''.format(coin))
        self.bittrex_db.commit()



    def create_binance_table(self, coin):
        self.binance_cursor.execute('''
            CREATE TABLE IF NOT EXISTS {0}(id INTEGER PRIMARY KEY AUTOINCREMENT, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            price REAL, volume REAL)'''.format(coin))
        self.binance_db.commit()
        



    def write_to_bittrex_database(self, coin_table, price, volume):
        self.create_bittrex_table(coin_table)
        try:
            with self.bittrex_db:
                self.bittrex_db.execute('''INSERT INTO {0}(price, volume)
                          VALUES({1},{2})'''.format(coin_table, price, volume))
        except sqlite3.IntegrityError:
            log.error('E3: Record already exists')



    def write_to_binance_database(self, coin_table, price, volume):
        self.create_binance_table(coin_table)
        try:
            with self.binance_db:
                self.binance_db.execute('''INSERT INTO {0}(price, volume)
                          VALUES({1},{2})'''.format(coin_table, price, volume))
        except sqlite3.IntegrityError:
            log.error('E3: Record already exists')

    
    
    def get_bittrex_tape(self):
        try:
            while True:
                time.sleep(self.bittrex_refresh_rate)
                all_coin_data = broker.get_data_for_all_coins('bittrex') # bids = broker.get_bids()
                txt.write('db_state.txt', 'locked')
                print('db_state: locked')
                for i in all_coin_data:
                    coin_table = re.sub('-','',i['MarketName'])
                    bid = i['Bid']
                    volume = i['Volume']
                    # print('    Getting bittrex data for: ', coin_table, '  ', end='\r')
                    # print('    Getting bittrex data for: ', coin_table)
                    self.create_bittrex_table(coin_table)
                    self.write_to_bittrex_database(coin_table, bid, volume)
                self.binance_db.close()
                txt.write('db_state.txt', 'unlocked')
                print('db_state: unlocked')

        except KeyboardInterrupt:
            self.bittrex_db.close()
        except:
            print('Reconnecting')
            self.get_bittrex_tape()



    def get_bittrex_tape_single_round(self):
        try:
            time.sleep(self.bittrex_refresh_rate)
            all_coin_data = broker.get_data_for_all_coins('bittrex')
            for i in all_coin_data:
                coin_table = re.sub('-','',i['MarketName'])
                bid = i['Bid']
                volume = i['Volume']
                # print('Getting bittrex data for: ', coin_table, '  ', end='\r')
                self.create_bittrex_table(coin_table)
                self.write_to_bittrex_database(coin_table, bid, volume)
        except KeyboardInterrupt:
            self.bittrex_db.close()
        '''
        except:
            print('')
            print('Reconnecting')
            self.bittrex_db.close()
            time.sleep(self.bittrex_refresh_rate)
            self.get_bittrex_tape_single_round()
        '''
            
        '''    
        finally:
            time.sleep(0.1)
            ('Reconnecting to bittrex feed...')
            self.get_bittrex_tape()
        '''



    def get_binance_tape(self):
        try:
            while True:
                time.sleep(self.binance_refresh_rate)
                all_coin_data = broker.get_data_for_all_coins('binance')
                for i in all_coin_data:
                    if coin_id is not -1:
                        coin_table = i['symbol']
                        bid = i['bidPrice']
                        volume = i['volume']
                        # print('    Getting binance data for: ', coin_table, '  ', end='\r')
                        print('    Getting binance data for: ', coin_table)
                        self.create_binance_table(coin_table)
                        self.write_to_binance_database(coin_table, bid, volume)
        except KeyboardInterrupt:
            self.binance_db.close()
        '''    
        finally:
            self.get_binance_tape()
        '''    



    def get_last_x_records(self, broker, coin, column, records=None):
        if broker == 'bittrex':
            query = "SELECT {0} from {1};".format(column, coin)
            self.bittrex_cursor.execute(query)
            rows = self.bittrex_cursor.fetchall()
            result = rows[len(rows)-records if records else 0:]
            return result
            
            
    
    def get_last_x_record(self, broker, coin, column, record):
        self.bittrex_db = sqlite3.connect('bittrex_tape.db')
        self.bittrex_cursor = self.bittrex_db.cursor()
        records = None
        try:
            if broker == 'bittrex':
                query = "SELECT {0} from {1} ORDER BY ID DESC;".format(column, coin)
                self.bittrex_cursor.execute(query)
                rows = self.bittrex_cursor.fetchall()
                self.bittrex_db.close()
                result = rows[len(rows)-records if records else 0:]
                result = str(result[record])
                result = re.sub(',', '', result)
                result = result.replace('(', '')
                result = result.replace(')', '')
                return float(result)
        except:
            print('Need more data points in database. Rerun without strategy.')


    def run(self):
        # self.initialize_databases('bittrex_tape.db', 'binance_tape.db')
        bittrex_feed_process = Process(target = self.get_bittrex_tape)
        bittrex_feed_process.start()
        # binance_feed_process = Process(target = self.get_binance_tape)
        # binance_feed_process.start()
    











'''
    def get_last_x_record(self, broker, coin, column, record):
        if broker == 'bittrex':
            query = "SELECT {0} from {1};".format(column, coin)
            self.bittrex_cursor.execute(query)
            rows = self.bittrex_cursor.fetchall()
            result = rows[len(rows)-record if record else 0:]
            return result[record]
'''
'''
    def get_last_x_record(self, broker, coin, column, record):
        while True:
            try:
                time.sleep(0.01)
                if txt.read('db_state.txt') is 'unlocked':
                    self.bittrex_db = sqlite3.connect('bittrex_tape.db')
                    self.bittrex_cursor = self.bittrex_db.cursor()
                    records = None
                    if broker == 'bittrex':
                        query = "SELECT {0} from {1} ORDER BY ID DESC;".format(column, coin)
                        self.bittrex_cursor.execute(query)
                        rows = self.bittrex_cursor.fetchall()
                        self.bittrex_db.close()
                        result = rows[len(rows)-records if records else 0:]
                        result = str(result[record])
                        result = re.sub(',', '', result)
                        result = result.replace('(', '')
                        result = result.replace(')', '')
                        return float(result)
            except:
                continue
'''









'''

for mountain, details in mountains.items():
    print(mountain, details['Elevation'])

mountains = {'Everst': {'Elevation': '8848', 'Range': 'Himilaya'}, 'K2': {'Elevation': '8611', 'Range': 'Baltaro'}, 'Kanchenjunga': {'Elevation': '8586', 'Range': 'Himalaya'}, 'Lhotse': {'Elevation': '8516', 'Range': 'Himalaya'}, 'Makalu': {'Elevation': '8485', 'Range': 'Himalaya'}}

'''
