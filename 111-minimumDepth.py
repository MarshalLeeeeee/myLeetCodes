'''
111. Minimum Depth of Binary Tree

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        queue, dep = [root], 0
        while queue:
            nq = []
            dep += 1
            while queue:
                node = queue.pop()
                if not node.left and not node.right: return dep
                else:
                    if node.left: nq.append(node.left)
                    if node.right: nq.append(node.right)
            queue = nq