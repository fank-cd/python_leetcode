
# @Title: 树的子结构 (树的子结构  LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-06-11 16:19:11
# @Runtime: 92 ms
# @Memory: 18.1 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubTree(self, A, B):
        if B==None:
            return True
        if A==None:
            return False
        if A.val != B.val:
            return False
        if A.val == B.val:
            return self.isSubTree(A.left, B.left) and self.isSubTree(A.right, B.right)
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B==None or A==None:
            return False
        return self.isSubTree(A, B) or self.isSubStructure(A.left, B) or self.isSubTree(A.right, B) 
