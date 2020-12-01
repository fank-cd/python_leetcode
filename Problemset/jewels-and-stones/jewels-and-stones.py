
# @Title: 宝石与石头 (Jewels and Stones)
# @Author: 2464512446@qq.com
# @Date: 2020-10-02 20:38:40
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        d = Counter(S)
        res = 0
        for i in J:
            res += d[i]
        return res
