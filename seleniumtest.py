from selenium import webdriver
driver = webdriver.Chrome(executable_path="C:\\Users\\Administrator\\Downloads\\chromedriver_win32\\chromedriver.exe")
driver.get("http://www.google.com")

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(chrome_options=options)

element = driver.find_element_by_name("q")
element.send_keys("catdog"+ Keys.RETURN)
element.submit()

results = driver.find_elements_by_xpath("//div[@class='g']//div[@class='r']//a[not(@class)]");
for result in results:
    print(result.get_attribute("href"))
