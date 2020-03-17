
-- @Title: 有趣的电影 (Not Boring Movies)
-- @Author: 2464512446@qq.com
-- @Date: 2019-09-06 15:52:20
-- @Runtime: 211 ms
-- @Memory: N/A

# Write your MySQL query statement below
SELECT id,movie,description,rating FROM cinema WHERE description <> "boring" AND id & 1 ORDER BY rating DESC
