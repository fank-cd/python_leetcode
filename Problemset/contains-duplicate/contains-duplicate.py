
# @Title: 存在重复元素 (Contains Duplicate)
# @Author: 2464512446@qq.com
# @Date: 2019-11-06 10:43:34
# @Runtime: 120 ms
# @Memory: 16.8 MB

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(list(set(nums)))
