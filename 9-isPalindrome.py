'''
9. Palindrome Number
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?
'''

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        sr = s[::-1]
        if(s == sr):
            return True
        else:
            return False

class Solution2:
    # not coverting to str
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0):
            return False
        digits = []
        while(x):
            digits.append(x%10)
            x //= 10
        l = len(digits)
        for i in range((l+1) // 2):
            if digits[i] != digits[l-i-1]:
                return False
        return True

if __name__ == '__main__':
    print(Solution().isPalindrome(121))