
# @Title: 跳跃游戏 VI (Jump Game VI)
# @Author: 2464512446@qq.com
# @Date: 2020-12-23 16:39:57
# @Runtime: 312 ms
# @Memory: 24.7 MB

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        dp = [-10001]*len(nums)
        stack = collections.deque()
        for i in range(len(nums)):
            if len(stack)==0:
                dp[i] = nums[i]
            else:
                ##保存dp[i-k]到dp[i-1]的最大值
                if stack[0]<i-k:
                    stack.popleft()
                dp[i] = dp[stack[0]]+nums[i]
                while stack and dp[stack[-1]]<dp[i]: 
                    stack.pop()
            stack.append(i)
        return dp[-1]



