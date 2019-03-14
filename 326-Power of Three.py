# coding:utf-8
# 3的幂
# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。
#
# 示例 1:
#
# 输入: 27
# 输出: true
#
# 示例 2:
#
# 输入: 0
# 输出: false
#
# 示例 3:
#
# 输入: 9
# 输出: true
#
# 示例 4:
#
# 输入: 45
# 输出: false

# 直接递归做吧。。

class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        elif n == 3:
            return True
        elif n % 3 != 0:
            return False
        elif n == 0:
            return False
        else:
            return self.isPowerOfThree(n / 3)
