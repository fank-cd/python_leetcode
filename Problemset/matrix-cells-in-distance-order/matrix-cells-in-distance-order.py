
# @Title: 距离顺序排列矩阵单元格 (Matrix Cells in Distance Order)
# @Author: 2464512446@qq.com
# @Date: 2020-11-17 00:58:00
# @Runtime: 180 ms
# @Memory: 16 MB

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = []
        for i in range(R):
            for j in range(C):
                distance = abs(j-c0) + abs(i-r0)
                res.append(([i,j],distance))
        res.sort(key=lambda x:x[1])
        return [i[0] for i in res]
