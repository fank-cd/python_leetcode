
-- @Title: 交换工资 (Swap Salary)
-- @Author: 2464512446@qq.com
-- @Date: 2019-03-15 11:48:02
-- @Runtime: 297 ms
-- @Memory: N/A

# Write your MySQL query statement below
update salary set sex = if(sex = 'm','f','m')
