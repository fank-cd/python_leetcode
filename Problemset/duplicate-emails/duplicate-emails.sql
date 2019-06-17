
-- @Title: 查找重复的电子邮箱 (Duplicate Emails)
-- @Author: 2464512446@qq.com
-- @Date: 2019-03-05 14:59:38
-- @Runtime: 306 ms
-- @Memory: N/A

# Write your MySQL query statement below
SELECT Email FROM Person GROUP BY Email HAVING COUNT(Email) >1;
