
# @Title: 零钱兑换 (Coin Change)
# @Author: 2464512446@qq.com
# @Date: 2020-11-23 12:27:37
# @Runtime: 1304 ms
# @Memory: 13.5 MB

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp =  [math.inf] * (amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for c in coins:
                if i >= c:
                    dp[i] = min(dp[i],dp[i-c]+1)
        return dp[-1] if dp[-1] != math.inf else - 1
