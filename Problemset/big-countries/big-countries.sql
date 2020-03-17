
-- @Title: 大的国家 (Big Countries)
-- @Author: 2464512446@qq.com
-- @Date: 2019-09-06 15:03:13
-- @Runtime: 271 ms
-- @Memory: N/A

# Write your MySQL query statement below
SELECT name,population,area FROM World WHERE area > 3000000 or population>25000000
