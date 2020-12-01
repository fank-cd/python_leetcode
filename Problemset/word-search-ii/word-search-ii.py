
# @Title: 单词搜索 II (Word Search II)
# @Author: 2464512446@qq.com
# @Date: 2020-11-27 10:47:41
# @Runtime: 36 ms
# @Memory: 13.3 MB

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0]:
            return 
        root = {}
        m,n = len(board),len(board[0])
        visited = set()
        res = []
        directions =  [(1, 0),(-1, 0),(0, 1),(0, -1)]

        for word in words:
            node = root
            for char in word:
                node = node.setdefault(char,{})
            node['#'] = '#'

        def dfs(i,j,cur_word,cur_dict,visited):
            cur_word += board[i][j]
            visited.add((i,j))
            if "#" in cur_dict:
                res.append(cur_word)
                del cur_dict['#']
            for x,y in directions:
                new_x, new_y = x + i ,y + j
                if 0 <= new_x < m and 0 <= new_y < n and (new_x,new_y) not in visited:
                    val = board[new_x][new_y]
                    if val in cur_dict:
                        dfs(new_x, new_y, cur_word,cur_dict[val],visited)
                        if not cur_dict[val]:
                            del cur_dict[val]
            visited.remove((i,j)) 
        for i in range(m):
            for j in range(n):
                if board[i][j] in root:
                    dfs(i,j,"",root[board[i][j]],visited)
                    if not root[board[i][j]]:
                        del root[board[i][j]]
        
        return res  
