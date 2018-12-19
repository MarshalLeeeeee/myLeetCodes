'''
99. Recover Binary Search Tree

Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

Example 1:
Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2

Example 2:
Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

Follow up:
A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:  
    # morris traverse  
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        curr = root
        l, r = None, None
        swapLeft, swapRight = None, None
        while curr:
            if curr.left:
                prev = curr.left
                while prev.right and prev.right != curr:
                    prev = prev.right
                
                if prev.right == curr:
                    l,r = r,curr
                    if l != None and r != None and l.val > r.val and not swapLeft: swapLeft, swapRight = l,r
                    elif l != None and r != None and l.val > r.val and swapLeft: swapRight = r
                    else: pass
                    prev.right = None
                    curr = curr.right
                    
                else:
                    prev.right = curr
                    curr = curr.left
            else:
                l,r = r,curr
                if l != None and r != None and l.val > r.val and not swapLeft: swapLeft, swapRight = l,r
                elif l != None and r != None and l.val > r.val and swapLeft: swapRight = r
                else: pass
                curr = curr.right
        swapLeft.val, swapRight.val = swapRight.val, swapLeft.val