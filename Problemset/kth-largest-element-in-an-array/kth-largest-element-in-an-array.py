
# @Title: 数组中的第K个最大元素 (Kth Largest Element in an Array)
# @Author: 2464512446@qq.com
# @Date: 2019-12-10 11:42:45
# @Runtime: 56 ms
# @Memory: 12.4 MB

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return heapq.nlargest(k, nums)[-1]
