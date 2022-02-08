#import the testing framework
import unittest

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

class isEvenTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(isEven(2), True)

    def testTwo(self):
        self.assertEqual(isEven(3), False)

    def setUp(self):
        print("Running setUp")

    def tearDown(self) -> None:
        print("Running teardown tasks")

if __name__ == '__main__':
    unittest.main()

