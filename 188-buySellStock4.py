'''
188. Best Time to Buy and Sell Stock IV

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most k transactions.

Note:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

Example 1:
Input: [2,4,1], k = 2
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Example 2:
Input: [3,2,6,5,0,3], k = 2
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4.
             Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
'''

class Solution:
    # dp 
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if not prices or not k: return 0
        state,np,res,minStep,minP = 1,[],[],[],float('inf')
        for i in range(len(prices)-1):
            if (state and prices[i] < prices[i+1]) or (not state and prices[i] > prices[i+1]): 
                np.append(prices[i])
                if state: 
                    minP = min(minP,np[-1])
                    if np[-1] == minP: minStep.append(-1)
                    else: 
                        j = len(np)-3
                        while j >= 0:
                            if np[-1] > np[j]: minStep.append(j//2);break
                            j -= 2
                else: res.append(max(res[-1],np[-1]-minP) if res else np[-1]-minP)
                state = 1-state
        if not state:
            np.append(prices[-1])
            res.append(max(res[-1],np[-1]-minP) if res else np[-1]-minP)
        prices = np
        l = len(prices)
        if l <= 1: return 0
        else:
            if len(res) <= k:
                ans = 0
                for i in range(len(res)):
                    ans += prices[2*i+1] - prices[2*i]
                return ans
            else:
                while k > 1:
                    i, newRes = 1, [res[0]]
                    while i < len(res):
                        j, maxRes = i, float('-inf')
                        while True:
                            maxRes = max(maxRes,res[j-1]+prices[2*i+1]-prices[2*j] if j > 0 else prices[2*i+1]-prices[2*j])
                            if minStep[j] == -1: break
                            else: j = minStep[j]
                        newRes.append(max(newRes[-1],maxRes))
                        i += 1
                    k -= 1
                    res = newRes
                return res[-1]

if __name__ == '__main__':
    print(Solution().maxProfit(2,[3,2,6,5,0,3]))