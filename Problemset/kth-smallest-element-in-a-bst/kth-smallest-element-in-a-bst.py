
# @Title: 二叉搜索树中第K小的元素 (Kth Smallest Element in a BST)
# @Author: 2464512446@qq.com
# @Date: 2019-12-02 16:25:15
# @Runtime: 44 ms
# @Memory: 19.2 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = [(root,False)]
        res = []
        count = 0
        while stack:
            curr,visited = stack.pop()
            if visited:
                count +=1
                if count == k:
                    return curr.val
            else:
                if curr.right:
                    stack.append((curr.right,False))
                stack.append((curr,True))
                if curr.left:
                    stack.append((curr.left,False))
                
