-- @Author        : Rock Wayne
-- @Created       : 2020-08-06 23:19:06
-- @Last Modified : 2020-08-06 23:19:06
--
-- #表：Sessions
-- #
-- # +---------------------+---------+
-- #| Column Name         | Type    |
-- #+---------------------+---------+
-- #| session_id          | int     |
-- #| duration            | int     |
-- #+---------------------+---------+
-- #session_id 是该表主键
-- #duration 是用户访问应用的时间, 以秒为单位
-- #
-- #
-- #
-- #
-- # 你想知道用户在你的 app 上的访问时长情况。因此决定统计访问时长区间分别为 "[0-5>", "[5-10>", "[10-15>" 和 "15 or m
-- #ore" （单位：分钟）的会话数量，并以此绘制柱状图。
-- #
-- # 写一个SQL查询来报告（访问时长区间，会话总数）。结果可用任何顺序呈现。
-- #
-- #
-- #
-- # 下方为查询的输出格式：
-- #
-- # Sessions 表：
-- #+-------------+---------------+
-- #| session_id  | duration      |
-- #+-------------+---------------+
-- #| 1           | 30            |
-- #| 2           | 199           |
-- #| 3           | 299           |
-- #| 4           | 580           |
-- #| 5           | 1000          |
-- #+-------------+---------------+
-- #
-- #Result 表：
-- #+--------------+--------------+
-- #| bin          | total        |
-- #+--------------+--------------+
-- #| [0-5>        | 3            |
-- #| [5-10>       | 1            |
-- #| [10-15>      | 0            |
-- #| 15 or more   | 1            |
-- #+--------------+--------------+
-- #
-- #对于 session_id 1，2 和 3 ，它们的访问时间大于等于 0 分钟且小于 5 分钟。
-- #对于 session_id 4，它的访问时间大于等于 5 分钟且小于 10 分钟。
-- #没有会话的访问时间大于等于 10 分钟且小于 15 分钟。
-- #对于 session_id 5, 它的访问时间大于等于 15 分钟。
-- #
-- # 👍 6 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below

select if(bounds.lo = 15, '15 or more',
          concat('[', bounds.lo, '-', bounds.hi, '>')
           )                        as bin,
       ifnull(count(session_id), 0) as total
from (
         select 0 as lo, 5 as hi
         UNION
         select 5 as lo, 10 as hi
         UNION
         select 10 as lo, 15 as hi
         UNION
         select 15 as lo, null as hi) bounds
         left join Sessions as s
                   on s.duration >= bounds.lo * 60
                       and (s.duration < bounds.hi * 60 or bounds.hi is null)
group by bin;

-- SELECT
--     CASE
--         WHEN duration/60 BETWEEN 0 AND 5 THEN "[0-5>"
--         WHEN duration/60 BETWEEN 5 AND 10 THEN "[5-10>"
--         WHEN duration/60 BETWEEN 10 AND 15 THEN "[10-15>"
--         WHEN duration/60 >= 15 THEN "15 or more"
--         ELSE NULL END AS BIN
-- FROM Sessions

-- #leetcode submit region end(Prohibit modification and deletion)
