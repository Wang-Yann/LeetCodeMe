-- @Author        : Rock Wayne
-- @Created       : 2020-08-07 00:17:03
-- @Last Modified : 2020-08-07 00:17:03
--
-- #表: Points
-- #
-- # +---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| id            | int     |
-- #| x_value       | int     |
-- #| y_value       | int     |
-- #+---------------+---------+
-- #id 是该表主键.
-- #每个点都表示为二维空间 (x_value, y_value).
-- #
-- # 写一个 SQL 语句, 报告由表中任意两点可以形成的所有可能的矩形.
-- #
-- # 结果表中的每一行包含三列 (p1, p2, area) 如下:
-- #
-- #
-- # p1 和 p2 是矩形两个对角的 id 且 p1 < p2.
-- # 矩形的面积由列 area 表示.
-- #
-- #
-- # 请按照面积大小降序排列，如果面积相同的话, 则按照 p1 和 p2 升序对结果表排序
-- #
-- # Points 表:
-- #+----------+-------------+-------------+
-- #| id       | x_value     | y_value     |
-- #+----------+-------------+-------------+
-- #| 1        | 2           | 8           |
-- #| 2        | 4           | 7           |
-- #| 3        | 2           | 10          |
-- #+----------+-------------+-------------+
-- #
-- #Result 表:
-- #+----------+-------------+-------------+
-- #| p1       | p2          | area        |
-- #+----------+-------------+-------------+
-- #| 2        | 3           | 6           |
-- #| 1        | 2           | 2           |
-- #+----------+-------------+-------------+
-- #
-- #p1 应该小于 p2 并且面积大于 0.
-- #p1 = 1 且 p2 = 2 时, 面积等于 |2-4| * |8-7| = 2.
-- #p1 = 2 且 p2 = 3 时, 面积等于 |4-2| * |7-10| = 6.
-- #p1 = 1 且 p2 = 3 时, 是不可能为矩形的, 因为面积等于 0.
-- #
-- # 👍 1 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below


SELECT *
FROM
    (SELECT a.id AS P1,
            b.id AS P2,
            abs(a.x_value - b.x_value) * abs(a.y_value - b.y_value) AS area
     FROM Points a
              INNER JOIN Points b ON a.id < b.id
     ORDER BY area DESC, P1, P2) r
WHERE area > 0;




-- #leetcode submit region end(Prohibit modification and deletion)


-- AC
select p1, p2, abs(dx * dy) as area
from (
         select a.id as p1, b.id as p2, (a.x_value - b.x_value) as dx, (a.y_value - b.y_value) as dy
         from Points a,
              Points b
         where a.id < b.id
           and a.x_value != b.x_value
           and a.y_value != b.y_value
         group by a.id, b.id)
         as t
order by area desc, p1 asc, p2 asc;
