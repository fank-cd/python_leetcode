
# @Title: 扁平化嵌套列表迭代器 (Flatten Nested List Iterator)
# @Author: 2464512446@qq.com
# @Date: 2019-12-04 18:28:21
# @Runtime: 68 ms
# @Memory: 17 MB

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def build_generator(nestedList):
            for i in nestedList:
                if i.isInteger():
                    yield i.getInteger()
                else:
                    i = i.getList()
                    for j in build_generator(i):
                        yield j
        self.g = build_generator(nestedList)

    def next(self):
        """
        :rtype: int
        """
        #print(self.v)
        # print(type(self.g))
        return self.v

    def hasNext(self):
        """
        :rtype: bool
        """
        try:
            self.v = next(self.g)
        #print(self.v)
            return True
        except:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
