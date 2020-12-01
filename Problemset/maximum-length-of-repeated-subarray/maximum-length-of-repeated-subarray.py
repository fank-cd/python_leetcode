
# @Title: 最长重复子数组 (Maximum Length of Repeated Subarray)
# @Author: 2464512446@qq.com
# @Date: 2020-07-01 15:15:37
# @Runtime: 6484 ms
# @Memory: 37.9 MB

class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        n, m = len(A), len(B)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        ans = 0
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                # print(i,j)
                dp[i][j] = dp[i + 1][j + 1] + 1 if A[i] == B[j] else 0
                ans = max(ans, dp[i][j])
        return ans


