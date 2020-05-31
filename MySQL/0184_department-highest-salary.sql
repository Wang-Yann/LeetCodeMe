
--
-- #Employee 表包含所有员工信息，每个员工有其对应的 Id, salary 和 department Id。
-- #
-- # +----+-------+--------+--------------+
-- #| Id | Name  | Salary | DepartmentId |
-- #+----+-------+--------+--------------+
-- #| 1  | Joe   | 70000  | 1            |
-- #| 2  | Henry | 80000  | 2            |
-- #| 3  | Sam   | 60000  | 2            |
-- #| 4  | Max   | 90000  | 1            |
-- #+----+-------+--------+--------------+
-- #
-- #
-- # Department 表包含公司所有部门的信息。
-- #
-- # +----+----------+
-- #| Id | Name     |
-- #+----+----------+
-- #| 1  | IT       |
-- #| 2  | Sales    |
-- #+----+----------+
-- #
-- #
-- # 编写一个 SQL 查询，找出每个部门工资最高的员工。例如，根据上述给定的表格，Max 在 IT 部门有最高工资，Henry 在 Sales 部门有最高工资。
-- #
-- #
-- # +------------+----------+--------+
-- #| Department | Employee | Salary |
-- #+------------+----------+--------+
-- #| IT         | Max      | 90000  |
-- #| Sales      | Henry    | 80000  |
-- #+------------+----------+--------+
-- #
-- #


select d.Name as Department, e.Name as Employee, sm.maxSalary as Salary
from (
         select DepartmentId, max(Salary) as maxSalary
         from Employee
         group by DepartmentId
     ) as sm
         left join
     Employee as e on e.Salary = sm.maxSalary and e.DepartmentId = sm.DepartmentId
         inner join Department d
                    on sm.DepartmentId = d.Id;



SELECT Department.Name AS Department, Employee.Name AS Employee, Employee.Salary AS Salary
FROM Department
         JOIN Employee ON Employee.DepartmentId = Department.Id
WHERE Employee.Salary IN (SELECT MAX(e.Salary) FROM Employee e WHERE e.DepartmentId = Employee.DepartmentId);



select d.Name as Department, e.Name as Employee, e.Salary as Salary
from Employee e
         inner join Department d on e.DepartmentId = d.Id
where (e.DepartmentId, e.Salary) in (
    select DepartmentId, MAX(Salary)
    from Employee
    group by DepartmentId
);
