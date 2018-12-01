class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for x in s:
            if(x == '('):
                stack.append(1)
            elif(x == '['):
                stack.append(2)
            elif(x == '{'):
                stack.append(3)
            elif(x == ')'):
                if len(stack) == 0 or stack[-1] != 1:
                    return False
                else:
                    stack.pop()
            elif(x == ']'):
                if len(stack) == 0 or stack[-1] != 2:
                    return False
                else:
                    stack.pop()
            elif(x == '}'):
                if len(stack) == 0 or stack[-1] != 3:
                    return False
                else:
                    stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False
        