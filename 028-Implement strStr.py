# coding:utf-8

# 实现 strStr() 函数。
#
# 给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。
#
# 示例 1:
#
# 输入: haystack = "hello", needle = "ll"
# 输出: 2
#
# 示例 2:
#
# 输入: haystack = "aaaaa", needle = "bba"
# 输出: -1
#
# 说明:
#
# 当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。
#
# 对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与C语言的 strstr() 以及 Java的 indexOf() 定义相符。


# 直接调用内部函数
# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         if needle == None:
#             return 0
#         try:
#             return haystack.index(needle)
#         except:
#             return -1
#

#

# 自己实现

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int

        """

        needle_len = len(needle)
        haystack_len = len(haystack)
        if needle_len == 0 and haystack_len == 0:
            return 0

        if needle_len == 0:
            return 0
        state = False

        for i in range(haystack_len):
            if haystack[i] == needle[0]:
                if haystack[i:i + needle_len] == needle:
                    state = True
                    return i

        if not state:
            return -1