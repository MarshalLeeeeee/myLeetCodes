'''
7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:
Input: 123
Output: 321

Example 2:
Input: -123
Output: -321

Example 3:
Input: 120
Output: 21


Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
'''

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT32_MAX = 2147483647
        INT32_MIN = -2147483648
        if(x < 0):
            x = -x
            sx = str(x)[::-1]
            ans = -int(sx)
            if ans < INT32_MIN:
                return 0
            else:
                return ans
        elif(x == 0):
            return 0
        else:
            ans = int(str(x)[::-1])
            if ans > INT32_MAX:
                return 0
            else:
                return ans

class Solution2:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        INT32_MAX = 2147483647
        INT32_MIN = -2147483648
        neg = 1 if x > 0 else -1
        x *= neg
        ans = 0
        while(x):
            ans = ans * 10 + x % 10
            x //= 10
        ans *= neg
        if (ans > INT32_MAX or ans < INT32_MIN):
            return 0
        else:
            return ans

if __name__ == '__main__':
    print(Solution2().reverse(-15302))