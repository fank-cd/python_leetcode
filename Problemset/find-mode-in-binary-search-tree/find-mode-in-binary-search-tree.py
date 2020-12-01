
# @Title: 二叉搜索树中的众数 (Find Mode in Binary Search Tree)
# @Author: 2464512446@qq.com
# @Date: 2020-09-24 15:39:57
# @Runtime: 60 ms
# @Memory: 17.2 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:

        res,most,pre,count = [], 0, None, 0
        def helper(root):
            nonlocal res,most,pre,count
            if not root:
                return 
            helper(root.left)
            count = count + 1 if root.val == pre else 1
            if count ==most:
                res.append(root.val)
            if count > most:
                most = count
                res = [root.val]
            pre = root.val
            helper(root.right)

        helper(root)
        return res
