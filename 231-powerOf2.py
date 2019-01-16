'''
231. Power of Two

Given an integer, write a function to determine if it is a power of two.

Example 1:
Input: 1
Output: true 
Explanation: 20 = 1

Example 2:
Input: 16
Output: true
Explanation: 24 = 16

Example 3:
Input: 218
Output: false
'''

class Solution:  
    # bit solution             
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if not n: return False
        m = -n
        return m&n == n

class Solution2:
    # naive solution
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set([1,2,4,8,16,32,64,128,256,512,1024,2048,4096])
        if n <= 4096: return n in s
        else:
            while n > 4096:
                if n % 4096: return False
                n //= 4096
            return n in s        
