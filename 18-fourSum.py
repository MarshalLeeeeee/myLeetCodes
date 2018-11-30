'''
18. 4Sum

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
'''

class Solution:   
    def triple(self,track,target):
        res = []
        for x in track:
            if track[x] == 3:
                temp, track[x] = track[x], 0
                y = target-3*x
                try:
                    if track[y] > 0:
                        res.append([x,x,x,y])
                except:
                    pass
                track[x] = temp
        return res
    
    def double_double(self,track,target):
        res = []
        if target % 2 == 1:
            return res
        for x in track:
            if track[x] >= 2 and target//2-x > x:
                try:
                    if track[target//2-x] >= 2:
                        res.append([x,x,target//2-x,target//2-x])
                except:
                    pass
        return res
    
    def double_uni(self,track,target):
        res = []
        for x in track:
            if track[x] >= 2:
                temp, track[x] = track[x], 0
                for y in track:
                    if track[y] > 0 and target-2*x-y > y:
                        temp2, track[y] = track[y], 0
                        try:
                            if track[target-2*x-y] > 0:
                                res.append([x,x,y,target-2*x-y])
                        except:
                            pass
                        track[y] = temp2
                track[x] = temp
        return res
    
    def uni_quad(self,track,target):
        res = []
        distinguish = [x for x in track]
        distinguish.sort()
        if(len(distinguish) < 4):
            return res
        if(distinguish[-1]+distinguish[-2]+distinguish[-3]+distinguish[-4] < target):
            return res
        if(distinguish[0]+distinguish[1]+distinguish[2]+distinguish[3] > target):
            return res
        for i in range(len(distinguish)-3):
            for j in range(i+1,len(distinguish)-2):
                for k in range(j+1,len(distinguish)-1):
                    if target-distinguish[i]-distinguish[j]-distinguish[k] > distinguish[k]:
                        try:
                            if track[target-distinguish[i]-distinguish[j]-distinguish[k]] > 0:
                                res.append([distinguish[i],distinguish[j],distinguish[k],target-distinguish[i]-distinguish[j]-distinguish[k]])
                        except:
                            pass
        return res
                        
        
        
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 4:
            return []
        
        nums.sort()
        track = dict()
        for i,n in enumerate(nums):
            try:
                track[n] += 1
            except:
                track[n] = 1
        
        if (target % 4 == 0):
            x = target // 4
            try:
                if track[x] >= 4:
                    res= [[x,x,x,x]]
                else:
                    res = []
            except:
                res = []
        else:
            res = []
        
        distinguish = []
        for x in track:
            distinguish.append(x)
            track[x] = min(3,track[x])
        res += self.triple(track,target)
        res += self.double_double(track,target)
        res += self.double_uni(track,target)
        res += self.uni_quad(track,target)
        return res

if __name__ == '__main__':
    print(Solution().fourSum([0,4,-5,2,-2,4,2,-1,4],12))