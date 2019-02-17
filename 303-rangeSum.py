'''
303. Range Sum Query - Immutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3

Note:
You may assume that the array does not change.
There are many calls to sumRange function.
'''

class NumArray:
    def __init__(self, nums: 'List[int]'):
        self.sum, s = [], 0
        for n in nums:
            s += n
            self.sum.append(s)

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        if not i: return self.sum[j]
        else: return self.sum[j] - self.sum[i-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)