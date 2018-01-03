#!/usr/bin/python3

import datetime
import pickle 



class State():


    def __init__(self, file_name):
        self.file_name = file_name # storing user settings in a text file and in the future a db
        self.trades = {} # holds the inventory of trades, indexed by the key of "ID"



    # machine states
    def set_machine(self, machine_state):
        self.machine_state = machine_state



    def get_machine(self):
        return self.machine_state



    # inventory
    def add_trade(self, key): # key format: {a:b}
        self.trades.update(key)



    def remove_trade_by_id(self, id):
        if (not self.trades):
            return
        if (id in self.trades):
            del self.atWar[declaredByID]



    def get_trades(self):
        return self.trades



    def get_trade_features(self, id):
        trade_features = self.trades[id]
        return trade_features



    def get_trade_by_id(self, id):
        return (trade in self.trades(id))



    def set_trade_queue(self, data):
        self.trade_queue = data
        
        

    def get_trade_queue(self):
        return self.trade_queue


    
    def save_trade_history(self):
        pickle.dump(self.trades, open(self.file_name, 'wb'))



    def load_trade_history(self):
        history = pickle.load(open(filename, 'rb'))
        return history



    # reading / writing trade list data
    def reset_trade_list(self):
        self.trades = {}



    def initialize_saved_trade_list(self):
        self.load_trade_history()


    def set_some_state(self, state):
        self.some_state = state


    def get_some_state(self):
        return self.some_state 



    def add_quote(self, time, price, volume):
        pass



# s = State('settings.txt')



    
'''

# Example


# 1. Create a user - Luigi
file_name = 'luigi_settings.txt'
luigi = State(file_name)

# 2. create a trade and place into trade history

# trade features:
id = 1
open_time = datetime.datetime.now()
pair = 'BTC/LTC'
side = 'bull'

trade_list = luigi.add_trade({id: {'open_time': open_time,
                                   'pair':pair,
                                   'side':side}})

# view the trade history
luigi_trade_history = luigi.get_trades()
print('luigi_trade_history: ', luigi_trade_history)

# 3. add another trade to luigi's trade history (reusing same variables, but can be turned into a method)
id = 2
open_time = datetime.datetime.now()
pair = 'BTC/LTC'
side = 'bull'

# adding trade by index of trade id: 2
luigi.add_trade({id: {'open_time': open_time,
                      'pair':pair,
                      'side':side}})

updated_trade_list = luigi.get_trades()

print('\n\nluigi'"'"'s new trade list: ', updated_trade_list)


# query access to trade features by trade ID
trade_features = luigi.get_trade_features(id)
print('\ntrade_features: ', trade_features)

'''










    




    