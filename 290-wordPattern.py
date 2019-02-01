'''
290. Word Pattern

Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:
Input: pattern = "abba", str = "dog cat cat dog"
Output: true

Example 2:
Input:pattern = "abba", str = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false

Example 4:
Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
'''

class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        if len(words) != len(pattern): return False
        dic1, dic2 = {}, {}
        for i in range(len(words)):
            if words[i] not in dic1 and pattern[i] not in dic2: dic1[words[i]] = pattern[i]; dic2[pattern[i]] = words[i]
            elif words[i] not in dic1 or pattern[i] not in dic2 or dic1[words[i]] != pattern[i] or dic2[pattern[i]] != words[i]: return False
        return True