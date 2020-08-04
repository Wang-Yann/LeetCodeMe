-- @Author        : Rock Wayne
-- @Created       : 2020-08-04 22:32:12
-- @Last Modified : 2020-08-04 22:32:12
--
-- #表: Queue
-- #
-- # +-------------+---------+
-- #| Column Name | Type    |
-- #+-------------+---------+
-- #| person_id   | int     |
-- #| person_name | varchar |
-- #| weight      | int     |
-- #| turn        | int     |
-- #+-------------+---------+
-- #person_id 是这个表的主键。
-- #该表展示了所有等待电梯的人的信息。
-- #表中 person_id 和 turn 列将包含从 1 到 n 的所有数字，其中 n 是表中的行数。
-- #
-- #
-- #
-- #
-- # 电梯最大载重量为 1000。
-- #
-- # 写一条 SQL 查询语句查找最后一个能进入电梯且不超过重量限制的 person_name 。题目确保队列中第一位的人可以进入电梯 。
-- #
-- # 查询结果如下所示 :
-- #
-- # Queue 表
-- #+-----------+-------------------+--------+------+
-- #| person_id | person_name       | weight | turn |
-- #+-----------+-------------------+--------+------+
-- #| 5         | George Washington | 250    | 1    |
-- #| 3         | John Adams        | 350    | 2    |
-- #| 6         | Thomas Jefferson  | 400    | 3    |
-- #| 2         | Will Johnliams    | 200    | 4    |
-- #| 4         | Thomas Jefferson  | 175    | 5    |
-- #| 1         | James Elephant    | 500    | 6    |
-- #+-----------+-------------------+--------+------+
-- #
-- #Result 表
-- #+-------------------+
-- #| person_name       |
-- #+-------------------+
-- #| Thomas Jefferson  |
-- #+-------------------+
-- #
-- #为了简化，Queue 表按 turn 列由小到大排序。
-- #上例中 George Washington(id 5), John Adams(id 3) 和 Thomas Jefferson(id 6) 将可以进入电梯,
-- #因为他们的体重和为 250 + 350 + 400 = 1000。
-- #Thomas Jefferson(id 6) 是最后一个体重合适并进入电梯的人。
-- #
-- # 👍 17 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below


select person_name
from (
         select person_name, turn, sum(weight) over (order by turn) addup_weight
         from Queue a
     ) t
where addup_weight <= 1000
order by turn desc
limit 1;



-- #leetcode submit region end(Prohibit modification and deletion)

select person_name
from (
         select person_name, @accu := @accu + weight as accu
         from (
                  select person_name, weight
                  from Queue
                  order by turn
              ) as q,
              (select @accu := 0) as vars
     ) as t
where accu <= 1000
order by accu desc
limit 1;

SELECT a.person_name
FROM Queue a,
     Queue b
WHERE a.turn >= b.turn
GROUP BY a.person_id
HAVING SUM(b.weight) <= 1000
ORDER BY a.turn DESC
LIMIT 1;
