'''
96. Unique Binary Search Trees

Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:
Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def solve(self, n):
        if not n: return [0]
        elif n == 1: return [1]
        else:
            res, ans, s = self.solve(n-1), [], 0
            for r in res:
                s += r
                ans.append(s)
            ans.append(s)
            return ans
        
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans,s = self.solve(n),0
        for a in ans:
            s += a
        return s