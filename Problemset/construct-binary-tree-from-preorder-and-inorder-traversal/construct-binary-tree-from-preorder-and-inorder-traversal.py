
# @Title: 从前序与中序遍历序列构造二叉树 (Construct Binary Tree from Preorder and Inorder Traversal)
# @Author: 2464512446@qq.com
# @Date: 2020-03-17 17:54:54
# @Runtime: 240 ms
# @Memory: 86.8 MB

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
ndex+1:])
        return root
