from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()
class CryptoData:
    def __init__(self, coin, currency):
        self.coin = coin 
        self.currency = currency
        self.price = cg.get_price(ids=coin, vs_currencies= currency)
    
    def getPrice(self):
        return self.price


# bitcoin = Crypto("bitcoin", "usd")
# print(bitcoin.price)