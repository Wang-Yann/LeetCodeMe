-- @Author        : Rock Wayne
-- @Created       : 2020-07-28 22:10:29
-- @Last Modified : 2020-07-28 22:10:29
--
-- #从 survey_log 表中获得回答率最高的问题，survey_log 表包含这些列：id, action, question_id, answer_id,
-- # q_num, timestamp。
-- #
-- # id 表示用户 id；action 有以下几种值："show"，"answer"，"skip"；当 action 值为 "answer" 时 answer_
-- #id 非空，而 action 值为 "show" 或者 "skip" 时 answer_id 为空；q_num 表示当前会话中问题的编号。
-- #
-- # 请编写 SQL 查询来找到具有最高回答率的问题。
-- #
-- #
-- #
-- # 示例：
-- #
-- # 输入：
-- #+------+-----------+--------------+------------+-----------+------------+
-- #| id   | action    | question_id  | answer_id  | q_num     | timestamp  |
-- #+------+-----------+--------------+------------+-----------+------------+
-- #| 5    | show      | 285          | null       | 1         | 123        |
-- #| 5    | answer    | 285          | 124124     | 1         | 124        |
-- #| 5    | show      | 369          | null       | 2         | 125        |
-- #| 5    | skip      | 369          | null       | 2         | 126        |
-- #+------+-----------+--------------+------------+-----------+------------+
-- #输出：
-- #+-------------+
-- #| survey_log  |
-- #+-------------+
-- #|    285      |
-- #+-------------+
-- #解释：
-- #问题 285 的回答率为 1/1，而问题 369 回答率为 0/1，因此输出 285 。
-- #
-- #
-- #
-- #
-- # 提示：回答率最高的含义是：同一问题编号中回答数占显示数的比例最高。
-- # 👍 3 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below


select question_id as survey_log
from survey_log
group by question_id
order by count(answer_id) / COUNT(IF(action = 'show', 1, 0)) desc
limit 1;

-- #leetcode submit region end(Prohibit modification and deletion)


select tt.question_id as survey_log
from (
         select question_id, sum(case action when 'answer' then 1 else 0 end) / sum(case action when 'show' then 1 else 0 end) as rate
         from survey_log
         group by question_id
         order by rate desc
         limit 1
     ) as tt;