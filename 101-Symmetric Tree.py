# coding:utf-8

# 对称二叉树

# 给定一个二叉树，检查它是否是镜像对称的。
#
# 例如，二叉树 [1,2,2,3,4,4,3] 是对称的。
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
# 但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3
#
# 说明:
#
# 如果你可以运用递归和迭代两种方法解决这个问题，会很加分。
# 很简单的写法，更像是层次遍历，将待遍历的节点放进栈中，按照左右遍历。


# class Solution(object):
#     def isSymmetric(self, root):
#
#         # :type root: TreeNode
#         # :rtype: bool
#
#         if not root:
#             return True
#         stack_l, stack_r = [root.left], [root.right]
#
#         while stack_l and stack_r:
#             left = stack_l.pop()
#             right = stack_r.pop()
#
#             if not left and not right:
#                 continue
#             elif not left or not right:
#                 return False
#             elif left.val != right.val:
#                 return False
#             else:
#                 stack_l.append(left.left)
#                 stack_r.append(right.right)
#                 stack_l.append(left.right)
#                 stack_r.append(right.left)
#
#         if stack_l or stack_r:
#             return False
#         else:
#             return True
#

# 递归方法

class Solution(object):
    def isSymmetric(self, root):
        # :type root: TreeNode
        # :rtype: bool
        return self.isMirror(root,root)
    def isMirror(self,t1,t2):
        if not t1 and not t2: return True
        elif not t1 or not t2: return False
        return t1.val==t2.val and self.isMirror(t1.right,t2.left) and self.isMirror(t1.left,t2.right)
