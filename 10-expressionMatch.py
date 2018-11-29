'''
10. Regular Expression Matching

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:
Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:
Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:
Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:
Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".

Example 5:
Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def windowMatch(s,window):
            if window == []:
                return True if (s == '') else False
            if '.' in window:
                return True
            shead = 0
            slen = len(s)
            for token in window:
                while(shead < slen and s[shead] == token):
                    shead += 1
            return True if (shead == slen) else False
        
        def targetMatch(c,target):
            if(target == '.'):
                return True
            else:
                return True if (target == c) else False
            
        def Match(s,p):
            shead = 0
            phead = 0
            slen = len(s)
            plen = len(p)
            window = []
            while phead < plen:
                if phead < plen - 1:
                    if p[phead+1] == '*':
                        window.append(p[phead])
                        phead += 2
                    else:
                        target = p[phead]
                        while shead < slen:
                            if targetMatch(s[shead],target):
                                if not windowMatch(s[:shead],window):
                                    return False
                                if Match(s[shead+1:],p[phead+1:]):
                                    return True
                                shead += 1
                            else:
                                shead += 1
                        return False
                else:
                    target = p[phead]
                    while shead < slen:
                        if targetMatch(s[shead],target):
                            if not windowMatch(s[:shead],window):
                                return False
                            if Match(s[shead+1:],p[phead+1:]):
                                return True
                            shead += 1
                        else:
                            shead += 1
                    return False
            return windowMatch(s[shead:],window)
        
        return Match(s,p)  


if __name__ == '__main__':
    print(Solution().isMatch('aa','a*'))
    print(Solution().isMatch('ab','.*'))
    print(Solution().isMatch('aab','c*a*b'))
    print(Solution().isMatch('mississippi','mis*is*p*.'))
    print(Solution().isMatch('abbabb','c*.*abbb*'))