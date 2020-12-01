
# @Title: 最接近原点的 K 个点 (K Closest Points to Origin)
# @Author: 2464512446@qq.com
# @Date: 2020-11-09 15:25:21
# @Runtime: 804 ms
# @Memory: 19.1 MB

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = [(-x ** 2 -y ** 2,i) for i, (x,y) in enumerate(points[:K])]
        heapq.heapify(heap)
        size = len(points)
        for i in range(K,size):
            x,y =  points[i]
            distance = -x ** 2 - y ** 2
            if distance > heap[0][0]:
                heapq.heapreplace(heap,(distance,i))
        res = []
        for _,i in heap:
            res.append(points[i])
        return res
