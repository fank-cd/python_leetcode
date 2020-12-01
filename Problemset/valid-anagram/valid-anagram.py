
# @Title: 有效的字母异位词 (Valid Anagram)
# @Author: 2464512446@qq.com
# @Date: 2020-10-26 18:05:29
# @Runtime: 64 ms
# @Memory: 13.5 MB

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return collections.Counter(s) == collections.Counter(t)
        if len(s) != len(t):
            return False
        d = {}
        for i in s:
            d[i] = d.get(i,0) + 1
        for i in t:
            d[i] = d.get(i,0)-1
            if d[i] <0:
                return False

        return True
