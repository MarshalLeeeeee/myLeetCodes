class Solution:  
    def ifIn(self,nums,target):
        left = 0
        right = len(nums) - 1
        while(left <= right):
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return True
        return False

    def pairIterator(self,seq):
        l = len(seq)
        for i in range(l):
            for j in range(i+1,l):
                yield (seq[i],seq[j])
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        length = len(nums)
        if length < 3:
            return []
        if length == 3:
            return [nums] if nums[0]+nums[1]+nums[2] == 0 else []
        nums.sort()
        ans = []
        
        duplicate = {}
        positiveEven = {}
        negativeEven = {}
        Odd = {}
        i = 0
        while i < length:
            while(i < length - 1 and nums[i] == nums[i+1]):
                try:
                    duplicate[nums[i]] += 1
                except:
                    duplicate[nums[i]] = 2
                i += 1
            if nums[i] % 2 == 1:
                Odd[nums[i]] = 1
            elif nums[i] >= 0 and nums[i] % 2 == 0:
                positiveEven[nums[i]] = 1
            else:
                negativeEven[nums[i]] = 1
            i += 1
        for d in duplicate:
            if d != 0:
                if self.ifIn(nums,-2*d):
                    ans.append([d,d,-2*d])
            else:
                if duplicate[d] >= 3:
                    ans.append([0,0,0])
        OddList = list(Odd.keys())
        positiveEvenList = list(positiveEven.keys())
        negativeEvenList = list(negativeEven.keys())
        for x,y in self.pairIterator(positiveEvenList):
            try:
                negativeEven[-(x+y)]
                ans.append([x,y,-(x+y)])
            except:
                continue
        for x,y in self.pairIterator(negativeEvenList):
            try:
                positiveEven[-(x+y)]
                ans.append([x,y,-(x+y)])
            except:
                continue
        for x,y in self.pairIterator(OddList):
            if (x+y > 0):
                try:
                    negativeEven[-(x+y)]
                    ans.append([x,y,-(x+y)])
                except:
                    continue
            else:
                try:
                    positiveEven[-(x+y)]
                    ans.append([x,y,-(x+y)])
                except:
                    continue
        return ans
        
class Solution2:       
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if(len(nums) < 3):
            return []
        
        nums.sort()
        track = dict()
        distinguish = []
        for i,n in enumerate(nums):
            try:
                track[n].append(i)
            except:
                track[n] = [i]
                distinguish.append(n)
        
        ans = []
        for n in track:
            if n == 0 and len(track[n]) >= 3:
                ans.append([0,0,0])
            if n!= 0 and len(track[n]) >= 2:
                try:
                    track[-2*n]
                    ans.append([n,n,-2*n])
                except:
                    continue
            
        for i in range(len(distinguish)):
            for j in range(i+1, len(distinguish)):
                k = -(distinguish[i]+distinguish[j])
                if(k <= distinguish[j]):
                    continue
                try:
                    track[k]
                    ans.append([distinguish[i],distinguish[j],k])
                except:
                    continue
        
        return ans


class Solution3(object):
    # other one's strong solution
    def threeSum(self, nums):
        # Key: elements in nums
        # Val: number of occurrences
        # Can use defaultdict to make this shorter, but I don't want to use additional library
        lookup = dict()
        for num in nums:
            if not num in lookup:
                lookup[num] = 0
            lookup[num] += 1
        
        #Check 0, 0, 0 condition
        if 0 in lookup and lookup[0] > 2:
            res = [[0,0,0]]
        else:
            res = []
        
        #We will iterate by positive and then negative
        pos = [p for p in lookup if p > 0]
        neg = [n for n in lookup if n < 0]
        
        # check whether the missing value is in dictionary
        for p in pos:
            for n in neg:
                i = -p-n
                if i not in lookup:
                    continue
                # We now found possible correspondence in dictionary, but still little to compare
                # 1. the missing value is 0
                if i == 0 and lookup[i] > 0:
                    res.append([n, 0, p])
                # 2. the missing value is same as positive value, so the occurrences should be greater than 1
                elif i == p and lookup[i] > 1:
                    res.append([n, p, p])
                # 3. Same above
                elif i == n and lookup[i] > 1:
                    res.append([n, n, p])
                # 4. Deciding position in the answer
                elif i > p:
                    res.append([n, p, i])
                elif i < n:
                    res.append([i, n, p])
                
                # At here, we don't consider n < i < p, because we iterate through every possible pair in the for loops
                # So this situation (n < i < p)  will definitely be considered in other situation, in terms of i=p, p=i, or n=i, i=n
                # If you are still afraid, you can add the append code here and take set operation when returning answer


                    
        return res


if __name__ == '__main__':
    #print(Solution().threeSum([-6,-6,-4,-2,0,1,3,3,5,6,6]))
    #print(Solution2().threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]))
    print(Solution2().threeSum([-1,0,1,2,-1,-4]))