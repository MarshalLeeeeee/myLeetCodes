class Solution:
    # calulate every possible result for every substring
    # First, calculate all possible result using operation Combine / Multiply, because their priority is the highest in the calculation
    # Then calculate all possible result using operation Add / Minus
    # logically feasible, but ETL
    def init(self,num):
        from collections import defaultdict
        res, length = [], len(num)
        for i in range(length):
            res.append([])
            for j in range(length):
                res[i].append(defaultdict(list))
                if j >= i and (num[i] != '0' or num[i:j+1] == '0'): res[i][j][int(num[i:j+1])].append(num[i:j+1])
        return res

    def show(self,res):
        length = len(res)
        for i in range(length):
            for j in range(length):
                print('i: %d, j: %d' % (i,j),res[i][j])
        
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num: return []
        res1, length = self.init(num), len(num)
        # multiply
        for k in range(1,length):
            for i in range(length-k):
                for j in range(k):
                    for a in res1[i][i+j]:
                        for b in res1[i+j+1][i+k]:
                            new = a*b
                            for ae in res1[i][i+j][a]:
                                for be in res1[i+j+1][i+k][b]: 
                                    if ae+'*'+be not in res1[i][i+k][new]: res1[i][i+k][new].append(ae+'*'+be)
        # minus and add
        res2 = res1.copy()
        for k in range(1,length):
            for i in range(length-k):
                for j in range(k):
                    for a in res2[i][i+j]:
                        for b in res1[i+j+1][i+k]:
                            add, sub = a+b, a-b
                            for ae in res2[i][i+j][a]:
                                for be in res1[i+j+1][i+k][b]:
                                    if ae+'+'+be not in res2[i][i+k][add]: res2[i][i+k][add].append(ae+'+'+be)
                                    if ae+'-'+be not in res2[i][i+k][sub]: res2[i][i+k][sub].append(ae+'-'+be)
        
        self.show(res2)
        return res2[0][-1][target] if target in res2[0][-1] else []


class Solution2:
    # optimization of Solution1
    # First, calculate all possible result using operation Combine / Multiply, because their priority is the highest in the calculation.
    # Then calculate using operation Add / Minus using recursion.
    # Notice that we actually dont have to calculate all possible answers, but if answer == 'target'.
    # Thus, we start from tail (because it is the last step in the calculation in the recursion) with the previous result of 'target-num' and 'target+num'
    def highPriority(self,num):
        from collections import defaultdict
        res, length = [], len(num)
        for i in range(length):
            res.append([])
            for j in range(length):
                res[i].append(defaultdict(list))
                if j >= i and (num[i] != '0' or num[i:j+1] == '0'): res[i][j][int(num[i:j+1])].append(num[i:j+1])
        for k in range(1,length):
            for i in range(length-k):
                for j in range(k):
                    for a in res[i][i+j]:
                        for b in res[i+j+1][i+k]:
                            new = a*b
                            for ae in res[i][i+j][a]:
                                for be in res[i+j+1][i+k][b]: 
                                    if ae+'*'+be not in res[i][i+k][new]: res[i][i+k][new].append(ae+'*'+be)
        return res
    
    def lowPriority(self,res,num,target):
        if not num:
            if not target: return ['']
            else: return []
        length = len(num)
        ans = []
        for i in range(length-1,-1,-1):
            for k in res[i][length-1]:
                for e in res[i][length-1][k]:
                    for r in self.lowPriority(res,num[:i],target-k):
                        if r: ans.append(r+'+'+e)
                        else: ans.append(e)
                    for r in self.lowPriority(res,num[:i],target+k):
                        if r: ans.append(r+'-'+e)
        return ans
        
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num: return []
        length = len(num)
        res = self.highPriority(num)
        return self.lowPriority(res,num,target)

if __name__ == '__main__':
    print(Solution().addOperators("3456237490",9191))