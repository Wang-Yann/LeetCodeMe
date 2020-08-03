-- @Author        : Rock Wayne
-- @Created       : 2020-08-03 23:36:42
-- @Last Modified : 2020-08-03 23:36:42
--
-- #产品数据表: Products
-- #
-- #
-- #+---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| product_id    | int     |
-- #| new_price     | int     |
-- #| change_date   | date    |
-- #+---------------+---------+
-- #这张表的主键是 (product_id, change_date)。
-- #这张表的每一行分别记录了 某产品 在某个日期 更改后 的新价格。
-- #
-- #
-- #
-- # 写一段 SQL来查找在 2019-08-16 时全部产品的价格，假设所有产品在修改前的价格都是 10。
-- #
-- # 查询结果格式如下例所示：
-- #
-- #
-- #Products table:
-- #+------------+-----------+-------------+
-- #| product_id | new_price | change_date |
-- #+------------+-----------+-------------+
-- #| 1          | 20        | 2019-08-14  |
-- #| 2          | 50        | 2019-08-14  |
-- #| 1          | 30        | 2019-08-15  |
-- #| 1          | 35        | 2019-08-16  |
-- #| 2          | 65        | 2019-08-17  |
-- #| 3          | 20        | 2019-08-18  |
-- #+------------+-----------+-------------+
-- #
-- #Result table:
-- #+------------+-------+
-- #| product_id | price |
-- #+------------+-------+
-- #| 2          | 50    |
-- #| 1          | 35    |
-- #| 3          | 10    |
-- #+------------+-------+
-- #
-- # 👍 15 👎 0
--

--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below

SELECT t1.product_id        AS product_id,
       IFNUll(t2.price, 10) AS price
FROM (SELECT DISTINCT product_id
      FROM Products) AS t1
         left join (SELECT product_id,
                           new_price AS price
                    FROM Products
                    WHERE (product_id, change_date) IN (SELECT product_id,
                                                               Max(change_date)
                                                        FROM Products
                                                        WHERE change_date <= '2019-08-16'
                                                        GROUP BY product_id)
) AS t2 ON t1.product_id = t2.product_id;


-- #leetcode submit region end(Prohibit modification and deletion)
	