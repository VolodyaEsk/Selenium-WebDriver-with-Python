from selenium import webdriver


driver = webdriver.Firefox()

driver.implicitly_wait(15)

driver.get("http://google.com")

searchField = driver.find_element_by_css_selector("input[name=d]")

driver.quit()
