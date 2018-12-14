'''
72. Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.
You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')
'''

class Solution:       
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1, len2 = len(word1), len(word2)
        if not len1 and not len2: return 0
        elif not len1 and len2: return len2
        elif len1 and not len2: return len1
        else:
            dn = []
            for i in range(len1+1):
                dn.append([])
                for j in range(len2+1):
                    if i == 0: dn[-1].append(j)
                    elif j == 0: dn[-1].append(i)
                    else:
                        if word1[i-1] == word2[j-1]:
                            dn[-1].append(min(dn[i-1][j]+1, dn[i][j-1]+1, dn[i-1][j-1]))
                        else:
                            dn[-1].append(min(dn[i-1][j]+1, dn[i][j-1]+1, dn[i-1][j-1]+1))
            return dn[-1][-1]