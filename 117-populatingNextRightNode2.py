'''
117. Populating Next Right Pointers in Each Node II

Given a binary tree
struct TreeLinkNode {
  TreeLinkNode *left;
  TreeLinkNode *right;
  TreeLinkNode *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
Initially, all next pointers are set to NULL.

Note:
You may only use constant extra space.
Recursive approach is fine, implicit stack space does not count as extra space for this problem.

Example:
Given the following binary tree,

     1
   /  \
  2    3
 / \    \
4   5    7
After calling your function, the tree should look like:

     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL

'''

# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
	# recursion solution
    def findLeftmost(self,root):
        if root:
            if root.left: return root.left
            elif root.right: return root.right
            else: return self.findLeftmost(root.next)
        else: return None
            
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: return nothing
        """
        if root:
            self.connect(root.left)
            self.connect(root.right)
            left, right = root.left,root.right
            while left and right:
                print(left.val,right.val)
                leftNext = self.findLeftmost(left)
                rightNext = self.findLeftmost(right)
                curr = left
                while curr.next:
                    curr = curr.next
                curr.next = right
                left, right = leftNext, rightNext

class Solution2:
	# iteration solution
	# level update
	# find nearby subtree by root.next          
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: return nothing
        """
        while root:
            levelHead = TreeLinkNode(0)
            curr = levelHead
            while root:
                if root.left:
                    curr.next = root.left
                    curr = curr.next
                if root.right:
                    curr.next = root.right
                    curr = curr.next
                root = root.next
            root = levelHead.next