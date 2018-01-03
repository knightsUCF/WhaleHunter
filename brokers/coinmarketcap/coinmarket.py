from brokers.coinmarketcap import Market
coinmarketcap = Market()

# https://www.cryptocompare.com/api/#introduction



class CoinMarket():
    
    
    def general(self):
        print(coinmarketcap.stats())



    def stats(self, coin):
        return (coinmarketcap.ticker(coin, limit=3, convert='USD'))



    def rank(self, coin):
        return (coinmarketcap.ticker(coin, limit=3, convert='USD'))[0]['rank']

    

    def price_usd(self, coin):
        return (coinmarketcap.ticker(coin, limit=3, convert='USD'))[0]['price_usd']



    def price_btc(self, coin):
        return (coinmarketcap.ticker(coin, limit=3, convert='USD'))[0]['price_btc']



    def volume(self, coin):
        return (coinmarketcap.ticker(coin, limit=3, convert='USD'))[0]['24h_volume_usd']



    def percent_change_one_hour(self, coin):
        return (coinmarketcap.ticker(coin, limit=3, convert='USD'))[0]['percent_change_1h']

    

    def percent_change_24_hours(self, coin):
        return (coinmarketcap.ticker(coin, limit=3, convert='USD'))[0]['percent_change_24h']
