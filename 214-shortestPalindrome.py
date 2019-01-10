class Solution:
    # manage all the valid to the current pointer
    # O(n^2) time
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return s
        offset,res = [1],0
        for i in range(1,len(s)):
            newoffset = []
            for d in offset:
                if s[i] == s[d-1]: 
                    if not d-1: res = i
                    else: newoffset.append(d-1)
            newoffset.append(i)
            newoffset.append(i+1)
            offset = newoffset
        return s[:res:-1]+s

class Solution2:
    # kmp solution
    def kmp(self,s):
        k = [0]
        for i in range(1,len(s)):
            ki = k[-1]
            while s[i] != s[ki]: 
                if ki == 0: ki = -1; break
                else: ki = k[ki-1]
            k.append(ki+1)
        return k
        
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return s
        sr, sri, srh, si = s[::-1], 0, 0, 0
        k = self.kmp(s)
        while sri < len(s):
            if sr[sri] == s[si]:
                sri += 1
                si += 1
            else:
                if si > 0:
                    offset = si - k[si-1]
                    srh += offset
                    si -= offset
                else: 
                    srh += 1
                    sri += 1
        return sr[:srh]+s

if __name__ == '__main__':
    print(Solution().shortestPalindrome("abcd"))