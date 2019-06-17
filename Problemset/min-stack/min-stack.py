
# @Title: 最小栈 (Min Stack)
# @Author: 2464512446@qq.com
# @Date: 2018-12-17 10:09:49
# @Runtime: 120 ms
# @Memory: 11 MB

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
        print self.min_l
        return self.min_l[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
