'''
228. Summary Ranges

Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:
Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.

Example 2:
Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
'''

class Solution:
	# recursion
    def form(self,res):
        ans = []
        for r in res:
            if r[0] == r[1]: ans.append(str(r[0]))
            else: ans.append(str(r[0])+'->'+str(r[1]))
        return ans

    def solve(self,nums):
        if not nums: return []
        elif len(nums) == 1: return [[nums[0],nums[0]]]
        elif len(nums) == 2: return [[nums[0],nums[0]],[nums[1],nums[1]]] if nums[0] + 1 != nums[1] else [[nums[0],nums[1]]]
        elif nums[-1]-nums[0] == len(nums)-1: return [[nums[0],nums[-1]]]
        else:
            left = self.solve(nums[:len(nums)//2])
            right = self.solve(nums[len(nums)//2:])
            print(left,right)
            if left[-1][1] == right[0][0] or left[-1][1] + 1 == right[0][0]: res = left[:-1]+[[left[-1][0],right[0][1]]]+right[1:]
            else : res = left+right
            return res
        
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        return self.form(self.solve(nums))

if __name__ == '__main__':
    print(Solution().summaryRanges([0,1,2,4,5,7]))