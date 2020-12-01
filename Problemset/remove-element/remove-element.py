
# @Title: 移除元素 (Remove Element)
# @Author: 2464512446@qq.com
# @Date: 2020-07-30 15:31:10
# @Runtime: 44 ms
# @Memory: 13.4 MB

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i 



