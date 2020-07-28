-- @Author        : Rock Wayne
-- @Created       : 2020-07-29 00:13:23
-- @Last Modified : 2020-07-29 00:13:23
--
-- #一所大学有 2 个数据表，分别是 student 和 department ，这两个表保存着每个专业的学生数据和院系数据。
-- #
-- # 写一个查询语句，查询 department 表中每个专业的学生人数 （即使没有学生的专业也需列出）。
-- #
-- # 将你的查询结果按照学生人数降序排列。 如果有两个或两个以上专业有相同的学生数目，将这些部门按照部门名字的字典序从小到大排列。
-- #
-- # student 表格如下：
-- #
-- # | Column Name  | Type      |
-- #|--------------|-----------|
-- #| student_id   | Integer   |
-- #| student_name | String    |
-- #| gender       | Character |
-- #| dept_id      | Integer   |
-- #
-- #
-- # 其中， student_id 是学生的学号， student_name 是学生的姓名， gender 是学生的性别， dept_id 是学生所属专业的专业编
-- #号。
-- #
-- # department 表格如下：
-- #
-- # | Column Name | Type    |
-- #|-------------|---------|
-- #| dept_id     | Integer |
-- #| dept_name   | String  |
-- #
-- #
-- # dept_id 是专业编号， dept_name 是专业名字。
-- #
-- # 这里是一个示例输入：
-- #student 表格：
-- #
-- # | student_id | student_name | gender | dept_id |
-- #|------------|--------------|--------|---------|
-- #| 1          | Jack         | M      | 1       |
-- #| 2          | Jane         | F      | 1       |
-- #| 3          | Mark         | M      | 2       |
-- #
-- #
-- # department 表格：
-- #
-- # | dept_id | dept_name   |
-- #|---------|-------------|
-- #| 1       | Engineering |
-- #| 2       | Science     |
-- #| 3       | Law         |
-- #
-- #
-- # 示例输出为：
-- #
-- # | dept_name   | student_number |
-- #|-------------|----------------|
-- #| Engineering | 2              |
-- #| Science     | 1              |
-- #| Law         | 0              |
-- #
-- # 👍 8 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below


select dp.dept_name as dept_name, ifnull(s.cnt,0) as student_number
from department dp
         left join (
    select dept_id, count(student_id) as cnt
    from student
    group by dept_id
) as s on dp.dept_id = s.dept_id
order by student_number desc, dept_name asc;

-- #leetcode submit region end(Prohibit modification and deletion)
	