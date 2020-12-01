
# @Title: 字符串的排列 (字符串的排列  LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-08-18 00:34:59
# @Runtime: 516 ms
# @Memory: 27.7 MB

class Solution:
    def permutation(self, s: str) -> List[str]:
        res = []
        def helper(index,path,visited):
            if index == len(s):
                res.append("".join(path))
                return 
            for i in range(len(s)):
                if i not in visited:
                    path.append(s[i])
                    visited.append(i)
                    helper(index+1,path,visited)
                    path.pop()
                    visited.pop()


        helper(0,[],[])
        return list(set(res)) 
