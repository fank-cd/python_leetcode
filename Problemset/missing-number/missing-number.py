
# @Title: 缺失数字 (Missing Number)
# @Author: 2464512446@qq.com
# @Date: 2019-11-05 17:42:38
# @Runtime: 140 ms
# @Memory: 12.5 MB

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # return sum(i for i in range(len(nums)+1))-sum(nums)
        res = len(nums)
        for i in range(res):
            res = res ^ nums[i]
            res = res ^i
            
        return res
            
