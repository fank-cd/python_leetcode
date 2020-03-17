
# @Title: 山脉数组的峰顶索引 (Peak Index in a Mountain Array)
# @Author: 2464512446@qq.com
# @Date: 2019-09-29 17:30:57
# @Runtime: 76 ms
# @Memory: 12.8 MB

class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        return A.index(max(A))
