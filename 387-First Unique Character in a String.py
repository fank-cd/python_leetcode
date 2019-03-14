# coding:utf-8
# 字符串中的第一个唯一字符
# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 - 1。
#
# 案例:
#
# s = "leetcode"
# 返回
# 0.
#
# s = "loveleetcode",
# 返回
# 2.
#
# 注意事项：您可以假定该字符串只包含小写字母。

# 拿一个字典去计数，计算字母出现的次数。。

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = {}
        for i in s:
            m[i] = m.get(i, 0) + 1
        for i in range(len(s)):
            if m[s[i]] == 1:
                return i
        return -1