
# @Title: 验证二叉搜索树 (Validate Binary Search Tree)
# @Author: 2464512446@qq.com
# @Date: 2020-11-27 11:07:26
# @Runtime: 76 ms
# @Memory: 15.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(left,right,root):
            if not root:
                return True
            if left < root.val < right:
                return helper(root.val,right,root.right) and helper(left,root.val,root.left)
            else:
                return False
        return helper(-math.inf, math.inf, root)
