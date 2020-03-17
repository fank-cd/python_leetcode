
# @Title: 最小栈 (Min Stack)
# @Author: 2464512446@qq.com
# @Date: 2019-11-06 11:09:28
# @Runtime: 80 ms
# @Memory: 15.6 MB

class MinStack:

    def __init__(self):
        # 数据栈
        self.data = []
        # 辅助栈
        self.helper = []

    def push(self, x):
        self.data.append(x)
        # 关键 1 和关键 2
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self):
        # 关键 3：【注意】不论怎么样，数据栈都要 pop 出元素
        if self.data:
            top = self.data.pop()

            if self.helper and top == self.helper[-1]:
                self.helper.pop()
            return top

    def top(self):
        if self.data:
            return self.data[-1]

    def getMin(self):
        if self.helper:
            return self.helper[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
