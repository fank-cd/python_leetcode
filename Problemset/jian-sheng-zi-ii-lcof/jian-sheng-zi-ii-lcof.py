
# @Title: 剪绳子 II (剪绳子 II LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-05-08 16:25:18
# @Runtime: 44 ms
# @Memory: 13.7 MB

class Solution:
    def cuttingRope(self, n: int) -> int:

        # 贪心法：当n大于等于5的时候，尽量去切3的段，
        # 当n还剩4的时候，去切成2 x 2 的段
        if not isinstance(n, int):
            return

        if n < 2:
            return 0

        if n == 2:
            return 1

        if n == 3:
            return 2

        times_of_3 = n // 3
        if (n - 3 * times_of_3) == 1:
            times_of_3 -= 1

        times_of_2 = (n - 3 * times_of_3) // 2
        # return (3 ** times_of_3) * (2 ** times_of_2) % 1000000007
        return pow(3,times_of_3) * pow(2,times_of_2) % 1000000007
