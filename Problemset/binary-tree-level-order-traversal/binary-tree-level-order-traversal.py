
# @Title: 二叉树的层序遍历 (Binary Tree Level Order Traversal)
# @Author: 2464512446@qq.com
# @Date: 2020-11-23 16:40:09
# @Runtime: 40 ms
# @Memory: 13.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        res = []
        if not root:
            return res
        stack = [root]
        while stack:
            level = []
            for i in range(len(stack)):
                root = stack.pop(0)
                level.append(root.val)
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)
            res.append(level)
        return res
