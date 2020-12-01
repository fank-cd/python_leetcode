
# @Title: 长按键入 (Long Pressed Name)
# @Author: 2464512446@qq.com
# @Date: 2020-10-21 10:47:25
# @Runtime: 40 ms
# @Memory: 13.4 MB

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        j = 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return i == len(name)




