import unittest
from first_test_with_unitest import WaitForElements
from assertTitle import AssertTitle

class TestSuite1(unittest.TestSuite):

	def suite():
		suite = unittest.TestSuite1()
		suite.addTest(WaitForElements('test_WaitForCheckOutPhotosButton'))
		suite.addTest(WaitForElements('test_WaitForSearchField'))
		suite.addTest(WaitForElements('test_AssertTitle'))
		return suite

if __name__ == '__main__':
	unittest.main()
