
# @Title: 平衡二叉树 (平衡二叉树 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-10-11 18:33:07
# @Runtime: 56 ms
# @Memory: 18.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(root):
            if not root:
                return 0
            left = helper(root.left)
            if left == -1:
                return -1
            right = helper(root.right)
            if right == -1 :
                return -1
            return max(left,right) + 1 if abs(left-right)<=1 else -1
        return helper(root) != -1
