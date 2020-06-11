
# @Title: 正则表达式匹配 (正则表达式匹配 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-05-25 17:48:15
# @Runtime: 68 ms
# @Memory: 13.5 MB

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m = len(s),len(p)
        # print(n,m)
        f = [[False for i in range(m+1)] for j in range(n+1)]
        # print(f)
        for i in range(n+1):
            for j in range(m+1):
        
                if j == 0:
                    # print(i,j,f[i][j])
                    if i == 0:
                        f[i][j] = True
                    else:
                        f[i][j] = False
                else:
                    if p[j-1] != "*":
                        if i >0 and (s[i-1] == p[j-1] or p[j-1]== "."):
                            f[i][j] = f[i-1][j-1]
                    else:
                        if j >= 2:
                            f[i][j] =f[i][j] or f[i][j-2]
                        if i >= 1 and j>= 2 and(s[i-1]==p[j-2] or p[j-2]== "."):
                            f[i][j] = f[i][j] or f[i-1][j]
                            
        return f[n][m]

        # # print(s,p)
        # if len(s) == 0:
        #     if len(p) % 2 != 0:
        #         return False

        #     for i in range(1,len(p),2):
        #         if p[i] != "*":
        #             return False
        #     return True

        # if len(p) == 0: return False

        # c1,c2,c3 = s[0],p[0],'a'
        # if len(p) >1:
        #     c3 = p[1]

        # if c3 != "*":
        #     if c1 == c2 or c2 == ".":
        #         return self.isMatch(s[1:],p[1:])
        #     else:
        #         return False
        # else:
        #     if c1 == c2 or c2 == ".":
        #         return self.isMatch(s[1:],p) or self.isMatch(s,p[2:])
        #     else:
        #         return self.isMatch(s,p[2:])
