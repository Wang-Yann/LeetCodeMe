-- @Author        : Rock Wayne
-- @Created       : 2020-08-03 22:34:40
-- @Last Modified : 2020-08-03 22:34:40
--
-- #Transactions 记录表
-- #
-- # +----------------+---------+
-- #| Column Name    | Type    |
-- #+----------------+---------+
-- #| id             | int     |
-- #| country        | varchar |
-- #| state          | enum    |
-- #| amount         | int     |
-- #| trans_date     | date    |
-- #+----------------+---------+
-- #id 是这个表的主键。
-- #该表包含有关传入事务的信息。
-- #状态列是类型为 [approved（已批准）、declined（已拒绝）] 的枚举。
-- #
-- #
-- #
-- # Chargebacks 表
-- #
-- # +----------------+---------+
-- #| Column Name    | Type    |
-- #+----------------+---------+
-- #| trans_id       | int     |
-- #| charge_date    | date    |
-- #+----------------+---------+
-- #退单包含有关放置在事务表中的某些事务的传入退单的基本信息。
-- #trans_id 是 transactions 表的 id 列的外键。
-- #每项退单都对应于之前进行的交易，即使未经批准。
-- #
-- #
-- #
-- # 编写一个 SQL 查询，以查找每个月和每个国家/地区的已批准交易的数量及其总金额、退单的数量及其总金额。
-- #
-- # 注意：在您的查询中，给定月份和国家，忽略所有为零的行。
-- #
-- # 查询结果格式如下所示：
-- #
-- # Transactions 表：
-- #+------+---------+----------+--------+------------+
-- #| id   | country | state    | amount | trans_date |
-- #+------+---------+----------+--------+------------+
-- #| 101  | US      | approved | 1000   | 2019-05-18 |
-- #| 102  | US      | declined | 2000   | 2019-05-19 |
-- #| 103  | US      | approved | 3000   | 2019-06-10 |
-- #| 104  | US      | declined | 4000   | 2019-06-13 |
-- #| 105  | US      | approved | 5000   | 2019-06-15 |
-- #+------+---------+----------+--------+------------+
-- #
-- #Chargebacks 表：
-- #+------------+------------+
-- #| trans_id   | trans_date |
-- #+------------+------------+
-- #| 102        | 2019-05-29 |
-- #| 101        | 2019-06-30 |
-- #| 105        | 2019-09-18 |
-- #+------------+------------+
-- #
-- #Result 表：
-- #+----------+---------+----------------+-----------------+-------------------+--
-- #------------------+
-- #| month    | country | approved_count | approved_amount | chargeback_count  | c
-- #hargeback_amount  |
-- #+----------+---------+----------------+-----------------+-------------------+--
-- #------------------+
-- #| 2019-05  | US      | 1              | 1000            | 1                 | 2
-- #000               |
-- #| 2019-06  | US      | 2              | 8000            | 1                 | 1
-- #000               |
-- #| 2019-09  | US      | 0              | 0               | 1                 | 5
-- #000               |
-- #+----------+---------+----------------+-----------------+-------------------+--
-- #------------------+
-- #
-- # 👍 19 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below


SELECT month,
       country,
       count(IF(type = 'approved', 1, null))   AS approved_count,
       SUM(IF(type = 'approved', amount, 0))   AS approved_amount,
       count(IF(type = 'chargeback', 1, null)) AS chargeback_count,
       SUM(IF(type = 'chargeback', amount, 0)) AS chargeback_amount
FROM (
         (SELECT DATE_FORMAT(t.trans_date, '%Y-%m') AS month,
                 t.country,
                 amount,
                 'approved'                         AS type
          FROM Transactions AS t
          WHERE state = 'approved')
         UNION ALL
         (SELECT DATE_FORMAT(c.trans_date, '%Y-%m') AS month,
                 t.country,
                 amount,
                 'chargeback'                       AS type
          FROM Transactions AS t
                   INNER JOIN Chargebacks AS c ON t.id = c.trans_id)
     ) AS tt
GROUP BY tt.month, tt.country;

-- #leetcode submit region end(Prohibit modification and deletion)
	