
# @Title: 寻找两个有序数组的中位数 (Median of Two Sorted Arrays)
# @Author: 2464512446@qq.com
# @Date: 2019-06-10 12:19:39
# @Runtime: 284 ms
# @Memory: 12.1 MB

#
# @lc app=leetcode.cn id=4 lang=python
#
# [4] 寻找两个有序数组的中位数
#
class Solution(object):
    
    def merge(self,left,right):
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0))

        return result

    def mergeSort(self,relist):
        if len(relist) <= 1:
            return relist
        mid_index = len(relist)/2
        left = self.mergeSort(relist[:mid_index])  # 递归拆解的过程
        right = self.mergeSort(relist[mid_index:])
        return self.merge(left, right)  # 合并的过程


    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        result = self.mergeSort(nums1+nums2)
        mid_index = len(result)//2
        if len(result) %2 == 0:
            # print(float((result[mid_index])+result[mid_index-1])/2)
            return float((result[mid_index])+result[mid_index-1])/2
        else:
            return result[mid_index]




