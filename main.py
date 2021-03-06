from selenium import webdriver
import time

# declares chromedriver
browser = webdriver.Chrome("C:\\Users\\Andrey\\Downloads\\chromedriver_win32\\chromedriver.exe")

# open page
browser.get("https://www.google.com/finance/quote/PEP:NASDAQ?window=5Y%22")
time.sleep(1)
# gets price
price = browser.find_element_by_xpath("//div[@class='YMlKec fxKbKc']")
print(price.text)
quit()

browser.find_element_by_tag_name("body")