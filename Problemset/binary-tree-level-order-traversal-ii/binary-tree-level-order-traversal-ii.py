
# @Title: 二叉树的层次遍历 II (Binary Tree Level Order Traversal II)
# @Author: 2464512446@qq.com
# @Date: 2019-06-26 10:42:41
# @Runtime: 56 ms
# @Memory: 13.4 MB

#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = [root]
        res = []
        while queue:
            next_queue = []
            layer = []
            for node in queue:
                if node:
                    layer.append(node.val)
                    next_queue += [node.left, node.right]
            queue = next_queue[:]
            if layer:
                res.append(layer[:])
        return res[::-1]

