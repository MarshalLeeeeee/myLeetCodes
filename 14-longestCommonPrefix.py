'''
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""

Explanation: There is no common prefix among the input strings.
Note: All given inputs are in lowercase letters a-z.
''' 

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        index = 0
        strNum = len(strs)
        if strNum == 0:
            return ''
        if strNum == 1:
            return strs[0]
        while(True):
            try:
                for i in range(strNum):
                    if(strs[i][index] != strs[0][index]):
                        return strs[0][:index]
                index += 1
            except:
                return strs[0][:index]

if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["flower","flow","flight"]))