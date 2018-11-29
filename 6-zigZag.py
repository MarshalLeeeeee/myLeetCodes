'''
6. ZigZag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);

Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
'''
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(numRows == 1):
            return s
        groupNum = 2 * numRows - 2
        turningPoint = groupNum // 2
        split = []
        length = []
        for i in range(groupNum):
            split.append(s[i::groupNum])
            length.append(len(split[i]))
        ans = split[0]
        for i in range(1,turningPoint):
            for j in range(length[i]):
                ans += split[i][j]
                try:
                    ans += split[2*turningPoint-i][j]
                except:
                    break
        ans += split[turningPoint]
        return ans

class Solution2:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if(numRows == 1):
            return s
        row = []
        groupNum = 2 * numRows - 2
        turningPoint = groupNum // 2
        for i in range(groupNum):
            if(i < numRows):
                row.append(i)
            else:
                row.append(groupNum-i)
        #print(row)
        ans = []
        for i in range(numRows):
        	ans.append('')
        #print(ans)
        for i,c in enumerate(s):
            m = i % groupNum
            ans[row[m]]+=c
        trueAns = ''
        for i in range(numRows):
            trueAns += ans[i]
        return trueAns

if __name__ == '__main__':
	print(Solution2().convert("PAYPALISHIRING",4))