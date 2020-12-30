
# @Title: 同构字符串 (Isomorphic Strings)
# @Author: 2464512446@qq.com
# @Date: 2020-12-28 16:12:46
# @Runtime: 48 ms
# @Memory: 17.1 MB

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d1,d2 = defaultdict(list), defaultdict(list)
        for index,i in enumerate(s):
            d1[i].append(index)
        for index,i in enumerate(t):
            d2[i].append(index)

        # print(list(d1.values()),list(d2.values()))
        return list(d1.values()) == list(d2.values())
