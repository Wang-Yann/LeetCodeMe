-- @Author        : Rock Wayne
-- @Created       : 2020-07-30 21:39:09
-- @Last Modified : 2020-07-30 21:39:09
--
-- #Table: Activity
-- #
-- #
-- #+--------------+---------+
-- #| Column Name  | Type    |
-- #+--------------+---------+
-- #| player_id    | int     |
-- #| device_id    | int     |
-- #| event_date   | date    |
-- #| games_played | int     |
-- #+--------------+---------+
-- #（player_id，event_date）是此表的主键。
-- #这张表显示了某些游戏的玩家的活动情况。
-- #每一行是一个玩家的记录，他在某一天使用某个设备注销之前登录并玩了很多游戏（可能是 0）。
-- #
-- #
-- #
-- #
-- # 编写一个 SQL 查询，报告在首次登录的第二天再次登录的玩家的分数，四舍五入到小数点后两位。换句话说，您需要计算从首次登录日期开始至少连续两天登录的玩家的数
-- #量，然后除以玩家总数。
-- #
-- # 查询结果格式如下所示：
-- #
-- #
-- #Activity table:
-- #+-----------+-----------+------------+--------------+
-- #| player_id | device_id | event_date | games_played |
-- #+-----------+-----------+------------+--------------+
-- #| 1         | 2         | 2016-03-01 | 5            |
-- #| 1         | 2         | 2016-03-02 | 6            |
-- #| 2         | 3         | 2017-06-25 | 1            |
-- #| 3         | 1         | 2016-03-02 | 0            |
-- #| 3         | 4         | 2018-07-03 | 5            |
-- #+-----------+-----------+------------+--------------+
-- #
-- #Result table:
-- #+-----------+
-- #| fraction  |
-- #+-----------+
-- #| 0.33      |
-- #+-----------+
-- #只有 ID 为 1 的玩家在第一天登录后才重新登录，所以答案是 1/3 = 0.33
-- #
-- # 👍 17 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below

--     is not null判断后，有eventdate值的返回1，null的返回0，avg相当于求和后(即符合条件的id个数)除以总id数即所求比例


select round(avg(a.event_date is not null), 2) fraction
from (select player_id, min(event_date) as login
      from Activity
      group by player_id
     ) p
         left join Activity a on p.player_id = a.player_id and datediff(a.event_date, p.login) = 1


-- #leetcode submit region end(Prohibit modification and deletion)


select round(count(distinct player_id) / (select count(distinct player_id) from Activity), 2) as fraction
from (
         select *, first_value(event_date) over (partition by player_id order by event_date) as fisrt_date from Activity
     ) as a
where datediff(a.event_date, a.fisrt_date) = 1;

