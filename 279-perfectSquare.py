'''
279. Perfect Squares

Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

class Solution:
    # dictionary version
    # recursion takes time
    def dfs(self,n,d):
        if n in d: return d[n]
        i = 1
        while i*i < n:
            self.dfs(n-i*i,d)
            if n in d: d[n] = min(d[n],d[n-i*i]+1)
            else: d[n] = d[n-i*i]+1
            i += 1
        return d[n]
        
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        d, i = {}, 1
        while i*i < n:
            d[i*i] = 1
            i += 1
        if i*i == n: return 1        
        self.dfs(n,d)
        print(len(d))
        return d[n]

class Solution2:
    # calculate every number before 'n'
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """                
        sol = {1:1,2:2,3:3}
        sqs = [1]
        for i in range(4,n+1):
            if int(i ** (1/2)) ** 2 == i:
                sol[i] = 1
                sqs.append(i)
            else:
                sol[i] = float('inf')
                for sq in sqs:
                    sol[i] = min(sol[i],sol[sq]+sol[i-sq])
        return sol[n]



if __name__ == '__main__':
    print(Solution().numSquares(356))