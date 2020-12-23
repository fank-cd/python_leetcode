
# @Title: 将有序数组转换为二叉搜索树 (Convert Sorted Array to Binary Search Tree)
# @Author: 2464512446@qq.com
# @Date: 2020-07-05 11:36:16
# @Runtime: 80 ms
# @Memory: 15.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        else:
            mid = len(nums)//2
            root_node = TreeNode(nums[mid])
            nums1 = nums[0:mid]
            nums2 = nums[mid+1:]
            root_node.left = self.sortedArrayToBST(nums1)
            root_node.right = self.sortedArrayToBST(nums2)

            return root_node
     root_node.right = self.sortedArrayToBST(nums2)

            return root_node
