'''
236. Lowest Common Ancestor of a Binary Tree

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
According to the definition of LCA on Wikipedia: 
    “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]

      3
   /     \
  5       1  
 / \     / \
6   2   0   8
   / \
  7   4

Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
 
Note:
All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def dfs(self,root,node,path):
        path.append(root)
        if node.val == root.val: return True
        if root.left and self.dfs(root.left,node,path): return True
        if root.right and self.dfs(root.right,node,path): return True
        path.pop()
        return False
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pathP, pathQ = [], []
        self.dfs(root,p,pathP)
        self.dfs(root,q,pathQ)
        i,res = 1,root
        while i < len(pathP) and i < len(pathQ):
            if pathP[i] == pathQ[i]: res = pathP[i]; i+=1
            else: break
        return res
        