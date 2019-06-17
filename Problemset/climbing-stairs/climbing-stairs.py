
# @Title: 爬楼梯 (Climbing Stairs)
# @Author: 2464512446@qq.com
# @Date: 2018-12-04 11:18:40
# @Runtime: 28 ms
# @Memory: N/A

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        c, a, b = 0, 0, 1
        while c < n:
            a, b = b, a + b
            c = c+1
        return b
