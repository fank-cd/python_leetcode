
# @Title: 四数相加 II (4Sum II)
# @Author: 2464512446@qq.com
# @Date: 2019-12-17 11:49:45
# @Runtime: 256 ms
# @Memory: 34.2 MB

class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        count = 0
        ab_map = dict()
        
        for a in A:
            for b in B:
                ab_map[a + b] = ab_map.get(a + b, 0) + 1
            
        for c in C:
            for d in D:
                s = -(c + d)
                if s in ab_map:
                    count += ab_map[s]
        
        return count
