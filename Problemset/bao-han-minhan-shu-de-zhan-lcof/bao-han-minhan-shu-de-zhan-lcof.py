
# @Title: 包含min函数的栈 (包含min函数的栈 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-06-18 16:32:16
# @Runtime: 84 ms
# @Memory: 16.6 MB

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.min_data = []



    def push(self, x: int) -> None:
        if not self.min_data or x <= self.min_data[-1]:
            self.min_data.append(x)
        self.data.append(x)

    def pop(self) -> None:
        if not self.data:
            return 
        
        temp = self.data.pop()
        # print(self.min_data[-1])
        if temp ==self.min_data[-1]:
            self.min_data.pop()
        return temp

    def top(self) -> int:
        if not self.data:
            return 
        return self.data[-1]

    def min(self) -> int:

        if not self.min_data:
            return 

        return self.min_data[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
