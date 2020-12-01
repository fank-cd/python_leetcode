
# @Title: 最大子序和 (Maximum Subarray)
# @Author: 2464512446@qq.com
# @Date: 2020-11-23 15:48:34
# @Runtime: 52 ms
# @Memory: 14.4 MB

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1]+nums[i],nums[i])
            res = max(res,nums[i])
        return res

