
# @Title: 自除数 (Self Dividing Numbers)
# @Author: 2464512446@qq.com
# @Date: 2019-09-28 17:14:52
# @Runtime: 28 ms
# @Memory: 11.6 MB

class Solution(object):
    def selfDividingNumbers(self, left, right):
        ans = []
        for num in range(left,right + 1):
            copy = num
            while copy > 0:
                div, copy = copy % 10, copy // 10
                if div == 0 or num % div != 0: break
            else: ans.append(num) # while … else 在循环条件为 false 时执行 else 语句块
        return ans


