
# @Title: 平衡二叉树 (Balanced Binary Tree)
# @Author: 2464512446@qq.com
# @Date: 2020-10-11 18:37:56
# @Runtime: 44 ms
# @Memory: 18.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            if left == - 1:
                return - 1
            right = helper(root.right)
            if right == - 1:
                return - 1
            return max(left,right) + 1 if abs(left-right) <= 1 else - 1
        return helper(root) != -1
