
# @Title: 数字的补数 (Number Complement)
# @Author: 2464512446@qq.com
# @Date: 2019-10-08 16:12:21
# @Runtime: 24 ms
# @Memory: 11.4 MB

class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return int(bin(num)[2:].replace('0', '2').replace('1', '0').replace('2', '1'), 2)
