
# @Title: 单值二叉树 (Univalued Binary Tree)
# @Author: 2464512446@qq.com
# @Date: 2019-10-14 17:08:17
# @Runtime: 24 ms
# @Memory: 11.4 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def isUnivalTree(self, root):
        left_correct = (not root.left or root.val == root.left.val
                and self.isUnivalTree(root.left))
        right_correct = (not root.right or root.val == root.right.val
                and self.isUnivalTree(root.right))
        return left_correct and right_correct


# class Solution(object):
#     def isUnivalTree(self, root):
#         vals = []

#         def dfs(node):
#             if node:
#                 vals.append(node.val)
#                 dfs(node.left)
#                 dfs(node.right)

#         dfs(root)
#         return len(set(vals)) == 1
