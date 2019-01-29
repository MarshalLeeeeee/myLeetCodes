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

class Solution3: 
    # bfs solution       
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        visited = set([n])
        q, depth = [n], 1
        while q:
            nq = []
            while q:
                x = q.pop(0)
                sqt = int(x ** (1/2))
                if sqt ** 2 == x: return depth
                for i in range(1,sqt+1):
                    if x - i*i not in visited:
                        visited.add(x-i*i)
                        nq.append(x-i*i)
            q = nq
            depth += 1

class Solution4: 
    # math solution
    # The idea is to use basic square-root check for 1, 
    # Then, Lagrange's 4 squares theorem for 4 (which is also the maximum, since theorem states every integer can be represented by sum of 4 squares). 
    # This only leaves case 2 and 3. 
    # To check case 2, all we need is to iterate through to sqrt of n, and check if the difference between n and square of i is also a square. 
    # If this fails, then we know it must be 3.
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # determine if n itself is a square
        if int(n ** (1/2)) ** 2 == n: return 1
        # the first step is to keep dividing 4, because the solution of 'n' is the same with '4n' by simply doubling every base number
        while n % 4 == 0: n /= 4
        # Legendre's three-square theorem
        if n % 8 == 7: return 4
        # determine case 2
        x = int(n ** (1/2))
        for i in range(1,x+1):
            m = n - i*i
            if int(m ** (1/2)) ** 2 == m: return 2
        # only case 3 is left
        return 3

if __name__ == '__main__':
    print(Solution().numSquares(356))