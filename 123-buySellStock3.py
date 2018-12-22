'''
123. Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. You may complete at most two transactions.
Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if not l or l == 1: return 0
        else:
            single, double = [0], [0]
            minIndex, pre = 0, 0
            if prices[0] <= prices[1]: floor = [0]
            else: floor = []
            for i in range(1,l):
                if prices[i] < prices[minIndex]:
                    minIndex = i
                single.append(max(single[-1],prices[i]-prices[minIndex]))
                
                if prices[i] < prices[pre]:
                    maxProfit = double[-1]
                    for f in floor:
                        if maxProfit < single[f]+prices[pre]-prices[f]: 
                            maxProfit = single[f]+prices[pre]-prices[f]
                    double.append(maxProfit)
                    for j in range(len(floor)-1,-1,-1):
                        if prices[i] <= prices[floor[j]]:
                            floor.pop(j)
                        else:
                            break
                    floor.append(i)
                pre += 1
                
            maxProfit = double[-1]
            for f in floor:
                if maxProfit < single[f]+prices[pre]-prices[f]: 
                    maxProfit = single[f]+prices[pre]-prices[f]
            double.append(maxProfit)
            return double[-1]