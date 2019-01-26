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



if __name__ == '__main__':
    print(Solution().nthUglyNumber(43))