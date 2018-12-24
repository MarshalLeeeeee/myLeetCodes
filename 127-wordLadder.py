'''
127. Word Ladder

Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

class Solution:
    # TLE if not using set
    def adword(self,wordset):
        st = []
        for word in wordset:
            for i in range(len(word)):
                for s in 'abcdefghijklmnopqrstuvwxyz':
                    if s != word[i]: 
                        st.append(word[:i]+s+word[i+1:])
        return set(st)
        
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList: return 0
        else:
            dep, queue, wordList = 1, set([beginWord]), set(wordList)
            while queue:
                if endWord in queue: return dep
                nq = wordList & self.adword(queue)
                wordList -= set(nq)
                queue = nq
                dep += 1
            return 0