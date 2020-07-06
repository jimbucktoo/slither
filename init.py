from selenium import webdriver
PATH = "/Users/jamesliang/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://jimbucktoo.com")
print(driver.title)
driver.quit()
