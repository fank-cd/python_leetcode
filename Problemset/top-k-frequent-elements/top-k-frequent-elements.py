
# @Title: 前 K 个高频元素 (Top K Frequent Elements)
# @Author: 2464512446@qq.com
# @Date: 2020-12-28 12:23:18
# @Runtime: 40 ms
# @Memory: 17.4 MB

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        d = Counter(nums)
        res = []
        hp = []
        for i in d:
            heapq.heappush(hp,(-d[i],i))
        for i in range(k):
            res.append(heapq.heappop(hp)[1])
        return res
