'''
208. Implement Trie (Prefix Tree)

Implement a trie with insert, search, and startsWith methods.

Example:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");   
trie.search("app");     // returns true

Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''

#############################################################################################
################################## Solution 1 ###############################################

class LetterNode:
    def __init__(self):
        self.child = {'a':None,'b':None,'c':None,'d':None,'e':None,'f':None,
                      'g':None,'h':None,'i':None,'j':None,'k':None,'l':None,
                      'm':None,'n':None,'o':None,'p':None,'q':None,'r':None,
                      's':None,'t':None,'u':None,'v':None,'w':None,'x':None,
                      'y':None,'z':None, '':None}

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = LetterNode()
        
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        curr = self.root
        for x in word:
            if not curr.child[x]: curr.child[x] = LetterNode()
            curr = curr.child[x]
        curr.child[''] = LetterNode()
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for x in word:
            if not curr.child[x]: return False
            curr = curr.child[x]
        return True if curr.child[''] else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for x in prefix:
            if not curr.child[x]: return False
            curr = curr.child[x]
        return True


        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)