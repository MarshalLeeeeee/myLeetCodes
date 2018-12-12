'''
67. Add Binary

Given two binary strings, return their sum (also a binary string).
The input strings are both non-empty and contains only characters 1 or 0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
'''

class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        aReverse, bReverse, cReverse, i, add = a[::-1], b[::-1], '', 0, 0
        while i < len(a) or i < len(b):
            aBit = int(aReverse[i]) if i < len(a) else 0
            bBit = int(bReverse[i]) if i < len(b) else 0
            cBit = aBit + bBit + add
            cReverse += str(cBit % 2)
            add = cBit // 2
            i += 1
        if add: cReverse += '1'
        return cReverse[::-1]
        