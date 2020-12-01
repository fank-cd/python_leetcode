
# @Title: 二叉树的最小深度 (Minimum Depth of Binary Tree)
# @Author: 2464512446@qq.com
# @Date: 2020-11-16 16:48:33
# @Runtime: 528 ms
# @Memory: 49.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        stack =[(root,1)]
        while stack:
            node,level = stack.pop(0)
            if not node.left and not node.right:
                return level
            if node.left:
                stack.append((node.left,level+1))
            if node.right:
                stack.append((node.right,level+1))
