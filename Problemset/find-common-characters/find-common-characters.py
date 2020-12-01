
# @Title: 查找常用字符 (Find Common Characters)
# @Author: 2464512446@qq.com
# @Date: 2020-10-14 11:57:31
# @Runtime: 56 ms
# @Memory: 13.6 MB

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        from collections import Counter
        ans = Counter(A[0])
        for i in A[1:]:
            ans &= Counter(i)
        return list(ans.elements())


