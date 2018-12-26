'''
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        currOrigin, currPrev = head, RandomListNode(0)
        labelDict, nodes, i = {}, [], 0
        ansHead = currPrev
        while currOrigin:
            node = RandomListNode(currOrigin.label)
            currPrev.next = node
            currPrev = node
            nodes.append(node)
            labelDict[node.label] = i
            i += 1
            currOrigin = currOrigin.next
        ansHead = ansHead.next
        currOrigin, curr = head, ansHead
        while currOrigin:
            if currOrigin.random:
                curr.random = nodes[labelDict[currOrigin.random.label]]
            currOrigin = currOrigin.next
            curr = curr.next
        return ansHead