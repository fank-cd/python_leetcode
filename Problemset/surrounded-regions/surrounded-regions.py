
# @Title: 被围绕的区域 (Surrounded Regions)
# @Author: 2464512446@qq.com
# @Date: 2020-11-24 16:39:42
# @Runtime: 276 ms
# @Memory: 15.4 MB

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return board
        row, col = len(board), len(board[0])
        dummy  = row * col + 1
        p = [i for i in range(dummy+1)]

        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    if i == 0 or i == row - 1 or j == 0 or j == col - 1:
                        self.union(p, i * col + j, dummy)
                    else:
                        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            if board[i + x][j + y] == "O":
                                self.union(p,i * col + j, (i + x) * col + (j + y))

        for i in range(row):
            for j in range(col):
                if self.parent(p,i*col + j) == self.parent(p,dummy):
                    board[i][j] = "O"
                else:
                    board[i][j] = "X"

    def union(self,p, i, j):
        p1 = self.parent(p, i)
        p2 = self.parent(p, j)
        p[p1] = p2
    
    def parent(self,p,i ):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            x = i
            i = p[i]
            p[x] = root
        return root

