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
prices = {} # key is the link, value is a tuple that looks like (xPath, price)

try:
    prices = pickle.load(open("save.p","rb"))
    print("exists")
except:
    pass

# checks the current price, if it is different from the previous price, return True else False
def check(link, current_price):
    previous_price = prices[link][1]
    if previous_price != current_price:
        return True
    return False

# adds a link to the ditionary as a key with the xPath and price as its value
def add(link, xPath):
    driver.get(link)
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xPath))
        )
        price = driver.find_element_by_xpath(xPath).text
        prices[link] = (xPath, price)
    finally:
        driver.quit()

if __name__ == "__main__":
    change = False
    # go through the items to see if any prices changed
    for key in prices:
        driver.get(key)
        time.sleep(5) # give the page time to load
        try:
            element = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, prices[key][0]))
            )
            price = driver.find_element_by_xpath(prices[key][0]).text
            if check(key, price):
                change = True
        finally:
            driver.quit()
    if change:
        print("Prices have changed for: ")
    else:
        print("No change in prices")
    while True:
        print("1. add item\n2. remove item\n3. exit")
        r = input()
        if r == '1':
            print("Link: ")
            link = input()
            print("xPath: ")
            xPath = input()
            add(link, xPath)
            pickle.dump(prices, open("save.p", "wb"))
        elif r == '2':
            pass
        elif r == '3':
            break
        else:
            print("That is not a valid response.")
    
    
    