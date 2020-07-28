-- @Author        : Rock Wayne
-- @Created       : 2020-07-28 21:38:30
-- @Last Modified : 2020-07-28 21:38:30
--
-- #Numbers 表保存数字的值及其频率。
-- #
-- # +----------+-------------+
-- #|  Number  |  Frequency  |
-- #+----------+-------------|
-- #|  0       |  7          |
-- #|  1       |  1          |
-- #|  2       |  3          |
-- #|  3       |  1          |
-- #+----------+-------------+
-- #
-- #
-- # 在此表中，数字为 0, 0, 0, 0, 0, 0, 0, 1, 2, 2, 2, 3，所以中位数是 (0 + 0) / 2 = 0。
-- #
-- # +--------+
-- #| median |
-- #+--------|
-- #| 0.0000 |
-- #+--------+
-- #
-- #
-- # 请编写一个查询来查找所有数字的中位数并将结果命名为 median 。
-- # 👍 14 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below
select avg(number) as median
from
    (select Number, frequency,
            sum(frequency) over(order by number asc) as total,
            sum(frequency) over(order by number desc) as total1,
            (SELECT SUM(Frequency) FROM Numbers) AS TOTAL_ALL
     from Numbers
     order by number asc) as a
where total>=TOTAL_ALL/2
  and total1>=TOTAL_ALL/2

-- #leetcode submit region end(Prohibit modification and deletion)
SELECT AVG(Number) AS median FROM
    (
        SELECT *,
               SUM(Frequency) OVER(ORDER BY Number)- Frequency + 1 AS DN,
               SUM(Frequency) OVER(ORDER BY Number) AS UP,
               (SELECT SUM(Frequency) FROM Numbers) AS TOTAL
        FROM Numbers
    ) as T
WHERE (TOTAL/2)<= UP AND (TOTAL/2 + 1)>= DN
