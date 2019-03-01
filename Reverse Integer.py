# coding:utf-8

# 整数反转
# 给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

# 这道题目主要用了切片的方法，还是比较取巧吧，主要是边界的设定比较麻烦


def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """

    if x > 0:
        a = int(str(x)[::-1])
    elif x < 0:
        a = -int((str(x)[1:])[::-1])
    elif x == 0:
        return 0
    min = -2147483648
    max = 2147483647

    if a > min and a < max:
        return a
    else:
        return 0