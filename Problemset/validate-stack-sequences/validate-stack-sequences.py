
# @Title: 验证栈序列 (Validate Stack Sequences)
# @Author: 2464512446@qq.com
# @Date: 2020-06-18 17:11:12
# @Runtime: 112 ms
# @Memory: 13.4 MB

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        res = []
        i = 0

        for num in pushed:
            res.append(num)
            while res and res[-1] == popped[i]:
                res.pop()
                i += 1

        return not res
