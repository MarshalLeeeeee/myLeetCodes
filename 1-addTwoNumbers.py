'''
2. Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# my solution
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ansRoot = ListNode(0)
        currNode = ansRoot
        addition = 0
        while(True):
            if(l1 != None and l2 != None):
                val = l1.val + l2.val + addition
                valMod = int(val % 10)
                addition = int(val / 10)
                currNode.next = ListNode(valMod)
                currNode = currNode.next
                l1 = l1.next
                l2 = l2.next
            elif(l1 == None and l2 != None):
                val = l2.val + addition
                valMod = int(val % 10)
                addition = int(val / 10)
                currNode.next = ListNode(valMod)
                currNode = currNode.next
                l2 = l2.next
            elif(l1 != None and l2 == None):
                val = l1.val + addition
                valMod = int(val % 10)
                addition = int(val / 10)
                currNode.next = ListNode(valMod)
                currNode = currNode.next
                l1 = l1.next
            else:
                break
        if addition:
            currNode.next = ListNode(1)
        return ansRoot.next

'''
# better solution whoes thinking is similar to mine
# more simplified
def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        
        new_list = ListNode(0)
        current = new_list
        carryover = 0
        
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            current_sum = l1_val + l2_val + carryover
            
            if current_sum < 10:
                current.next = ListNode(current_sum)
                carryover = 0
            else:
                current.next = ListNode(current_sum % 10)
                carryover = current_sum // 10
                
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            current = current.next
            
        if carryover:
            current.next = ListNode(carryover)
            
        return new_list.next
'''