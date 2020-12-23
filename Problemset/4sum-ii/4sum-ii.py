
# @Title: 四数相加 II (4Sum II)
# @Author: 2464512446@qq.com
# @Date: 2020-11-27 09:54:12
# @Runtime: 276 ms
# @Memory: 33.9 MB

class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        count = 0
        map_d = {}
        for a in A:
            for b in B:
                map_d[a+b] = map_d.get(a+b,0) + 1
        for c in C:
            for d in D:
                temp = - (c+d)
                if temp in map_d:
                    count += map_d[temp]
        return count
        for d in D:
                s = -(c + d)
                if s in ab_map:
                    count += ab_map[s]
        
        return count
