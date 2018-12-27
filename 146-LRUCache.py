'''
146. LRU Cache

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. 
				  When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

class doubleListNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = {}
        self.cnt = 0
        self.capacity = capacity
        self.head = doubleListNode([-1,0])
        self.tail = doubleListNode([-1,0])
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def _toHead(self, node):
        nodePrev, nodeNext = node.prev, node.next
        if nodePrev != self.head:
            headNext = self.head.next
            node.prev, node.next = self.head, headNext
            self.head.next, headNext.prev = node, node
            nodePrev.next = nodeNext
            nodeNext.prev = nodePrev
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache: 
            ans = self.cache[key].val[1]
            self._toHead(self.cache[key])
            return ans
        else: return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity:
            if key not in self.cache:
                if self.cnt == self.capacity:
                    node = self.tail.prev
                    tailPrevPrev = self.tail.prev.prev
                    tailPrevPrev.next = self.tail
                    self.tail.prev = tailPrevPrev
                    self.cnt -= 1
                    del self.cache[node.val[0]]

                headNext = self.head.next
                node = doubleListNode([key,value])
                self.head.next = node
                node.prev, node.next = self.head, headNext
                headNext.prev = node
                self.cnt += 1
                self.cache[key] = node
            else: 
                self.cache[key].val[1] = value
                self._toHead(self.cache[key])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)