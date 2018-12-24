'''
128. Longest Consecutive Sequence

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
Your algorithm should run in O(n) complexity.

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
'''

class Solution:
    def find(self,union,x):
        if union[x][0] < 0: return x
        else: return self.find(union,union[x][0])
    
    def union(self,union,x,y):
        xr = self.find(union,x)
        yr = self.find(union,y)
        if xr != yr:
            if union[xr][1] < union[yr][1]: 
                union[xr][0] = yr
                union[yr][1] = max(union[xr][1]+1,union[yr][1])
                union[yr][2] += union[xr][2]
                return union[yr][2]
            else:
                union[yr][0] = xr
                union[xr][1] = max(union[yr][1]+1,union[xr][1])
                union[xr][2] += union[yr][2]
                return union[xr][2]
        else: return 0
        
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if not l: return 0
        elif l == 1: return 1
        else:
            nums = list(set(nums))
            union, maxSet = [[-1,0,1] for _ in range(len(nums))], 1
            for i,n in enumerate(nums):
                try: 
                    index = nums.index(n-1)
                    maxSet = max(maxSet,self.union(union,i,index))
                except: continue
            return maxSet

if __name__ == '__main__':
    print(Solution().longestConsecutive([4,0,-4,-2,2,5,2,0,-8,-8,-8,-8,-1,7,4,5,5,-4,6,6,-3]))