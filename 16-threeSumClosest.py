class Solution:
    # merely pass :(
    # only beat 3.42%
    # O(n^2log(n))
    def find(self,nums,target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if(nums[mid] > target):
                right = mid - 1
            elif(nums[mid] < target):
                left = mid + 1
            else:
                return mid
        return left
    
    def judge(self,res,new,target):
        return res if abs(res-target) < abs(new-target) else new
        
    
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 1e20
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k = self.find(nums,target-nums[i]-nums[j])
                if k < j and j < len(nums) - 1:
                    res = self.judge(res,nums[i]+nums[j]+nums[j+1],target)
                if k == j and k < len(nums) - 1:
                    res = self.judge(res,nums[i]+nums[j]+nums[k+1],target)
                if k > j and k < len(nums):
                    res = self.judge(res,nums[i]+nums[j]+nums[k],target)
                if k-1 > j:
                    res = self.judge(res,nums[i]+nums[j]+nums[k-1],target)
                if res == target:
                    return res
        return res

class Solution2:
    # O(n^2)
    # beat 97.32%
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            j, k = i + 1, len(nums)-1
            if nums[i] + nums[k] + nums[k-1] < target:
                res.append(nums[i] + nums[k] + nums[k-1])
            elif nums[i] + nums[j] + nums[j+1] > target:
                res.append(nums[i] + nums[j] + nums[j+1])
            else:
                while j < k:
                    s = nums[i] + nums[j] + nums[k]
                    if s > target:
                        res.append(s)
                        k -= 1
                    elif s < target:
                        res.append(s)
                        j += 1
                    else:
                        return target
        
        res.sort(key = lambda x: abs(target-x))
        return res[0]

if __name__ == '__main__':
    print(Solution().threeSumClosest([13,34,8,91,0,-47,52,23,76,14,0,-9,22,49,-1,68,49,-83,-34,5,38,3,47,-2,-73,-29,19,-4,-3,-16,89,52,18,27,40,88,-84,-68,84,53,52,28,-86,-80,18,-93,11,77,11,-83,69,-29,-26,-83,32,65,-49,-88,-24,-56,95,-82,-25,-69,-27,20,-87,-49,78,89,100,26,45,-15,47,77,86,46,82,-80,-31,72,-82,-63,-50,35,-36,-30,-40,82,83,-61,-49,-11,88,73,-23,2,63,29,-82,95,-91,31,-35,-84,37,-86,-17,-84,-54,-89,32,13,-21,73,-73,53,-57,-60,62,-43,54,52,91,-7,23,-53,53,-82,-75,43,21,76,45,-2,-46,-39,-39,-3,24,6,-73,34,58,-67,35,45,-72,-67,-57,-22,-81,68,-84,-15,14,-87,14,-45,-68,4,-88,-25,-36,-74,-27,27,-23,26,-99,-47,97,32,53,82,-89,91,-1,-67,-74,-97,-36,7,-51,-100,-74,28,-12,-46,-37,87,80,-33,-58,51,5]
,-61))