# coding:utf-8
# 最后一个单词的长度

# 给定一个仅包含大小写字母和空格 ' ' 的字符串，返回其最后一个单词的长度。
#
# 如果不存在最后一个单词，请返回 0 。
#
# 说明：一个单词是指由字母组成，但不包含任何空格的字符串。
#
# 示例:
#
# 输入: "Hello World"
# 输出: 5
#

# 没啥好多的，直接split以空格分隔，
# 再strip去除空格 直接计算长度就行了

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int

        """

        a = s.strip().split(' ')
        if len(a):
            return len(a[-1])
        else:
            return 0