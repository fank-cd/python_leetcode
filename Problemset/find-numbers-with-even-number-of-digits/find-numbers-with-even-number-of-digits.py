
# @Title: 统计位数为偶数的数字 (Find Numbers with Even Number of Digits)
# @Author: 2464512446@qq.com
# @Date: 2020-01-03 11:59:50
# @Runtime: 64 ms
# @Memory: 12.4 MB

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in nums:
            if len(str(i)) % 2 == 0:
                count +=1

        return count
