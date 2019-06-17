
# @Title: 相同的树 (Same Tree)
# @Author: 2464512446@qq.com
# @Date: 2019-01-16 11:37:44
# @Runtime: 28 ms
# @Memory: 7.1 MB

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def same(self,p,q):
        if not q and not p:
            return True
        elif not q or not p:
            return False
        elif p.val == q.val:
            return self.same(p.left,q.left) and self.same(p.right,q.right)

        return False
    
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        return self.same(p,q)
    

