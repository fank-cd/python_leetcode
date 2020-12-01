
# @Title: 合并区间 (Merge Intervals)
# @Author: 2464512446@qq.com
# @Date: 2020-11-24 16:59:44
# @Runtime: 44 ms
# @Memory: 14.4 MB

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x:x[0])
        
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1],i[1])
        return res
