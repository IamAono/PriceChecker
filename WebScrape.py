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
driver.get("https://www.amazon.com/Powerbeats-Pro-Totally-Wireless-Earphones/dp/B07R5QD598/ref=sr_1_1_sspa?dchild=1&keywords=powerbeats+pro&qid=1605052572&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExSTRFRURGR1hDVUNXJmVuY3J5cHRlZElkPUEwOTc1MTM4M01FN0lEUTBaWU40VSZlbmNyeXB0ZWRBZElkPUEwNDIwODgzVDhaREE0Tlo2VlZEJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")
time.sleep(5) # give the page time to load
prices = {} # key is the link, value is a tuple that looks like (xPath, price)

try:
    prices = pickle.load(open("save.p","rb"))
    print("exists")
except:
    pass

def add(link, xPath):
    driver.get(link)
    price = driver.find_element_by_xpath(xPath).text
    prices[link] = (xPath, price)

if __name__ == "__main__":
    change = False
    # go through the items to see if any prices changed
    '''for key in prices:
        driver.get(key)
        price = driver.find_element_by_xpath(prices[key][0])
        previousPrice = prices[key][1]
        if price != previousPrice:
            change = True
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
            print("That is not a valid response.")'''
    try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="priceblock_ourprice"]'))
        )
        print("found")
        price = driver.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text
        print(price)
    finally:
        driver.quit()
    
    