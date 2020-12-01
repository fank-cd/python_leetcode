
# @Title: 二叉搜索树的最近公共祖先 (二叉搜索树的最近公共祖先 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-11-09 16:45:48
# @Runtime: 80 ms
# @Memory: 17.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val > q.val:
            p, q = q, p
        while root:
            if p.val > root.val:
                root =  root.right
            elif q.val < root.val:
                root = root.left
            else:
                break
        return root
