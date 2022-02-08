import unittest

def reverseList(list):
    list.reverse()
    return list

def isPalindrome(str):
    if(str[::-1] == str):
        return True
    else:
        return False

def coins(changeOwed): #[quarters,dimes,nickles,pennies"]
    changeArr = [0,0,0,0]
    while(changeOwed >= 25):
        changeArr[0] += 1
        changeOwed -= 25
    while(changeOwed >= 10):
        changeArr[1] += 1
        changeOwed -= 10
    while(changeOwed >= 5):
        changeArr[2] += 1
        changeOwed -= 5
    while(changeOwed >= 1):
        changeArr[3] += 1
        changeOwed -= 1
    return changeArr


def factorial(num):
    if(num == 1):
        return 1
    else:
        return num * factorial(num - 1)

def fibonnaci(num):
    index = 1
    current_num = 1
    prev_num = 0
    while(index < num):
        temp = current_num
        current_num = prev_num + current_num
        prev_num = temp
        index += 1
    return current_num



class reverseListTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(reverseList([5,3,1]), [1,3,5])
    
    def testTwo(self):
        self.assertEqual(reverseList([7,8,9]), [9,8,7])

    def testThree(self):
        self.assertEqual(reverseList([5,3,1,4,6]), [6,4,1,3,5])
    
    def testFour(self):
        self.assertEqual(reverseList([1,2]), [2,1])
        

class isPalindromeTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(isPalindrome("racecar"), True)
    
    def testTwo(self):
        self.assertEqual(isPalindrome("tacocat"), True)

    def testThree(self):
        self.assertEqual(isPalindrome("cherry"), False)
    
    def testFour(self):
        self.assertEqual(isPalindrome("hello"), False)
        
    def testFive(self):
        self.assertEqual(isPalindrome("cac"), True)
    
    def testSix(self):
        self.assertEqual(isPalindrome("loop"), False)

class coinsTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(coins(87), [3,1,0,2])
    
    def testTwo(self):
        self.assertEqual(coins(2), [0,0,0,2])

    def testThree(self):
        self.assertEqual(coins(5), [0,0,1,0])
    
    def testFour(self):
        self.assertEqual(coins(50), [2,0,0,0])
        
    def testFive(self):
        self.assertEqual(coins(74), [2,2,0,4])
    
    def testSix(self):
        self.assertEqual(coins(124), [4,2,0,4])

class factorialTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(factorial(5), 120)
    
    def testTwo(self):
        self.assertEqual(factorial(3), 6)

    def testThree(self):
        self.assertEqual(factorial(4), 24)
    
    def testFour(self):
        self.assertEqual(factorial(1), 1)


class fibonacciTests(unittest.TestCase):
    def testOne(self):
        self.assertEqual(fibonnaci(2), 1)

    def testTwo(self):
        self.assertEqual(fibonnaci(3), 2)

    def testThree(self):
        self.assertEqual(fibonnaci(5), 5)
        

if __name__ == '__main__':
    unittest.main()