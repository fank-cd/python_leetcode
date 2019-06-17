
# @Title: 字符串中的第一个唯一字符 (First Unique Character in a String)
# @Author: 2464512446@qq.com
# @Date: 2019-03-14 11:48:14
# @Runtime: 228 ms
# @Memory: 11.8 MB

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
