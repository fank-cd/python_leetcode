
# @Title: 二叉树的锯齿形层序遍历 (Binary Tree Zigzag Level Order Traversal)
# @Author: 2464512446@qq.com
# @Date: 2020-12-22 09:46:44
# @Runtime: 44 ms
# @Memory: 14.9 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        if not root:
            return res
        stack = [root]
        index = True
        while stack:
            level = []
            index = not index
            for i in range(len(stack)):
                root = stack.pop(0)
                level.append(root.val)
                if root.left:
                    stack.append(root.left)
                if root.right:
                    stack.append(root.right)
            if index:
                res.append(level[::-1])
            else:
                res.append(level)
        return res
