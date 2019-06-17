
# @Title: 存在重复元素 (Contains Duplicate)
# @Author: 2464512446@qq.com
# @Date: 2018-03-23 14:39:03
# @Runtime: 48 ms
# @Memory: N/A

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) > len(set(nums)):
            return True
        else:
            return False
        
