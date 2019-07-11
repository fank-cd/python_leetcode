
# @Title: 寻找两个有序数组的中位数 (Median of Two Sorted Arrays)
# @Author: 2464512446@qq.com
# @Date: 2019-07-11 17:02:23
# @Runtime: 236 ms
# @Memory: 13.4 MB

class Solution(object):

    def merge(self, left, right):
        result = []
        while left and right:
            result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        while left:
            result.append(left.pop(0))
        while right:
            result.append(right.pop(0))

        return result

    def mergeSort(self, relist):
        if len(relist) <= 1:
            return relist
        mid_index = len(relist) // 2
        left = self.mergeSort(relist[:mid_index])  # 递归拆解的过程
        right = self.mergeSort(relist[mid_index:])
        return self.merge(left, right)  # 合并的过程

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        基本思想是利用递归思想将两个数组再次合并成有序数组后再求中位数
        实际发现不用mergeSort，直接调用merge速度也差不多，这种写法非常慢，有调整的空间
        """

        result = self.mergeSort(nums1 + nums2)
        mid_index = len(result) // 2
        if len(result) % 2 == 0:
            print((result[mid_index] + result[mid_index - 1]) / 2)
            return (result[mid_index] + result[mid_index - 1]) / 2
        else:
            return result[mid_index]




