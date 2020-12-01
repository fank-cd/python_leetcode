
# @Title: 访问所有点的最小时间 (Minimum Time Visiting All Points)
# @Author: 2464512446@qq.com
# @Date: 2019-12-17 10:16:27
# @Runtime: 48 ms
# @Memory: 11.5 MB

class Solution:
    def minTimeToVisitAllPoints(self, points):
        x0, x1 = points[0]
        ans = 0
        for i in range(1, len(points)):
            y0, y1 = points[i]
            ans += max(abs(x0 - y0), abs(x1 - y1))
            x0, x1 = points[i]
        return ans

