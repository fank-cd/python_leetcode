
# @Title: 到家的最少跳跃次数 (Minimum Jumps to Reach Home)
# @Author: 2464512446@qq.com
# @Date: 2020-11-15 00:22:14
# @Runtime: 264 ms
# @Memory: 15 MB

class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        queue = deque()
        queue.append((0,0,True))
        visited = set()
        visited.add((0,True))
        
        while queue:
            for i in range(len(queue)):
                cur_index,step,can = queue.popleft()
                if cur_index == x:
                    return step
                if (cur_index) < 4999 and (cur_index+a) not in forbidden and (cur_index+a,True) not in visited:
                    queue.append((cur_index+a,step+1,True))
                    visited.add((cur_index+a,True))
                if can and (cur_index-b) >= 0 and (cur_index-b) not in forbidden and (cur_index-b,False) not in visited:
                    queue.append((cur_index-b,step+1,False))
                    visited.add((cur_index-b,False))
            # print(queue)
        return -1
