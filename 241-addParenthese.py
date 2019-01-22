'''
241. Different Ways to Add Parentheses

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. 
The valid operators are +, - and *.

Example 1:
Input: "2-1-1"
Output: [0, 2]
Explanation: 
((2-1)-1) = 0 
(2-(1-1)) = 2

Example 2:
Input: "2*3-4*5"
Output: [-34, -14, -10, -10, 10]
Explanation: 
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
'''

class Solution:
    def calc(self,a,o,b):
        if o == '+': return a+b
        elif o == '-': return a-b
        elif o == '*': return a*b
        
    def init(self,length):
        res = []
        for i in range(length):
            res.append([])
            for j in range(length):
                res[-1].append([])
        return res
        
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        form,num = [],0
        for x in input:
            if ord('0') <= ord(x) and ord(x) <= ord('9'):
                num = 10*num+ord(x)-ord('0')
            else:
                form.append(num)
                form.append(x)
                num = 0
        form.append(num)
        res = self.init(len(form)//2+1)
        for gap in range(len(form)//2+1):
            for x in range(len(form)//2+1-gap):
                if gap == 0: res[x][x+gap].append(form[x*2])
                else:
                    for i in range(gap):
                        op = form[(x+i)*2+1]
                        for r1 in res[x][x+i]:
                            for r2 in res[x+i+1][x+gap]:
                                res[x][x+gap].append(self.calc(r1,op,r2))
        return res[0][-1]
        