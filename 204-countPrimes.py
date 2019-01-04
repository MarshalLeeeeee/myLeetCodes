'''
204. Count Primes

Count the number of prime numbers less than a non-negative number, n.

Example:
Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
'''

class Solution:
    # whenever meets a prime, mark its multiplicatios as False
    def init(self,n):
        res = []
        for i in range(n):
            if i % 2 == 0: res.append(0)
            else: res.append(1)
        return res
        
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 0
        res,ans = self.init(n), 1
        for i in range(3,n):
            if res[i]:
                ans += 1
                j = 3
                while i * j < n:
                    res[i*j] = 0
                    j += 2
        return ans

class Solution2:
    # optimization of Solution1
    # first is the initialization process, which is can easied as []*n
    #     the copy of non-base element will cause the consistent modification if one is modified
    # the marking mnultiple can be optimized by start at i*i with step as i
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2: return 0
        res = [1] * n
        res[0] = res[1] = 0
        for i in range(2,int(n ** 0.5)+1):
            if res[i]:
                res[i*i::i] = [0] * ((n-1-i*i)//i+1)
        return sum(res)
                    