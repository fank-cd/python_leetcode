
# @Title: 字符串中的第一个唯一字符 (First Unique Character in a String)
# @Author: 2464512446@qq.com
# @Date: 2020-12-23 10:09:32
# @Runtime: 92 ms
# @Memory: 15.1 MB

class Solution:
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1
