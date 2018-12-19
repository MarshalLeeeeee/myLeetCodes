'''
97. Interleaving String

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
'''

class Solution:
    def solve(self,s1,r1,s2,r2,s3,visited):
        if not s1: return True if s2 == s3 else False
        if not s2: return True if s1 == s3 else False
        if s3[0] == s1[0]:
            i = 0
            while i < len(s1):
                if s3[i] != s1[i]: break
                i += 1
            for j in range(i,0,-1):
                if not visited[r1+j][r2]:
                    visited[r1+j][r2] = 1
                    res = self.solve(s1[j:],j+r1,s2,r2,s3[j:],visited)
                    if res: return True
        if s3[0] == s2[0]:
            i = 0
            while i < len(s2):
                if s3[i] != s2[i]: break
                i += 1
            for j in range(i,0,-1):
                if not visited[r1][r2+j]:
                    visited[r1][r2+j] = 1
                    res = self.solve(s1,r1,s2[j:],j+r2,s3[j:],visited)
                    if res: return True
        return False
    
    def init(self,l1,l2):
        res = []
        for i in range(l1+1):
            res.append([])
            for j in range(l2+1):
                res[-1].append(0)
        return res
    
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if not s1: return True if s2 == s3 else False
        elif not s2: return True if s1 == s3 else False
        elif not s3: return False
        elif len(s1) + len(s2) != len(s3): return False
        else:
            visited = self.init(len(s1),len(s2))
            return self.solve(s1,0,s2,0,s3,visited)

if __name__ == '__main__':
    s1 = "cbcccbabbccbbcccbbbcabbbabcababbbbbbaccaccbabbaacbaabbbc"
    s2 = "abcbbcaababccacbaaaccbabaabbaaabcbababbcccbbabbbcbbb"
    s3 = "abcbcccbacbbbbccbcbcacacbbbbacabbbabbcacbcaabcbaaacbcbbbabbbaacacbbaaaabccbcbaabbbaaabbcccbcbabababbbcbbbcbb"
    s11 = "aacaac"
    s22 = "aacaaeaac"
    s33 = "aacaacaaeaacaac"
    s111 = "aabcc"
    s222 = "dbbca"
    s333 = "aadbcbbcac"
    print(Solution().isInterleave(s111,s222,s333))