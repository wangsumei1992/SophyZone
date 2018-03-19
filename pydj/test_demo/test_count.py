#coding=utf-8
from count import countor
import unittest

class Testadd(unittest.TestCase):
    def test_add(self):
        c = countor(3,5)
        self.assertEqual(c.add(),8)
    def test_add1(self):
        c = countor(0,6)
        self.assertEqual(c.add(),6)

class Testsub(unittest.TestCase):

    def test_sub(self):
        c = countor(3,5)
        self.assertEqual(c.sub(),-2)

    def test_sub1(self):
        c = countor(0, 6)
        self.assertEqual(c.sub(), -6)

if __name__ == "__main__":
    #unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(Testadd("test_add"))
    suit.addTest(Testadd("test_add1"))
    suit.addTest(Testsub("test_sub"))
    suit.addTest(Testsub("test_sub1"))
    runner = unittest.TextTestRunner()
    runner.run()

    #suit = unittest.defaultTestLoader.discover()


