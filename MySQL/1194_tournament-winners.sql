-- @Author        : Rock Wayne
-- @Created       : 2020-08-04 20:20:31
-- @Last Modified : 2020-08-04 20:20:31
--
-- #Players 玩家表
-- #
-- # +-------------+-------+
-- #| Column Name | Type  |
-- #+-------------+-------+
-- #| player_id   | int   |
-- #| group_id    | int   |
-- #+-------------+-------+
-- #玩家 ID 是此表的主键。
-- #此表的每一行表示每个玩家的组。
-- #
-- #
-- # Matches 赛事表
-- #
-- # +---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| match_id      | int     |
-- #| first_player  | int     |
-- #| second_player | int     |
-- #| first_score   | int     |
-- #| second_score  | int     |
-- #+---------------+---------+
-- #match_id 是此表的主键。
-- #每一行是一场比赛的记录，第一名和第二名球员包含每场比赛的球员 ID。
-- #第一个玩家和第二个玩家的分数分别包含第一个玩家和第二个玩家的分数。
-- #你可以假设，在每一场比赛中，球员都属于同一组。
-- #
-- #
-- #
-- #
-- # 每组的获胜者是在组内得分最高的选手。如果平局，player_id 最小 的选手获胜。
-- #
-- # 编写一个 SQL 查询来查找每组中的获胜者。
-- #
-- # 查询结果格式如下所示
-- #
-- # Players 表:
-- #+-----------+------------+
-- #| player_id | group_id   |
-- #+-----------+------------+
-- #| 15        | 1          |
-- #| 25        | 1          |
-- #| 30        | 1          |
-- #| 45        | 1          |
-- #| 10        | 2          |
-- #| 35        | 2          |
-- #| 50        | 2          |
-- #| 20        | 3          |
-- #| 40        | 3          |
-- #+-----------+------------+
-- #
-- #Matches 表:
-- #+------------+--------------+---------------+-------------+--------------+
-- #| match_id   | first_player | second_player | first_score | second_score |
-- #+------------+--------------+---------------+-------------+--------------+
-- #| 1          | 15           | 45            | 3           | 0            |
-- #| 2          | 30           | 25            | 1           | 2            |
-- #| 3          | 30           | 15            | 2           | 0            |
-- #| 4          | 40           | 20            | 5           | 2            |
-- #| 5          | 35           | 50            | 1           | 1            |
-- #+------------+--------------+---------------+-------------+--------------+
-- #
-- #Result 表:
-- #+-----------+------------+
-- #| group_id  | player_id  |
-- #+-----------+------------+
-- #| 1         | 15         |
-- #| 2         | 35         |
-- #| 3         | 40         |
-- #+-----------+------------+
-- #
-- # 👍 7 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below

-- GROUP BY就可以返回每组的第一条记录 真的没问题吗？确定
SELECT group_id,
       player_id
FROM (SELECT p.group_id,
             ps.player_id,
             Sum(ps.score) AS score
      FROM Players p
               INNER JOIN
           (SELECT first_player AS player_id,
                   first_score  AS score
            FROM Matches
            UNION ALL
            SELECT second_player AS player_id,
                   second_score  AS score
            FROM Matches) ps
           ON p.player_id = ps.player_id
      GROUP BY ps.player_id
      ORDER BY group_id,
               score DESC,
               player_id) top_scores
GROUP BY group_id;


-- #leetcode submit region end(Prohibit modification and deletion)
	