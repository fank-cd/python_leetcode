
# @Title: 二进制求和 (Add Binary)
# @Author: 2464512446@qq.com
# @Date: 2019-01-15 11:03:39
# @Runtime: 28 ms
# @Memory: 7 MB

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        return bin(int(a,2)+int(b,2))[2:]
