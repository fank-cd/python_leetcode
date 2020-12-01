
# @Title: 最长公共前缀 (Longest Common Prefix)
# @Author: 2464512446@qq.com
# @Date: 2020-06-15 11:41:19
# @Runtime: 40 ms
# @Memory: 13.2 MB

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 这个方法太屌了
        if not strs: return ""
        ss = list(map(set, zip(*strs)))
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            print(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res

