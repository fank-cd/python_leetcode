
# @Title: 合并两个有序数组 (Merge Sorted Array)
# @Author: 2464512446@qq.com
# @Date: 2019-11-12 11:09:40
# @Runtime: 28 ms
# @Memory: 11.7 MB

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        p,q,i = m-1,n-1,m+n-1
        while p >=0 and q >=0:
            if nums1[p] < nums2[q]:
                nums1[i] = nums2[q]
                i -=1
                q -=1
            else:
                nums1[i] = nums1[p]
                i -=1
                p -=1
        
        nums1[:q + 1] = nums2[:q + 1]

