# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # recursion solution
    def judge(self, r1, r2):
        if not r1 and not r2: return True
        elif r1 and r2: return r1.val == r2.val and self.judge(r1.left,r2.right) and self.judge(r1.right,r2.left)
        else: return False
    
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        else:
            if root.left and root.right: return self.judge(root.left,root.right)
            elif not root.left and not root.right: return True
            else: return False
                
        