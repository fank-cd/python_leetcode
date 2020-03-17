
-- @Title: 组合两个表 (Combine Two Tables)
-- @Author: 2464512446@qq.com
-- @Date: 2019-09-28 17:24:22
-- @Runtime: 162 ms
-- @Memory: N/A

# Write your MySQL query statement below
SELECT FirstName, LastName, City, State FROM
PERSON LEFT JOIN Address on Person.PersonId = Address.PersonId


