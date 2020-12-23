
# @Title: 柱状图中最大的矩形 (Largest Rectangle in Histogram)
# @Author: 2464512446@qq.com
# @Date: 2020-11-16 15:33:30
# @Runtime: 64 ms
# @Memory: 15.4 MB

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        heights = [0] + heights + [0]
        stack = [0]
        size = len(heights)
        for i in range(1,size):
            while heights[stack[-1]] > heights[i]:
                cur_height = heights[stack.pop()]
                cur_width = i - stack[-1] -1
                res = max(res,cur_height*cur_width)
            stack.append(i)
        return res


eight*cur_width,res)
            stack.append(i)

        return res

