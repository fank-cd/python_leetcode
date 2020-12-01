
# @Title: 求根到叶子节点数字之和 (Sum Root to Leaf Numbers)
# @Author: 2464512446@qq.com
# @Date: 2020-10-29 00:49:03
# @Runtime: 36 ms
# @Memory: 13.6 MB

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(root,prev):
            if not root:
                return 0
            total = prev * 10 + root.val
            if not root.left and not root.right:
                return total
            else:
                return helper(root.left,total) + helper(root.right,total)
        return helper(root,0)
