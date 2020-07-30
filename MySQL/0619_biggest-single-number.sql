-- @Author        : Rock Wayne
-- @Created       : 2020-07-30 23:33:11
-- @Last Modified : 2020-07-30 23:33:11
--
-- #表 my_numbers 的 num 字段包含很多数字，其中包括很多重复的数字。
-- #
-- # 你能写一个 SQL 查询语句，找到只出现过一次的数字中，最大的一个数字吗？
-- #
-- # +---+
-- #|num|
-- #+---+
-- #| 8 |
-- #| 8 |
-- #| 3 |
-- #| 3 |
-- #| 1 |
-- #| 4 |
-- #| 5 |
-- #| 6 |
-- #
-- #
-- # 对于上面给出的样例数据，你的查询语句应该返回如下结果：
-- #
-- # +---+
-- #|num|
-- #+---+
-- #| 6 |
-- #
-- #
-- # 注意：
-- #
-- # 如果没有只出现一次的数字，输出 null 。
-- #
-- #
-- # 👍 12 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below
select max(t.num) as num
from (
         select num
         from my_numbers
         group by num
         having count(num) = 1
     ) as t;


-- #leetcode submit region end(Prohibit modification and deletion)
	