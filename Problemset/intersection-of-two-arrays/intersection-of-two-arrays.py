
# @Title: 两个数组的交集 (Intersection of Two Arrays)
# @Author: 2464512446@qq.com
# @Date: 2020-11-02 11:38:20
# @Runtime: 76 ms
# @Memory: 13.7 MB

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums1) & set(nums2)
        return list(s)
