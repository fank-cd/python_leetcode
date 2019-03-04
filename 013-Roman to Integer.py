# coding:utf-8

# 罗马数字转整数
#
# 罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。
#
# 字符          数值
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
#
# 例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。
#
# 通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，
# 所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：
#
#     I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
#     X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
#     C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。
#
# 给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。
#
# 示例 1:
#
# 输入: "III"
# 输出: 3

# 示例 4:
#
# 输入: "LVIII"
# 输出: 58
# 解释: L = 50, V= 5, III = 3.
#
# 示例 5:
#
# 输入: "MCMXCIV"
# 输出: 1994
# 解释: M = 1000, CM = 900, XC = 90, IV = 4.

# 主要思路还是通过字典形式存储，这样来做一个转换


def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    rotonum = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90,
               "CD": 400, "CM": 900}
    half = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    half_alpha = ["I", "X", "C"]
    i = 0
    leng = len(s)
    sum = 0
    while i < leng:
        if s[i] in half_alpha and i + 1 < leng:
            if s[i:i + 2] in half.keys():
                sum += half[s[i:i + 2]]
                i += 2
                continue
        sum += rotonum[s[i]]
        i += 1

    return sum