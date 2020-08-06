-- @Author        : Rock Wayne
-- @Created       : 2020-08-06 23:38:41
-- @Last Modified : 2020-08-06 23:38:41
--
-- #表: Sales
-- #
-- # +---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| sale_date     | date    |
-- #| fruit         | enum    |
-- #| sold_num      | int     |
-- #+---------------+---------+
-- #(sale_date,fruit) 是该表主键.
-- #该表包含了每一天中"苹果" 和 "桔子"的销售情况.
-- #
-- #
-- #
-- #
-- # 写一个 SQL 查询, 报告每一天 苹果 和 桔子 销售的数目的差异.
-- #
-- # 返回的结果表, 按照格式为 ('YYYY-MM-DD') 的 sale_date 排序.
-- #
-- # 查询结果表如下例所示:
-- #
-- #
-- #
-- # Sales 表:
-- #+------------+------------+-------------+
-- #| sale_date  | fruit      | sold_num    |
-- #+------------+------------+-------------+
-- #| 2020-05-01 | apples     | 10          |
-- #| 2020-05-01 | oranges    | 8           |
-- #| 2020-05-02 | apples     | 15          |
-- #| 2020-05-02 | oranges    | 15          |
-- #| 2020-05-03 | apples     | 20          |
-- #| 2020-05-03 | oranges    | 0           |
-- #| 2020-05-04 | apples     | 15          |
-- #| 2020-05-04 | oranges    | 16          |
-- #+------------+------------+-------------+
-- #
-- #Result 表:
-- #+------------+--------------+
-- #| sale_date  | diff         |
-- #+------------+--------------+
-- #| 2020-05-01 | 2            |
-- #| 2020-05-02 | 0            |
-- #| 2020-05-03 | 20           |
-- #| 2020-05-04 | -1           |
-- #+------------+--------------+
-- #
-- #在 2020-05-01, 卖了 10 个苹果 和 8 个桔子 (差异为 10 - 8 = 2).
-- #在 2020-05-02, 卖了 15 个苹果 和 15 个桔子 (差异为 15 - 15 = 0).
-- #在 2020-05-03, 卖了 20 个苹果 和 0 个桔子 (差异为 20 - 0 = 20).
-- #在 2020-05-04, 卖了 15 个苹果 和 16 个桔子 (差异为 15 - 16 = -1).
-- #
-- # 👍 3 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below
--

select sale_date,
       sum(case fruit
               when 'apples' then sold_num
               when 'oranges' then -sold_num
               else 0
           end) as diff
from Sales
group by sale_date;

-- #leetcode submit region end(Prohibit modification and deletion)
	