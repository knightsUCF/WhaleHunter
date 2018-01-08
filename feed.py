#!/usr/bin/python3

import re
import txt
import log
import time
import user
import random
import broker
import sqlite3
import datetime
from multiprocessing import Process



class Feed():


    def __init__(self):
        self.initialize_databases('bittrex_tape.db',
                                  'binance_tape.db',
                                  'bitx_tape.db',
                                  'bitgrail_tape.db',
                                  'kucoin_tape.db',
                                  'mercatox_tape.db',
                                  'bitflip_tape.db')

        self.bittrex_refresh_rate = 1
        self.binance_refresh_rate = (random.randint(3,10)) # very picky broker
        self.bitx_refresh_rate = 1
        self.bitgrail_refresh_rate = 1
        self.kucoin_refresh_rate = 1
        self.mercatox_refresh_rate = 1
        self.bitflip_refresh_rate = 1



    def initialize_databases(self,
                             bittrex,
                             binance,
                             bitx,
                             bitgrail,
                             kucoin,
                             mercatox,
                             bitflip):
        try:
            self.bittrex_db = sqlite3.connect(bittrex)
            self.binance_db = sqlite3.connect(binance)
            self.bitx_db = sqlite3.connect(bitx)
            self.bitgrail_db = sqlite3.connect(bitgrail)
            self.kucoin_db = sqlite3.connect(kucoin)
            self.mercatox_db = sqlite3.connect(mercatox)
            self.bitflip_db = sqlite3.connect(bitflip)

            self.bittrex_cursor = self.bittrex_db.cursor()
            self.binance_cursor = self.binance_db.cursor()
            self.bitx_cursor = self.bitx_db.cursor()
            self.bitgrail_cursor = self.bitgrail_db.cursor()
            self.kucoin_cursor = self.kucoin_db.cursor()
            self.mercatox_cursor = self.mercatox_db.cursor()
            self.bitflip_cursor = self.bitflip_db.cursor()


        except sqlite3.Error as e:
            log.error('E2: No database(s) connection')



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



    def create_bitx_table(self, coin):
        self.bitx_cursor.execute('''
            CREATE TABLE IF NOT EXISTS {0}(id INTEGER PRIMARY KEY AUTOINCREMENT, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            price REAL, volume REAL)'''.format(coin))
        self.bitx_db.commit()



    def create_bitgrail_table(self, coin):
        self.bitgrail_cursor.execute('''
            CREATE TABLE IF NOT EXISTS {0}(id INTEGER PRIMARY KEY AUTOINCREMENT, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            price REAL, volume REAL)'''.format(coin))
        self.bitgrail_db.commit()



    def create_kucoin_table(self, coin):
        self.kucoin_cursor.execute('''
            CREATE TABLE IF NOT EXISTS {0}(id INTEGER PRIMARY KEY AUTOINCREMENT, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            price REAL, volume REAL)'''.format(coin))
        self.kucoin_db.commit()



    def create_mercatox_table(self, coin):
        self.mercatox_cursor.execute('''
            CREATE TABLE IF NOT EXISTS {0}(id INTEGER PRIMARY KEY AUTOINCREMENT, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            price REAL, volume REAL)'''.format(coin))
        self.mercatox_db.commit()



    def create_bitflip_table(self, coin):
        self.bitflip_cursor.execute('''
            CREATE TABLE IF NOT EXISTS {0}(id INTEGER PRIMARY KEY AUTOINCREMENT, time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            price REAL, volume REAL)'''.format(coin))
        self.bitflip_db.commit()



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



    def write_to_bitx_database(self, coin_table, price, volume):
        self.create_bitx_table(coin_table)
        try:
            with self.bitx_db:
                self.bitx_db.execute('''INSERT INTO {0}(price, volume)
                          VALUES({1},{2})'''.format(coin_table, price, volume))
        except sqlite3.IntegrityError:
            log.error('E3: Record already exists')



    def write_to_bitgrail_database(self, coin_table, price, volume):
        self.create_bitgrail_table(coin_table)
        try:
            with self.bitgrail_db:
                self.bitgrail_db.execute('''INSERT INTO {0}(price, volume)
                          VALUES({1},{2})'''.format(coin_table, price, volume))
        except sqlite3.IntegrityError:
            log.error('E3: Record already exists')



    def write_to_kucoin_database(self, coin_table, price, volume):
        self.create_kucoin_table(coin_table)
        try:
            with self.kucoin_db:
                self.kucoin_db.execute('''INSERT INTO {0}(price, volume)
                          VALUES({1},{2})'''.format(coin_table, price, volume))
        except sqlite3.IntegrityError:
            log.error('E3: Record already exists')



    def write_to_mercatox_database(self, coin_table, price, volume):
        self.create_mercatox_table(coin_table)
        try:
            with self.mercatox_db:
                self.mercatox_db.execute('''INSERT INTO {0}(price, volume)
                          VALUES({1},{2})'''.format(coin_table, price, volume))
        except sqlite3.IntegrityError:
            log.error('E3: Record already exists')



    def write_to_bitflip_database(self, coin_table, price, volume):
        self.create_bitflip_table(coin_table)
        try:
            with self.bitflip_db:
                self.bitflip_db.execute('''INSERT INTO {0}(price, volume)
                          VALUES({1},{2})'''.format(coin_table, price, volume))
        except sqlite3.IntegrityError:
            log.error('E3: Record already exists')



    def get_bittrex_tape(self):
        try:
            time.sleep(self.bittrex_refresh_rate)
            all_coin_data = broker.get_data_for_all_coins('bittrex')
            for i in all_coin_data:
                coin_table = re.sub('-','',i['MarketName'])
                bid = i['Bid']
                volume = i['Volume']
                print('Getting bittrex data for: ', coin_table, '  ', end='\r')
                self.create_bittrex_table(coin_table)
                self.write_to_bittrex_database(coin_table, bid, volume)
        except KeyboardInterrupt:
            print('Bittrex feed off')
            self.bittrex_db.close()



    def get_binance_tape(self):
        try:
            time.sleep(self.binance_refresh_rate)
            all_coin_data = broker.get_data_for_all_coins('binance')
            for i in all_coin_data:
                if i['lastId'] is not -1:
                    coin_table = i['symbol']
                    bid = i['bidPrice']
                    volume = i['volume']
                    print('    Getting binance data for: ', coin_table, '  ', end='\r')
                    self.create_binance_table(coin_table)
                    self.write_to_binance_database(coin_table, bid, volume)
        except:
            print('Binance feed off')
            self.binance_db.close()



    def get_bitx_tape(self):
        try:
            time.sleep(self.bitx_refresh_rate)
            all_coin_data = broker.get_data_for_all_coins('bitx')
            for i in all_coin_data:
                # figure out how to parse feed
                print('    Getting bitx data for: ', coin_table, '  ', end='\r')
                self.create_bitx_table(coin_table)
                self.write_to_bitx_database(coin_table, bid, volume)
        except:
            print('Bitx feed off')
            self.bitx_db.close()



    def get_bitgrail_tape(self):
        try:
            time.sleep(self.bitgrail_refresh_rate)
            all_coin_data = broker.get_data_for_all_coins('bitgrail')
            for i in all_coin_data:
                # figure out how to parse feed
                print('    Getting bitgrail data for: ', coin_table, '  ', end='\r')
                self.create_bitgrail_table(coin_table)
                self.write_to_bitgrail_database(coin_table, bid, volume)
        except:
            print('Bitgrail feed off')
            self.bitgrail_db.close()



    def get_kucoin_tape(self):
        try:
            time.sleep(self.kucoin_refresh_rate)
            all_coin_data = broker.get_data_for_all_coins('kucoin')
            for i in all_coin_data:
                # figure out how to parse feed
                print('    Getting kucoin data for: ', coin_table, '  ', end='\r')
                self.create_kucoin_table(coin_table)
                self.write_to_kucoin_database(coin_table, bid, volume)
        except:
            print('Kucoin feed off')
            self.kucoin_db.close()



    def get_mercatox_tape(self):
        try:
            time.sleep(self.mercatox_refresh_rate)
            all_coin_data = broker.get_data_for_all_coins('mercatox')
            for i in all_coin_data:
                # figure out how to parse feed
                print('    Getting mercatox data for: ', coin_table, '  ', end='\r')
                self.create_mercatox_table(coin_table)
                self.write_to_mercatox_database(coin_table, bid, volume)
        except:
            print('Mercatox feed off')
            self.mercatox_db.close()



   def get_bitflip_tape(self):
       try:
           time.sleep(self.bitflip_refresh_rate)
           all_coin_data = broker.get_data_for_all_coins('bitflip')
           for i in all_coin_data:
               # figure out how to parse feed
               print('    Getting bitflip data for: ', coin_table, '  ', end='\r')
               self.create_bitflip_table(coin_table)
               self.write_to_bitflip_database(coin_table, bid, volume)
       except:
           print('Bitflip feed off')
           self.mercatox_db.close()



    def get_last_x_records(self, broker, coin, column, records=None):
        if broker == 'bittrex':
            query = "SELECT {0} from {1};".format(column, coin)
            self.bittrex_cursor.execute(query)
            rows = self.bittrex_cursor.fetchall()
            result = rows[len(rows)-records if records else 0:]
            return result



    def get_last_x_record(self, broker, coin, column, record):
        # old:
        # self.bittrex_db = sqlite3.connect('bittrex_tape.db')
        # self.bittrex_cursor = self.bittrex_db.cursor()

        self.bittrex_db = sqlite3.connect('bittrex_tape.db')
        self.binance_db = sqlite3.connect('binance_tape.db')
        self.bitx_db = sqlite3.connect('bitx_tape.db')
        self.bitgrail_db = sqlite3.connect('bitgrail_tape.db')
        self.kucoin_db = sqlite3.connect('kucoin_tape.db')
        self.mercatox_db = sqlite3.connect('mercatox_tape.db')
        self.bitflip_db = sqlite3.connect('bitflip_tape.db')

        self.bittrex_cursor = self.bittrex_db.cursor()
        self.binance_cursor = self.binance_db.cursor()
        self.bitx_cursor = self.bitx_db.cursor()
        self.bitgrail_cursor = self.bitgrail_db.cursor()
        self.kucoin_cursor = self.kucoin_db.cursor()
        self.mercatox_cursor = self.mercatox_db.cursor()
        self.bitflip_cursor = self.bitflip_db.cursor()

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
            print('Bittrex parsing db error, or, need more data points in database. Rerun without strategy.')

        try:
            if broker == 'binance':
                query = "SELECT {0} from {1} ORDER BY ID DESC;".format(column, coin)
                self.binance_cursor.execute(query)
                rows = self.binance_cursor.fetchall()
                self.binance_db.close()
                result = rows[len(rows)-records if records else 0:]
                result = str(result[record])
                result = re.sub(',', '', result)
                result = result.replace('(', '')
                result = result.replace(')', '')
                return float(result)
        except:
            print('Binance parsing db error, or, need more data points in database. Rerun without strategy.')

        try:
            if broker == 'bitx':
                query = "SELECT {0} from {1} ORDER BY ID DESC;".format(column, coin)
                self.bitx_cursor.execute(query)
                rows = self.bitx_cursor.fetchall()
                self.bitx_db.close()
                result = rows[len(rows)-records if records else 0:]
                result = str(result[record])
                result = re.sub(',', '', result)
                result = result.replace('(', '')
                result = result.replace(')', '')
                return float(result)
        except:
            print('Bitx parsing db error, or, need more data points in database. Rerun without strategy.')

        try:
            if broker == 'bitgrail':
                query = "SELECT {0} from {1} ORDER BY ID DESC;".format(column, coin)
                self.bitgrail_cursor.execute(query)
                rows = self.bitgrail_cursor.fetchall()
                self.bitgrail_db.close()
                result = rows[len(rows)-records if records else 0:]
                result = str(result[record])
                result = re.sub(',', '', result)
                result = result.replace('(', '')
                result = result.replace(')', '')
                return float(result)
        except:
            print('Bitgrail parsing error, or, need more data points in database. Rerun without strategy.')

        try:
            if broker == 'kucoin':
                query = "SELECT {0} from {1} ORDER BY ID DESC;".format(column, coin)
                self.kucoin_cursor.execute(query)
                rows = self.kucoin_cursor.fetchall()
                self.kucoin_db.close()
                result = rows[len(rows)-records if records else 0:]
                result = str(result[record])
                result = re.sub(',', '', result)
                result = result.replace('(', '')
                result = result.replace(')', '')
                return float(result)
        except:
            print('Kucoin parsing error, or, need more data points in database. Rerun without strategy.')

        try:
            if broker == 'mercatox':
                query = "SELECT {0} from {1} ORDER BY ID DESC;".format(column, coin)
                self.mercatox_cursor.execute(query)
                rows = self.mercatox_cursor.fetchall()
                self.mercatox_db.close()
                result = rows[len(rows)-records if records else 0:]
                result = str(result[record])
                result = re.sub(',', '', result)
                result = result.replace('(', '')
                result = result.replace(')', '')
                return float(result)
        except:
            print('Mercatox parsing error, or, need more data points in database. Rerun without strategy.')

        try:
            if broker == 'bitflip':
                query = "SELECT {0} from {1} ORDER BY ID DESC;".format(column, coin)
                self.bitflip_cursor.execute(query)
                rows = self.bitflip_cursor.fetchall()
                self.bitflip_db.close()
                result = rows[len(rows)-records if records else 0:]
                result = str(result[record])
                result = re.sub(',', '', result)
                result = result.replace('(', '')
                result = result.replace(')', '')
                return float(result)
        except:
            print('Bitflip parsing error, or, need more data points in database. Rerun without strategy.')







'''


    def run(self):
        # self.initialize_databases('bittrex_tape.db', 'binance_tape.db')
        bittrex_feed_process = Process(target = self.get_bittrex_tape)
        bittrex_feed_process.start()
        # binance_feed_process = Process(target = self.get_binance_tape)
        # binance_feed_process.start()

'''











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
