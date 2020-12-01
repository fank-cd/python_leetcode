
# @Title: 设计循环双端队列 (Design Circular Deque)
# @Author: 2464512446@qq.com
# @Date: 2020-07-13 18:01:05
# @Runtime: 76 ms
# @Memory: 13.8 MB

class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        """
        self.lenth = k
        self.data = []

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        """
        if len(self.data) + 1 > self.lenth:
            return False
        self.data.insert(0,value)
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        """
        if len(self.data) + 1 > self.lenth:
            return False
        self.data.append(value)
        return True
        

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        """
        if not self.data:
            return False
        
        self.data.pop(0)
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        """
        if not self.data:
            return False

        self.data.pop()
        return True

    def getFront(self) -> int:
        """
        Get the front item from the deque.
        """
        if not self.data:
            return -1
        
        return self.data[0]

    def getRear(self) -> int:
        """
        Get the last item from the deque.
        """
        if not self.data:
            return -1
        
        return self.data[-1]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular deque is empty or not.
        """
        return True if not self.data else False

    def isFull(self) -> bool:
        """
        Checks whether the circular deque is full or not.
        """

        return True if len(self.data) == self.lenth else False
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
