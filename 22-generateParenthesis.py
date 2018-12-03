'''
22. Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''

class Solution:   
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if(n == 0):
        	return ['']
        ans = self.generateParenthesis(n-1)
        newAns = {}
        for a in ans:
        	for i in range(n):
        		s = a[:i] + '()' + a[i:]
        		newAns[s] = 1
        return list(newAns.keys())


if __name__ == '__main__':
	print(Solution().generateParenthesis(1))