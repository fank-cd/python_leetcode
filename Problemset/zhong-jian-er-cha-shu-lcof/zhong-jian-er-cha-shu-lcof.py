
# @Title: 重建二叉树 (重建二叉树 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-04-20 17:56:57
# @Runtime: 244 ms
# @Memory: 89.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(preorder) == 0 or len(inorder)== 0:
            return None

        root = preorder[0]
        root_index=  inorder.index(root)
        root = TreeNode(root)
        root.left = self.buildTree(preorder=preorder[1:root_index+1],inorder=inorder[:root_index])
        root.right = self.buildTree(preorder=preorder[root_index+1:],inorder=inorder[root_index+1:])
        return root
