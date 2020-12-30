
# @Title: 最后一块石头的重量 (Last Stone Weight)
# @Author: 2464512446@qq.com
# @Date: 2020-12-30 11:39:31
# @Runtime: 40 ms
# @Memory: 14.8 MB

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = [-i for i in stones]
        heapq.heapify(hp)
        while len(hp) >= 2:
            first = heapq.heappop(hp)
            second = heapq.heappop(hp)
            res =  first-second
            if res:
                heapq.heappush(hp,res)
        
        return -hp[0] if hp else 0


