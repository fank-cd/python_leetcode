
# @Title: 二叉搜索树的最近公共祖先 (Lowest Common Ancestor of a Binary Search Tree)
# @Author: 2464512446@qq.com
# @Date: 2020-09-27 17:27:08
# @Runtime: 100 ms
# @Memory: 17.5 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p,q = q,p

        while root:
            if root.val > q.val:
                root = root.left
            elif root.val < p.val:
                root = root.right
            else:
                break
        return root
