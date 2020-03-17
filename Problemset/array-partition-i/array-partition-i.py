
# @Title: 数组拆分 I (Array Partition I)
# @Author: 2464512446@qq.com
# @Date: 2019-10-08 16:23:43
# @Runtime: 368 ms
# @Memory: 14.1 MB

class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])
