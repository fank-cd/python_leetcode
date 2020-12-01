
# @Title: 有序矩阵中第K小的元素 (Kth Smallest Element in a Sorted Matrix)
# @Author: 2464512446@qq.com
# @Date: 2020-07-02 16:10:43
# @Runtime: 252 ms
# @Memory: 19.2 MB

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        pq = [(matrix[i][0], i, 0) for i in range(n)]
        heapq.heapify(pq)

        ret = 0
        for i in range(k - 1):
            num, x, y = heapq.heappop(pq)
            if y != n - 1:
                heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))
        
        return heapq.heappop(pq)[0]

