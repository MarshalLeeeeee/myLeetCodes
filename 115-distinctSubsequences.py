'''
115. Distinct Subsequences

Given a string S and a string T, count the number of distinct subsequences of S which equals T.
A subsequence of a string 
    is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:
Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

Example 2:
Input: S = "babgbag", T = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
'''

class Solution:
    # work but exceed time limit
    # O(n*n*m)
    # consider s = 'aaaaaaaaaaaaaaaaaaaaaaaaab', t = 'ab'
    def solve(self,s,t):
        if not t: return 1
        elif len(s) < len(t): return 0
        else: 
            cnt = 0
            for i,n in enumerate(s):
                if n == t[0]:
                    cnt += self.solve(s[i+1:],t[1:])
            return cnt
            
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not s and not t: return 1
        else: return self.solve(s,t)

class Solution2:
    # dp solution
    # O(n*m)
    def init(self,lent,lens):
        res = []
        for i in range(lent):
            res.append([])
            for j in range(lens):
                if not i: res[-1].append(1)
                else: res[-1].append(0)
        return res

    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not t: return 1
        elif len(s) < len(t): return 0
        else: 
            ways = self.init(len(t)+1,len(s)+1)
            for i in range(1,len(t)+1):
                for j in range(i,len(s)+1):
                    if t[i-1] == s[j-1]:
                        ways[i][j] = ways[i][j-1] + ways[i-1][j-1] # the case of deleting s[j-1] + the case of keeping s[j-1]
                    else:
                        ways[i][j] = ways[i][j-1] # only the case of deleting s[j-1]
            return ways[-1][-1]

if __name__ == '__main__':
    s = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
    t = "bddabdcae"
    print(Solution().numDistinct(s,t))
            