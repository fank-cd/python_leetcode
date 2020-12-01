
# @Title: 两个数组的交集 II (Intersection of Two Arrays II)
# @Author: 2464512446@qq.com
# @Date: 2020-07-13 18:17:28
# @Runtime: 56 ms
# @Memory: 13.4 MB

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if not nums2 or not nums1:
            return []
        res = []
        d = {}
        if len(nums1) > len(nums2):
            short_num = nums2
            long_num = nums1
        else:
            short_num = nums1
            long_num = nums2
        for i in short_num:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        
        for i in long_num:
            if i in d and d[i]!=0:
                res.append(i)
                d[i] -= 1
        return res

