
# @Title: 分割等和子集 (Partition Equal Subset Sum)
# @Author: 2464512446@qq.com
# @Date: 2020-10-11 18:38:13
# @Runtime: 1236 ms
# @Memory: 13.2 MB

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 2:
            return False
        
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [True] + [False] * target
        for i, num in enumerate(nums):
            for j in range(target, num - 1, -1):
                dp[j] |= dp[j - num]
        
        return dp[target]


