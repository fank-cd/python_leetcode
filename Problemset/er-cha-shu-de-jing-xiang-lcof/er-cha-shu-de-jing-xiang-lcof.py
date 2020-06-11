
# @Title: 二叉树的镜像 (二叉树的镜像  LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-06-11 16:49:31
# @Runtime: 36 ms
# @Memory: 13.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root: 
            return
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root


        # if not root:
        #     return None
        # root.right,root.left = root.left,root.right

        # self.mirrorTree(root.left)
        # self.mirrorTree(root.right)

        # return root
