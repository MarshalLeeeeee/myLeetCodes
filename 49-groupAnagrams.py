'''
49. Group Anagrams

Given an array of strings, group anagrams together.

Example:
Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
'''

class Solution:
    # merely below the time limits
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dicts = []
        ans = []
        for word in strs:
            letterDict = {}
            for w in word:
                try:
                    letterDict[w] += 1
                except:
                    letterDict[w] = 1
            if letterDict in dicts:
                for i,d in enumerate(dicts):
                    if d == letterDict:
                        ans[i].append(word)
            else:
                dicts.append(letterDict)
                ans.append([word])
        return ans

class Solution2:
    # solve using sorting
    # much faster than solution1
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dicts = {}
        for word in strs:
            wordSort = ''.join(sorted(word))
            if wordSort in dicts:
                dicts[wordSort].append(word)
            else:
                dicts[wordSort] = [word]
        return list(dicts.values())

if __name__ == '__main__':
    print(Solution().groupAnagrams(strs))