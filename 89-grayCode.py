'''
89. Gray Code

The gray code is a binary numeral system where two successive values differ in only one bit.
Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.

Example 1:
Input: 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2

For a given n, a gray code sequence may not be uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence.
00 - 0
10 - 2
11 - 3
01 - 1

Example 2:
Input: 0
Output: [0]
Explanation: We define the gray code sequence to begin with 0.
             A gray code sequence of n has size = 2n, which for n = 0 the size is 20 = 1.
             Therefore, for n = 0 the gray code sequence is [0].
'''

class Solution:
    # recursion
    def solve(self, n):
        if not n: return [0], 0
        elif n == 1: return [0, 1], 1
        else:
            res, p = self.solve(n-1)
            l,add,base = len(res),[],2*p
            for i in range(l-1,-1,-1):
                add.append(res[i]+base)
            return res+add, base
        
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = self.solve(n)
        return res[0]