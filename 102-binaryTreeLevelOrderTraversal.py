'''
102. Binary Tree Level Order Traversal

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # queue
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        else:
            q, res = [root], []
            while q:
                sub, nq = [], []
                while q:
                    node = q.pop(0)
                    if node.left: nq.append(node.left)
                    if node.right: nq.append(node.right)
                    sub.append(node.val)
                q = nq
                res.append(sub)
            return res
            
                
        