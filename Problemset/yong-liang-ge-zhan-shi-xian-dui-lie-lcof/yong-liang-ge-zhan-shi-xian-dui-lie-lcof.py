
# @Title: 用两个栈实现队列 (用两个栈实现队列 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-03-18 11:42:16
# @Runtime: 720 ms
# @Memory: 17.1 MB

class CQueue:

    def __init__(self):
        self.data = []
        self.helper = []


    def appendTail(self, value: int) -> None:
        self.data.append(value)

    def deleteHead(self) -> int:
        if not self.data and not self.helper:
            return -1
        if not self.helper:
            while self.data:
                self.helper.append(self.data.pop())
        return self.helper.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
