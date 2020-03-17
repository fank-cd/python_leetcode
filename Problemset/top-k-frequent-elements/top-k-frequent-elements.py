
# @Title: 前 K 个高频元素 (Top K Frequent Elements)
# @Author: 2464512446@qq.com
# @Date: 2019-12-12 10:53:25
# @Runtime: 112 ms
# @Memory: 15.3 MB

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        # d = {}
        # for i in nums:
        #     if i not in d:
        #         d[i] = 0
        #     d[i] +=1
        # res = []

        result = Counter(nums).most_common(k)
        # print(result)
        res = []
        for k,v in result:
            res.append(k)
        return res

