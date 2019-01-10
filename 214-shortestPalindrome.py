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

if __name__ == '__main__':
    print(Solution().shortestPalindrome("abcd"))