
# @Title: 替换空格 (替换空格 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-03-17 14:50:44
# @Runtime: 44 ms
# @Memory: 13.5 MB

class Solution:
    def replaceSpace(self, s: str) -> str:
        # return s.replace(" ",'%20')

        res = []
        for c in s:
            if c == ' ': 
                res.append("%20")
            else: 
                res.append(c)
        return "".join(res)


