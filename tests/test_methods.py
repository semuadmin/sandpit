"""
Created on 19 Dec 2020

@author: semuadmin
"""

import unittest

from src.sandpit.main import bearing, haversine


class StaticTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testhaversine(self):
        res = haversine(51.23, -2.41, 34.205, 56.34)
        self.assertAlmostEqual(res, 5010.722, 3)
        res = haversine(-12.645, 34.867, 145.1745, -56.27846)
        self.assertAlmostEqual(res, 10715.371, 3)
        res = haversine(53.45, -2.14, 53.451, -2.141)
        self.assertAlmostEqual(res, 0.1296, 3)

    def testbearing(self):
        res = bearing(51.23, -2.41, 53.205, -2.34)
        self.assertAlmostEqual(res, 1.216362703824359, 4)
        res = bearing(51.23145, -2.41, 51.23145, -2.34)
        self.assertAlmostEqual(res, 89.9727111358776, 4)
        res = bearing(51.23, -2.41, 34.205, 56.34)
        self.assertAlmostEqual(res, 88.58134073451902, 4)
        res = bearing(-12.645, 34.867, -34.1745, 48.27846)
        self.assertAlmostEqual(res, 152.70835788275326, 4)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
