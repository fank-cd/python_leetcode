
# @Title: 删除排序数组中的重复项 (Remove Duplicates from Sorted Array)
# @Author: 2464512446@qq.com
# @Date: 2019-11-11 14:53:28
# @Runtime: 68 ms
# @Memory: 13.8 MB

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        for j in range(1,len(nums)):
            if nums[j] !=nums[i]:
                i +=1
                nums[i] = nums[j]
                
        return i +1
        

#     if (nums.length == 0) return 0;
#     int i = 0;
#     for (int j = 1; j < nums.length; j++) {
#         if (nums[j] != nums[i]) {
#             i++;
#             nums[i] = nums[j];
#         }
#     }
#     return i + 1;
# }


