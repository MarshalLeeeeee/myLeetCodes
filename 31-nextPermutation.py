'''
31. Next Permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

'''

class Solution:    
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not len(nums) or len(nums) == 1:
            pass
        else:
            hillleft, hillright = -1,-1
            curr = 1
            while(curr < len(nums)):
                if nums[curr] > nums[curr-1]:
                    hillleft, hillright = curr-1, curr
                else:
                    if hillleft == -1 or (nums[curr] > nums[hillleft]):
                        hillright = curr
                curr += 1
            if(hillleft == -1):
                half = (len(nums)-1) // 2 + 1
                for i in range(half):
                    nums[i], nums[len(nums)-1-i] = nums[len(nums)-1-i], nums[i]
            else:
                nums[hillleft], nums[hillright] = nums[hillright], nums[hillleft]
                half = (hillleft+len(nums)) // 2 + 1
                for i in range(hillleft+1,half):
                    nums[i], nums[hillleft+len(nums)-i] = nums[hillleft+len(nums)-i], nums[i]
        
if __name__ == '__main__':
    print(Solution().nextPermutation([1,2,3]))