'''
225. Implement Stack using Queues

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

Example:
MyStack stack = new MyStack();
stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false

Notes:
You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
'''

class MyStack:
	# double queue
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = [[],[]]
        self.flag = 1

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.q[1-self.flag].append(x)
        while self.q[self.flag]:
            self.q[1-self.flag].append(self.q[self.flag].pop(0))
        self.flag = 1-self.flag

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        return self.q[self.flag].pop(0)        

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        res = self.q[self.flag].pop(0)
        self.push(res)
        return res

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return False if self.q[self.flag] else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()