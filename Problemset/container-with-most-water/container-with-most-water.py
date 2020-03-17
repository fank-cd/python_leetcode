
# @Title: 盛最多水的容器 (Container With Most Water)
# @Author: 2464512446@qq.com
# @Date: 2019-12-10 11:40:19
# @Runtime: 112 ms
# @Memory: 13 MB

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        p, q = 0, len(height)-1
        maxArea = 0
        while p < q:
            area = (q-p)*min(height[q],height[p])
            maxArea = area if area > maxArea else maxArea
            if height[q] > height[p]:
                p +=1
            else:
                q -=1

        return maxArea
