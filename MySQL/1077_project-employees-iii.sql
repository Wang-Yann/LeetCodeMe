-- @Author        : Rock Wayne
-- @Created       : 2020-08-02 23:29:06
-- @Last Modified : 2020-08-02 23:29:06
--
-- #项目表 Project：
-- #
-- #
-- #+-------------+---------+
-- #| Column Name | Type    |
-- #+-------------+---------+
-- #| project_id  | int     |
-- #| employee_id | int     |
-- #+-------------+---------+
-- #(project_id, employee_id) 是这个表的主键
-- #employee_id 是员工表 Employee 的外键
-- #
-- #
-- # 员工表 Employee：
-- #
-- #
-- #+------------------+---------+
-- #| Column Name      | Type    |
-- #+------------------+---------+
-- #| employee_id      | int     |
-- #| name             | varchar |
-- #| experience_years | int     |
-- #+------------------+---------+
-- #employee_id 是这个表的主键
-- #
-- #
-- #
-- #
-- # 写 一个 SQL 查询语句，报告在每一个项目中经验最丰富的雇员是谁。如果出现经验年数相同的情况，请报告所有具有最大经验年数的员工。
-- #
-- # 查询结果格式在以下示例中：
-- #
-- #
-- #Project 表：
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
-- #Employee 表：
-- #+-------------+--------+------------------+
-- #| employee_id | name   | experience_years |
-- #+-------------+--------+------------------+
-- #| 1           | Khaled | 3                |
-- #| 2           | Ali    | 2                |
-- #| 3           | John   | 3                |
-- #| 4           | Doe    | 2                |
-- #+-------------+--------+------------------+
-- #
-- #Result 表：
-- #+-------------+---------------+
-- #| project_id  | employee_id   |
-- #+-------------+---------------+
-- #| 1           | 1             |
-- #| 1           | 3             |
-- #| 2           | 1             |
-- #+-------------+---------------+
-- #employee_id 为 1 和 3 的员工在 project_id 为 1 的项目中拥有最丰富的经验。在 project_id 为 2 的项目中，empl
-- #oyee_id 为 1 的员工拥有最丰富的经验。
-- # 👍 9 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below

select project_id, employee_id
from (
         select a.project_id,
                b.employee_id,
                b.experience_years,
                RANK() over (partition by a.project_id order by b.experience_years desc) as ranking
         from Project a
                  left join Employee b on a.employee_id = b.employee_id
     )  as k
where ranking = 1;


-- #leetcode submit region end(Prohibit modification and deletion)

SELECT project_id,
       p1.employee_id
FROM Project AS p1
         INNER JOIN Employee AS e1
                    ON p1.employee_id = e1.employee_id
WHERE (project_id, experience_years) IN (SELECT project_id,
                                                Max(experience_years)
                                         FROM Project AS p2
                                                  INNER JOIN Employee AS e2
                                                             ON p2.employee_id =
                                                                e2.employee_id
                                         GROUP BY project_id);
