
# @Title: 字母异位词分组 (Group Anagrams)
# @Author: 2464512446@qq.com
# @Date: 2020-11-11 12:21:16
# @Runtime: 68 ms
# @Memory: 18.1 MB

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for i in strs:
            count = [0] * 26
            for c in i:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(i)
        # print(res)
        return list(res.values())
