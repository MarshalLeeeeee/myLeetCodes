'''
187. Repeated DNA Sequences

All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". 
When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.
Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]
'''

class Solution:
    # constant length makes it O(n) time and O(n) space
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dic, res = set([]), set([])
        for i in range(len(s)-9):
            if s[i:i+10] not in dic: dic |= set([s[i:i+10]])
            else: res |= set([s[i:i+10]])
        return list(res)