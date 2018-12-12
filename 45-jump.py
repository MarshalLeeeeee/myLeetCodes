'''
45. Jump Game II

Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

Example:
Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
             Jump 1 step from index 0 to 1, then 3 steps to the last index.


Note:
You can assume that you can always reach the last index.
'''

class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        if nums[0] >= len(nums):
            return 1
        nums = nums[::-1]
        steps = [0]
        for i,n in enumerate(nums):
            if i >= 1:
                if i-n <= 0: steps.append(1)
                else:
                    step, minStep, index = n, float('inf'), i-n
                    while(index<i):
                        minStep = steps[index]+1 if steps[index]+1 < minStep else minStep
                        if minStep == 2: break
                        index += 1
                    steps.append(minStep)
        return steps[-1]
                
            
if __name__ == '__main__':
    print(Solution().jump([1,2,3]))