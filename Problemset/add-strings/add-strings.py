
# @Title: 字符串相加 (Add Strings)
# @Author: 2464512446@qq.com
# @Date: 2020-08-03 17:18:02
# @Runtime: 56 ms
# @Memory: 13.5 MB

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = ""
        i,j =len(num1) -1,len(num2)-1
        carry = 0
        while i>=0 or j>=0:
            n1 = int(num1[i]) if i >=0 else 0
            n2 = int(num2[j]) if j >=0 else 0
            tmp = n1 + n2 + carry

            carry = tmp // 10
            res = str(tmp%10) + res
            i, j = i - 1, j - 1

        return "1" + res if carry else res
