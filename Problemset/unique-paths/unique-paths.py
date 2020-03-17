
# @Title: 不同路径 (Unique Paths)
# @Author: 2464512446@qq.com
# @Date: 2019-12-13 14:15:57
# @Runtime: 24 ms
# @Memory: 11.6 MB

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # self.count = 0
        # def helper(x,y):
        #     if x == m-1 or y == n-1:
        #         self.count +=1
        #     else:
        #         if x <m:
        #             helper(x+1,y)
        #         if y < n:
        #             helper(x,y+1)

        # helper(0,0)
        # return self.count
        # dp = [[0 for i in range(n)] for j in range(m)]

        # for i in range(len(dp)):
        #     dp[i][0] = 1

        # for i in range(len(dp[0])):
        #     # print(dp)
        #     dp[0][i] = 1
        # # print(dp)
        # for i in range(1, m):
        #     for j in range(1, n):
        #         dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # return (dp[-1][-1])
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        # print(cur)
        return cur[-1]


