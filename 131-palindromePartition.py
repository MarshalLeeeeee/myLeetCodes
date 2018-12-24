'''
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome.
Return all possible palindrome partitioning of s.

Example:
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
'''

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        if not s: return []
        else:
            res = [[]]
            for i,x in enumerate(s):
                ans = []
                for r in res:
                    ans.append(r+[x])
                    if len(r) >= 1 and r[-1] == x: ans.append(r[:-1]+[r[-1]+x])
                    if len(r) >= 2 and r[-2] == x: ans.append(r[:-2]+[r[-2]+r[-1]+x])
                res = ans
            return res