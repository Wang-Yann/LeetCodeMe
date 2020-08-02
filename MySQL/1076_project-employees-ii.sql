-- @Author        : Rock Wayne
-- @Created       : 2020-08-02 23:18:00
-- @Last Modified : 2020-08-02 23:18:00
--
-- #Table: Project
-- #
-- # +-------------+---------+
-- #| Column Name | Type    |
-- #+-------------+---------+
-- #| project_id  | int     |
-- #| employee_id | int     |
-- #+-------------+---------+
-- #主键为 (project_id, employee_id)。
-- #employee_id 是员工表 Employee 表的外键。
-- #
-- #
-- # Table: Employee
-- #
-- # +------------------+---------+
-- #| Column Name      | Type    |
-- #+------------------+---------+
-- #| employee_id      | int     |
-- #| name             | varchar |
-- #| experience_years | int     |
-- #+------------------+---------+
-- #主键是 employee_id。
-- #
-- #
-- #
-- # 编写一个SQL查询，报告所有雇员最多的项目。
-- #
-- # 查询结果格式如下所示：
-- #
-- # Project table:
-- #+-------------+-------------+
-- #| project_id  | employee_id |
-- #+-------------+-------------+
-- #| 1           | 1           |
-- #| 1           | 2           |
-- #| 1           | 3           |
-- #| 2           | 1           |
-- #| 2           | 4           |
-- #+-------------+-------------+
-- #
-- #Employee table:
-- #+-------------+--------+------------------+
-- #| employee_id | name   | experience_years |
-- #+-------------+--------+------------------+
-- #| 1           | Khaled | 3                |
-- #| 2           | Ali    | 2                |
-- #| 3           | John   | 1                |
-- #| 4           | Doe    | 2                |
-- #+-------------+--------+------------------+
-- #
-- #Result table:
-- #+-------------+
-- #| project_id  |
-- #+-------------+
-- #| 1           |
-- #+-------------+
-- #第一个项目有3名员工，第二个项目有2名员工。
-- # 👍 12 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below

SELECT
    project_id
FROM
    Project
GROUP BY project_id
HAVING COUNT(*) >= ALL(
    SELECT
        COUNT(*)
    FROM
        Project
    GROUP BY project_id
);



-- #leetcode submit region end(Prohibit modification and deletion)



select project_id
FROM Project
group by project_id
having count(employee_id) = (
    select count(p0.employee_id) as max_cnt
    from Project p0
    group by p0.project_id
    order by max_cnt desc
    limit 1
);