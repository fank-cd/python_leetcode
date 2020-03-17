
# @Title: 位1的个数 (Number of 1 Bits)
# @Author: 2464512446@qq.com
# @Date: 2019-11-01 18:01:21
# @Runtime: 4 ms
# @Memory: 11.7 MB

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        count = 0
        while n:
            count += 1
            n = n & (n - 1)
        return count

