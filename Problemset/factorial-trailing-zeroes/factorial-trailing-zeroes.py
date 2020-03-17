
# @Title: 阶乘后的零 (Factorial Trailing Zeroes)
# @Author: 2464512446@qq.com
# @Date: 2019-11-14 14:42:43
# @Runtime: 20 ms
# @Memory: 11.8 MB

class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = 0
        while n >= 5:
            n = n // 5
            p += n
        return p
