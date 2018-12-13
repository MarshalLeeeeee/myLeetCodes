'''
68. Text Justification

Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible. 
If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:
Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.

Example 3:
Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
'''

class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lens, head, curr, rowLen, rowCnt, ans, row = [len(w) for w in words], 0, 0, 0, 0, [], ''
        while curr < len(lens):
            #print(curr, rowLen, rowCnt)
            if rowLen + lens[curr] + rowCnt > maxWidth:
                space = maxWidth - rowLen
                spaceMin = space // (rowCnt - 1) if rowCnt > 1 else space
                spaceMaxNum = space - spaceMin * (rowCnt - 1) if rowCnt > 1 else 0
                for i in range(head,curr):
                    row += words[i]
                    if rowCnt > 1:
                        if i != curr - 1:
                            if spaceMaxNum > 0: 
                                row += ' ' * (spaceMin + 1)
                                spaceMaxNum -= 1
                            else:
                                row += ' ' * spaceMin
                    else: row += ' ' * spaceMin
                ans.append(row)
                row, head, rowLen, rowCnt = '', curr, 0, 0
            rowLen += lens[curr]
            rowCnt += 1
            curr += 1
        rowLen = 0
        for i in range(head,curr):
            row += words[i]
            rowLen += lens[i]
            if i != curr - 1:
                row += ' '
                rowLen += 1
        row += (maxWidth - rowLen) * ' '
        ans.append(row)
        return ans