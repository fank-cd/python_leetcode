
-- @Title: 超过5名学生的课 (Classes More Than 5 Students)
-- @Author: 2464512446@qq.com
-- @Date: 2019-03-15 11:44:38
-- @Runtime: 310 ms
-- @Memory: N/A

# Write your MySQL query statement below
select class
from courses
group by class
having count(distinct student) >= 5
