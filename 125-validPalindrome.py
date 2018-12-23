'''
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
'''

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: return True
        else:
            s = s.lower()
            sn = []
            for x in s:
                if  ('a' <= x and x <= 'z') or ('0' <= x and x <= '9'): sn.append(x)    
            head, tail, ans = 0, len(sn)-1, True
            while head <= tail:
                if sn[head] != sn[tail]: return False
                head += 1
                tail -= 1
            return True