
# @Title: 划分字母区间 (Partition Labels)
# @Author: 2464512446@qq.com
# @Date: 2020-10-22 10:36:03
# @Runtime: 48 ms
# @Memory: 13.5 MB

class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = [0] * 26
        for i,ch in enumerate(S):
            last[ord(ch)-ord('a')] = i
        
        res = []
        start,end = 0, 0
        for i, ch in enumerate(S):
            end = max(end,last[ord(ch)-ord('a')])
            if i == end:
                res.append(end- start + 1)
                start = end + 1
        return res
