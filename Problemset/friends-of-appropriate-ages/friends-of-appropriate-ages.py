
# @Title: 适龄的朋友 (Friends Of Appropriate Ages)
# @Author: 2464512446@qq.com
# @Date: 2020-12-23 15:29:22
# @Runtime: 224 ms
# @Memory: 15.4 MB

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0] *121
        for i in ages:
            count[i] += 1
        res = 0
        for ageA,countA in enumerate(count):
            for ageB,countB in enumerate(count):
                if 0.5 * ageA + 7 >= ageB:
                    continue
                if ageB > ageA:
                    continue
                if ageB > 100 and ageA < 100:
                    continue
                res += countA * countB
                if ageA == ageB:
                    res -= countA
        return res
