# coding:utf-8

# 二进制求和

# 给定两个二进制字符串，返回他们的和（用二进制表示）。
#
# 输入为非空字符串且只包含数字 1 和 0。
#
# 示例 1:
#
# 输入: a = "11", b = "1"
# 输出: "100"
#
# 示例 2:
#
# 输入: a = "1010", b = "1011"
# 输出: "10101"
#

# 直接用int转为十进制相加，再bin转换为二进制
# 结论：这样可能会溢出的。。

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        return bin(int(a, 2) + int(b, 2))[2:]