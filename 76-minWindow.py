class Solution:
	# only work for non-duplicated t
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t: return ''
        lenS, lenT = len(s), len(t)
        if lenS < lenT: return ''
        if lenT == 1:
            if t[0] in s: return t[0]
            else: return ''
            
        dicT = {}
        for i in range(lenT):
            try:
                dicT[t[i]] += 1
            except:
                dicT[t[i]] = 1
        
        rightgap, leftgap, curr, currIndex, currNum, record = 0, 0, '*', -1, 0, []
        for i in range(lenS):
            if s[i] in dicT:
                if curr == '*':
                    curr = s[i]
                    currNum = 1
                elif curr == s[i]:
                    rightgap = 0
                    currNum += 1
                else:
                    record.append((leftgap, currNum, currIndex, curr))
                    leftgap, rightgap = rightgap, 0
                    curr = s[i]
                    currNum = 1
                currIndex = i
            else:
                if curr == '*':
                    leftgap += 1
                else:
                    rightgap += 1
        record.append((leftgap, currNum, currIndex, curr))
        print(record)
        
        dicRecord, anshead, anstail = {}, 0, -1
        for i in range(lenT):
            try: dicRecord[record[i][-1]] += 1
            except: dicRecord[record[i][-1]] = 1
        if dicRecord == dicT:
            head, tail = 0, lenT-1
            ansLen = record[tail-1][-2] + record[tail][0] + 1 - record[head][-2] + 1
            anshead, anstail = head, tail
        
        for i in range(lenT,len(record)):
            dicRecord[record[i-lenT][-1]] -= 1
            head += 1
            tail += 1
            try: dicRecord[record[i][-1]] += 1
            except: dicRecord[record[i][-1]] = 1
            if dicRecord == dicT:
                currLen = record[tail-1][-2] + record[tail][0] + 1 - record[head][-2] + 1
                if currLen < ansLen: anshead, anstail, ansLen = head, tail, currLen
        if anstail == -1: return ''
        else: return s[record[anshead][-2]:record[anshead][-2]+ansLen]

class Solution2:
	# double pointer
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t: return ''
        lenS, lenT = len(s), len(t)
        if lenS < lenT: return ''
        if lenT == 1:
            if t[0] in s: return t[0]
            else: return ''
            
        dicT = {}
        for i in range(lenT):
            try:
                dicT[t[i]] += 1
            except:
                dicT[t[i]] = 1
        
        left, right = 0, 0
        for i in range(lenS):
            if s[i] in dicT:
                right = left = i
                break

        match, ansLeft, ansRight, rightMode = 0, -1, -1, True
        while left < lenS and right < lenS:
            print('-'*10)
            print(left,right,rightMode)
            if rightMode:
                if s[right] in dicT:
                    dicT[s[right]] -= 1
                    if dicT[s[right]] >= 0:
                        match += 1
                        if match == lenT:
                            if ansRight == -1 or right - left < ansRight - ansLeft:
                                ansLeft, ansRight = left, right # record the true head ans tail
                            rightMode = False
                        else: right += 1
                    else: right += 1
                else: right += 1
            else:
                if s[left] in dicT:
                    dicT[s[left]] += 1
                    if dicT[s[left]] > 0:
                        if right >= lenS: break
                        match -= 1
                        left += 1
                        right += 1
                        while True:
                        	if s[left] not in dicT:
                        	    left += 1
                        	else:
                        		break
                        rightMode = True
                    else:
                        left += 1
                        while True:
                        	if s[left] not in dicT:
                        	    left += 1
                        	else:
                        		break
                        if right - left < ansRight - ansLeft:
                            ansLeft, ansRight = left, right
                else: left += 1
        if ansRight == -1: return ''
        else: return s[ansLeft:ansRight+1]

if __name__ == '__main__':
	print(Solution2().minWindow('aa','aa'))