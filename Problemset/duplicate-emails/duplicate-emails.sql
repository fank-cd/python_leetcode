
-- @Title: 查找重复的电子邮箱 (Duplicate Emails)
-- @Author: 2464512446@qq.com
-- @Date: 2019-09-06 12:14:11
-- @Runtime: 348 ms
-- @Memory: N/A

# Write your MySQL query statement below
SELECT Email FROM person GROUP BY Email HAVING COUNT(Email)>1

