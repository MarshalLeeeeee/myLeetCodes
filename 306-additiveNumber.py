'''
306. Additive Number

Additive number is a string whose digits can form additive sequence.
A valid additive sequence should contain at least three numbers. 
Except for the first two numbers, each subsequent number in the sequence must be the sum of the preceding two.
Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3 is invalid.

Example 1:
Input: "112358"
Output: true 
Explanation: The digits can form an additive sequence: 1, 1, 2, 3, 5, 8. 
             1 + 1 = 2, 1 + 2 = 3, 2 + 3 = 5, 3 + 5 = 8

Example 2:
Input: "199100199"
Output: true 
Explanation: The additive sequence is: 1, 99, 100, 199. 
             1 + 99 = 100, 99 + 100 = 199

Follow up:
How would you handle overflow for very large input integers?
'''

class Solution:
    def exam(self,i,j,num):
        if num[i] == '0' and (j != i + 1): return -1
        else: return int(num[i:j])
    
    def judge(self,i,j,k,num):
        a = self.exam(i,j,num)
        b = self.exam(j,k,num)
        if a == -1: return -2
        if b == -1: return -3
        l = max(j-i, k-j)
        if self.exam(k,k+l,num) == a+b: return k+l
        elif self.exam(k,k+l+1,num) == a+b: return k+l+1
        else: return -1
    
    def isAdditiveNumber(self, num: 'str') -> 'bool':
        length, flagA, flagB = len(num), False, False
        for i in range(1,length):
            for j in range(i+1,length):
                a,b,c = 0,i,j
                while True:
                    print(a,b,c)
                    index = self.judge(a,b,c,num)
                    if index == length: return True
                    elif index == -2: flagA = True; break
                    elif index == -3: flagB = True; break
                    elif index == -1: break
                    else: a,b,c = b,c,index
                if flagB: flagB = False; break
            if flagA: flagA = False; break
        return False

if __name__ == '__main__':
    print(Solution().isAdditiveNumber("199100199"))