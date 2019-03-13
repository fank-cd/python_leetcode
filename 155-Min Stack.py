# coding:utf-8

# 最小栈

# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
#
#     push(x) -- 将元素 x 推入栈中。
#     pop() -- 删除栈顶的元素。
#     top() -- 获取栈顶元素。
#     getMin() -- 检索栈中的最小元素。
#
# 示例:
#
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
#

# 非常典型的问题，借助辅助栈实现


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        self.min_l = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.min_l:
            self.min_l.append(x)
        elif self.min_l[-1] >= x:
            self.min_l.append(x)

        self.l.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.l[-1] > self.min_l[-1]:
            pass
        elif self.l[-1] == self.min_l[-1]:
            self.min_l.pop()

        return self.l.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.l[-1]

    def getMin(self):
        """
        :rtype: int
        """
        # print self.min_l
        return self.min_l[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()