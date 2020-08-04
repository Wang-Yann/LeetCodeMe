-- @Author        : Rock Wayne
-- @Created       : 2020-08-05 00:04:29
-- @Last Modified : 2020-08-05 00:04:29
--
-- #员工表：Employees
-- #
-- # +---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| employee_id   | int     |
-- #| employee_name | varchar |
-- #| manager_id    | int     |
-- #+---------------+---------+
-- #employee_id 是这个表的主键。
-- #这个表中每一行中，employee_id 表示职工的 ID，employee_name 表示职工的名字，manager_id 表示该职工汇报工作的直线经理。
-- #这个公司 CEO 是 employee_id = 1 的人。
-- #
-- #
-- #
-- #
-- # 用 SQL 查询出所有直接或间接向公司 CEO 汇报工作的职工的 employee_id 。
-- #
-- # 由于公司规模较小，经理之间的间接关系不超过 3 个经理。
-- #
-- # 可以以任何顺序返回的结果，不需要去重。
-- #
-- # 查询结果示例如下：
-- #
-- # Employees table:
-- #+-------------+---------------+------------+
-- #| employee_id | employee_name | manager_id |
-- #+-------------+---------------+------------+
-- #| 1           | Boss          | 1          |
-- #| 3           | Alice         | 3          |
-- #| 2           | Bob           | 1          |
-- #| 4           | Daniel        | 2          |
-- #| 7           | Luis          | 4          |
-- #| 8           | Jhon          | 3          |
-- #| 9           | Angela        | 8          |
-- #| 77          | Robert        | 1          |
-- #+-------------+---------------+------------+
-- #
-- #Result table:
-- #+-------------+
-- #| employee_id |
-- #+-------------+
-- #| 2           |
-- #| 77          |
-- #| 4           |
-- #| 7           |
-- #+-------------+
-- #
-- #公司 CEO 的 employee_id 是 1.
-- #employee_id 是 2 和 77 的职员直接汇报给公司 CEO。
-- #employee_id 是 4 的职员间接汇报给公司 CEO 4 --> 2 --> 1 。
-- #employee_id 是 7 的职员间接汇报给公司 CEO 7 --> 4 --> 2 --> 1 。
-- #employee_id 是 3, 8 ，9 的职员不会直接或间接的汇报给公司 CEO。
-- #
-- # 👍 12 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below

with RECURSIVE t as (
    select employee_id
    from Employees
    where manager_id = 1
      and employee_id != 1
    UNION ALL
    select e.employee_id
    from Employees as e
             inner join t on e.manager_id = t.employee_id
)
select employee_id from t;

-- #leetcode submit region end(Prohibit modification and deletion)



SELECT e1.employee_id
FROM   employees e1
           LEFT JOIN employees e2
                     ON e1.manager_id = e2.employee_id
           LEFT JOIN employees e3
                     ON e2.manager_id = e3.employee_id
WHERE  e3.manager_id = 1
  AND e1.employee_id != 1