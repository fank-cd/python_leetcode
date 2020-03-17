
# @Title: 二叉树的最近公共祖先 (Lowest Common Ancestor of a Binary Tree)
# @Author: 2464512446@qq.com
# @Date: 2019-12-12 12:28:21
# @Runtime: 60 ms
# @Memory: 26.2 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def recurse_tree(current_node):
            if not current_node:
                return False
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)
            mid = current_node == p or current_node == q
            if mid + left + right >= 2:
                self.ans = current_node
            return mid or left or right
        recurse_tree(root)
        return self.ans


