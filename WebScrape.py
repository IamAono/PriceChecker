from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless') # so that the web browser doesn't open
driver_path = "C:\\Drivers\\chromedriver.exe"
driver = webdriver.Chrome(executable_path = driver_path, chrome_options = options)
prices = {} # key is the name, value is a list that has the link, xPath, and price

try:
    prices = pickle.load(open("C:\\Github\\PriceChecker\\save.p","rb"))
    print("exists")
except:
    pass

# will return the list of items whose price has changed
def price_change():
    changes = [] # holds the names of all items that have changed prices
    for key in prices:
        driver.get(prices[key][0])
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, prices[key][1]))
            )
            price = driver.find_element_by_xpath(prices[key][1]).text
            if check(key, price):
                changes.append(key)
                prices[key][2] = price # now we update the price
        finally:
            driver.quit()
    return changes

# checks the current price, if it is different from the previous price, return True else False
def check(link, current_price):
    previous_price = prices[link][2]
    if previous_price != current_price:
        return True
    return False

# adds a link to the ditionary as a key with the xPath and price as its value
def add(name, link, xPath):
    driver.get(link)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xPath))
        )
        price = driver.find_element_by_xpath(xPath).text
        prices[name] = [link, xPath, price]
    finally:
        driver.quit()

if __name__ == "__main__":
    change = price_change() # go through the items to see if any prices changed
    if len(change) > 0:
        print("Prices have changed for: ")
        for c in change:
            print(c)
    else:
        print("No change in prices")
    while True:
        print("1. add item\n2. remove item\n3. exit")
        r = input()
        if r == '1':
            print("Name: ")
            name = input()
            print("Link: ")
            link = input()
            print("xPath: ")
            xPath = input()
            add(name, link, xPath)
        elif r == '2':
            print("These are the items currently saved")
            for key in prices:
                print(key)
            print("Enter in the name of the item you want to remove")
            remove = input()
            if prices.__contains__(remove):
                prices.pop(remove)
                print("Successfully removed")
            else:
                print("That is not a name in the dictionary")
        elif r == '3':
            pickle.dump(prices, open("C:\\Github\\PriceChecker\\save.p", "wb"))
            break
        else:
            print("That is not a valid response.")
    
    
    