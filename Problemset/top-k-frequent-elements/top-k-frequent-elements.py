
# @Title: 前 K 个高频元素 (Top K Frequent Elements)
# @Author: 2464512446@qq.com
# @Date: 2020-11-25 17:56:00
# @Runtime: 48 ms
# @Memory: 16.4 MB

class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """ 
        d = Counter(nums)
        heap = []
        res = []
        for i in d:
            heapq.heappush(heap,(-d[i],i))
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
s).most_common(k)
        # print(result)
        res = []
        for k,v in result:
            res.append(k)
        return res

