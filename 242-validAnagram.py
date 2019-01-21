'''
242. Valid Anagram

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): return False
        dicS, dicT = {}, {}
        for i in range(len(s)):
            if s[i] not in dicS: dicS[s[i]] = 1
            else: dicS[s[i]] += 1
            if t[i] not in dicT: dicT[t[i]] = 1
            else: dicT[t[i]] += 1
        return dicS == dicT
        