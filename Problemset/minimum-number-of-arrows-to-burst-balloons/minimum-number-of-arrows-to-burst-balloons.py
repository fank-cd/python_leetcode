
# @Title: 用最少数量的箭引爆气球 (Minimum Number of Arrows to Burst Balloons)
# @Author: 2464512446@qq.com
# @Date: 2020-11-23 10:45:37
# @Runtime: 136 ms
# @Memory: 16.6 MB

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        count = 0
        l = []
        points.sort(key=lambda x:x[0])
        for i in points:
            if not l or l[-1][1] < i[0]:
                l.append(i)
                count += 1
            else:
                l[-1][0] = max(l[-1][0],i[0])
                l[-1][1] = min(l[-1][1],i[1]) 
        return count
