class Solution:
    # add one after another
    # time comp O(?)
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 6: return n
        cnt = 5
        q2, q3, q5 = [4], [3], [5]
        while cnt < n:
            m = max(q2[-1],q3[-1],q5[-1])
            candidate = []
            for q in q2:
                if 2*q > m: candidate.append([2*q,0])
            if len(candidate) != 1: candidate.append([float('inf'),0])
            for q in q3:
                if 2*q > m: candidate.append([2*q,1])
            if len(candidate) != 2: candidate.append([float('inf'),1])
            for q in q5:
                if 2*q > m: candidate.append([2*q,2])
            if len(candidate) != 3: candidate.append([float('inf'),2])
            for q in q3:
                if 3*q > m: candidate.append([3*q,3])
            if len(candidate) != 4: candidate.append([float('inf'),3])
            for q in q5:
                if 3*q > m: candidate.append([3*q,4])
            if len(candidate) != 5: candidate.append([float('inf'),4])
            for q in q5:
                if 5*q > m: candidate.append([5*q,5])
            if len(candidate) != 6: candidate.append([float('inf'),5])
            candidate.sort()
            for c in candidate:
                if c[0] > m:
                    if c[1] < 3: 
                        q2.append(c[0])
                        if c[1] == 0: q2.pop(0)
                    elif c[1] < 5:
                        q3.append(c[0])
                        if c[1] == 3: q3.pop(0)
                    else:
                        q5.append(c[0])
                        q5.pop(0)
                    break
            cnt += 1
        return max(q2[-1],q3[-1],q5[-1])

class Solution2:
    # time comp O(n) dp solution
    # abviously we want append the minimal one not in the 'res'
    # we always manage/update the minimal multilpy result for 2, 3, 5 respectively
    # specifically, the update is done by simply move from the current number in 'res' to the next one
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [1]
        i2, i3, i5 = 0, 0, 0
        for i in range(1,n):
            m = min(res[i2]*2,res[i3]*3,res[i5]*5)
            res.append(m)
            if m == res[i2]*2: i2 += 1
            if m == res[i3]*3: i3 += 1
            if m == res[i5]*5: i5 += 1
        return res[-1]

if __name__ == '__main__':
    print(Solution().nthUglyNumber(43))