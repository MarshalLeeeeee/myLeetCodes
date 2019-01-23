'''
257. Binary Tree Paths

Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.

Example:
Input:

   1
 /   \
2     3
 \
  5
Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def solve(self,root,path,res):
        path.append(root.val)
        if not root.left and not root.right: 
            res.append(path.copy())
        if root.left: self.solve(root.left,path,res)
        if root.right: self.solve(root.right,path,res)
        path.pop()
    
    def form(self,res):
        ans = []
        for r in res:
            ans.append(str(r[0]))
            for i in range(1,len(r)):
                ans[-1] += '->'+str(r[i])
        return ans
    
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root: return []
        else: 
            res = []
            self.solve(root,[],res)
            #print(res)
            return self.form(res)