from TravelingTony.Constants            import TT_Constants
from TravelingTony.pages.ContactPage    import ContactPage
from TravelingTony.BaseTestCase         import BaseTestCase
import unittest
import time


class SendRequestTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(SendRequestTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'] + "contact")
        
    def test_SendRequestTest(self):
        contact_page_obj = ContactPage(self.driver)
        contact_page_obj.submit_request()
        """
        Just using time.sleep() so that you see the last webdriver action.
        I do not recommend using this in your tests.
        """
        time.sleep(5)

    def test_Validation(self):
        contact_page_obj = ContactPage(self.driver)
        contact_page_obj.validation_check()
        """
        Just using time.sleep() so that you see the last webdriver action.
        I do not recommend using this in your tests.
        """
        time.sleep(5)

    def tearDown(self):
        super(SendRequestTest, self).tearDown()
        

if __name__ == "__main__":
   unittest.main()



