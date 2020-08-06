-- @Author        : Rock Wayne
-- @Created       : 2020-08-06 21:52:15
-- @Last Modified : 2020-08-06 21:52:15
--
-- #Customers 表：
-- #
-- #
-- #+---------------------+---------+
-- #| Column Name         | Type    |
-- #+---------------------+---------+
-- #| customer_id         | int     |
-- #| customer_name       | varchar |
-- #+---------------------+---------+
-- #customer_id 是这张表的主键。
-- #customer_name 是顾客的名称。
-- #
-- #
-- #
-- # Orders 表：
-- #
-- #
-- #+---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| order_id      | int     |
-- #| customer_id   | int     |
-- #| product_name  | varchar |
-- #+---------------+---------+
-- #order_id 是这张表的主键。
-- #customer_id 是购买了名为 "product_name" 产品顾客的id。
-- #
-- #
-- #
-- #
-- # 请你设计 SQL 查询来报告购买了产品 A 和产品 B 却没有购买产品 C 的顾客的 ID 和姓名（ customer_id 和 customer_name
-- # ），我们将基于此结果为他们推荐产品 C 。
-- #您返回的查询结果需要按照 customer_id 排序。
-- #
-- #
-- #
-- # 查询结果如下例所示。
-- #
-- #
-- #Customers table:
-- #+-------------+---------------+
-- #| customer_id | customer_name |
-- #+-------------+---------------+
-- #| 1           | Daniel        |
-- #| 2           | Diana         |
-- #| 3           | Elizabeth     |
-- #| 4           | Jhon          |
-- #+-------------+---------------+
-- #
-- #Orders table:
-- #+------------+--------------+---------------+
-- #| order_id   | customer_id  | product_name  |
-- #+------------+--------------+---------------+
-- #| 10         |     1        |     A         |
-- #| 20         |     1        |     B         |
-- #| 30         |     1        |     D         |
-- #| 40         |     1        |     C         |
-- #| 50         |     2        |     A         |
-- #| 60         |     3        |     A         |
-- #| 70         |     3        |     B         |
-- #| 80         |     3        |     D         |
-- #| 90         |     4        |     C         |
-- #+------------+--------------+---------------+
-- #
-- #Result table:
-- #+-------------+---------------+
-- #| customer_id | customer_name |
-- #+-------------+---------------+
-- #| 3           | Elizabeth     |
-- #+-------------+---------------+
-- #只有 customer_id 为 3 的顾客购买了产品 A 和产品 B ，却没有购买产品 C 。
-- # 👍 1 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below

select c.customer_id,  customer_name
from customers c join orders o
                      on c.customer_id = o.customer_id
group by c.customer_id
having sum(product_name = 'A') and sum(product_name = 'B') and not sum(product_name = 'C')



-- #leetcode submit region end(Prohibit modification and deletion)


select customer_id, customer_name
from Customers
where customer_id in (
    select customer_id
    from Orders as o
    where not exists(
            select 1 from Orders as io where io.product_name = 'C' and io.customer_id = o.customer_id
        )
      and exists(
            select 1 from Orders as io where io.product_name = 'A' and io.customer_id = o.customer_id
        )
      and exists(
            select 1 from Orders as io where io.product_name = 'B' and io.customer_id = o.customer_id
        )
);
