-- @Author        : Rock Wayne
-- @Created       : 2020-08-07 22:08:16
-- @Last Modified : 2020-08-07 22:08:16
--
-- #表：Orders
-- #
-- # +---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| order_id      | int     |
-- #| customer_id   | int     |
-- #| order_date    | date    |
-- #| item_id       | varchar |
-- #| quantity      | int     |
-- #+---------------+---------+
-- #(order_id, item_id) 是该表主键
-- #该表包含了订单信息
-- #order_date 是id为 item_id 的商品被id为 customer_id 的消费者订购的日期.
-- #
-- # 表：Items
-- #
-- # +---------------------+---------+
-- #| Column Name         | Type    |
-- #+---------------------+---------+
-- #| item_id             | varchar |
-- #| item_name           | varchar |
-- #| item_category       | varchar |
-- #+---------------------+---------+
-- #item_id 是该表主键
-- #item_name 是商品的名字
-- #item_category 是商品的类别
-- #
-- #
-- #
-- #
-- # 你是企业主，想要获得分类商品和周内每天的销售报告。
-- #
-- # 写一个SQL语句，报告 周内每天 每个商品类别下订购了多少单位。
-- #
-- # 返回结果表单 按商品类别排序 。
-- #
-- # 查询结果格式如下例所示：
-- #
-- #
-- #
-- # Orders 表：
-- #+------------+--------------+-------------+--------------+-------------+
-- #| order_id   | customer_id  | order_date  | item_id      | quantity    |
-- #+------------+--------------+-------------+--------------+-------------+
-- #| 1          | 1            | 2020-06-01  | 1            | 10          |
-- #| 2          | 1            | 2020-06-08  | 2            | 10          |
-- #| 3          | 2            | 2020-06-02  | 1            | 5           |
-- #| 4          | 3            | 2020-06-03  | 3            | 5           |
-- #| 5          | 4            | 2020-06-04  | 4            | 1           |
-- #| 6          | 4            | 2020-06-05  | 5            | 5           |
-- #| 7          | 5            | 2020-06-05  | 1            | 10          |
-- #| 8          | 5            | 2020-06-14  | 4            | 5           |
-- #| 9          | 5            | 2020-06-21  | 3            | 5           |
-- #+------------+--------------+-------------+--------------+-------------+
-- #
-- #Items 表：
-- #+------------+----------------+---------------+
-- #| item_id    | item_name      | item_category |
-- #+------------+----------------+---------------+
-- #| 1          | LC Alg. Book   | Book          |
-- #| 2          | LC DB. Book    | Book          |
-- #| 3          | LC SmarthPhone | Phone         |
-- #| 4          | LC Phone 2020  | Phone         |
-- #| 5          | LC SmartGlass  | Glasses       |
-- #| 6          | LC T-Shirt XL  | T-Shirt       |
-- #+------------+----------------+---------------+
-- #
-- #Result 表：
-- #+------------+-----------+-----------+-----------+-----------+-----------+-----
-- #------+-----------+
-- #| Category   | Monday    | Tuesday   | Wednesday | Thursday  | Friday    | Satu
-- #rday  | Sunday    |
-- #+------------+-----------+-----------+-----------+-----------+-----------+-----
-- #------+-----------+
-- #| Book       | 20        | 5         | 0         | 0         | 10        | 0
-- #      | 0         |
-- #| Glasses    | 0         | 0         | 0         | 0         | 5         | 0
-- #      | 0         |
-- #| Phone      | 0         | 0         | 5         | 1         | 0         | 0
-- #      | 10        |
-- #| T-Shirt    | 0         | 0         | 0         | 0         | 0         | 0
-- #      | 0         |
-- #+------------+-----------+-----------+-----------+-----------+-----------+-----
-- #------+-----------+
-- #在周一(2020-06-01, 2020-06-08)，Book分类(ids: 1, 2)下，总共销售了20个单位(10 + 10)
-- #在周二(2020-06-02)，Book分类(ids: 1, 2)下，总共销售了5个单位
-- #在周三(2020-06-03)，Phone分类(ids: 3, 4)下，总共销售了5个单位
-- #在周四(2020-06-04)，Phone分类(ids: 3, 4)下，总共销售了1个单位
-- #在周五(2020-06-05)，Book分类(ids: 1, 2)下，总共销售了10个单位，Glasses分类(ids: 5)下，总共销售了5个单位
-- #在周六, 没有商品销售
-- #在周天(2020-06-14, 2020-06-21)，Phone分类(ids: 3, 4)下，总共销售了10个单位(5 + 5)
-- #没有销售 T-Shirt 类别的商品
-- #
-- # 👍 2 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below
-- AC


select i.item_category as  Category   ,
       sum(if(weekday(o.order_date)=0,o.quantity,0)) as Monday    ,
       sum(if(weekday(o.order_date)=1,o.quantity,0)) as Tuesday    ,
       sum(if(weekday(o.order_date)=2,o.quantity,0)) as Wednesday    ,
       sum(if(weekday(o.order_date)=3,o.quantity,0)) as Thursday    ,
       sum(if(weekday(o.order_date)=4,o.quantity,0)) as Friday    ,
       sum(if(weekday(o.order_date)=5,o.quantity,0)) as Saturday    ,
       sum(if(weekday(o.order_date)=6,o.quantity,0)) as Sunday
from  Items  as i left join Orders as o on  o.item_id=i.item_id
group by i.item_category order by i.item_category;

-- #leetcode submit region end(Prohibit modification and deletion)
	