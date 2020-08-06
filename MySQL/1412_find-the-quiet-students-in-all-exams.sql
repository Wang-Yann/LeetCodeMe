-- @Author        : Rock Wayne
-- @Created       : 2020-08-06 23:07:39
-- @Last Modified : 2020-08-06 23:07:39
--
-- #表: Student
-- #
-- # +---------------------+---------+
-- #| Column Name         | Type    |
-- #+---------------------+---------+
-- #| student_id          | int     |
-- #| student_name        | varchar |
-- #+---------------------+---------+
-- #student_id 是该表主键.
-- #student_name 学生名字.
-- #
-- #
-- #
-- # 表: Exam
-- #
-- # +---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| exam_id       | int     |
-- #| student_id    | int     |
-- #| score         | int     |
-- #+---------------+---------+
-- #(exam_id, student_id) 是该表主键.
-- #学生 student_id 在测验 exam_id 中得分为 score.
-- #
-- #
-- #
-- #
-- # 成绩处于中游的学生是指至少参加了一次测验, 且得分既不是最高分也不是最低分的学生。
-- #
-- # 写一个 SQL 语句，找出在所有测验中都处于中游的学生 (student_id, student_name)。
-- #
-- # 不要返回从来没有参加过测验的学生。返回结果表按照 student_id 排序。
-- #
-- # 查询结果格式如下。
-- #
-- #
-- #
-- # Student 表：
-- #+-------------+---------------+
-- #| student_id  | student_name  |
-- #+-------------+---------------+
-- #| 1           | Daniel        |
-- #| 2           | Jade          |
-- #| 3           | Stella        |
-- #| 4           | Jonathan      |
-- #| 5           | Will          |
-- #+-------------+---------------+
-- #
-- #Exam 表：
-- #+------------+--------------+-----------+
-- #| exam_id    | student_id   | score     |
-- #+------------+--------------+-----------+
-- #| 10         |     1        |    70     |
-- #| 10         |     2        |    80     |
-- #| 10         |     3        |    90     |
-- #| 20         |     1        |    80     |
-- #| 30         |     1        |    70     |
-- #| 30         |     3        |    80     |
-- #| 30         |     4        |    90     |
-- #| 40         |     1        |    60     |
-- #| 40         |     2        |    70     |
-- #| 40         |     4        |    80     |
-- #+------------+--------------+-----------+
-- #
-- #Result 表：
-- #+-------------+---------------+
-- #| student_id  | student_name  |
-- #+-------------+---------------+
-- #| 2           | Jade          |
-- #+-------------+---------------+
-- #
-- #对于测验 1: 学生 1 和 3 分别获得了最低分和最高分。
-- #对于测验 2: 学生 1 既获得了最高分, 也获得了最低分。
-- #对于测验 3 和 4: 学生 1 和 4 分别获得了最低分和最高分。
-- #学生 2 和 5 没有在任一场测验中获得了最高分或者最低分。
-- #因为学生 5 从来没有参加过任何测验, 所以他被排除于结果表。
-- #由此, 我们仅仅返回学生 2 的信息。
-- # 👍 2 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below
--

select student_id, student_name
from Student
where student_id not in
      (select student_id
       from Exam e
       where score >= all(select score from Exam where exam_id=e.exam_id)
          or score <= all(select score from Exam where exam_id=e.exam_id))
  and student_id in (select student_id from Exam);

-- #leetcode submit region end(Prohibit modification and deletion)


SELECT DISTINCT t1.student_id, student_name
FROM Student t1
         INNER JOIN Exam t2
                    ON t1.student_id = t2.student_id
WHERE t1.student_id NOT IN (
    SELECT student_id
    FROM
        (
            SELECT
                student_id
                 ,RANK() OVER(PARTITION BY exam_id ORDER BY score DESC) AS first_id
                 ,RANK() OVER(PARTITION BY exam_id ORDER BY score) AS last_id
            FROM Exam
        ) a
    WHERE first_id = 1 OR last_id = 1
)
ORDER BY student_id;