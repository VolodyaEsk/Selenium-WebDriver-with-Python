from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
import time

class GetTextOrAttribute(unittest.TestCase):

	def setUp(self):
		global driver
		driver = webdriver.Firefox()
		driver.get("http://travelingtony.weebly.com/")
		driver.maximize_window()

	def test_homework(self):
		search_field_name_locator = 'q'
		search_field_element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_name(search_field_name_locator))
		search_field_element.send_keys("leatherback")

		search_button_locator = 'wsite-search-button'
		search_button_element = WebDriverWait(driver, 10).\
								until(lambda driver: driver.find_element_by_class_name(search_button_locator))
		search_button_element.click()

		leatherback_product_locator = '//span[@title="Leatherback Turtle Picture"]'
		leatherback_product_element = WebDriverWait(driver, 10).\
									until(lambda driver: driver.find_element_by_xpath(leatherback_product_locator))
		leatherback_product_element.click()

		dropDownId = "wsite-com-product-option-Quantity"	
		dropDownElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id(dropDownId))
		Select(dropDownElement).select_by_visible_text("3")

		time.sleep(5)

	def tearDown(self):
		driver.quit()



if __name__ == '__main__':
	unittest.main()