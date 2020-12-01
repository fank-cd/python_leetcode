
# @Title: 具有给定数值的最小字符串 (Smallest String With A Given Numeric Value)
# @Author: 2464512446@qq.com
# @Date: 2020-11-27 11:59:18
# @Runtime: 6092 ms
# @Memory: 15.2 MB

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        left = n
        count = 0
        res = ""
        while count < n:
            # start = min(k,26)
            for i in range(26,0,-1):
                # print(k,i<k,(k-i,left-1))
                if i <= k and k -i >= left -1:
                    temp = i
                    k = k - temp
                    res += chr(temp - 1 + ord('a'))
                    left -= 1
                    count += 1
                    # print(res)
                    break
        return res[::-1]
