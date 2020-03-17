
-- @Title: 交换工资 (Swap Salary)
-- @Author: 2464512446@qq.com
-- @Date: 2019-09-06 17:36:17
-- @Runtime: 310 ms
-- @Memory: N/A

# Write your MySQL query statement below
Update salary set sex = if(sex='m','f',"m")
