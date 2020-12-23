
# @Title: 二叉树的最近公共祖先 (Lowest Common Ancestor of a Binary Tree)
# @Author: 2464512446@qq.com
# @Date: 2020-08-01 17:16:01
# @Runtime: 108 ms
# @Memory: 23.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if not left:
            return right
        if not right:
            return left
        
        return root
= current_node == p or current_node == q
            if mid + left + right >= 2:
                self.ans = current_node
            return mid or left or right
        recurse_tree(root)
        return self.ans


