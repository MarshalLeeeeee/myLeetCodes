'''
124. Binary Tree Maximum Path Sum

Given a non-empty binary tree, find the maximum path sum.
For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. 
The path must contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]

       1
      / \
     2   3

Output: 6

Example 2:
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def solve(self,root):
        if not root: return None, None
        else:
            lpath, lrpath = self.solve(root.left)
            rpath, rrpath = self.solve(root.right)
            if not lrpath and not rrpath: rootPath = root.val
            elif lrpath and not rrpath: rootPath = max(lrpath+root.val,root.val)
            elif not lrpath and rrpath: rootPath = max(rrpath+root.val,root.val)
            else: rootPath = max(lrpath+root.val,rrpath+root.val,root.val)
            if not lpath and not rpath: path = root.val
            elif lpath and not rpath: path = max(lpath,lrpath+root.val,root.val)
            elif not lpath and rpath: path = max(rpath,rrpath+root.val,root.val)
            else: path = max(lpath,rpath,lrpath+rrpath+root.val,lrpath+root.val,rrpath+root.val,root.val)
        return path, rootPath
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        p, rp = self.solve(root)
        return p