
# @Title: 矩形重叠 (Rectangle Overlap)
# @Author: 2464512446@qq.com
# @Date: 2020-03-18 17:34:40
# @Runtime: 32 ms
# @Memory: 13.3 MB

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        return not (rec1[2] <= rec2[0] or  # left
                    rec1[3] <= rec2[1] or  # bottom
                    rec1[0] >= rec2[2] or  # right
                    rec1[1] >= rec2[3])    # top
