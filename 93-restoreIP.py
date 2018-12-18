'''
93. Restore IP Addresses

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''

class Solution:
    def judge(self, s):
        num = int(s)
        if len(s) > 1 and s[0] == '0': return False
        elif 0 <= num and num <= 255: return True
        else: return False
        
    def solve(self,s,n):
        if not s: return []
        l = len(s)
        if l > 3*n or l < n: return []
        else:
            if n > 1:
                ans = []
                if self.judge(s[-1:]):
                    res = self.solve(s[:-1],n-1)
                    for r in res:
                        ans.append(r+'.'+s[-1:])
                if self.judge(s[-2:]):
                    res = self.solve(s[:-2],n-1)
                    for r in res:
                        ans.append(r+'.'+s[-2:])
                if self.judge(s[-3:]):
                    res = self.solve(s[:-3],n-1)
                    for r in res:
                        ans.append(r+'.'+s[-3:])
                return ans
            else:
                if self.judge(s): return [s]
                else: return []
        
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return self.solve(s,4)

if __name__ == '__main__':
    print(Solution().restoreIpAddresses("9999999"))