'''
211. Add and Search Word - Data structure design

Design a data structure that supports the following two operations:
void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.
'''

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        
    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for x in word:
            if x not in curr: curr[x] = {}
            curr = curr[x]
        if '' not in curr: curr[''] = {}
            
    def __dfs__(self,curr,word):
        if not word: return True if '' in curr else False
        if word[0] == '.':
            for k in curr:
                if self.__dfs__(curr[k],word[1:]): return True
            return False
        else:
            if word[0] not in curr: return False
            else: return self.__dfs__(curr[word[0]],word[1:])

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.__dfs__(self.root,word)
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)