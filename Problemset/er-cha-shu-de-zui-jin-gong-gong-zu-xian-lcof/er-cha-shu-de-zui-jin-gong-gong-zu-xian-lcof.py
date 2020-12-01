
# @Title: 二叉树的最近公共祖先 (二叉树的最近公共祖先 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-12-01 15:11:15
# @Runtime: 80 ms
# @Memory: 24 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root == q or root == p:
            return root
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)
        if not left:
            return right
        if not right:
            return left
        return root
