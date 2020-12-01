
# @Title: 最小的k个数 (最小的k个数  LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-11-25 17:52:27
# @Runtime: 64 ms
# @Memory: 15.2 MB

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not k:
            return []
        heap = [-i for i in arr[:k]]
        heapq.heapify(heap)
        for i in arr[k:]:
            if -i > heap[0]:
                heapq.heapreplace(heap,-i)

        return [-i for i in heap]
