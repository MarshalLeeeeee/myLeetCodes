'''
119. Pascal's Triangle II

Example:
Input: 3
Output: [1,3,3,1]

Follow up:
Could you optimize your algorithm to use only O(k) extra space?
'''

class Solution:
    # O(2k) space
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if not rowIndex: return [1]
        else:
            curr, index = [1], 0
            while index < rowIndex+1:
                pre = curr.copy()
                curr = [1]
                for j in range(1,index):
                    curr.append(pre[j-1]+pre[j])
                curr.append(1)
                index += 1
            return curr

class Solution2:
    # O(k) space
    # using factorial method to compute directly
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        fact,ans = [1],[]
        for i in range(1,rowIndex+1):
            fact.append(fact[-1]*i)
        for i in range(rowIndex+1):
            ans.append(fact[-1]//(fact[i]*fact[rowIndex-i]))
        return ans