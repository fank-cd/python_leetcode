
# @Title: 插入区间 (Insert Interval)
# @Author: 2464512446@qq.com
# @Date: 2020-11-05 16:46:31
# @Runtime: 40 ms
# @Memory: 15 MB

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left,right  = newInterval
        res  =[]
        flag = False
        for li,ri in intervals:
            if ri < left:
                res.append([li,ri])
            elif li > right:
                if not flag:
                    res.append([left,right])
                    flag =  True
                res.append([li,ri])
            else:
                left = min(li,left)
                right = max(ri,right)
        
        if not flag:
            res.append([left,right])
        return res
