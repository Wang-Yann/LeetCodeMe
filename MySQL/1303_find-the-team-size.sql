-- @Author        : Rock Wayne
-- @Created       : 2020-08-05 23:00:49
-- @Last Modified : 2020-08-05 23:00:49
--
-- #员工表：Employee
-- #
-- #
-- #+---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| employee_id   | int     |
-- #| team_id       | int     |
-- #+---------------+---------+
-- #employee_id 字段是这张表的主键，表中的每一行都包含每个员工的 ID 和他们所属的团队。
-- #
-- #
-- # 编写一个 SQL 查询，以求得每个员工所在团队的总人数。
-- #
-- # 查询结果中的顺序无特定要求。
-- #
-- # 查询结果格式示例如下：
-- #
-- #
-- #Employee Table:
-- #+-------------+------------+
-- #| employee_id | team_id    |
-- #+-------------+------------+
-- #|     1       |     8      |
-- #|     2       |     8      |
-- #|     3       |     8      |
-- #|     4       |     7      |
-- #|     5       |     9      |
-- #|     6       |     9      |
-- #+-------------+------------+
-- #Result table:
-- #+-------------+------------+
-- #| employee_id | team_size  |
-- #+-------------+------------+
-- #|     1       |     3      |
-- #|     2       |     3      |
-- #|     3       |     3      |
-- #|     4       |     1      |
-- #|     5       |     2      |
-- #|     6       |     2      |
-- #+-------------+------------+
-- #ID 为 1、2、3 的员工是 team_id 为 8 的团队的成员，
-- #ID 为 4 的员工是 team_id 为 7 的团队的成员，
-- #ID 为 5、6 的员工是 team_id 为 9 的团队的成员。
-- #
-- # 👍 12 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below
--


select employee_id, team_size
from Employee as e
         join (
    select team_id, count(employee_id) as team_size
    from Employee
    group by team_id
) eg on e.team_id = eg.team_id;

-- #leetcode submit region end(Prohibit modification and deletion)
	