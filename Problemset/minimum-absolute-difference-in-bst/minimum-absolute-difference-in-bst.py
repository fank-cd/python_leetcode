
# @Title: 二叉搜索树的最小绝对差 (Minimum Absolute Difference in BST)
# @Author: 2464512446@qq.com
# @Date: 2020-10-12 10:20:22
# @Runtime: 64 ms
# @Memory: 15.6 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        res = math.inf
        pre = - 1
        def helper(root):
            nonlocal res
            nonlocal pre
            if not root:
                return 
            # print(root.val,pre)
            helper(root.left)
            
            if pre == - 1:
                pre = root.val
            else:
                res = min(res,root.val - pre)
                pre = root.val
            helper(root.right)

        helper(root)
        return res
