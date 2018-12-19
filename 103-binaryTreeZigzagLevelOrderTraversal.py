'''
103. Binary Tree Zigzag Level Order Traversal

Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        queue, mode, res = [root], 1, []
        while queue:
            nq, sub = [], []
            while queue:
                node = queue.pop()
                if mode:
                    if node.left: nq.append(node.left)
                    if node.right: nq.append(node.right)
                    sub.append(node.val)
                else:
                    if node.right: nq.append(node.right) 
                    if node.left: nq.append(node.left)
                    sub.append(node.val)
            mode = 1 - mode
            queue = nq
            res.append(sub)
        return res
            