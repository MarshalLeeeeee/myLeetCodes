'''
126. Word Ladder II

Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:
Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: []
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

class Solution:
    # recursion dfs
    # time limit exceed
    def adjoin(self,w1,w2):
        diff = 0
        for i,s in enumerate(w1):
            if s != w2[i]: diff += 1
            if diff > 1: return False
        if diff != 1: return False
        else: return True
    
    def solve(self,beginWord, endWord, wordList, visited, res, shortest, path):
        print('  '*len(path),path)
        print('  '*len(path),res)
        print('  '*len(path),shortest)
        print('  '*len(path),'-'*10)
        if len(path) > shortest[0]: return 
        elif endWord == beginWord:
            if len(path) < shortest[0]:
                while res: res.pop()
            res.append(path)
            shortest[0] = len(path)
        else:
            for w in wordList:
                if self.adjoin(beginWord,w) and w not in visited:
                    visited[w] = 1
                    self.solve(w,endWord,wordList,visited,res,shortest,path+[w])
                    del visited[w]
    
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        res = []
        shortest = [float('inf')]
        visited = {beginWord:1}
        path = [beginWord]
        flag = False
        for w in wordList:
            if w == endWord: 
                flag = True
                break
        if flag:
            self.solve(beginWord,endWord,wordList,visited,res,shortest,path)
        return res

class Solution2:
    #iterative bfs
    def adjoin(self,w1,w2):
        diff = 0
        for i,s in enumerate(w1):
            if s != w2[i]: diff += 1
            if diff > 1: return False
        if diff != 1: return False
        else: return True
    
    def solve(self,beginWord,endWord,level,index):
        if index == len(level) - 1:
            if beginWord == endWord: return [[endWord]]
            else: return []
        else:
            ans = []
            for w in level[index+1]:
                if self.adjoin(beginWord,w):
                    res = self.solve(w,endWord,level,index+1)
                    for r in res:
                        ans.append([beginWord]+r)
            return ans
        
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        res = []
        shortest = [float('inf')]
        visited, record, path = {beginWord:1}, {beginWord:1}, [beginWord]
        flag = False
        for w in wordList:
            if w == endWord: flag = True
            record[w] = float('inf')
        if flag:
            level = [[beginWord]]
            while True:
                level.append([])
                for qw in level[-2]:
                    for w in wordList:
                        if w not in visited and self.adjoin(w,qw):
                            level[-1].append(w)
                            visited[w] = 1
                if level[-1] == [] or endWord in level[-1]: break
            if level[-1] == []: level.pop()
            print(level)
            return self.solve(beginWord,endWord,level,0)
        else: return []

class Solution3:
    # ac one
    def iter(self,word):
        for i in range(len(word)):
            for s in 'abcdefghijklmnopqrstuvwxyz':
                if s != word[i]: 
                    yield word[:i]+s+word[i+1:]
    
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord in wordList:
            level, wordList = {beginWord:[[beginWord]]}, set(wordList)
            while True:
                newlevel = {}
                for w in level:
                    for adword in self.iter(w):
                        if adword in wordList:
                            try: newlevel[adword] += [p+[adword] for p in level[w]]
                            except: newlevel[adword] = [p+[adword] for p in level[w]]
                wordList -= set(newlevel.keys())
                level = newlevel
                if endWord in level: return level[endWord]
                elif level == {}: return []
        else: return []

if __name__ == '__main__':
    print(Solution2().findLadders(beginWord,endWord,wordList))