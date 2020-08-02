-- @Author        : Rock Wayne
-- @Created       : 2020-08-02 23:11:26
-- @Last Modified : 2020-08-02 23:11:26
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
-- #主键为 (project_id, employee_id)。
-- #employee_id 是员工表 Employee 表的外键。
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
-- #主键是 employee_id。
-- #
-- #
-- #
-- #
-- # 请写一个 SQL 语句，查询每一个项目中员工的 平均 工作年限，精确到小数点后两位。
-- #
-- # 查询结果的格式如下：
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
-- #| 3           | John   | 1                |
-- #| 4           | Doe    | 2                |
-- #+-------------+--------+------------------+
-- #
-- #Result 表：
-- #+-------------+---------------+
-- #| project_id  | average_years |
-- #+-------------+---------------+
-- #| 1           | 2.00          |
-- #| 2           | 2.50          |
-- #+-------------+---------------+
-- #第一个项目中，员工的平均工作年限是 (3 + 2 + 1) / 3 = 2.00；第二个项目中，员工的平均工作年限是 (3 + 2) / 2 = 2.50
-- #
-- # 👍 7 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below


select p.project_id,
       round(avg(e.experience_years), 2) as average_years
from Project as p
         join Employee as e on p.employee_id = e.employee_id
group by p.project_id;

-- #leetcode submit region end(Prohibit modification and deletion)
	