
# @Title: 复杂链表的复制 (复杂链表的复制  LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-06-30 18:13:51
# @Runtime: 44 ms
# @Memory: 13.9 MB

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# 解法1
# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         visited = {}
#         if not head: return head
#         clone = Node(head.val, None, None) # 创建新结点
#         # queue = collections.deque()
#         queue = []
#         queue.append(head)
#         visited[head] = clone
#         while queue:
#             tmp = queue.pop()
#             if tmp.next and tmp.next not in visited:
#                 visited[tmp.next] = Node(tmp.next.val, [], [])
#                 queue.append(tmp.next)  
#             if tmp.random and tmp.random not in visited:
#                 visited[tmp.random] = Node(tmp.random.val, [], [])
#                 queue.append(tmp.random)
#             visited[tmp].next = visited.get(tmp.next)
#             visited[tmp].random = visited.get(tmp.random)
#         return clone

# 解法2
# class Solution:
#     def copyRandomList(self, head: 'Node') -> 'Node':
#         visited = {}

#         def dfs(head):
#             if not head: return
#             if head in visited:
#                 return visited[head]

#             copy = Node(head.val)
#             visited[head]= copy
#             copy.next = dfs(head.next)
#             copy.random = dfs(head.random)
#             return copy
        
#         return dfs(head)

# 解法三
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        cur = head
        while cur: # 克隆新旧节点
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next
        cur = head
    
        while cur: # 连接random节点
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next

        cur_old = head
        cur_new = head.next
        new_head = head.next
        while cur_old:
            cur_old.next = cur_old.next.next
            cur_new.next = cur_new.next.next if cur_new.next else None
            cur_old = cur_old.next
            cur_new = cur_new.next
        
        return new_head
