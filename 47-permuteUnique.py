'''
47. Permutations II

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

class Solution:
    # only work for positive integers
    def permuteNum(self,nums,length):
        if not nums: return []
        elif length == 1: return [nums[0]]
        else:
            res = self.permuteNum(nums[1:],length-1)
            track = dict()
            n = nums[0]
            for r in res:
                i, base = 0, 1
                while(i < length):
                    x = r % base + n * base + 10 * base * (r // base)
                    try:
                        track[x]+=1
                    except:
                        track[x]=1
                    i += 1
                    base *= 10
            return list(track.keys())
    
    def toList(self,nums):
        ans = []
        for i,n in enumerate(nums):
            ans.append([])
            s = str(n)
            for x in s:
                ans[i].append(int(x))
        return ans
    
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = self.permuteNum(nums,len(nums))
        return self.toList(res)

class Solution2:
    # reference to others solution
    # duplication is eliminated by order
    # since dupplication exists, it means that those duplicated answer can be generated via multiple ways
    # thus by making the principle, the duplication can be eliminated
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = [[]]
        for n in nums:
            newAns = []
            for a in ans:
                for i in range(len(a)+1):
                    newAns.append(a[:i]+[n]+a[i:])
                    if i < len(a) and n == a[i]: break
            ans = newAns
        return ans