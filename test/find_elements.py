from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import unittest


class FindAnElement(unittest.TestCase):

	def setUp(self):
		global driver
		driver = webdriver.Firefox()
		driver.get("http://travelingtony.weebly.com/store/c2/Lope.html")
		#driver.implicitly_wait(10)

	def test_FindAnElement(self):
		#webElementsList = driver.find_elements_by_xpath("//img")
		#webElementsList = driver.find_elements_by_css_selector("img")
		webElementsList = WebDriverWait(driver, 10).until(lambda driver: driver.find_elements_by_xpath("//img"))

		print webElementsList
		print type(webElementsList)


	def tearDown(self):
		driver.quit()

if __name__ == '__main__':
	unittest.main()
