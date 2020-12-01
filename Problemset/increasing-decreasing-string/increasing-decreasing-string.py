
# @Title: 上升下降字符串 (Increasing Decreasing String)
# @Author: 2464512446@qq.com
# @Date: 2020-11-25 10:09:36
# @Runtime: 64 ms
# @Memory: 13.6 MB

class Solution:
    def sortString(self, s: str) -> str:
        count = [0] *26
        for i in s:
            count[ord(i)- ord('a')] += 1
        res = []
        while len(res) < len(s):
            for i in range(26):
                if count[i]:
                    res.append(chr(i+ord('a')))
                    count[i] -= 1
            for i in range(25,-1,-1):
                if count[i]:
                    res.append(chr(i+ord('a')))
                    count[i] -= 1
        return "".join(res)
