"""
Created on 19 Dec 2020

@author: semuadmin
"""

#pylint: disable=missing-class-docstring, missing-function-docstring

from subprocess import run, PIPE
import unittest

from sandpit.calculate import Calculate


class StaticTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testadd(self):
        c = Calculate()
        self.assertEqual(c.add(2.5,3.5),6)

    def testmultiply(self):
        c = Calculate()
        self.assertEqual(c.multiply(2.5,3.5),8.75)

    def testcalculate(self):
        c = Calculate()
        self.assertEqual(c.calc("add", 2.5,3.5),6)
        self.assertEqual(c.calc("multiply", 2.5,3.5),8.75)

    def testcalculateerror(self):
        c = Calculate()
        with self.assertRaisesRegex(ValueError,"Invalid function"):
            res = c.calc("divide", 2.5,3.5),0.7142857142857143

    def testcli(self):
        res = run(['calculate', '--function', 'add', '--arg1', '2.5', '--arg2', '3.5'], stdout=PIPE, check=False)
        res = res.stdout.decode('utf-8').strip("\r\n")
        self.assertEqual(res, '6.0')

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
