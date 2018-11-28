'''
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9
Because nums[0] + nums[1] = 2 + 7 = 9
return [0, 1].
'''

'''
# O(n) solution using hashtable
class Solution:    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashMap=dict()
        for i,x in enumerate(nums):
            if target-x in hashMap:
                return [hashMap[target-x],i]
            hashMap[x] = i
'''

# my solution is O(nlogn)
class Solution:    
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def keySort(elem):
            return elem[0]
        
        def returnTerminal(nums, target):
            end = len(nums) - 1
            start = 0
            while(end >= start):
                mid = int((start + end) / 2)
                if(nums[mid][0] == target):
                    return mid
                elif(nums[mid][0] > target):
                    end = mid - 1
                else:
                    start = mid + 1
            return -1
        
        def answer(nums,target):
            l = len(nums)
            index = returnTerminal(nums,target)
            if(index == -1):
                return -1
            else:
                return nums[index][1]
        
        l = len(nums)
        nIndex = []
        for i in range(l):
            nIndex.append((nums[i],i))
        
        nIndex.sort(key=keySort)
        for i in range(l):
            pairIndex = answer(nIndex[i+1:],target-nIndex[i][0])
            if pairIndex != -1:
                answer = [nIndex[i][1],pairIndex]
                break
        answer.sort()
        return answer

if __name__ == '__main__':
    obj = Solution()
    print(obj.twoSum([3,2,3],6))