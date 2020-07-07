from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = "/Users/jamesliang/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://google.com")

search = driver.find_element_by_name("q")
search.send_keys("Beyonce")
search.send_keys(Keys.RETURN)

try:
    contents = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    titles = contents.find_elements_by_class_name("g")
    print(str(len(titles)) + " search results")
    for title in titles:
        header = title.find_element_by_tag_name("h3")
        print(header.text)
finally:
    driver.quit()
