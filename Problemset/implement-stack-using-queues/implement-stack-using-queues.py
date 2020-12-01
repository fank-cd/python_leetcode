
# @Title: 用队列实现栈 (Implement Stack using Queues)
# @Author: 2464512446@qq.com
# @Date: 2020-03-05 10:48:47
# @Runtime: 44 ms
# @Memory: 13.1 MB

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.empty():
            return self.data.pop()

    def top(self) -> int:
        """
        Get the top element.
        """
        if self.data:
            return self.data[-1]

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return True if len(self.data) == 0 else False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
