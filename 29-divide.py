'''
29. Divide Two Integers

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2

Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. 
For the purpose of this problem, assume that your function returns 2^31 − 1 when the division result overflows.
'''

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if not dividend:
            return 0
        negDividend = 1 if dividend > 0 else -1
        negDivisor = 1 if divisor > 0 else -1
        dividend = abs(dividend)
        divisor = abs(divisor)
        intMax = (1 << 31) -1
        intMin = -(1 << 31)
        ans = 0
        exp = 0
        while(True):
            if (dividend - divisor * (1 << exp) >= 0):
                dividend -= divisor * (1 << exp)
                ans += (1 << exp)
                exp += 1
            else:
                if exp == 0:
                    break
                else:
                    exp -= 1
        ans = negDividend * negDivisor * ans
        if (ans > intMax or ans < intMin):
            ans = intMax
        return ans

if __name__ == '__main__':
    print(Solution().divide(1,2))