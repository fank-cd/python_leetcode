
# @Title: 栈的压入、弹出序列 (栈的压入、弹出序列 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-06-18 17:06:42
# @Runtime: 48 ms
# @Memory: 13.5 MB

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        helper = []
        i = 0

        for num in pushed:
            helper.append(num)
            while helper and helper[-1] == popped[i]:
                helper.pop()
                i += 1

       #  print(helper)
        return not helper
