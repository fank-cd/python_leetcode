
# @Title: Nim 游戏 (Nim Game)
# @Author: 2464512446@qq.com
# @Date: 2019-09-29 15:04:35
# @Runtime: 20 ms
# @Memory: 11.7 MB

class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n %4 !=0
