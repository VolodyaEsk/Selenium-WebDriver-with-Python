from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.implicitly_wait(15)

driver.get("http://google.com")

fLocator = "input[name=d]"

try:
	search = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, fLocator)))
finally:
	driver.quit()

