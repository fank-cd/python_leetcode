
-- @Title: 组合两个表 (Combine Two Tables)
-- @Author: 2464512446@qq.com
-- @Date: 2019-03-06 15:22:02
-- @Runtime: 466 ms
-- @Memory: N/A

# Write your MySQL query statement below
SELECT FirstName, LastName, City, State FROM Person LEFT OUTER JOIN Address on Person.PersonId = Address.PersonId
