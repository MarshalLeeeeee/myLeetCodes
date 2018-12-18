# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # trivial recursion
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        else:
            left = self.inorderTraversal(root.left)
            right = self.inorderTraversal(root.right)
            return left+[root.val]+right