-- @Author        : Rock Wayne
-- @Created       : 2020-07-28 21:53:38
-- @Last Modified : 2020-07-28 21:53:38
--
-- #表: Candidate
-- #
-- # +-----+---------+
-- #| id  | Name    |
-- #+-----+---------+
-- #| 1   | A       |
-- #| 2   | B       |
-- #| 3   | C       |
-- #| 4   | D       |
-- #| 5   | E       |
-- #+-----+---------+
-- #
-- #
-- # 表: Vote
-- #
-- # +-----+--------------+
-- #| id  | CandidateId  |
-- #+-----+--------------+
-- #| 1   |     2        |
-- #| 2   |     4        |
-- #| 3   |     3        |
-- #| 4   |     2        |
-- #| 5   |     5        |
-- #+-----+--------------+
-- #id 是自动递增的主键，
-- #CandidateId 是 Candidate 表中的 id.
-- #
-- #
-- # 请编写 sql 语句来找到当选者的名字，上面的例子将返回当选者 B.
-- #
-- # +------+
-- #| Name |
-- #+------+
-- #| B    |
-- #+------+
-- #
-- #
-- # 注意:
-- #
-- #
-- # 你可以假设没有平局，换言之，最多只有一位当选者。
-- #
-- #
-- #
-- # 👍 10 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below

select Name
from Candidate
where id = (
               select CandidateId
               from Vote
               group by CandidateId
               order by count(id) desc limit 1
           )

-- #leetcode submit region end(Prohibit modification and deletion)
	