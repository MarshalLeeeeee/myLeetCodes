'''
105. Construct Binary Tree from Preorder and Inorder Traversal

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

Example:
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder: return None
        elif len(preorder) == 1: return TreeNode(preorder[0])
        else:
            root = TreeNode(preorder[0])
            for i,n in enumerate(inorder):
                if n == preorder[0]:
                    break
            left = self.buildTree(preorder[1:1+i],inorder[:i])
            right = self.buildTree(preorder[1+i:],inorder[i+1:])
            root.left, root.right = left, right
            return root
        