
# @Title: 对称的二叉树 (对称的二叉树  LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-06-18 10:36:41
# @Runtime: 44 ms
# @Memory: 13.4 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def helper(left_node,right_node):

            if not left_node and not right_node:
                return True
            elif not left_node or not right_node:
                # print(left_node.val,right_node.val)
                return False
            
            if left_node and right_node:
                return left_node.val == right_node.val and helper(left_node.left,right_node.right) \
                and helper(left_node.right,right_node.left)

        if not root:
            return True
        return helper(root.left,root.right)


