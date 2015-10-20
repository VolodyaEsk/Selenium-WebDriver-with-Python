from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import unittest


class FindAnElement(unittest.TestCase):

	def setUp(self):
		global driver
		driver = webdriver.Firefox()
		driver.get("http://travelingtony.weebly.com")
		#driver.implicitly_wait(10)

	def test_FindAnElement(self):
		#webElement = driver.find_element_by_xpath("//input[@name='q']")
		#webElement = driver.find_element_by_css_selector("input[name=q]")
		#webElement = driver.find_element_by_name("q")
		#webElement = driver.find_element_by_class_name("wsite-search-input")
		webElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath("//input[@name='q']"))

		print webElement
		print type(webElement)


	def tearDown(self):
		driver.quit()
		
if __name__ == '__main__':
	unittest.main()
