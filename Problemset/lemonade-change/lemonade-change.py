
# @Title: 柠檬水找零 (Lemonade Change)
# @Author: 2464512446@qq.com
# @Date: 2020-11-16 16:25:07
# @Runtime: 144 ms
# @Memory: 13.9 MB

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        ten,five = 0, 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10:
                if not five:
                    return False
                    print(22)
                five -= 1
                ten += 1
            elif i == 20:
                if ten and five :
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    print(333)
                    return False

        return True

