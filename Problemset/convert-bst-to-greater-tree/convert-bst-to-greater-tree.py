
# @Title: 把二叉搜索树转换为累加树 (Convert BST to Greater Tree)
# @Author: 2464512446@qq.com
# @Date: 2020-03-05 12:13:02
# @Runtime: 64 ms
# @Memory: 15.8 MB

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rdl(self, root, preans = 0):
        if root is None:
            return preans #遍历到底，将累加和返回出去，方便上一级累加
        
        root.val += self.rdl(root.right, preans) # 每一层的节点将右子树的累加和加进来
        return self.rdl(root.left, root.val) #左子树最终的累加和就是这个子树的全部累加和
            
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.rdl(root) #累加和起始状态为0
        return root
