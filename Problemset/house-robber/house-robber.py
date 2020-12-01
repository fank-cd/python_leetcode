
# @Title: 打家劫舍 (House Robber)
# @Author: 2464512446@qq.com
# @Date: 2020-11-23 12:10:29
# @Runtime: 32 ms
# @Memory: 13.5 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size < 2:
            return nums[0]
        dp = [0] * size
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,size):
            dp[i] = max(dp[i-1],dp[i-2] + nums[i])
        # print(dp)
        return dp[-1]
