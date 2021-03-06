'''
295. Find Median from Data Stream

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:
void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.

Example:
addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3) 
findMedian() -> 2
 
Follow up:
If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?
'''

########################################################################################################################
# Solution 1
# BST solution with 0-100 nodes initialized 
# Every tree node manege the count of duplicated nums and the number of nodes in its subtree
class TreeNode:
    def __init__(self,val,cnt=0):
        self.val = val
        self.cnt = cnt
        self.num = cnt
        self.left = None
        self.right = None

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root, cnt = TreeNode(-1), 1
        q = [self.root]
        while cnt < 101:
            nq = []
            while q and cnt < 101:
                node = q.pop(0)
                node.left, node.right = TreeNode(-1), TreeNode(-1)
                nq.append(node.left); nq.append(node.right); cnt += 2
            q = nq
        q, cnt = [self.root], 0
        while q:
            if q[-1].left: q.append(q[-1].left)
            else:
                node = q.pop(); node.val = cnt; cnt += 1
                if q:
                    node = q.pop(); node.val = cnt; cnt += 1
                    if node.right: q.append(node.right)

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        curr = self.root
        while num != curr.val:
            curr.num += 1
            if num > curr.val:
                if curr.right: curr = curr.right
                else: curr.right = TreeNode(num); curr = curr.right; break
            else:
                if curr.left: curr = curr.left
                else: curr.left = TreeNode(num); curr = curr.left; break
        curr.cnt += 1; curr.num += 1
        

    def findMedian(self):
        """
        :rtype: float
        """
        length = self.root.num
        curr = self.root
        left, right = None, None
        numLeft, numRight = -1, -1
        while True:
            numLeft2 = ((numLeft + left.cnt) if left else 0) + (curr.left.num if curr.left else 0)
            numRight2 = ((numRight + right.cnt) if right else 0) + (curr.right.num if curr.right else 0)
            if numLeft2 > length//2: right = curr; numRight = numRight2; curr = curr.left 
            elif numRight2 > length//2: left = curr; numLeft = numLeft2; curr = curr.right
            else:
                if not length % 2:
                    q, res = [[curr,left,right,numLeft,numRight]], []
                    while q:
                        nq = []
                        while q:
                            node = q.pop(0)
                            curr, left, right, numLeft, numRight = node[0], node[1], node[2], node[3], node[4]
                            numLeft2 = ((numLeft + left.cnt) if left else 0) + (curr.left.num if curr.left else 0)
                            numRight2 = ((numRight + right.cnt) if right else 0) + (curr.right.num if curr.right else 0)
                            if numLeft2 < length//2 and numRight2 < length//2: return curr.val
                            if (numLeft2 < length//2 and numRight2 == length//2) or (numRight2 < length//2 and numLeft2 == length//2): 
                                res.append(curr.val)
                                if len(res) == 2:  return (res[0]+res[1])/2
                            if curr.left and numLeft2 >= length//2:  nq.append([curr.left,left,curr,numLeft,numRight2])
                            if curr.right and numRight2 >= length//2: nq.append([curr.right,curr,right,numLeft2,numRight])
                        q = nq
                else: return curr.val

#############################################################################################################################################
# Solution 2
# Double heap solution which manage the first half of the array and the second half respectively
class maxHeap:
    def __init__(self):
        self.heap = []

    def len(self):
        return len(self.heap)

    def pop(self):
        if self.heap:
            res = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            index = 0
            length = self.len()
            while index*2+1 < length:
                if (index*2+1 < length and self.heap[index] < self.heap[index*2+1]) or (index*2+2 < length and self.heap[index] < self.heap[index*2+2]):
                    if index*2+2 < length:
                        if self.heap[index*2+1] > self.heap[index*2+2]:
                            self.heap[index], self.heap[index*2+1] =  self.heap[index*2+1], self.heap[index]
                            index = index*2+1
                        else:
                            self.heap[index], self.heap[index*2+2] =  self.heap[index*2+2], self.heap[index]
                            index = index*2+2
                    else: 
                        self.heap[index], self.heap[index*2+1] =  self.heap[index*2+1], self.heap[index]
                        index = index*2+1
                else: break
            return res


    def push(self,num):
        self.heap.append(num)
        index = len(self.heap) - 1
        while index:
            if self.heap[(index-1) // 2] < self.heap[index]:
                self.heap[(index-1) // 2], self.heap[index] = self.heap[index], self.heap[(index-1) // 2]
                index = (index-1) // 2
            else: break

    def peek(self):
        if self.heap: return self.heap[0]

class MedianFinder:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small = maxHeap()
        self.large = maxHeap() # every element times -1

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.small.len() == self.large.len():
            if self.small.len() and num >= self.small.peek(): self.large.push(-num)
            else: self.small.push(num); self.large.push(-self.small.pop())
        else:
            if self.large.len() and num <= -self.large.peek(): self.small.push(num)
            else: self.large.push(-num); self.small.push(-self.large.pop())

    def findMedian(self):
        """
        :rtype: float
        """
        if self.small.len() == self.large.len():
            return (self.small.peek() - self.large.peek()) / 2
        else:
            return -self.large.peek()

if __name__ == '__main__':
    
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())
    

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()