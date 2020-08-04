-- @Author        : Rock Wayne
-- @Created       : 2020-08-05 00:22:44
-- @Last Modified : 2020-08-05 00:22:44
--
-- #学生表: Students
-- #
-- # +---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| student_id    | int     |
-- #| student_name  | varchar |
-- #+---------------+---------+
-- #主键为 student_id（学生ID），该表内的每一行都记录有学校一名学生的信息。
-- #
-- #
-- #
-- #
-- # 科目表: Subjects
-- #
-- # +--------------+---------+
-- #| Column Name  | Type    |
-- #+--------------+---------+
-- #| subject_name | varchar |
-- #+--------------+---------+
-- #主键为 subject_name（科目名称），每一行记录学校的一门科目名称。
-- #
-- #
-- #
-- #
-- # 考试表: Examinations
-- #
-- # +--------------+---------+
-- #| Column Name  | Type    |
-- #+--------------+---------+
-- #| student_id   | int     |
-- #| subject_name | varchar |
-- #+--------------+---------+
-- #这张表压根没有主键，可能会有重复行。
-- #学生表里的一个学生修读科目表里的每一门科目，而这张考试表的每一行记录就表示学生表里的某个学生参加了一次科目表里某门科目的测试。
-- #
-- #
-- #
-- #
-- # 要求写一段 SQL 语句，查询出每个学生参加每一门科目测试的次数，结果按 student_id 和 subject_name 排序。
-- #
-- # 查询结构格式如下所示：
-- #
-- # Students table:
-- #+------------+--------------+
-- #| student_id | student_name |
-- #+------------+--------------+
-- #| 1          | Alice        |
-- #| 2          | Bob          |
-- #| 13         | John         |
-- #| 6          | Alex         |
-- #+------------+--------------+
-- #Subjects table:
-- #+--------------+
-- #| subject_name |
-- #+--------------+
-- #| Math         |
-- #| Physics      |
-- #| Programming  |
-- #+--------------+
-- #Examinations table:
-- #+------------+--------------+
-- #| student_id | subject_name |
-- #+------------+--------------+
-- #| 1          | Math         |
-- #| 1          | Physics      |
-- #| 1          | Programming  |
-- #| 2          | Programming  |
-- #| 1          | Physics      |
-- #| 1          | Math         |
-- #| 13         | Math         |
-- #| 13         | Programming  |
-- #| 13         | Physics      |
-- #| 2          | Math         |
-- #| 1          | Math         |
-- #+------------+--------------+
-- #Result table:
-- #+------------+--------------+--------------+----------------+
-- #| student_id | student_name | subject_name | attended_exams |
-- #+------------+--------------+--------------+----------------+
-- #| 1          | Alice        | Math         | 3              |
-- #| 1          | Alice        | Physics      | 2              |
-- #| 1          | Alice        | Programming  | 1              |
-- #| 2          | Bob          | Math         | 1              |
-- #| 2          | Bob          | Physics      | 0              |
-- #| 2          | Bob          | Programming  | 1              |
-- #| 6          | Alex         | Math         | 0              |
-- #| 6          | Alex         | Physics      | 0              |
-- #| 6          | Alex         | Programming  | 0              |
-- #| 13         | John         | Math         | 1              |
-- #| 13         | John         | Physics      | 1              |
-- #| 13         | John         | Programming  | 1              |
-- #+------------+--------------+--------------+----------------+
-- #结果表需包含所有学生和所有科目（即便测试次数为0）：
-- #Alice 参加了 3 次数学测试, 2 次物理测试，以及 1 次编程测试；
-- #Bob 参加了 1 次数学测试, 1 次编程测试，没有参加物理测试；
-- #Alex 啥测试都没参加；
-- #John  参加了数学、物理、编程测试各 1 次。
-- #
-- # 👍 26 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below

SELECT a.student_id, a.student_name, b.subject_name, COUNT(e.subject_name) AS attended_exams
FROM Students a CROSS JOIN Subjects b
                LEFT JOIN Examinations e ON a.student_id = e.student_id AND b.subject_name = e.subject_name
GROUP BY a.student_id, b.subject_name
ORDER BY a.student_id, b.subject_name;


-- #leetcode submit region end(Prohibit modification and deletion)

--ME
select s.student_id,
       s.student_name,
       sub.subject_name,
       sum(if(sub.subject_name = e.subject_name, 1, 0)) as attended_exams
from Students s
         left join Examinations as e on e.student_id = s.student_id,
     Subjects as sub
group by s.student_id, sub.subject_name
order by student_id, subject_name;