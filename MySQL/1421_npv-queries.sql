-- @Author        : Rock Wayne
-- @Created       : 2020-08-06 23:14:51
-- @Last Modified : 2020-08-06 23:14:51
--
-- #表: NPV
-- #
-- # +---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| id            | int     |
-- #| year          | int     |
-- #| npv           | int     |
-- #+---------------+---------+
-- #(id, year) 是该表主键.
-- #该表有每一笔存货的年份, id 和对应净现值的信息.
-- #
-- #
-- #
-- #
-- # 表: Queries
-- #
-- # +---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| id            | int     |
-- #| year          | int     |
-- #+---------------+---------+
-- #(id, year) 是该表主键.
-- #该表有每一次查询所对应存货的 id 和年份的信息.
-- #
-- #
-- #
-- #
-- # 写一个 SQL, 找到 Queries 表中每一次查询的净现值.
-- #
-- # 结果表没有顺序要求.
-- #
-- # 查询结果的格式如下所示:
-- #
-- # NPV 表:
-- #+------+--------+--------+
-- #| id   | year   | npv    |
-- #+------+--------+--------+
-- #| 1    | 2018   | 100    |
-- #| 7    | 2020   | 30     |
-- #| 13   | 2019   | 40     |
-- #| 1    | 2019   | 113    |
-- #| 2    | 2008   | 121    |
-- #| 3    | 2009   | 12     |
-- #| 11   | 2020   | 99     |
-- #| 7    | 2019   | 0      |
-- #+------+--------+--------+
-- #
-- #Queries 表:
-- #+------+--------+
-- #| id   | year   |
-- #+------+--------+
-- #| 1    | 2019   |
-- #| 2    | 2008   |
-- #| 3    | 2009   |
-- #| 7    | 2018   |
-- #| 7    | 2019   |
-- #| 7    | 2020   |
-- #| 13   | 2019   |
-- #+------+--------+
-- #
-- #结果表:
-- #+------+--------+--------+
-- #| id   | year   | npv    |
-- #+------+--------+--------+
-- #| 1    | 2019   | 113    |
-- #| 2    | 2008   | 121    |
-- #| 3    | 2009   | 12     |
-- #| 7    | 2018   | 0      |
-- #| 7    | 2019   | 0      |
-- #| 7    | 2020   | 30     |
-- #| 13   | 2019   | 40     |
-- #+------+--------+--------+
-- #
-- #(7, 2018)的净现值不在 NPV 表中, 我们把它看作是 0.
-- #所有其它查询的净现值都能在 NPV 表中找到.
-- #
-- # 👍 0 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below


select q.id, q.year, ifnull(n.npv, 0) as npv
from Queries as q
         left join NPV as n on q.id = n.id and q.year = n.year;

-- #leetcode submit region end(Prohibit modification and deletion)
	