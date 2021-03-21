class Item:
    def __init__(self, link, xPath, price):
        self.link = link
        self.xPath = xPath
        self.price = price
        self.priceHistory = [price]
    # price has changed, so update to new price    
    def newPrice(self, price):
        self.price = price
        self.priceHistory.append(price)