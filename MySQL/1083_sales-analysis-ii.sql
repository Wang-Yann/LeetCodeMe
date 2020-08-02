-- @Author        : Rock Wayne
-- @Created       : 2020-08-02 23:43:37
-- @Last Modified : 2020-08-02 23:43:37
--
-- #Table: Product
-- #
-- # +--------------+---------+
-- #| Column Name  | Type    |
-- #+--------------+---------+
-- #| product_id   | int     |
-- #| product_name | varchar |
-- #| unit_price   | int     |
-- #+--------------+---------+
-- #product_id 是这张表的主键
-- #
-- #
-- # Table: Sales
-- #
-- # +-------------+---------+
-- #| Column Name | Type    |
-- #+-------------+---------+
-- #| seller_id   | int     |
-- #| product_id  | int     |
-- #| buyer_id    | int     |
-- #| sale_date   | date    |
-- #| quantity    | int     |
-- #| price       | int     |
-- #+------ ------+---------+
-- #这个表没有主键，它可以有重复的行.
-- #product_id 是 Product 表的外键.
-- #
-- #
-- # 编写一个 SQL 查询，查询购买了 S8 手机却没有购买 iPhone 的买家。注意这里 S8 和 iPhone 是 Product 表中的产品。
-- #
-- # 查询结果格式如下图表示：
-- #
-- # Product table:
-- #+------------+--------------+------------+
-- #| product_id | product_name | unit_price |
-- #+------------+--------------+------------+
-- #| 1          | S8           | 1000       |
-- #| 2          | G4           | 800        |
-- #| 3          | iPhone       | 1400       |
-- #+------------+--------------+------------+
-- #
-- #Sales table:
-- #+-----------+------------+----------+------------+----------+-------+
-- #| seller_id | product_id | buyer_id | sale_date  | quantity | price |
-- #+-----------+------------+----------+------------+----------+-------+
-- #| 1         | 1          | 1        | 2019-01-21 | 2        | 2000  |
-- #| 1         | 2          | 2        | 2019-02-17 | 1        | 800   |
-- #| 2         | 1          | 3        | 2019-06-02 | 1        | 800   |
-- #| 3         | 3          | 3        | 2019-05-13 | 2        | 2800  |
-- #+-----------+------------+----------+------------+----------+-------+
-- #
-- #Result table:
-- #+-------------+
-- #| buyer_id    |
-- #+-------------+
-- #| 1           |
-- #+-------------+
-- #id 为 1 的买家购买了一部 S8，但是却没有购买 iPhone，而 id 为 3 的买家却同时购买了这 2 部手机。
-- #
-- #
-- # 👍 13 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below


select buyer_id
from Sales as s
         left join Product as p on s.product_id = p.product_id
group by buyer_id
having sum(if(product_name = 'S8', 1, 0)) >= 1
   and sum(if(product_name = 'iPhone', 1, 0)) = 0;

-- COUNT(IF(P.product_name = 'S8',TRUE, NULL)) >= 1 AND COUNT(IF(P.product_name = 'iPhone',TRUE, NULL)) = 0


-- #leetcode submit region end(Prohibit modification and deletion)
	