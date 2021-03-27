from datetime import date

class Item:
    def __init__(self, name, link, xPath, price):
        self.name = name
        self.link = link
        self.xPath = xPath
        self.price = price
        self.priceHistory = {} # date is the key and price is the value 
        self.priceHistory[date.today()] = price

    # price has changed, so update to new price    
    def newPrice(self, price):
        self.price = price
        self.priceHistory[date.today()] = price
    
    def viewPriceHist(self):
        for key in self.priceHistory:
            print("On", key, "the price was", self.priceHistory[key])

