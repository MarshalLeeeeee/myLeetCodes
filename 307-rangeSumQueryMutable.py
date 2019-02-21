'''
307. Range Sum Query - Mutable

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.
The update(i, val) function modifies nums by updating the element at index i to val.

Example:
Given nums = [1, 3, 5]
sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8

Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
'''

class NumArray:
    # seegment tree
    # O(logn)
    def __init__(self, nums: 'List[int]'):
        self.len = len(nums) + 1
        self.data = [0] * self.len
        for i in range(len(nums)):
            curr = i+1
            while curr < self.len:
                self.data[curr] += nums[i]
                curr = curr + (curr & (-curr))
        #self._show()
                
    def _show(self) -> 'None':
        for n in self.data:
            print(n, end = ' ')
        print('')
                
    def _sum(self, i: 'int') -> 'int':
        res = 0
        while i > 0:
            res += self.data[i]
            i = i - (i & (-i))
        return res
                
    def _index(self, i: 'int') -> 'int':
        return self._sum(i) - self._sum(i-1)

    def update(self, i: 'int', val: 'int') -> 'None':
        old = self._index(i+1)
        gap = val - old
        curr = i+1
        while curr < self.len:
            self.data[curr] += gap
            curr = curr + (curr & (-curr))

    def sumRange(self, i: 'int', j: 'int') -> 'int':
        return self._sum(j+1) - self._sum(i)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)