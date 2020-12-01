
# @Title: 扫雷游戏 (Minesweeper)
# @Author: 2464512446@qq.com
# @Date: 2020-11-16 16:10:47
# @Runtime: 212 ms
# @Memory: 16 MB

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        direction = (
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (-1, 1), (-1, -1), (1, -1)
        )
        x,y = click
        if board[x][y] == "M":
            board[x][y] = "X"
            return board
        
        def check(x,y):
            count = 0
            for i,j in direction:
                new_x,new_y = x+i, y+j
                if 0<= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] == "M":
                    count += 1
            return count
        def dfs(x,y):
            count = check(x,y)
        
            if not count:
                board[x][y] = "B"
                for i,j in direction:
                    new_x,new_y = x+i, y+j
                    if 0<= new_x < len(board) and 0 <= new_y < len(board[0]) and board[new_x][new_y] == "E":
                        dfs(new_x,new_y)
                
            else:
                count = str(count)
                board[x][y] = count

        dfs(x,y)
        return board
