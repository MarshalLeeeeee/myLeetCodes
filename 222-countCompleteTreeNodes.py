'''
222. Count Complete Tree Nodes

Given a complete binary tree, count the number of nodes.

Note:
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. 
It can have between 1 and 2h nodes inclusive at the last level h.

Example:
Input: 
    1
   / \
  2   3
 / \  /
4  5 6
Output: 6
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pow2(self,p):
        if not p: return 1
        elif p == 1: return 2
        elif p%2 == 0: 
            res = self.pow2(p//2)
            return res*res
        else: 
            res = self.pow2(p//2)
            return 2*res*res
        
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        else:
            if not root.left and not root.right: return 1
            elif (root.left and not root.right) or (not root.left and root.right): return 2
            else:
                leftmost,rightmost,mid = 0,0,0
                curr = root.left
                while curr:
                    leftmost += 1
                    curr = curr.left
                curr = root.right
                while curr:
                    rightmost += 1
                    curr = curr.right
                curr = root.left
                while curr:
                    mid += 1
                    curr = curr.right
                if leftmost == mid and mid == rightmost: return self.pow2(mid+1)-1
                elif leftmost == mid: return self.countNodes(root.right)+self.pow2(leftmost) 
                else: return self.countNodes(root.left)+self.pow2(rightmost) 