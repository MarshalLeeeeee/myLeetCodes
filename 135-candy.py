'''
135. Candy

There are N children standing in a line. Each child is assigned a rating value.
You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?

Example 1:
Input: [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
             The third child gets 1 candy because it satisfies the above two conditions.
'''

class Solution:       
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings: return 0
        elif len(ratings) == 1: return 1
        else:
            cnt = 1
            prevflag = None
            updown = []
            for i in range(1,len(ratings)):
                if ratings[i-1] < ratings[i]: flag = 1 # up
                elif ratings[i-1] > ratings[i]: flag = -1 # down
                else: flag = 0
                if flag != prevflag:
                    if prevflag != None: updown.append([prevflag,cnt])
                    cnt = 2
                else: cnt += 1
                prevflag = flag
            updown.append([prevflag,cnt])
            ans = 0
            for i,ud in enumerate(updown):
                if not i: 
                    if ud[0] == 0: ans += ud[1]
                    else: ans += (ud[1] + 1) * ud[1] // 2
                else:
                    if updown[i-1][0] == 1:
                        if ud[0] == -1:
                            if ud[1] > updown[i-1][1]: 
                                ans = ans - updown[i-1][1]
                                ans += (ud[1] + 1) * ud[1] // 2
                            else: ans += (ud[1] - 1) * ud[1] // 2
                        else: ans += ud[1] - 1
                    elif updown[i-1][0] == -1:
                        if ud[0] == 1: ans += (ud[1] + 1) * ud[1] // 2 - 1
                        else: ans += ud[1] - 1
                    else:
                        if ud[0] == -1: 
                            ans -= 1
                            ans += (ud[1] + 1) * ud[1] // 2
                        else: ans += (ud[1] + 1) * ud[1] // 2 - 1
            return ans

if __name__ == '__main__':
    nums = [5,6,7,6,7,8,7,6,5,4,3,2,1]
    nums2 = [1,2,2]
    print(Solution().candy(nums2))