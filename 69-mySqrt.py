'''
69. Sqrt(x)

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
'''

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if not x: return 0
        if x == 1: return 1
        left, right = 1, x // 2
        while left <= right:
            mid = (left+right) // 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid -1
            else:
                return mid
        return right
        