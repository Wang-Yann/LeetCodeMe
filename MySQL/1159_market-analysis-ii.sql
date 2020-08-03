-- @Author        : Rock Wayne
-- @Created       : 2020-08-03 21:44:15
-- @Last Modified : 2020-08-03 21:44:15
--
-- #表: Users
-- #
-- #
-- #+----------------+---------+
-- #| Column Name    | Type    |
-- #+----------------+---------+
-- #| user_id        | int     |
-- #| join_date      | date    |
-- #| favorite_brand | varchar |
-- #+----------------+---------+
-- #user_id 是该表的主键
-- #表中包含一位在线购物网站用户的个人信息，用户可以在该网站出售和购买商品。
-- #
-- #
-- # 表: Orders
-- #
-- #
-- #+---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| order_id      | int     |
-- #| order_date    | date    |
-- #| item_id       | int     |
-- #| buyer_id      | int     |
-- #| seller_id     | int     |
-- #+---------------+---------+
-- #order_id 是该表的主键
-- #item_id 是 Items 表的外键
-- #buyer_id 和 seller_id 是 Users 表的外键
-- #
-- #
-- # 表: Items
-- #
-- #
-- #+---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| item_id       | int     |
-- #| item_brand    | varchar |
-- #+---------------+---------+
-- #item_id 是该表的主键
-- #
-- #
-- #
-- #
-- # 写一个 SQL 查询确定每一个用户按日期顺序卖出的第二件商品的品牌是否是他们最喜爱的品牌。如果一个用户卖出少于两件商品，查询的结果是 no 。
-- #
-- # 题目保证没有一个用户在一天中卖出超过一件商品
-- #
-- # 下面是查询结果格式的例子：
-- #
-- #
-- #Users table:
-- #+---------+------------+----------------+
-- #| user_id | join_date  | favorite_brand |
-- #+---------+------------+----------------+
-- #| 1       | 2019-01-01 | Lenovo         |
-- #| 2       | 2019-02-09 | Samsung        |
-- #| 3       | 2019-01-19 | LG             |
-- #| 4       | 2019-05-21 | HP             |
-- #+---------+------------+----------------+
-- #
-- #Orders table:
-- #+----------+------------+---------+----------+-----------+
-- #| order_id | order_date | item_id | buyer_id | seller_id |
-- #+----------+------------+---------+----------+-----------+
-- #| 1        | 2019-08-01 | 4       | 1        | 2         |
-- #| 2        | 2019-08-02 | 2       | 1        | 3         |
-- #| 3        | 2019-08-03 | 3       | 2        | 3         |
-- #| 4        | 2019-08-04 | 1       | 4        | 2         |
-- #| 5        | 2019-08-04 | 1       | 3        | 4         |
-- #| 6        | 2019-08-05 | 2       | 2        | 4         |
-- #+----------+------------+---------+----------+-----------+
-- #
-- #Items table:
-- #+---------+------------+
-- #| item_id | item_brand |
-- #+---------+------------+
-- #| 1       | Samsung    |
-- #| 2       | Lenovo     |
-- #| 3       | LG         |
-- #| 4       | HP         |
-- #+---------+------------+
-- #
-- #Result table:
-- #+-----------+--------------------+
-- #| seller_id | 2nd_item_fav_brand |
-- #+-----------+--------------------+
-- #| 1         | no                 |
-- #| 2         | yes                |
-- #| 3         | yes                |
-- #| 4         | no                 |
-- #+-----------+--------------------+
-- #
-- #id 为 1 的用户的查询结果是 no，因为他什么也没有卖出
-- #id为 2 和 3 的用户的查询结果是 yes，因为他们卖出的第二件商品的品牌是他们自己最喜爱的品牌
-- #id为 4 的用户的查询结果是 no，因为他卖出的第二件商品的品牌不是他最喜爱的品牌
-- #
-- # 👍 5 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below


select aa.user_id as seller_id, if(aa.favorite_brand = bb.item_brand, 'yes', 'no') as `2nd_item_fav_brand`
from Users aa
         left join
     (select a.order_id,
             a.order_date,
             a.seller_id,
             b.item_brand,
             rank() over (partition by seller_id order by order_date) as num
      from Orders a
               left join
           Items b
           on a.item_id = b.item_id
     ) as bb
     on aa.user_id = bb.seller_id and num = 2;

-- #leetcode submit region end(Prohibit modification and deletion)



select user_id as seller_id, if(r2.item_brand is null || r2.item_brand != favorite_brand, "no", "yes") as 2nd_item_fav_brand
from Users
         left join (
    select r1.seller_id, it.item_brand
    from (
             select @rk := if(@seller = a.seller_id, @rk + 1, 1) as rank,
                    @seller := a.seller_id as seller_id,
                    a.item_id
             from (
                      select seller_id, item_id
                      from Orders
                      order by seller_id, order_date
                  ) a, (select @seller := -1, @rk := 0) b) r1
             join Items as it
                  on r1.item_id = it.item_id
    where r1.rank = 2
) r2 on user_id = r2.seller_id;