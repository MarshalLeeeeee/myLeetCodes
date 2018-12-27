'''
140. Word Break II

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''

class Solution:
    # dfs with dp
    def solve(self,s,head,wordDict,visited,res,path):
        if head < len(s):
            for i,w in enumerate(wordDict):
                if s[head:head+len(w)] == w:
                    if (head,i) not in visited: 
                        visited |= set([(head,i)])
                        self.solve(s,head+len(w),wordDict,visited,res,path+[w])
                        for r in res[head+len(w)]:
                            res[head].append([w]+r)

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        visited = set([])
        res = []
        for i in range(len(s)+1):
            res.append([])
        res[-1] = [['']]
        self.solve(s,0,wordDict,visited,res,[])
        #print(res)
        ans = []
        for r in res[0]:
            ans.append(' '.join(r))
            ans[-1] = ans[-1][:-1]
        return ans