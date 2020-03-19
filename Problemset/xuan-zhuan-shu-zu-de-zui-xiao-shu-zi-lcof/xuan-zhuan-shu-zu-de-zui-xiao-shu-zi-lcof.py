
# @Title: 旋转数组的最小数字 (旋转数组的最小数字  LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-03-19 18:04:54
# @Runtime: 56 ms
# @Memory: 13.6 MB

class Solution:
    def minArray(self, numbers: List[int]) -> int:
        low,high = 0,len(numbers)-1


        while low<high:
            mid = (low+high) //2
            if numbers[mid] > numbers[high]:
                low = mid + 1 
            elif numbers[mid] < numbers[high]:
                high = mid
            else:
                high = high -1


        return numbers[low]
