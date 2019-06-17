
-- @Title: 有趣的电影 (Not Boring Movies)
-- @Author: 2464512446@qq.com
-- @Date: 2019-03-06 11:49:02
-- @Runtime: 594 ms
-- @Memory: N/A

# Write your MySQL query statement below
SELECT * FROM cinema WHERE description != "boring" AND
mod(id,2)=1 ORDER BY rating DESC;
