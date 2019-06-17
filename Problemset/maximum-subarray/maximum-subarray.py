
# @Title: 最大子序和 (Maximum Subarray)
# @Author: 2464512446@qq.com
# @Date: 2019-03-07 14:51:52
# @Runtime: 52 ms
# @Memory: 11.7 MB

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
   
        thissum = 0
        maxsum = -2147483647

        for i in nums:
            thissum +=i
            # maxsum = thissum if thissum > maxsum
            if thissum > maxsum:
                maxsum = thissum
            elif thissum < 0:
                thissum =0
                
        return maxsum
         """
        for i in range(1, len(nums)):
            nums[i]= nums[i] + max(nums[i-1], 0)
        return max(nums)
