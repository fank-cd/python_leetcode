
| [English](README_EN.md) | 简体中文 |

# [94. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)

## 题目描述

<p>给定一个二叉树的根节点 <code>root</code> ，返回它的 <strong>中序</strong> 遍历。</p>

<p> </p>

<p><strong>示例 1：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_1.jpg" style="width: 202px; height: 324px;" />
<pre>
<strong>输入：</strong>root = [1,null,2,3]
<strong>输出：</strong>[1,3,2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = []
<strong>输出：</strong>[]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>root = [1]
<strong>输出：</strong>[1]
</pre>

<p><strong>示例 4：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_5.jpg" style="width: 202px; height: 202px;" />
<pre>
<strong>输入：</strong>root = [1,2]
<strong>输出：</strong>[2,1]
</pre>

<p><strong>示例 5：</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/15/inorder_4.jpg" style="width: 202px; height: 202px;" />
<pre>
<strong>输入：</strong>root = [1,null,2]
<strong>输出：</strong>[1,2]
</pre>

<p> </p>

<p><strong>提示：</strong></p>

<ul>
	<li>树中节点数目在范围 <code>[0, 100]</code> 内</li>
	<li><code>-100 <= Node.val <= 100</code></li>
</ul>

<p> </p>

<p><strong>进阶:</strong> 递归算法很简单，你可以通过迭代算法完成吗？</p>


## 相关话题

- [栈](https://leetcode-cn.com/tag/stack)
- [树](https://leetcode-cn.com/tag/tree)
- [哈希表](https://leetcode-cn.com/tag/hash-table)

## 相似题目

- [验证二叉搜索树](../validate-binary-search-tree/README.md)
- [二叉树的前序遍历](../binary-tree-preorder-traversal/README.md)
- [二叉树的后序遍历](../binary-tree-postorder-traversal/README.md)
- [二叉搜索树迭代器](../binary-search-tree-iterator/README.md)
- [二叉搜索树中第K小的元素](../kth-smallest-element-in-a-bst/README.md)
- [最接近的二叉搜索树值 II](../closest-binary-search-tree-value-ii/README.md)
- [二叉搜索树中的顺序后继](../inorder-successor-in-bst/README.md)
- [将二叉搜索树转化为排序的双向链表](../convert-binary-search-tree-to-sorted-doubly-linked-list/README.md)
- [二叉搜索树节点最小距离](../minimum-distance-between-bst-nodes/README.md)
