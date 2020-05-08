
# @Title: 机器人的运动范围 (机器人的运动范围  LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-05-07 12:10:50
# @Runtime: 108 ms
# @Memory: 16.1 MB

class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        visited = [[False]*n  for i in range(m)]
        res = []
        def _sum(n):
            res = 0
            while n:
                res += n % 10
                n = n//10
            return res

        def check(col,row):
            if 0 <=col<m and 0<=row<n and sum([_sum(col),_sum(row)]) <= k\
                and not visited[col][row]:
                return True
            return False

        def helper(col, row):

            # step = 1
            if col == 0 and row == 0:
                res.append(True)
            visited[col][row] = True
            if check(col + 1, row):
                if helper(col + 1, row):
                    res.append(True)
            if check(col - 1, row):
                if helper(col - 1, row):
                    res.append(True)
            if check(col, row + 1):
                if helper(col, row + 1):
                    res.append(True)
            if check(col, row - 1):
                if helper(col, row - 1):
                    res.append(True)
            return True

        # print(visited)
        helper(0, 0)
        return len(res)

