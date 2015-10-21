from TravelingTony.Constants            import TT_Constants
from TravelingTony.BaseTestCase         import BaseTestCase
from TravelingTony.Common               import Common
import unittest
import time


class SendRequestTest(BaseTestCase, unittest.TestCase):

    def setUp(self):
        super(SendRequestTest, self).setUp()
        self.navigate_to_page(TT_Constants['Base_URL'])
        

    def test_SendRequestTest(self):
        common_obj = Common(self.driver)
        common_obj.wait_for_element_visibility(10, 
                                               "name", 
                                               "q"
        )
        common_obj.fill_out_field("name", 
                                  "q", 
                                  "Leatherback"
        )
        
        common_obj.click(10, "cssSelector", "span.wsite-search-button")
        common_obj.wait_for_element_visibility(10, 
                                               "xpath", 
                                               "//span[@title='Leatherback Turtle Picture']"
        )

        """
        Just using time.sleep() so that you see the last webdriver action.
        I do not recommend using this in your tests.
        """
        time.sleep(5)

    
    def tearDown(self):
        super(SendRequestTest, self).tearDown()
        

if __name__ == "__main__":
   unittest.main()


