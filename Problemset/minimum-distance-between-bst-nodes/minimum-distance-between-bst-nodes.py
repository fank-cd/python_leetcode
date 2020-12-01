
# @Title: 二叉搜索树节点最小距离 (Minimum Distance Between BST Nodes)
# @Author: 2464512446@qq.com
# @Date: 2020-11-27 16:15:35
# @Runtime: 40 ms
# @Memory: 13.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.pre = -math.inf
        self.res = math.inf

        def helper(root):
            if not root:
                return 
            helper(root.left)
            self.res = min(self.res,root.val-self.pre)
            self.pre = root.val
            helper(root.right)


        helper(root)
        return self.res
