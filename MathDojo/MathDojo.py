import unittest


class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for x in nums:
            self.result += x
        return self
        

    def subtract(self, num, *nums):
        self.result -= num
        for x in nums:
            self.result -= x
        return self



class mathDojoTests(unittest.TestCase):
    def testOne(self):
        md = MathDojo()
        self.assertEqual(md.add(5).subtract(2).result, 3)

    def testTwo(self):
        md = MathDojo()
        self.assertEqual(md.add(5).result, 5)



if __name__ == '__main__':
    unittest.main()


