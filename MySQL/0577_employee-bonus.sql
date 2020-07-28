-- @Author        : Rock Wayne
-- @Created       : 2020-07-28 22:03:24
-- @Last Modified : 2020-07-28 22:03:24
--
-- #选出所有 bonus < 1000 的员工的 name 及其 bonus。
-- #
-- # Employee 表单
-- #
-- # +-------+--------+-----------+--------+
-- #| empId |  name  | supervisor| salary |
-- #+-------+--------+-----------+--------+
-- #|   1   | John   |  3        | 1000   |
-- #|   2   | Dan    |  3        | 2000   |
-- #|   3   | Brad   |  null     | 4000   |
-- #|   4   | Thomas |  3        | 4000   |
-- #+-------+--------+-----------+--------+
-- #empId 是这张表单的主关键字
-- #
-- #
-- # Bonus 表单
-- #
-- # +-------+-------+
-- #| empId | bonus |
-- #+-------+-------+
-- #| 2     | 500   |
-- #| 4     | 2000  |
-- #+-------+-------+
-- #empId 是这张表单的主关键字
-- #
-- #
-- # 输出示例：
-- #
-- # +-------+-------+
-- #| name  | bonus |
-- #+-------+-------+
-- #| John  | null  |
-- #| Dan   | 500   |
-- #| Brad  | null  |
-- #+-------+-------+
-- #
-- # 👍 7 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below

select e.name, b.bonus
from Employee e
         left join Bonus b on e.empId = b.empId
where ifnull(b.bonus, 0) < 1000;

-- #leetcode submit region end(Prohibit modification and deletion)
	