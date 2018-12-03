'''
28. Implement strStr()

Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:
What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
'''

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        length = len(needle)
        for i in range(len(haystack)-length+1):
            if haystack[i:i+length] == needle:
                return i
        return -1

class Solution2:
    # try kmp
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        length = len(needle)
        kmp = [0]
        prefixTail = 0
        i = 1
        while i < length:
            if needle[i] == needle[prefixTail]:
                prefixTail += 1
                kmp.append(prefixTail)    
                i += 1
            else:
                if prefixTail == 0:
                    kmp.append(0)
                    i += 1
                else:
                    prefixTail -= prefixTail - kmp[prefixTail-1]
        print(kmp)
        prefixTail = 0
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[prefixTail]:
                prefixTail += 1
                if prefixTail == length:
                    return i-length+1
                i += 1
            else:
                if not prefixTail:
                    i += 1
                else:
                    prefixTail -= prefixTail - kmp[prefixTail-1]
        return -1

if __name__ == '__main__':
    print(Solution().strStr("ababcaababcaabc","ababcaabc"))