# coding:utf-8

# 报数

# 报数序列是一个整数序列，按照其中的整数的顺序进行报数，得到下一个数。其前五项如下：
#
# 1.1
# 2.11
# 3.21
# 4.1211
# 5.111221
#
# 1被读作"one 1"("一个一"), 即11。
# 11被读作"two 1s"("两个一"）, 即21。
# 21被读作"one 2", "one 1" （"一个二", "一个一"), 即1211。

# 给定一个正整数
# n（1 ≤ n ≤ 30），输出报数序列的第
# n
# 项。
#
# 注意：整数顺序将表示为一个字符串。
#
#
#
# 示例
# 1:
#
# 输入: 1
# 输出: "1"
#
# 示例
# 2:
#
# 输入: 4
# 输出: "1211"
#


# 正则表达式解决
# (.)\2*
# \num 匹配num，其中num是一个正整数。对所获取的匹配的引用。例如，“(.)\1”匹配两个连续的相同字符。
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        import re
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(p[0])) + p[1] for p in re.findall(r'((.)\2*)', s))
        return s