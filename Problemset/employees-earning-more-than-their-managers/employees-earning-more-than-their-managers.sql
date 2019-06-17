
-- @Title: 超过经理收入的员工 (Employees Earning More Than Their Managers)
-- @Author: 2464512446@qq.com
-- @Date: 2019-03-15 11:51:37
-- @Runtime: 860 ms
-- @Memory: N/A

SELECT 
    Name Employee
FROM
    Employee AS a
WHERE
    Salary > (SELECT 
            Salary
        FROM
            Employee
        WHERE
            Id = a.Managerid)
