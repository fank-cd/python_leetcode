
# @Title: 打印从1到最大的n位数 (打印从1到最大的n位数 LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-05-11 17:16:41
# @Runtime: 44 ms
# @Memory: 18.8 MB

class Solution:
    def printNumbers(self, n: int) -> List[int]:

        return list(range(1, 10**n)) if n > 0 else []

        # 脱了裤子放屁写法
        # res = []
        # if n < 0:
        #     return []
        # for i in range(1,pow(10,n)):
        #     res.append(i)

        # return res
