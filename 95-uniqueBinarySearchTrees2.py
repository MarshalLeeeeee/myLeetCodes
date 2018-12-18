'''
95. Unique Binary Search Trees II

Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:
Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def copyTree(self, root):
        if not root: return None
        else:
            newRoot = TreeNode(root.val)
            newLeft = self.copyTree(root.left)
            newRight = self.copyTree(root.right)
            newRoot.left, newRoot.right = newLeft, newRight
            return newRoot
              
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n: return []
        elif n == 1: return [TreeNode(1)]
        else:
            res, ans = self.generateTrees(n-1), []
            for root in res:
                cnt, r = 0, root
                while r:
                    cnt += 1
                    r = r.right
                for i in range(cnt+1):
                    newRoot, node = self.copyTree(root), TreeNode(n)
                    if i == 0:
                        node.left = newRoot
                        ans.append(node)
                    else:
                        parent, curr, cnt = newRoot, newRoot.right, 1
                        while cnt < i:
                            parent, curr = curr, curr.right
                            cnt += 1
                        parent.right = node
                        node.left = curr
                        ans.append(newRoot)
            return ans