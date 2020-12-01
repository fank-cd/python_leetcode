
# @Title: 青蛙跳台阶问题 (青蛙跳台阶问题  LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-03-18 16:52:27
# @Runtime: 36 ms
# @Memory: 13.2 MB

class Solution:
    def numWays(self, n: int) -> int:
        a,b = 0 ,1
        for _ in range(n+1):
            a,b = b, a+b
        return a % 1000000007

