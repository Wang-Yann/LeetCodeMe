-- @Author        : Rock Wayne
-- @Created       : 2020-08-03 20:36:42
-- @Last Modified : 2020-08-03 20:36:42
--
-- #动作表：Actions
-- #
-- #
-- #+---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| user_id       | int     |
-- #| post_id       | int     |
-- #| action_date   | date    |
-- #| action        | enum    |
-- #| extra         | varchar |
-- #+---------------+---------+
-- #此表没有主键，所以可能会有重复的行。
-- #action 字段是 ENUM 类型的，包含:('view', 'like', 'reaction', 'comment', 'report', 'share
-- #')
-- #extra 字段是可选的信息（可能为 null），其中的信息例如有：1.报告理由(a reason for report) 2.反应类型(a type of
-- #reaction)
-- #
-- #
-- #
-- #
-- # 编写一条SQL，查询每种 报告理由（report reason）在昨天的报告数量。假设今天是 2019-07-05。
-- #
-- # 查询及结果的格式示例：
-- #
-- #
-- #Actions table:
-- #+---------+---------+-------------+--------+--------+
-- #| user_id | post_id | action_date | action | extra  |
-- #+---------+---------+-------------+--------+--------+
-- #| 1       | 1       | 2019-07-01  | view   | null   |
-- #| 1       | 1       | 2019-07-01  | like   | null   |
-- #| 1       | 1       | 2019-07-01  | share  | null   |
-- #| 2       | 4       | 2019-07-04  | view   | null   |
-- #| 2       | 4       | 2019-07-04  | report | spam   |
-- #| 3       | 4       | 2019-07-04  | view   | null   |
-- #| 3       | 4       | 2019-07-04  | report | spam   |
-- #| 4       | 3       | 2019-07-02  | view   | null   |
-- #| 4       | 3       | 2019-07-02  | report | spam   |
-- #| 5       | 2       | 2019-07-04  | view   | null   |
-- #| 5       | 2       | 2019-07-04  | report | racism |
-- #| 5       | 5       | 2019-07-04  | view   | null   |
-- #| 5       | 5       | 2019-07-04  | report | racism |
-- #+---------+---------+-------------+--------+--------+
-- #
-- #Result table:
-- #+---------------+--------------+
-- #| report_reason | report_count |
-- #+---------------+--------------+
-- #| spam          | 1            |
-- #| racism        | 2            |
-- #+---------------+--------------+
-- #注意，我们只关心报告数量非零的结果。
-- #
-- #
-- #
-- # 👍 6 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below

select extra as report_reason, count(distinct post_id) as report_count
from Actions
where action = 'report' and extra is not null
  and action_date = date_sub('2019-07-05', INTERVAL 1 day)
group by extra;


-- #leetcode submit region end(Prohibit modification and deletion)
	