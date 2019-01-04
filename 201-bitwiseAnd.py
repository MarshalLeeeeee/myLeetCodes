'''
201. Bitwise AND of Numbers Range

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:
Input: [5,7]
Output: 4

Example 2:
Input: [0,1]
Output: 0
'''

class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if not m: return 0
        elif m == n: return m
        num, base = n-m+1, 1
        for i in range(32):
            if base >= num: return base*self.rangeBitwiseAnd(m//base,n//base)
            base *= 2