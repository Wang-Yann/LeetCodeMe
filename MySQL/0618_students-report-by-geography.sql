-- @Author        : Rock Wayne
-- @Created       : 2020-08-02 21:08:28
-- @Last Modified : 2020-08-02 21:08:28
--
-- #一所美国大学有来自亚洲、欧洲和美洲的学生，他们的地理信息存放在如下 student 表中。
-- #
-- #
-- #
-- # | name   | continent |
-- #|--------|-----------|
-- #| Jack   | America   |
-- #| Pascal | Europe    |
-- #| Xi     | Asia      |
-- #| Jane   | America   |
-- #
-- #
-- #
-- #
-- # 写一个查询语句实现对大洲（continent）列的 透视表 操作，使得每个学生按照姓名的字母顺序依次排列在对应的大洲下面。输出的标题应依次为美洲（Ameri
-- #ca）、亚洲（Asia）和欧洲（Europe）。数据保证来自美洲的学生不少于来自亚洲或者欧洲的学生。
-- #
-- #
-- #
-- # 对于样例输入，它的对应输出是：
-- #
-- #
-- #
-- # | America | Asia | Europe |
-- #|---------|------|--------|
-- #| Jack    | Xi   | Pascal |
-- #| Jane    |      |        |
-- #
-- #
-- #
-- #
-- # 进阶：如果不能确定哪个大洲的学生数最多，你可以写出一个查询去生成上述学生报告吗？
-- #
-- #
-- # 👍 14 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below


-- 2.用IF或CASE WHEN将行转列，过程会产生大量NULL，用聚合如MAX/MIN，均可去除NULL
SELECT
    MAX(IF(continent = 'America', name, NULL)) America,
    MAX(IF(continent = 'Asia', name, NULL)) Asia,
    MAX(IF(continent = 'Europe', name, NULL)) Europe
FROM
    (
-- 1.每个continent按name排序并记序号
        SELECT continent,name,ROW_NUMBER() OVER(PARTITION BY continent ORDER BY name) rn FROM student
    ) T
-- 3.按rn聚合
GROUP BY rn;

-- #leetcode submit region end(Prohibit modification and deletion)

select America, Asia, Europe
from (select @as := 0, @am := 0, @eu := 0) t,
     (select @as := @as + 1 as asid, name as Asia
      from student
      where continent = 'Asia'
      order by Asia) as t1
         right join
     (SELECT @am := @am + 1 AS amid,
             name           AS America
      FROM student
      WHERE continent = 'America'
      ORDER BY America) AS t2 ON asid = amid
         LEFT JOIN
     (SELECT @eu := @eu + 1 AS euid,
             name           AS Europe
      FROM student
      WHERE continent = 'Europe'
      ORDER BY Europe) AS t3 ON amid = euid
;



select America,Asia,Europe
from(
        select row_number() over(order by name) as rn,name as America from student
        where continent='America'
    ) a left join(
    select row_number() over(order by name) as rn,name as Asia from student
    where continent='Asia'
) b on a.rn=b.rn left join(
    select row_number() over(order by name) as rn,name as Europe from student
    where continent='Europe'
) c on a.rn=c.rn;