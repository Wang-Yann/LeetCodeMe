-- @Author        : Rock Wayne
-- @Created       : 2020-08-04 22:53:05
-- @Last Modified : 2020-08-04 22:53:05
--
-- #Table: Teams
-- #
-- #
-- #+---------------+----------+
-- #| Column Name   | Type     |
-- #+---------------+----------+
-- #| team_id       | int      |
-- #| team_name     | varchar  |
-- #+---------------+----------+
-- #此表的主键是 team_id，表中的每一行都代表一支独立足球队。
-- #
-- #
-- # Table: Matches
-- #
-- #
-- #+---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| match_id      | int     |
-- #| host_team     | int     |
-- #| guest_team    | int     |
-- #| host_goals    | int     |
-- #| guest_goals   | int     |
-- #+---------------+---------+
-- #此表的主键是 match_id，表中的每一行都代表一场已结束的比赛，比赛的主客队分别由它们自己的 id 表示，他们的进球由 host_goals 和 gues
-- #t_goals 分别表示。
-- #
-- #
-- #
-- #
-- # 积分规则如下：
-- #
-- #
-- # 赢一场得三分；
-- # 平一场得一分；
-- # 输一场不得分。
-- #
-- #
-- # 写出一条SQL语句以查询每个队的 team_id，team_name 和 num_points。结果根据 num_points 降序排序，如果有两队积分相同
-- #，那么这两队按 team_id 升序排序。
-- #
-- # 查询结果格式如下：
-- #
-- #
-- #Teams table:
-- #+-----------+--------------+
-- #| team_id   | team_name    |
-- #+-----------+--------------+
-- #| 10        | Leetcode FC  |
-- #| 20        | NewYork FC   |
-- #| 30        | Atlanta FC   |
-- #| 40        | Chicago FC   |
-- #| 50        | Toronto FC   |
-- #+-----------+--------------+
-- #
-- #Matches table:
-- #+------------+--------------+---------------+-------------+--------------+
-- #| match_id   | host_team    | guest_team    | host_goals  | guest_goals  |
-- #+------------+--------------+---------------+-------------+--------------+
-- #| 1          | 10           | 20            | 3           | 0            |
-- #| 2          | 30           | 10            | 2           | 2            |
-- #| 3          | 10           | 50            | 5           | 1            |
-- #| 4          | 20           | 30            | 1           | 0            |
-- #| 5          | 50           | 30            | 1           | 0            |
-- #+------------+--------------+---------------+-------------+--------------+
-- #
-- #Result table:
-- #+------------+--------------+---------------+
-- #| team_id    | team_name    | num_points    |
-- #+------------+--------------+---------------+
-- #| 10         | Leetcode FC  | 7             |
-- #| 20         | NewYork FC   | 3             |
-- #| 50         | Toronto FC   | 3             |
-- #| 30         | Atlanta FC   | 1             |
-- #| 40         | Chicago FC   | 0             |
-- #+------------+--------------+---------------+
-- #
-- # 👍 8 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below


select t.team_id, t.team_name, ifnull(sum(ts.points), 0) as num_points
from (
         select host_team as team_id, if(host_goals > guest_goals, 3, 1) as points
         from Matches
         where host_goals >= guest_goals
         UNION ALL
         select guest_team as team_id, if(guest_goals > host_goals, 3, 1) as points
         from Matches
         where guest_goals >= host_goals
     ) as ts
         right join Teams as t on ts.team_id = t.team_id
group by t.team_id order by  num_points desc,t.team_id asc;


-- #leetcode submit region end(Prohibit modification and deletion)
	