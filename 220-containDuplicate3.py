'''
220. Contains Duplicate III

Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.

Example 1
Input: nums = [1,2,3,1], k = 3, t = 0
Output: true

Example 2:
Input: nums = [1,0,1,1], k = 1, t = 2
Output: true

Example 3:
Input: nums = [1,5,9,1,5,9], k = 2, t = 3
Output: false
'''

class ListNode:
    def __init__(self,val,index):
        self.val = val
        self.index = index
        self.prev = None
        self.next = None

class Solution:
	# manage the dictionary of ListNode
	# insert comp O(n)
	# tle 
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k < 0 or t < 0: return False
        head, tail = ListNode(float('-inf'),-1), ListNode(float('inf'),-1)
        head.next = tail
        tail.prev = head
        dic = {}
        for i,n in enumerate(nums):
            if n not in dic:
                dic[n] = ListNode(n,i)
                currPrev,curr = head,head.next
                while curr.val < n:
                    currPrev,curr = curr,curr.next
                currPrev.next, curr.prev = dic[n], dic[n]
                dic[n].prev, dic[n].next = currPrev, curr
                curr = dic[n].next
                while curr.val - dic[n].val <= t:
                    if i - curr.index <= k: return True
                    curr = curr.next
                curr = dic[n].prev
                while dic[n].val - curr.val <= t:
                    if i - curr.index <= k: return True
                    curr = curr.prev
            else:
                if i - dic[n].index <= k: return True
                curr = dic[n].next
                while curr.val - dic[n].val <= t:
                    if i - curr.index <= k: return True
                    curr = curr.next
                curr = dic[n].prev
                while dic[n].val - curr.val <= t:
                    if i - curr.index <= k: return True
                    curr = curr.prev
                dic[n].index = i
        return False
       
############################################################################## 
class Solution2:
	# bucket dictionary
	# always managing elements within k previous index
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k <= 0 or t < 0: return False
        dic = {}
        m = min(nums)
        nums = [x-m for x in nums] # make it all natrual number
        for i,n in enumerate(nums):
            bucket = n//(t+1)
            if bucket in dic: return True
            if bucket-1 in dic and n-dic[bucket-1]<=t: return True
            if bucket+1 in dic and dic[bucket+1]-n<=t: return True
            if len(dic) == k:
                dic.pop(nums[i-k]//(t+1))
            dic[bucket] = n
        return False
        
############################################################################## 
class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Solution3:
	# BST solution
	# check the condition every time insert a number into the tree
	# always managing the cleraest k elements
    def add(self, root, val, t):
        if root:
            curr = root
            while(curr):
                if curr.val > val:
                    if curr.val - val <= t: return root,True
                    parent,curr,flag = curr,curr.left,1
                elif curr.val < val:
                    if val - curr.val <= t: return root,True
                    parent,curr,flag = curr,curr.right,0
                else: return root,True
            curr = TreeNode(val)
            if flag: parent.left = curr
            else: parent.right = curr
            return root,False
        else: return TreeNode(val),False
    
    def delete(self,root, val):
        parent, curr = None, root
        while curr:
            if curr.val > val: parent,curr,flag = curr,curr.left,1
            elif curr.val < val: parent,curr,flag = curr,curr.right,0
            else:
                if not curr.left and not curr.right: curr = None
                elif curr.left and not curr.right: curr = curr.left
                elif not curr.left and curr.right: curr = curr.right
                else:
                    left, right = curr.left, curr.right
                    if left.right:
                        p, c = left, left.right
                        while c.right:
                            p,c = c,c.right
                        p.right = None
                        c.left, c.right = left, right
                        curr = c
                    else:
                        left.right = right
                        curr = left
                if parent:
                    if flag: parent.left = curr
                    else: parent.right = curr
                    return root
                else: return curr
            
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if k <= 0 or t < 0 or not nums: return False
        root, cnt = None, 0
        for i,n in enumerate(nums):
            root,res = self.add(root,n,t)
            if res: return res
            if cnt == k: root = self.delete(root,nums[i-k])
            else: cnt += 1
        return False