
# @Title: 叶子相似的树 (Leaf-Similar Trees)
# @Author: 2464512446@qq.com
# @Date: 2020-10-21 12:02:09
# @Runtime: 32 ms
# @Memory: 13.7 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def helper(root,stack):
            if not root:
                return 
            helper(root.left,stack)
            if not root.left and not root.right:
                stack.append(root.val)
            helper(root.right,stack)
            return stack
        
        return helper(root1,[])== helper(root2,[])
