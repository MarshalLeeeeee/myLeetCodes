'''
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
'''

class Solution:
    def maxThree(self,a,b,c):
        if a > b:
            return c if c > a else a
        else:
            return c if c > b else b
        
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        stack = []
        stackDict = defaultdict(int)
        currLen = 0
        maxLen = 0
        for x in s:
            if x == '(': 
                stack.append('(')
            else:
                if not len(stack):
                    stackDict.clear()
                    maxLen = maxLen if maxLen > currLen else currLen
                else:
                    stack.pop()
                    stackDict[len(stack)] += 2 + stackDict[len(stack)+1]
                    stackDict[len(stack)+1] = 0
                    currLen = currLen if currLen > stackDict[len(stack)] else stackDict[len(stack)]   
        maxLen = maxLen if maxLen > currLen else currLen
        return maxLen

if __name__ == '__main__':
    print(Solution().longestValidParentheses(")(((((()())()()))()(()))("))