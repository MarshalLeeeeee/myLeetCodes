'''
166. Fraction to Recurring Decimal

Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 2, denominator = 3
Output: "0.(6)"
'''

class Solution:
    def solve(self, a, b):
        dic, res, i = {}, '', 0
        while a:
            if 10 * a in dic:
                return res[:dic[10*a]] + '(' + res[dic[10*a]:] + ')'
            else:
                dic[10*a] = i
                res += str(10*a//b)
                a = 10*a%b
                i += 1
        return res
        
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        aneg = 1 if numerator < 0 else -1
        bneg = 1 if denominator < 0 else -1
        a,b = abs(numerator), abs(denominator)
        if not a: aneg = 0
        if not b: bneg = 0
        d = a // b
        f = self.solve(a % b, b)
        if f: return str(d)+'.'+f if aneg*bneg >= 0 else '-'+str(d)+'.'+f
        else: return str(d) if aneg*bneg >= 0 else '-'+str(d)