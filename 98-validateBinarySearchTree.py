'''
98. Validate Binary Search Tree

Given a binary tree, determine if it is a valid binary search tree (BST).
Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input:
    2
   / \
  1   3
Output: true

Example 2:
    5
   / \
  1   4
     / \
    3   6
Output: false
Explanation: The input is: [5,1,4,null,null,3,6]. The root node's value
             is 5 but its right child's value is 4.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def preorder(self,root):
        if not root: return [],True
        else:
            left, right = root.left, root.right
            resLeft, flagLeft  = self.preorder(left)
            resRight, flagRight = self.preorder(right)
            if flagLeft and flagRight:
                if resLeft and resLeft[-1] >= root.val: return [], False
                elif resRight and resRight[0] <= root.val: return [], False
                else: return resLeft+[root.val]+resRight, True
            else: return [],False
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        order,flag = self.preorder(root)
        return flag