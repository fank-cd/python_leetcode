
-- @Title: 超过经理收入的员工 (Employees Earning More Than Their Managers)
-- @Author: 2464512446@qq.com
-- @Date: 2019-10-14 14:38:28
-- @Runtime: 258 ms
-- @Memory: N/A

SELECT
    a.Name as 'Employee'
FROM
    Employee AS a,
    Employee AS b
WHERE
    a.ManagerId = b.Id
        AND a.Salary > b.Salary

