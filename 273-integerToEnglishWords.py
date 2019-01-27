'''
273. Integer to English Words

Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:
Input: 123
Output: "One Hundred Twenty Three"

Example 2:
Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
'''

class Solution:
    def toHundred(self,num):
        lessThan20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", 
                      "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        res = ''
        a,b = num//100, num%100
        if a and b: 
            res += lessThan20[a]+' Hundred '
            if b < 20: res += lessThan20[b]
            else:
                c,d = b//10, b%10
                if d: res += tens[c]+' '+lessThan20[d]
                else: res += tens[c]
        elif a: res += lessThan20[a]+' Hundred'
        elif b: 
            if b < 20: res += lessThan20[b]
            else:
                c,d = b//10, b%10
                if d: res += tens[c]+' '+lessThan20[d]
                else: res += tens[c] 
        return res
    
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num: return 'Zero'
        adj, cnt, res = ['',' Thousand',' Million',' Billion',' Trillion'], 0, ''
        while num:
            n = num % 1000
            part = self.toHundred(n)
            if part: 
                if res: res = part + adj[cnt] + ' ' + res
                else: res = part + adj[cnt]
            cnt += 1
            num //= 1000
        return res