'''
301. Remove Invalid Parentheses

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
Note: The input string may contain letters other than the parentheses ( and ).

Example 1:
Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:
Input: ")("
Output: [""]
'''

class Solution:
    def removeInvalidParentheses(self, s: 'str') -> 'List[str]':
        if not s: return ['']
        else:
            sums, cnt, left = 0, 0, 0
            nums, pos = [], []
            suffix, remain = set(['']), set([''])
            for i in range(len(s)):
                if not sums:
                    if nums:
                        suffixNew = set([])
                        for r in suffix:
                            suffixNew.add(r + s[left:i])
                        suffix = suffixNew if suffixNew else set([''])
                        remain, nums, pos = set(['']), [], []
                    left = i
                    if s[i] == '(':
                        cnt += 1
                        sums += 1
                    elif s[i] == ')':
                        suffixNew = suffix.copy()
                        for r in suffix:
                            for j in range(len(r)):
                                if r[j] == ')':
                                    nr = r[:j]+r[j+1:]+')'
                                    suffixNew.add(nr)
                        suffix = suffixNew
                    else:
                        suffixNew = set([])
                        for r in suffix:
                            suffixNew.add(r + s[i])
                        suffix = suffixNew if suffixNew else set([''])
                else:
                    if s[i] == '(':
                        cnt += 1
                        sums += 1
                    elif s[i] == ')':
                        nums.append(cnt)
                        pos.append(i)
                        remainNew = set([])
                        for r in remain:
                            rs = (r+' '+str(cnt)).split()
                            for ci in range(len(rs)):
                                if int(rs[ci]) > 0:
                                    rs[ci] = str(int(rs[ci])-1)
                                    nr = ' '.join(rs)
                                    remainNew.add(nr)
                                    rs[ci] = str(int(rs[ci])+1)
                        remain = remainNew
                        sums -= 1
                        cnt = 0
                    else:
                        nums.append(cnt)
                        pos.append(i)
                        remainNew = set([])
                        for r in remain:
                            remainNew.add(r+' '+str(cnt))
                        remain = remainNew
                        cnt = 0
            if remain:
                res = set([])
                for r in remain:
                    rs = r.split()
                    nr = ''
                    for ci in range(len(rs)):
                        nr += '('*(nums[ci]-int(rs[ci]))+s[pos[ci]]
                    for suf in suffix:
                        res.add(suf+nr)
                return list(res)
            else: return list(suffix)

if __name__ == '__main__':
    print(Solution().removeInvalidParentheses('(a)c(b))(d)'))
    print(Solution().removeInvalidParentheses('(a)())()'))
    print(Solution().removeInvalidParentheses(')('))
    print(Solution().removeInvalidParentheses('n'))
    print(Solution().removeInvalidParentheses(')(f'))
    print(Solution().removeInvalidParentheses(')d))'))
    print(Solution().removeInvalidParentheses('p(r)'))
    print(Solution().removeInvalidParentheses('(0y'))