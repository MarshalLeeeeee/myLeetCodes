'''
173. Binary Search Tree Iterator

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
Calling next() will return the next smallest number in the BST.

Example:
  7
 / \ 
3  15
  /  \
 9   20

BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false

Note:
next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.path = []
        if root:
            self.curr = root
            while self.curr.left:
                self.path.append(self.curr)
                self.curr = self.curr.left
        else: self.curr = None
        
    def _toNext(self):
        if self.curr.right:
            self.curr = self.curr.right
            while self.curr.left:
                self.path.append(self.curr)
                self.curr = self.curr.left
        else: self.curr = self.path.pop() if self.path else None
    
    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        ans = self.curr.val
        self._toNext()
        return ans
        
    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return True if self.curr else False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()