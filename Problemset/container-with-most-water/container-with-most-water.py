
# @Title: 盛最多水的容器 (Container With Most Water)
# @Author: 2464512446@qq.com
# @Date: 2020-11-20 16:46:22
# @Runtime: 88 ms
# @Memory: 15 MB

class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        p,q = 0, len(height)-1
        while p < q:
            area =  (q-p) * min(height[q],height[p])
            res = max(area,res)
            if height[p] > height[q]:
                q -= 1
            else:
                p += 1
        return  res
 height[p]:
                p +=1
            else:
                q -=1

        return maxArea
