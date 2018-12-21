'''
118. Pascal's Triangle

Example:
Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        if not numRows: return res
        for i in range(numRows):
            if i == 0: res.append([1])
            else:
                res.append([1])
                for j in range(1,i):
                    res[-1].append(res[-2][j-1]+res[-2][j])
                res[-1].append(1)
        return res