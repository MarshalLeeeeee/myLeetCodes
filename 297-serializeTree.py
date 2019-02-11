'''
297. Serialize and Deserialize Binary Tree

Serialization is the process of converting a data structure or object into a sequence of bits 
so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. 
There is no restriction on how your serialization/deserialization algorithm should work. 
You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example: 
You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"

Clarification: The above format is the same as how LeetCode serializes a binary tree. 
You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. 
Your serialize and deserialize algorithms should be stateless.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    # BFS
    # record until the last None node
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        res = ''
        if root:
            q = [root]
            while q:
                nq = []
                while q:
                    node = q.pop(0)
                    if node:
                        res += str(node.val) + ' '
                        nq.append(node.left)
                        nq.append(node.right)
                    else:
                        res += 'none '
                q = nq
        return res
        

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if data:
            d = data.split()
            root = TreeNode(int(d[0]))
            q, i = [root], 1
            while q:
                #print(q)
                nq = []
                while q:
                    node = q.pop(0)
                    try:
                        n = int(d[i])
                        node.left = TreeNode(n)
                        nq.append(node.left)
                    except:
                        pass
                    i += 1
                    try:
                        n = int(d[i])
                        node.right = TreeNode(n)
                        nq.append(node.right)
                    except:
                        pass
                    i += 1
                q = nq
            return root
            
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))