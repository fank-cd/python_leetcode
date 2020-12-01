
# @Title: 根据身高重建队列 (Queue Reconstruction by Height)
# @Author: 2464512446@qq.com
# @Date: 2020-11-16 11:39:35
# @Runtime: 116 ms
# @Memory: 14 MB

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]: 

        if len(people) <= 1:
            return people
        people = sorted(people, key = lambda x: (-x[0], x[1]))
        # print(people)
        # new_people = [people[0]]    # 这个人是从前往后、从上往下看到的第一个人
        new_people = []
        for i in people:
            new_people.insert(i[1], i)
        return new_people


