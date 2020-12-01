
# @Title: 打家劫舍 II (House Robber II)
# @Author: 2464512446@qq.com
# @Date: 2020-11-04 11:54:16
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        if size <= 2:
            return max(nums)
        
        def helper(nums):
            if not nums:
                return 0
            size = len(nums)
            if size <= 2:
                return max(nums)
            dp = [0] * size
            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])
            for i in range(2,size):
                dp[i] = max(dp[i-1],nums[i]+dp[i-2])
            return dp[-1]
        print(nums[1:],nums[:size-1])
        print(helper(nums[1:]),helper(nums[:size-1]))
        return max(helper(nums[1:]),helper(nums[:size-1]))
