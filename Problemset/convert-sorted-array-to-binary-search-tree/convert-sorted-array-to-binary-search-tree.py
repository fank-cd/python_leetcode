
# @Title: 将有序数组转换为二叉搜索树 (Convert Sorted Array to Binary Search Tree)
# @Author: 2464512446@qq.com
# @Date: 2019-10-09 22:38:52
# @Runtime: 68 ms
# @Memory: 16.2 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        
        """
        if not nums:
            return None
        else:
            mid = len(nums)/2
            root_node = TreeNode(nums[mid])
            nums1 = nums[0:mid]
            nums2 = nums[mid+1:]
            root_node.left = self.sortedArrayToBST(nums1)
            root_node.right = self.sortedArrayToBST(nums2)

            return root_node
