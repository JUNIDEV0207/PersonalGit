from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "C:\\Users\\Administrator\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
driver.get("https://www.google.com")

search = driver.find_element_by_name("q")

search.send_keys("google")
search.send_keys(Keys.RETURN)

results = driver.find_elements_by_xpath("//div[@class='kno-rdesc']/span")
for value in results:
    print(value.text)
