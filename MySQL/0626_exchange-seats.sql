--
--
-- #小美是一所中学的信息科技老师，她有一张 seat 座位表，平时用来储存学生名字和与他们相对应的座位 id。
-- #
-- # 其中纵列的 id 是连续递增的
-- #
-- # 小美想改变相邻俩学生的座位。
-- #
-- # 你能不能帮她写一个 SQL query 来输出小美想要的结果呢？
-- #
-- #
-- #
-- # 示例：
-- #
-- #
-- #+---------+---------+
-- #|    id   | student |
-- #+---------+---------+
-- #|    1    | Abbot   |
-- #|    2    | Doris   |
-- #|    3    | Emerson |
-- #|    4    | Green   |
-- #|    5    | Jeames  |
-- #+---------+---------+
-- #
-- #
-- # 假如数据输入的是上表，则输出结果如下：
-- #
-- #
-- #+---------+---------+
-- #|    id   | student |
-- #+---------+---------+
-- #|    1    | Doris   |
-- #|    2    | Abbot   |
-- #|    3    | Green   |
-- #|    4    | Emerson |
-- #|    5    | Jeames  |
-- #+---------+---------+
-- #
-- # 注意：
-- #
-- # 如果学生人数是奇数，则不需要改变最后一个同学的座位。
-- #
--
create table seat
(
    id      int auto_increment primary key,
    student varchar(30)
);

insert into seat(id, student)
values (1, 'Abbot '),
       (2, 'Doris '),
       (3, 'Emerso'),
       (4, 'Green '),
       (5, 'Jeames');

select (
    case
        when t.id % 2 = 1 and id != seat_cnt then
                id + 1
        when t.id % 2 = 1 and id = seat_cnt then
            id
        else
                id - 1
        end) as id
     , student
from seat as t,
     (select count(1) as seat_cnt from seat) as max_cnt
order by id;


select s1.id, coalesce(s2.student, s1.student) as student
from seat s1
         left join seat s2
                   on ((s1.id + 1) ^ 1) - 1 = s2.id
order by s1.id;