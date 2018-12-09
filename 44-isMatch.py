'''
44. Wildcard Matching

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:
Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:
Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:
Input:
s = "acdcb"
p = "a*c?b"
Output: false
'''

class Solution:
    # work in logic
    # but in some sample, the time exceeds limit
    def match(self,s,p,cnt):
        print(s,p,cnt)
        if s and not p:
            return False
        if not s and not p:
            return True
        if len(s) < cnt:
            return False
        if len(p) == 1:
            if p[0] == '*': return True
            elif p[0] == '?':
                if len(s) == 1: return True
                else: return False
            else:
                if p[0] == s[0] and len(s) == 1: return True
                else: return False
        left, right = 0, len(p)-1
        if p[left] == '*':
            if p[right] == '*':
                if len(p) == 3:
                    if p[left+1] == '?': return True
                    else: return p[left+1] in s
                else:
                    start = 0
                    while(start < len(s)-cnt):
                        res = self.match(s[start:],p[1:],cnt)
                        if res: return True
                        start+=1
                    return False
            elif p[right] == '?':
                return self.match(s[0:-1],p[0:-1],cnt-1)
            else:
                if s[-1]!=p[right]: return False
                else: return self.match(s[0:-1],p[0:-1],cnt-1)
        elif p[left] == '?':
            if p[right] == '*':
                return self.match(s[1:],p[1:],cnt-1)
            elif p[right] == '?':
                return self.match(s[1:-1],p[1:-1],cnt-2)
            else:
                if s[-1]!=p[right]: return False
                else: return self.match(s[1:-1],p[1:-1],cnt-2)
        else:
            if p[right] == '*':
                if s[0]!=p[left]: return False
                else: return self.match(s[1:],p[1:],cnt-1)
            elif p[right] == '?':
                if s[0]!=p[left]: return False
                else: return self.match(s[1:-1],p[1:-1],cnt-2)
            else:
                if s[0]!=p[left] or s[-1]!=p[right]: return False
                else: return self.match(s[1:-1],p[1:-1],cnt-2)
    
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s and not p:
            return False
        if not s and not p:
            return True
        si = 0
        newp, cntp = '', 0
        for pi, pc in enumerate(p):
            if pc == '*':
                if pi < len(p)-1:
                    if p[pi+1] == '*': continue
                    else: newp += '*'
                else: newp += '*'
            else: 
                newp += pc
                cntp += 1
        p = newp
        return self.match(s,p,cntp)

class Solution2:
    # kpm does not work because of the kpm array does not work for '?'
    def charMatch(self,s,c):
        if c == '?' or s == '?': return True
        else: return s == c       
    
    def strMatch(self,s,p):
        length = len(s)
        if len(p) != length: return False
        for i,sx in enumerate(s):
            if not self.charMatch(sx,p[i]): return False
        return True

    def subMatch(self,s,p,start,end):
        if not p: return 0
        elif not s: return -1
        else:
            curr = start
            pLen = len(p)
            while curr < end - pLen + 1:
                if self.strMatch(p,s[curr:curr+pLen]): return curr
                else: curr += 1
            return -1
        
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if s and not p:
            return False
        if not s and not p:
            return True
        newp = ''
        for pi, pc in enumerate(p):
            if pc == '*':
                if pi < len(p)-1:
                    if p[pi+1] == '*': continue
                    else: newp += '*'
                else: newp += '*'
            else: 
                newp += pc
        p, start = newp, 0
        psplit = p.split('*')
        splitNum = len(psplit)
        if splitNum == 1:
            return self.strMatch(psplit[0],s)
        else:
            for i,x in enumerate(psplit):
                if i == 0:
                    head = self.subMatch(s,x,start,len(s))
                    if head != 0: return False
                    else: start = head + len(x)
                elif i < splitNum - 1:
                    head = self.subMatch(s,x,start,len(s))
                    if head == -1: return False
                    else: start = head + len(x)
                else:
                    head = self.subMatch(s[::-1],x[::-1],0,len(s)-start)
                    if head != 0: return False
                    else: return True


if __name__ == '__main__':
    #print(Solution().isMatch("babbbbaabababaabbababaababaabbaabababbaaababbababaaaaaabbabaaaabababbabbababbbaaaababbbabbbbbbbbbbaabbb","b**bb**a**bba*b**a*bbb**aba***babbb*aa****aabb*bbb***a"))
    '''
    print(Solution2().isMatch( \
        "abbabaa \
        abba \
        bba \
        ababb \
        abbbbbabbbabbbabaa \
        aaab \
        a \
        bababbbabababaabbababaabbbbbbaaaabababbbaabbbbaabbbbababababbaabbaababaabbbababababbbbaaabbbbbabaaaabbababbbbaababaabbababbbbbababbbabaaaaa \
        a \
        aabbbbba \
        abaaababaaaabb"
        ,"**aa*****ba*a*bb**aa*ab****a*aaaaaa***a*aaaa**bbabb*b*b**aaaaaaaaa*a********ba*bbb***a*ba*bb*bb**a*b*bb"))
    '''
    print(Solution2().isMatch("mississippi","m??*ss*?i*pi"))