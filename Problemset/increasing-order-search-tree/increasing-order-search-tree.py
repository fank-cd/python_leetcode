
# @Title: 递增顺序查找树 (Increasing Order Search Tree)
# @Author: 2464512446@qq.com
# @Date: 2020-12-23 15:06:39
# @Runtime: 44 ms
# @Memory: 14.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode(None)
        self.pre = dummy
        def helper(root):
            if not root:
                return 
            helper(root.left)
            root.left = None
            self.pre.right = root
            self.pre = root
            helper(root.right)
        helper(root)
        return dummy.right
