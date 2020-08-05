-- @Author        : Rock Wayne
-- @Created       : 2020-08-05 23:03:55
-- @Last Modified : 2020-08-05 23:03:55
--
-- #表: Scores
-- #
-- #
-- #+---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| player_name   | varchar |
-- #| gender        | varchar |
-- #| day           | date    |
-- #| score_points  | int     |
-- #+---------------+---------+
-- #(gender, day)是该表的主键
-- #一场比赛是在女队和男队之间举行的
-- #该表的每一行表示一个名叫 (player_name) 性别为 (gender) 的参赛者在某一天获得了 (score_points) 的分数
-- #如果参赛者是女性，那么 gender 列为 'F'，如果参赛者是男性，那么 gender 列为 'M'
-- #
-- #
-- #
-- #
-- # 写一条SQL语句查询每种性别在每一天的总分，并按性别和日期对查询结果排序
-- #
-- # 下面是查询结果格式的例子：
-- #
-- #
-- #Scores表:
-- #+-------------+--------+------------+--------------+
-- #| player_name | gender | day        | score_points |
-- #+-------------+--------+------------+--------------+
-- #| Aron        | F      | 2020-01-01 | 17           |
-- #| Alice       | F      | 2020-01-07 | 23           |
-- #| Bajrang     | M      | 2020-01-07 | 7            |
-- #| Khali       | M      | 2019-12-25 | 11           |
-- #| Slaman      | M      | 2019-12-30 | 13           |
-- #| Joe         | M      | 2019-12-31 | 3            |
-- #| Jose        | M      | 2019-12-18 | 2            |
-- #| Priya       | F      | 2019-12-31 | 23           |
-- #| Priyanka    | F      | 2019-12-30 | 17           |
-- #+-------------+--------+------------+--------------+
-- #结果表:
-- #+--------+------------+-------+
-- #| gender | day        | total |
-- #+--------+------------+-------+
-- #| F      | 2019-12-30 | 17    |
-- #| F      | 2019-12-31 | 40    |
-- #| F      | 2020-01-01 | 57    |
-- #| F      | 2020-01-07 | 80    |
-- #| M      | 2019-12-18 | 2     |
-- #| M      | 2019-12-25 | 13    |
-- #| M      | 2019-12-30 | 26    |
-- #| M      | 2019-12-31 | 29    |
-- #| M      | 2020-01-07 | 36    |
-- #+--------+------------+-------+
-- #女性队伍:
-- #第一天是 2019-12-30，Priyanka 获得 17 分，队伍的总分是 17 分
-- #第二天是 2019-12-31, Priya 获得 23 分，队伍的总分是 40 分
-- #第三天是 2020-01-01, Aron 获得 17 分，队伍的总分是 57 分
-- #第四天是 2020-01-07, Alice 获得 23 分，队伍的总分是 80 分
-- #男性队伍：
-- #第一天是 2019-12-18, Jose 获得 2 分，队伍的总分是 2 分
-- #第二天是 2019-12-25, Khali 获得 11 分，队伍的总分是 13 分
-- #第三天是 2019-12-30, Slaman 获得 13 分，队伍的总分是 26 分
-- #第四天是 2019-12-31, Joe 获得 3 分，队伍的总分是 29 分
-- #第五天是 2020-01-07, Bajrang 获得 7 分，队伍的总分是 36 分
-- #
-- # 👍 7 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below
--
--


select gender, day, sum(score_points) over (partition by gender order by day) as total
from Scores
group by gender, day
order by gender, day;


-- #leetcode submit region end(Prohibit modification and deletion)

SELECT s1.gender, s1.day, SUM(s2.score_points) AS total
FROM Scores AS s1,
     Scores AS s2
WHERE s1.gender = s2.gender
  AND s1.day >= s2.day
GROUP BY s1.gender, s1.day
ORDER BY s1.gender, s1.day;

