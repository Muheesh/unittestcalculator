import unittest

import calculator
class checkcalc(unittest.TestCase):
    def test_add(self):
        a = 12
        b = 45
        c = calculator.add(a,b)
        self.assertTrue(c, a+b)
    def test_sub(self):
        a = 47
        b = 5
        c = calculator.sub(a,b)
        self.assertTrue(c , a-b)
    def test_mul(self):
        a = 41
        b = 12
        c = calculator.mul(a,b)
        self.assertTrue(c , a*b)
    def test_div(self):
        a = 41
        b = 4
        c = calculator.div(a,b)
        self.assertTrue(c,a/b)
if __name__ =="__main__":
    unittest.main()