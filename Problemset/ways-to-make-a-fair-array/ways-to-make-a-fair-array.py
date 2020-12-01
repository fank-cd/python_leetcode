
# @Title: 生成平衡数组的方案数 (Ways to Make a Fair Array)
# @Author: 2464512446@qq.com
# @Date: 2020-11-27 15:57:26
# @Runtime: 288 ms
# @Memory: 19.8 MB

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i-1] + (nums[i-1] if i % 2 else -nums[i-1])

        ans = 0
        for i in range(1, n + 1):
            if dp[i - 1] == dp[n] - dp[i]:
                ans += 1

        return ans

