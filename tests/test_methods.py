'''
Created on 19 Dec 2020


@author: semuadmin
'''

import unittest
from sandpit.main import Classof2020, TWATS


class StaticTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRandomTwat(self):
        t = Classof2020()
        res = t.random_twat()
        self.assertIn(res, TWATS)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
