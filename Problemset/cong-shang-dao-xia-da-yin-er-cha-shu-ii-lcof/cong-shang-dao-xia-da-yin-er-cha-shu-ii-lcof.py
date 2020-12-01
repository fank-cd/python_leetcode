
# @Title: 从上到下打印二叉树 II (从上到下打印二叉树 II LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-06-18 18:39:01
# @Runtime: 64 ms
# @Memory: 13.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []

        res = []
        helper = [root]
        temp = []

        next_level = []
        while helper or next_level:
            # print(next_level,helper)
            if not helper:
                helper = next_level
                next_level = []
            node = helper.pop(0)
            # print(node.val,helper)
            # print(node.val)
            temp.append(node.val)
            if not helper:
                res.append(temp)
                temp = []
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        return res
