
# @Title: 最小的k个数 (最小的k个数  LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-12-28 12:13:53
# @Runtime: 60 ms
# @Memory: 16.5 MB

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if not k :
            return []
        hp = [-i for i in arr[:k]]
        
        heapq.heapify(hp)
        # print(hp[0])
        for i in arr[k:]:
            if -i > hp[0]:
                heapq.heapreplace(hp,-i)
        # print(hp)
        return [-i for i in hp]
