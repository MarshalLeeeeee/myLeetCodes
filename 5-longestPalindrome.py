'''
5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
'''

class Solution:
    # O(n^2)
    # similar to approach 4
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if(l < 1):
            return ''
        maxLen = 1
        center = 0
        for i in range(l-1):
            s1 = s[i::-1]
            s2 = s[i:]
            s3 = s[i+1:]
            len12,len13=0,0
            for j in range(min(len(s1),len(s2))):
                if(s1[j] == s2[j]):
                    len12 = 2 * j + 1
                else:
                    break
            for j in range(min(len(s1),len(s3))):
                if(s1[j] == s3[j]):
                    len13 = 2 * (j+1)
                else:
                    break
            len123 = len12 if len12>len13 else len13
            if len123 > maxLen:
                center = i
                maxLen = len123
        if maxLen % 2 == 0:
            half = maxLen // 2
            return s[center-half+1:center+half+1]
        else:
            half = maxLen // 2
            return s[center-half:center+half+1]
            
if __name__ == '__main__':
    print(Solution().longestPalindrome('bb'))