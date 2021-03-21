from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Item import Item
import pickle
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless') # so that the web browser doesn't open
options.add_argument("--log-level=3") # to ignore deprecation error 
driver_path = "C:\\Drivers\\chromedriver.exe"
driver = webdriver.Chrome(executable_path = driver_path, chrome_options = options)
prices = {} # key is the name, value is a list that has the link, xPath, and price
items = [] # list of items

try:
    items = pickle.load(open("C:\\Github\\PriceChecker\\save.p","rb"))
    print("exists")
except:
    pass

# will return the list of items whose price has changed
def price_change():
    changes = []
    for item in items:
        driver.get(item.link)
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, item.xPath))
            )
            price = driver.find_element_by_xpath(item.xPath).text
            if item.price != price:
                changes.append([item.name, item.price, price])
                item.price = price # now we update the price
        finally:
            pass
    return changes

# adds a link to the ditionary as a key with the xPath and price as its value
def add(name, link, xPath):
    driver.get(link)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xPath))
        )
        price = driver.find_element_by_xpath(xPath).text
        items.append(Item(name, link, xPath, price))
    finally:
        pass

if __name__ == "__main__":
    while True:
        print("1. add item\n2. remove item\n3. view items\n4. price history\n5. exit")
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
            for i in range(0, len(items)):
                print(i, items[i].name)
            print("Enter in the number of the item you want to remove")
            remove = int(input())
            if remove >= 0 and remove < len(items):
                del items[remove]
                print("Successfully removed")
            else:
                print("That is not a valid number")
        elif r == '3':
            for item in items:
                print("Name:", item.name, "price:", item.price)
        elif r == '4':
            print("These are the items currently saved")
            for item in items:
                print("Name:", item.name)
        elif r == '5':
            pickle.dump(items, open("C:\\Github\\PriceChecker\\save.p", "wb"))
            driver.quit()
            break
        else:
            print("That is not a valid response.")
    
    
    