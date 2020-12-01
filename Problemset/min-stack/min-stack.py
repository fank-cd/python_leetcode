
# @Title: 最小栈 (Min Stack)
# @Author: 2464512446@qq.com
# @Date: 2020-09-14 16:34:44
# @Runtime: 76 ms
# @Memory: 16.6 MB

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.mindata = [math.inf]

    def push(self, x: int) -> None:
        self.data.append(x)
        self.mindata.append(min(self.mindata[-1],x))
    def pop(self) -> None:
        self.data.pop()
        self.mindata.pop()

    def top(self) -> int:
        return self.data[-1]


    def getMin(self) -> int:
        return self.mindata[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
