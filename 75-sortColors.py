class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums: return nums
        left, right, curr = 0, len(nums)-1, 0
        while curr <= right:
            if nums[curr] == 0:
                if curr == left:
                    curr += 1
                else:
                    nums[curr], nums[left] = nums[left], nums[curr]
                left += 1
            elif nums[curr] == 2:
                nums[curr], nums[right] = nums[right], nums[curr]
                right -= 1
            else:
                curr += 1

if __name__ == '__main__':
    nums = [2,0,1]
    Solution().sortColors(nums)
    print(nums)