'''
216. Combination Sum III

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:
All numbers will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:
Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]
'''

class Solution:
    def init(self,k,n):
        res = []
        for i in range(k+1):
            res.append([])
            for j in range(n+1):
                if not j: res[-1].append([[]])
                else: res[-1].append([])
        return res
        
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n > (18-k+1)*k//2 or n < (1+k)*k//2: return []
        record = self.init(k,n)
        for x in range(1,min(9,n)+1):
            for i in range(min(x,k),0,-1):
                for j in range(1,n+1):
                    if j >= x:
                        for r in record[i-1][j-x]:
                            if len(r) == i-1: 
                                record[i][j].append(r+[x])
        return record[-1][-1]