
# @Title: 把二叉搜索树转换为累加树 (Convert BST to Greater Tree)
# @Author: 2464512446@qq.com
# @Date: 2020-09-21 23:28:10
# @Runtime: 76 ms
# @Memory: 15.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:

        def dfs(root):
            nonlocal total
            if root:
                dfs(root.right)
                total += root.val
                root.val = total
                dfs(root.left)
        total = 0
        dfs(root)
        return root
