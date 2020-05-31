
--
-- #编写一个 SQL 查询，获取 Employee 表中第 n 高的薪水（Salary）。
-- #
-- # +----+--------+
-- #| Id | Salary |
-- #+----+--------+
-- #| 1  | 100    |
-- #| 2  | 200    |
-- #| 3  | 300    |
-- #+----+--------+
-- #
-- #
-- # 例如上述 Employee 表，n = 2 时，应返回第二高的薪水 200。如果不存在第 n 高的薪水，那么查询应返回 null。
-- #
-- # +------------------------+
-- #| getNthHighestSalary(2) |
-- #+------------------------+
-- #| 200                    |
-- #+------------------------+
-- #
-- #
--
-- set global log_bin_trust_function_creators = 1;

CREATE FUNCTION getNthHighestSalary1(N INT) RETURNS INT
BEGIN
SET N := N - 1;
RETURN (
           SELECT Salary
           FROM Employee
           GROUP BY Salary
           ORDER BY Salary DESC
           LIMIT N, 1
       );
END;

CREATE FUNCTION getNthHighestSalary2(N INT) RETURNS INT
BEGIN
RETURN (
           SELECT DISTINCT e.Salary
           FROM Employee e
           WHERE (SELECT count(DISTINCT Salary) FROM Employee WHERE Salary > e.Salary) = N - 1
       );
END;

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
RETURN (
           SELECT DISTINCT Salary
           FROM (SELECT Salary,
           dense_rank() over (ORDER BY Salary DESC) AS rnk
           FROM Employee) tmp
           WHERE rnk = N
       );
END;