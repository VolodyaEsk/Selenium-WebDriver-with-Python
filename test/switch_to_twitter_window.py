from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
import time


class SwitchToWindow(unittest.TestCase):

	def setUp(self):
		global driver
		driver = webdriver.Firefox()
		driver.get("http://travelingtony.weebly.com/store/p3/Asala_Loadge.html")
		driver.maximize_window()

	def test_SwitchToFacebookWindow(self):
		#Locators
		twitterSharingLinkLocator = 'a.wsite-com-product-social-twitter'
		twitterUsernameFieldID = "username_or_email"
		twitterPasswordFieldID = 'password'
		twitterLoginButtonXpath = '//input[@value="Log in and Tweet"]'
		twitterNotCredentialLocator = "//div[@class='u-tableCell u-alignMiddle']/p[1]"
		expected_text = 'The username and password do not match.'

		#Facebook credentials
		twitterUsername = 'ivan'
		twitterPassword = '20d12m8qw'

		twSharingLingElement = WebDriverWait(driver, 10).\
								until(lambda driver: driver.find_element_by_css_selector(twitterSharingLinkLocator))

		#Get the main window handle
		mainWindowHandle = driver.window_handles
		print "main Window handle: %s" % mainWindowHandle

		#Click the "Facebook sharing" link, switch to the Facebook login window and log in
		twSharingLingElement.click()
		allWindowHandlesList = driver.window_handles
		print "all window handles %s " % allWindowHandlesList
		for handle in allWindowHandlesList:
			if handle != mainWindowHandle[0]:
				driver.switch_to_window(handle)
				print handle
				break

		twitterUsernameFieldElement = WebDriverWait(driver, 10).\
										until(lambda driver: driver.find_element_by_id(twitterUsernameFieldID))

		twitterPasswordFieldElement = WebDriverWait(driver, 10).\
										until(lambda driver: driver.find_element_by_id(twitterPasswordFieldID))
		twitterLoginButtonElement = WebDriverWait(driver, 10).\
										until(lambda driver: driver.find_element_by_xpath(twitterLoginButtonXpath))

		twitterUsernameFieldElement.send_keys(twitterUsername)
		twitterPasswordFieldElement.send_keys(twitterPassword)
		#time.sleep(10)
		twitterLoginButtonElement.click()
		allWindowHandlesList = driver.window_handles
		print "ALL (MAYBE MORE THAN 2) - %s" %allWindowHandlesList
		#time.sleep(10)

		twitterNotCredentialElement = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath(twitterNotCredentialLocator))
		actual_text = twitterNotCredentialElement.text
		self.assertEqual(expected_text, actual_text)

		time.sleep(5)

	def tearDown(self):
		driver.quit()

if __name__ == '__main__':
	unittest.main()