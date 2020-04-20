
# @Title: 最小的k个数 (最小的k个数  LCOF)
# @Author: 2464512446@qq.com
# @Date: 2020-03-24 18:31:05
# @Runtime: 208 ms
# @Memory: 14.9 MB

# class Solution:
#     # def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#     #     return heapq.nsmallest(k,arr)
#     # 方法
#     def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
#         if k == 0:
#             return list()

#         hp = [-x for x in arr[:k]]
#         heapq.heapify(hp)
#         for i in range(k, len(arr)):
#             if -hp[0] > arr[i]:
#                 # heapq.heappop(hp)
#                 # heapq.heappush(hp, -arr[i])
#                 heapq.heapreplace(hp,-arr[i]) # 这样比弹出再pushpush更快
#         ans = [-x for x in hp]
#         return ans
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k >= len(arr): 
            return arr
        return self.select(arr, 0, len(arr)-1, k)[:k]
       
    def partition(self, nums, left, right): #一次排序
        # print(left, right)
        temp = nums[left]
        while left < right:
            while (left < right) and (nums[right] >= temp):
                right -= 1
            nums[left] = nums[right]
            while (left < right) and (nums[left] <= temp):
                left += 1
            nums[right] = nums[left]
        nums[left] = temp 
        return left  #left左边的数字比left小

    def select(self, nums, left, right, k):
        p = self.partition(nums, left, right)
        if p == k:
            return nums[:k]
        if p < k: #此元素在左边
            return self.select(nums, p+1, right, k)
        elif p >= k:
            return self.select(nums, left, p-1, k)
