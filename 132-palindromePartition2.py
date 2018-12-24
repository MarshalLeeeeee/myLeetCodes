'''
132. Palindrome Partitioning II

Given a string s, partition s such that every substring of the partition is a palindrome.
Return the minimum cuts needed for a palindrome partitioning of s.

Example:
Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''

class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        else:
            tailPalin, cut = [0], [-1]
            for i,x in enumerate(s):
                newTailPalin = []
                cut.append(cut[-1]+1)
                for head in tailPalin:
                    if head and x == s[head-1]: 
                        newTailPalin.append(head-1)
                        cut[-1] = min(cut[-1],cut[head-1]+1)
                    elif not head: 
                        if i: cut[-1] = min(cut[-1],1)
                        else: cut[-1] = 0
                newTailPalin.append(i) # new character itself is a palindrome
                newTailPalin.append(i+1) # the empty string is a palindrome
                tailPalin = newTailPalin
            return cut[-1]