
# @Title: 连续子数组的最大和 (连续子数组的最大和  LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-12-23 15:15:10
# @Runtime: 72 ms
# @Memory: 19 MB

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            nums[i] = nums[i] + max(nums[i-1],0)
        return max(nums)
