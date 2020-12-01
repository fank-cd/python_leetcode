
# @Title: 分糖果 II (Distribute Candies to People)
# @Author: 2464512446@qq.com
# @Date: 2020-03-05 10:35:35
# @Runtime: 32 ms
# @Memory: 11.5 MB

class Solution(object):
    def distributeCandies(self, candies, num_people):
        """
        :type candies: int
        :type num_people: int
        :rtype: List[int]
        """
        res = num_people *[0]
        remain_candies = candies
        give_candies = 1
        index = 0
        while remain_candies > give_candies:
            res[index] += give_candies
            remain_candies = remain_candies - give_candies
            give_candies +=1
            index +=1
            if index >= num_people:
                index = 0

        res[index] += remain_candies

        return res
