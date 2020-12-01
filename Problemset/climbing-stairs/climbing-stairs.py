
# @Title: 爬楼梯 (Climbing Stairs)
# @Author: 2464512446@qq.com
# @Date: 2020-11-07 23:28:42
# @Runtime: 32 ms
# @Memory: 13.4 MB

class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 0 ,1
        for i in range(n):
            a,b = b,a+b
        return b
