# keys + user settings

bittrex_public_key = ""
bittrex_private_key = ""

binance_public_key = ""
binance_private_key = ""

# run mode

mode = 'demo' # demo or live
alerts = 'off' # off or on 



# demo settings

starting_btc_balance = 1.0
watermark_demo_equity_in_btc_shutoff = 1.0 # turn off system after drawing down beyond a capital watermark
scheduled_pumps = 'on' # this will close out all opened positions five minutes before scheduled time
scheduled_pump_time = '' # unix epoch time


# live settings

watermark_live_equity_in_btc_shutoff = 1.0
scheduled_pumps = 'on' # this will close out all opened positions five minutes before scheduled time
scheduled_pump_time = '' # unix epoch time


# set one of them to True

strategy_1 = True
strategy_2 = False
strategy_3 = False
strategy_4 = False



# strategy 1 settings:

entry_lookback = 30 # ten of time series data "time units" (candlebuilding)
exit_lookback = 10
volume_spike_magnitude_coefficient = 1.0 # 1.0 is 100%, unchanged
price_spike_magnitude_coefficient = 1.0 
volume_drop_magnitude_coefficient = 1.0
price_drop_magnitude_coefficient = 1.0


''' uncomment for multiple strategy settings - only use one set of variables 

# strategy 2 settings:

lookback_period = 10 
refresh_rate = 1 
volume_magnitude_coefficient = 1.0 
price_magnitude_coefficient = 1.0 

# strategy 3 settings:

lookback_period = 10 
refresh_rate = 1 
volume_magnitude_coefficient = 1.0 
price_magnitude_coefficient = 1.0 

# strategy 4 settings:

lookback_period = 10 
refresh_rate = 1 
volume_magnitude_coefficient = 1.0 
price_magnitude_coefficient = 1.0 

'''


coins = ['XMR',
         'BCC',
         'LTC',
         'ETH',
         'DASH',
         'NEO',
         'QTUM',
         'ADA',
         'LSK',
         'WAVES',
         'ETC',
         'STRAT',
         'XRP',
         'XLM',
         'ADX',
         'MCO',
         'STORJ',
         'POWR',
         'OMG',
         'SNT',
         'DNT',
         'ZEC',
         'BAT',
         'BNT',
         'ENG',
         'VIB',
         'KMD',
         'MANA',
         'RCN',
         'WAVES',
         'KMD'
         ]


