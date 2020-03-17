
# @Title: 汉明距离 (Hamming Distance)
# @Author: 2464512446@qq.com
# @Date: 2019-09-06 16:58:22
# @Runtime: 20 ms
# @Memory: 11.7 MB

class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')
