
# @Title: 重复 N 次的元素 (N-Repeated Element in Size 2N Array)
# @Author: 2464512446@qq.com
# @Date: 2019-10-14 15:21:13
# @Runtime: 280 ms
# @Memory: 12.8 MB

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        for i in A:
            if A.count(i) >1:
                return i 
        

