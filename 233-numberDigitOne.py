'''
233. Number of Digit One

Given an integer n, count the total number of digit 1 appearing in all non-negative integers less than or equal to n.

Example:
Input: 13
Output: 6 
Explanation: Digit 1 occurred in the following numbers: 1, 10, 11, 12, 13.
'''

class Solution:
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0: return 0
        digit = [0]
        cnt, base, res, m = 1, 1, 0, n
        while n:
            digit.append(base+10*digit[-1])
            d = n%10
            if d == 1: res += m-n*base+1+digit[cnt-1]
            elif d > 1: res += base + d * digit[cnt-1]
            cnt += 1
            base *= 10
            n //= 10
        return res

if __name__ == '__main__':
	print(Solution().countDigitOne(20))