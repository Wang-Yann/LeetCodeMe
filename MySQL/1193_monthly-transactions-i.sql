-- @Author        : Rock Wayne
-- @Created       : 2020-08-03 22:09:30
-- @Last Modified : 2020-08-03 22:09:30
--
-- #Table: Transactions
-- #
-- #
-- #+---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| id            | int     |
-- #| country       | varchar |
-- #| state         | enum    |
-- #| amount        | int     |
-- #| trans_date    | date    |
-- #+---------------+---------+
-- #id 是这个表的主键。
-- #该表包含有关传入事务的信息。
-- #state 列类型为 “[”批准“，”拒绝“] 之一。
-- #
-- #
-- #
-- #
-- # 编写一个 sql 查询来查找每个月和每个国家/地区的事务数及其总金额、已批准的事务数及其总金额。
-- #
-- # 查询结果格式如下所示：
-- #
-- #
-- #Transactions table:
-- #+------+---------+----------+--------+------------+
-- #| id   | country | state    | amount | trans_date |
-- #+------+---------+----------+--------+------------+
-- #| 121  | US      | approved | 1000   | 2018-12-18 |
-- #| 122  | US      | declined | 2000   | 2018-12-19 |
-- #| 123  | US      | approved | 2000   | 2019-01-01 |
-- #| 124  | DE      | approved | 2000   | 2019-01-07 |
-- #+------+---------+----------+--------+------------+
-- #
-- #Result table:
-- #+----------+---------+-------------+----------------+--------------------+-----
-- #------------------+
-- #| month    | country | trans_count | approved_count | trans_total_amount | appr
-- #oved_total_amount |
-- #+----------+---------+-------------+----------------+--------------------+-----
-- #------------------+
-- #| 2018-12  | US      | 2           | 1              | 3000               | 1000
-- #                  |
-- #| 2019-01  | US      | 1           | 1              | 2000               | 2000
-- #                  |
-- #| 2019-01  | DE      | 1           | 1              | 2000               | 2000
-- #                  |
-- #+----------+---------+-------------+----------------+--------------------+-----
-- #------------------+
-- #
-- # 👍 8 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below


select DATE_FORMAT(trans_date, '%Y-%m')       as month,
       country,
       count(id)                              as trans_count,
       count(if(state = 'approved', 1, null)) as approved_count,
       sum(amount)                            as trans_total_amount,
       sum(if(state = 'approved', amount, 0)) as approved_total_amount
from Transactions
group by country, month
order by month;

-- #leetcode submit region end(Prohibit modification and deletion)
	