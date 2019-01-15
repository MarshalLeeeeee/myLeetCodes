'''
224. Basic Calculator

Implement a basic calculator to evaluate a simple expression string.
The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:
Input: "1 + 1"
Output: 2

Example 2:
Input: " 2-1 + 2 "
Output: 3

Example 3:
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
'''

class Solution:
    def __init__(self):
        self.priority = {'+':1,'-':1,'*':2,'/':2, '(':0}
    
    def toSuffix(self,s):
        res, os = [],[]
        for x in s:
            if type(x) == int: res.append(x)
            elif x == ')': 
                while True:
                    o = os.pop()
                    if o != '(': res.append(o)
                    else: break
            elif x == '(': os.append(x)
            else: 
                while os:
                    if self.priority[os[-1]] < self.priority[x]: break
                    else: res.append(os.pop())
                os.append(x)
        while os: res.append(os.pop())
        return res

    def solve(self,s):
        ns = []
        for x in s:
            if type(x) == int: ns.append(x)
            else:
                a = ns.pop()
                b = ns.pop()
                if x == '+': ns.append(b+a)
                elif x == '-': ns.append(b-a)
                elif x == '*': ns.append(b*a)
                elif x == '/': ns.append(b//a)
        return ns[-1]
        
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ns,flag,num = [],0,0
        for i in range(len(s)):
            if s[i] == ' ': continue
            elif ord('0') <= ord(s[i]) and ord(s[i]) <= ord('9'):
                flag = 1
                num = num*10+ord(s[i])-ord('0')
            else: 
                if flag: ns.append(num); flag = 0; num = 0
                ns.append(s[i])
        if flag: ns.append(num)
        s = ns
        if s[0] == '-': s = [0] + s
        return self.solve(self.toSuffix(s))

if __name__ == '__main__':
    print(Solution().calculate("(1+(4+5+2)-3)+(6+8)"))