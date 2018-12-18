'''
91. Decode Ways

A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:
Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:
Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''

class Solution:
	# dp
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        else:
            if s[0] == '0': return 0
            cnt = [1,1]
            for i in range(1,len(s)):
                num = int(s[i-1:i+1])
                digit = int(s[i])
                if 10 <= num and num <= 26:
                    if digit:
                        cnt.append(cnt[-2]+cnt[-1])
                    else:
                        cnt.append(cnt[-2])
                else:
                    if digit:
                        cnt.append(cnt[-1])
                    else:
                        return 0
            return cnt[-1]
        