'''
40. Combination Sum II

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.
Each number in candidates may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

Example 1:
Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:
Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
'''

class Solution:
    def combination(self,nums,target,smallest):
        if target == 0:
            return [[]]
        flag = True
        for n in nums:
            if nums[n] > 0:
                if flag: 
                    minNum = n
                    flag = False
                else: minNum = n if n < minNum else minNum    
        if flag or target < minNum:
            return []
        ans = []
        for n in nums:
            if nums[n] > 0 and n >= smallest:
                nums[n] -= 1
                res = self.combination(nums,target-n,n)
                nums[n] += 1
                for r in res:
                    r.append(n)
                ans += res
        return ans
        
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        from collections import defaultdict
        nums = defaultdict(int)
        candidates.sort()
        minNum = candidates[0]
        for c in candidates:
            nums[c] += 1
        return self.combination(nums,target,minNum)

class Solution2:
    def combination(self,candidates,target):
        #print(candidates,target)
        if target == 0:
            return [[]]
        if not candidates or target < candidates[0]:
            return []
        ans = []
        cnt = 0
        curr = candidates[0]
        for i,c in enumerate(candidates):
            if c == curr:
                cnt += 1
            else:
                for j in range(cnt):
                    res = self.combination(candidates[i:],target-curr*(j+1))
                    for r in res:
                        r += [curr] * (j+1)
                    ans += res
                cnt = 1
                curr = c
        for j in range(cnt):
            res = self.combination([],target-curr*(j+1))
            for r in res:
                r += [curr] * (j+1)
            ans += res
        return ans
        
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        candidates.sort()
        return self.combination(candidates,target)

if __name__ == '__main__':
    print(Solution2().combinationSum2([1],2))
    print(Solution2().combinationSum2([1,2,8],9))