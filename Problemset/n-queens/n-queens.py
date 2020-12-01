
# @Title: N 皇后 (N-Queens)
# @Author: 2464512446@qq.com
# @Date: 2020-10-12 12:21:00
# @Runtime: 76 ms
# @Memory: 13.7 MB

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        visited_col = set()
        visited_pie = set()
        visited_na = set()

        res = []
        path = [["."] * n for i in range(n)]
        
        def valid(row, col):
            if (col+ row) not in visited_pie and (col-row) not in visited_na and col not in visited_col:
                return True
            return False
        
        def put_queen(row,col):
            visited_col.add(col)
            visited_na.add(col-row)
            visited_pie.add(col + row)
            path[row][col] = "Q"
        
        def remove_queen(row, col):
            visited_col.remove(col)
            visited_na.remove(col-row)
            visited_pie.remove(col + row)
            path[row][col] = "."

        def add_res(path):
            temp = []
            for i in path:
                temp.append("".join(i))
            return temp
        def helper(row,path):
            if row == n:
                res.append(add_res(path))
            for col in range(n):
                if valid(row,col):
                    put_queen(row, col)
                    helper(row + 1,path)
                    remove_queen(row, col)
        helper(0, path)

        return res
