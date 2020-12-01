
# @Title: 用栈实现队列 (Implement Queue using Stacks)
# @Author: 2464512446@qq.com
# @Date: 2020-10-29 01:02:18
# @Runtime: 40 ms
# @Memory: 13.6 MB

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.helper = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.helper:
            while self.data:
                self.helper.append(self.data.pop())
        return self.helper.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.helper:
            while self.data:
                self.helper.append(self.data.pop())
        return self.helper[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.data) == 0 and len(self.helper) == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
