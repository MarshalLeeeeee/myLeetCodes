'''
300. Longest Increasing Subsequence

Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:
Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 

Note:
There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
'''

class ListNode:
    def __init__(self,val,length):
        self.val = val
        self.len = length
        self.next = None

class Solution:
    # O(n^2) linked list
    def lengthOfLIS(self, nums: 'List[int]') -> 'int':
        if not nums: return 0
        else:
            mode, data, head, res = 0, [], ListNode(float('-inf'),0), 1
            for i in range(len(nums)-1):
                if not mode and nums[i] < nums[i+1]: # down
                    mode = 1
                    data.append(nums[i])
                elif mode: # up
                    if nums[i] > nums[i-1] or (nums[i] < nums[i-1] and nums[i] <= nums[i+1]): data.append(nums[i])
                    elif nums[i] < nums[i-1]: mode = 0
            if (not mode) or (mode and nums[-1] > nums[-2]): data.append(nums[-1])
            print(data)
            for i in range(len(data)):
                curr, ans  = head, 0
                while curr and curr.val < data[i]:
                    ans = max(ans,curr.len+1)
                    currPrev, curr = curr, curr.next
                if curr and curr.val == data[i]: curr.len = ans
                else:
                    node = ListNode(data[i],ans)
                    node.next = curr
                    currPrev.next = node
                res = max(res,ans)
            return res



if __name__ == '__main__':
    print(Solution().lengthOfLIS([0]))
    print(Solution().lengthOfLIS([1,3,6,6,7,9,4,4,10,5,6]))