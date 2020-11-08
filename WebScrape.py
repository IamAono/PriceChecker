from selenium import webdriver
import pickle
driver_path = "C:\\Drivers\\chromedriver.exe"
driver = webdriver.Chrome(executable_path = driver_path)
driver.get("https://www.adidas.com/us/continental-vulc-shoes/EF3524.html")
try:
    prices = pickle.load(open("save.p","rb"))
except:
    prices = {}
#pickle.dump( favorite_color, open("save.p", "wb"))
#favorite_color = pickle.load( open("save.p", "rb"))
#//*[@id="app"]/div/div/div/div/div[3]/div[2]/div[2]/div/div[2]/div[1]/div/div[2]
if __name__ == "__main__":
    change = False
    # go through the items to see if any prices changed
    for key in prices:
        pass
    if change:
        print("Prices have changed for: ")
    else:
        print("No change in prices")
    