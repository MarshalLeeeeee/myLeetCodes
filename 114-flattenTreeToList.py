'''
114. Flatten Binary Tree to Linked List

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def solve(self,root):
        if root:
            if root.left and root.right: 
                leftHead, leftTail = self.solve(root.left)
                rightHead, rightTail = self.solve(root.right)
                root.right, root.left = leftHead, None
                leftTail.right = rightHead
                return root, rightTail
            elif not root.left and root.right:
                rightHead, rightTail = self.solve(root.right)
                root.right = rightHead
                return root, rightTail
            elif root.left and not root.right: 
                leftHead, leftTail = self.solve(root.left)
                root.right, root.left = leftHead, None
                return root, leftTail
            else: return root, root
            
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.solve(root)