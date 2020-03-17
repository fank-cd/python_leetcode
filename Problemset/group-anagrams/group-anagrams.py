
# @Title: 字母异位词分组 (Group Anagrams)
# @Author: 2464512446@qq.com
# @Date: 2019-12-10 14:17:18
# @Runtime: 88 ms
# @Memory: 15.7 MB

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d= {}
        for i in strs:
            tmp = "".join(sorted(i))
            if tmp not in d:
                d[tmp] =[]
            d[tmp].append(i)

        res = []
        for i in d.values():
            res.append(i)
        return res
