
# @Title: 两个数组的交集 II (Intersection of Two Arrays II)
# @Author: 2464512446@qq.com
# @Date: 2019-11-12 11:34:38
# @Runtime: 56 ms
# @Memory: 12 MB

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        inter = set(nums1) & set(nums2)
        l = []
        for i in inter:
            l += [i] * min(nums1.count(i), nums2.count(i))  
        return l
