
# @Title: 替换空格 (替换空格 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-07-21 14:50:20
# @Runtime: 40 ms
# @Memory: 13.3 MB

class Solution:
    def replaceSpace(self, s: str) -> str:
        # return s.replace(" ",'%20')

        # 这道题也可以用双指针法来解（感觉这才是题目用意）
        # p1 等于末尾，p2等于用多少个空格就加多少个占位符的末尾
        # 然后向前遍历
        res = []
        for c in s:
            if c == ' ': 
                res.append("%20")
            else: 
                res.append(c)
        return "".join(res)
