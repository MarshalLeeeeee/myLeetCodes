'''
172. Factorial Trailing Zeroes

Given an integer n, return the number of trailing zeroes in n!.

Example 1:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.
'''

class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res, base = 0, 5
        while True:
            a = n // base
            if not a: return res
            res += a
            base *= 5