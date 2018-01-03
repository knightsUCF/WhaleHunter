from coinmarketcap import Market
coinmarketcap = Market()

# https://www.cryptocompare.com/api/#introduction



class CoinMarket():
    
    
    def General(self):
        print(coinmarketcap.stats())



    def Stats(self, coin):
        return (coinmarketcap.ticker(coin, limit=3, convert='USD'))



    def Rank(self, coin):
        return (coinmarketcap.ticker(coin, limit=3, convert='USD'))[0]['rank']

    

    def PriceUSD(self, coin):
        return (coinmarketcap.ticker(coin, limit=3, convert='USD'))[0]['price_usd']



    def PriceBTC(self, coin):
        return (coinmarketcap.ticker(coin, limit=3, convert='USD'))[0]['price_btc']



    def Volume(self, coin):
        return (coinmarketcap.ticker(coin, limit=3, convert='USD'))[0]['24h_volume_usd']



    def PercentChange1Hour(self, coin):
        return (coinmarketcap.ticker(coin, limit=3, convert='USD'))[0]['percent_change_1h']

    

    def PercentChange24Hours(self, coin):
        return (coinmarketcap.ticker(coin, limit=3, convert='USD'))[0]['percent_change_24h']
