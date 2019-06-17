
# @Title: 有效的字母异位词 (Valid Anagram)
# @Author: 2464512446@qq.com
# @Date: 2019-03-14 11:03:25
# @Runtime: 112 ms
# @Memory: 12.3 MB

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) == len(t):
            if sorted(s) == sorted(t):
                return True
            else:
                return False
        else:
            return False
