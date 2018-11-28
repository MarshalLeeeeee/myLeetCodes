'''
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''
class Solution:
	# O(n)
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        hashmap = dict()
        maxLen = 0
        currLen = 0
        head = 0
        for i in range(l):
            try:
                if (hashmap[s[i]] < head):
                    currLen += 1
                else:
                    currLen = i - hashmap[s[i]]
                    head = hashmap[s[i]]
            except:
                currLen += 1
            maxLen = currLen if (currLen > maxLen) else maxLen
            hashmap[s[i]] = i
        return maxLen