
-- @Title: 大的国家 (Big Countries)
-- @Author: 2464512446@qq.com
-- @Date: 2019-03-06 11:41:29
-- @Runtime: 422 ms
-- @Memory: N/A

# Write your MySQL query statement below
SELECT name,population,area FROM World WHERE area > 3000000 OR population > 25000000;
