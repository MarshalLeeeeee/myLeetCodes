'''
65. Valid Number

Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. 
However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."

Of course, the context of these characters also matters in the input.
'''

class Solution:
    def isPureInteger(self, s):
        if not s: return False
        for sx in s:
            if not ('0' <= sx and sx <= '9'): return False
        return True
    
    def isInteger(self, s):
        if '-' in s:
            if s[0] != '-': return False
            else: return self.isPureInteger(s[1:])
        if '+' in s:
            if s[0] != '+': return False
            else: return self.isPureInteger(s[1:])
        return self.isPureInteger(s)
    
    def isPointNumber(self, s):
        if '-' in s:
            if s[0] != '-': return False
            else: s = s[1:]
        elif '+' in s:
            if s[0] != '+': return False
            else: s = s[1:]
        else: pass
        if '.' in s:
            sp = s.split('.')
            if len(sp) != 2  or (sp[0] == '' and sp[1] == ''): return False
            elif sp[0] == '': return self.isPureInteger(sp[1])
            elif sp[1] == '': return self.isPureInteger(sp[0])
            else: return self.isPureInteger(sp[0]) and self.isPureInteger(sp[1])
        return self.isPureInteger(s)
    
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sp = s.split()
        if len(sp) != 1: return False
        s = sp[0]
        if 'e' in s:
            sp = s.split('e')
            if len(sp) != 2 or (sp[0] == '' or sp[1] == ''): return False
            else: return self.isPointNumber(sp[0]) and self.isInteger(sp[1])
        return self.isPointNumber(s)

if __name__ == '__main__':
    print(Solution().isNumber('.1'))