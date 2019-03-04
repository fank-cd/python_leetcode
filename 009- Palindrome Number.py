# coding:utf-8
# 回文数
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
#
# 示例 1:
#
# 输入: 121
# 输出: true
#
# 示例 2:
#
# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
#
# 示例 3:
#
# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。


# python写这个真的太简单了。。切片大法搞定

def isPalindrome(self, x):
    """
    :type x: int
    :rtype: bool
    """
    return str(x) == str(x)[::-1]


# 还有一种想法是把x转换成字符串的列表
def isPalindrome1(self, x):
    """
    :type x: int
    :rtype: bool
    """
    flag = True
    a = list(str(x))
    if x >= 0:
        while flag and len(a) > 1:
            if a.pop() == a.pop(0):
                pass
            else:
                flag = False

        if flag:
            return True

        else:
            return False

    return False
