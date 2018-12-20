'''
113. Path Sum II

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:
[
   [5,4,11,2],
   [5,8,4,5]
]

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def solve(self,root,sum,res,path):
        if root: 
            if root.left and root.right: 
                self.solve(root.left,sum-root.val,res,path+[root.val])
                self.solve(root.right,sum-root.val,res,path+[root.val])
            elif not root.left and root.right: self.solve(root.right,sum-root.val,res,path+[root.val])
            elif root.left and not root.right: self.solve(root.left,sum-root.val,res,path+[root.val])
            else: 
                if sum == root.val: res.append(path+[root.val])
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root: return []
        res, path = [], []
        self.solve(root,sum,res,path)
        return res