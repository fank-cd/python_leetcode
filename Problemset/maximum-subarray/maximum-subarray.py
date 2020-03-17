
# @Title: 最大子序和 (Maximum Subarray)
# @Author: 2464512446@qq.com
# @Date: 2019-11-08 16:25:54
# @Runtime: 56 ms
# @Memory: 12.3 MB

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(1,len(nums)):
            nums[i] = nums[i] +max(nums[i-1],0)
            
        return max(nums)
