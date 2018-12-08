'''
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution:
    def add(self, num1, num2, num3, num4):
        start, add, ans = 0, 0, ''
        while(True):
            x1,f1 = (int(num1[start]),True) if start < len(num1) else (0,False)
            x2,f2 = (int(num2[start]),True) if start < len(num2) else (0,False)
            x3,f3 = (int(num3[start]),True) if start < len(num3) else (0,False)
            x4,f4 = (int(num4[start]),True) if start < len(num4) else (0,False)
            if not f1 and not f2 and not f3 and not f4:
                if add: ans += str(add)
                return ans[::-1]
            else:
                x = x1+x2+x3+x4+add
                ans += str(x % 10)
                add = x // 10
                start += 1           
        
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1, len2 = len(num1), len(num2)
        if len2 < len1:
            len1, len2 = len2, len1
            num1, num2 = num2, num1
        if len1 == 1:
            ans, n, add = '', int(num1[0]), 0
            if not n: return '0'
            for s in num2[::-1]:
                x = int(s) * n + add
                ans += str(x % 10)
                add = x // 10
            if add: ans += str(add)
            return ans[::-1]
        else:
            numHead1, numHead2 = num1[:len1//2], num2[:len2//2]
            numTail1, numTail2 = num1[len1//2:], num2[len2//2:]
            mult1 = self.multiply(numHead1,numHead2) + '0' * (len(numTail1)+len(numTail2))
            mult2 = self.multiply(numHead1,numTail2) + '0' * len(numTail1)
            mult3 = self.multiply(numTail1,numHead2) + '0' * len(numTail2)
            mult4 = self.multiply(numTail1,numTail2)
            ans = self.add(mult1[::-1],mult2[::-1],mult3[::-1],mult4[::-1])
            return ans
            
if __name__ == '__main__':
    #print(Solution().multiply("123","456"))
    print(Solution().multiply("999","999"))