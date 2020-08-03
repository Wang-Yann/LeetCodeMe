-- @Author        : Rock Wayne
-- @Created       : 2020-08-03 20:53:50
-- @Last Modified : 2020-08-03 20:53:50
--
-- #Table: Activity
-- #
-- # +---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| user_id       | int     |
-- #| session_id    | int     |
-- #| activity_date | date    |
-- #| activity_type | enum    |
-- #+---------------+---------+
-- #该表没有主键，它可能有重复的行。
-- #activity_type列是一种类型的ENUM（“ open_session”，“ end_session”，“ scroll_down”，“ send_m
-- #essage”）。
-- #该表显示了社交媒体网站的用户活动。
-- #请注意，每个会话完全属于一个用户。
-- #
-- #
-- #
-- # 编写SQL查询以查找截至2019年7月27日（含）的30天内每个用户的平均会话数，四舍五入到小数点后两位。我们只统计那些会话期间用户至少进行一项活动的有效会
-- #话。
-- #
-- #
-- #
-- # 查询结果格式如下例所示：
-- #
-- # Activity table:
-- #+---------+------------+---------------+---------------+
-- #| user_id | session_id | activity_date | activity_type |
-- #+---------+------------+---------------+---------------+
-- #| 1       | 1          | 2019-07-20    | open_session  |
-- #| 1       | 1          | 2019-07-20    | scroll_down   |
-- #| 1       | 1          | 2019-07-20    | end_session   |
-- #| 2       | 4          | 2019-07-20    | open_session  |
-- #| 2       | 4          | 2019-07-21    | send_message  |
-- #| 2       | 4          | 2019-07-21    | end_session   |
-- #| 3       | 2          | 2019-07-21    | open_session  |
-- #| 3       | 2          | 2019-07-21    | send_message  |
-- #| 3       | 2          | 2019-07-21    | end_session   |
-- #| 3       | 5          | 2019-07-21    | open_session  |
-- #| 3       | 5          | 2019-07-21    | scroll_down   |
-- #| 3       | 5          | 2019-07-21    | end_session   |
-- #| 4       | 3          | 2019-06-25    | open_session  |
-- #| 4       | 3          | 2019-06-25    | end_session   |
-- #+---------+------------+---------------+---------------+
-- #
-- #Result table:
-- #+---------------------------+
-- #| average_sessions_per_user |
-- #+---------------------------+
-- #| 1.33                      |
-- #+---------------------------+
-- #User 1 和 2 在过去30天内各自进行了1次会话，而用户3进行了2次会话，因此平均值为（1 +1 + 2）/ 3 = 1.33。
-- # 👍 7 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below



select round(ifnull(sum(sessions) / count(user_id),0), 2) as average_sessions_per_user
from (
         select user_id, count(distinct session_id) as sessions
         from Activity
         where activity_date > date_sub('2019-07-27', Interval 30 day)
         group by user_id
     ) t;


-- #leetcode submit region end(Prohibit modification and deletion)

SELECT Round(Ifnull(Count(DISTINCT session_id) / Count(DISTINCT user_id), 0), 2)
           AS
           average_sessions_per_user
FROM   activity
WHERE  Datediff("2019-07-27", activity_date) < 30 ;