'''
87. Scramble String

Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:
Input: s1 = "great", s2 = "rgeat"
Output: true

Example 2:
Input: s1 = "abcde", s2 = "caebd"
Output: false
'''

class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s1 and not s2: return True
        len1, len2 = len(s1), len(s2)
        if len1 != len2: return False
        if len1 == 1: return True if s1[0] == s2[0] else False
        left, right, index = 0, len1-1, 0
        leftDic, rightDic, s1HeadDic = {}, {}, {}
        for i in range(len1-1):
            try: s1HeadDic[s1[i]] += 1
            except: s1HeadDic[s1[i]] = 1
            
            try: leftDic[s2[left]] += 1
            except: leftDic[s2[left]] = 1
            
            try: rightDic[s2[right]] += 1
            except: rightDic[s2[right]] = 1

            if leftDic == s1HeadDic:
                res1 = self.isScramble(s1[:i+1],s2[:left+1])
                res2 = self.isScramble(s1[i+1:],s2[left+1:])
                if res1 and res2: return True
            
            if rightDic == s1HeadDic:
                res3 = self.isScramble(s1[:i+1],s2[right:])
                res4 = self.isScramble(s1[i+1:],s2[:right])
                if res3 and res4: return True
                
            left += 1
            right -= 1
        return False

if __name__ == '__main__':
    print(Solution().isScramble("abcde","caebd"))