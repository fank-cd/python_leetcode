
# @Title: 两个数组的交集 (Intersection of Two Arrays)
# @Author: 2464512446@qq.com
# @Date: 2019-10-14 14:43:41
# @Runtime: 36 ms
# @Memory: 11.9 MB

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        return set(nums1) & set(nums2)
