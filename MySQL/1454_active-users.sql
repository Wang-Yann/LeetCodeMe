-- @Author        : Rock Wayne
-- @Created       : 2020-08-06 23:43:57
-- @Last Modified : 2020-08-06 23:43:57
--
-- #表 Accounts:
-- #
-- # +---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| id            | int     |
-- #| name          | varchar |
-- #+---------------+---------+
-- #id 是该表主键.
-- #该表包含账户 id 和账户的用户名.
-- #
-- #
-- #
-- #
-- # 表 Logins:
-- #
-- # +---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| id            | int     |
-- #| login_date    | date    |
-- #+---------------+---------+
-- #该表无主键, 可能包含重复项.
-- #该表包含登录用户的账户 id 和登录日期. 用户也许一天内登录多次.
-- #
-- #
-- #
-- #
-- # 写一个 SQL 查询, 找到活跃用户的 id 和 name.
-- #
-- # 活跃用户是指那些至少连续 5 天登录账户的用户.
-- #
-- # 返回的结果表按照 id 排序.
-- #
-- # 结果表格式如下例所示:
-- #
-- # Accounts 表:
-- #+----+----------+
-- #| id | name     |
-- #+----+----------+
-- #| 1  | Winston  |
-- #| 7  | Jonathan |
-- #+----+----------+
-- #
-- #Logins 表:
-- #+----+------------+
-- #| id | login_date |
-- #+----+------------+
-- #| 7  | 2020-05-30 |
-- #| 1  | 2020-05-30 |
-- #| 7  | 2020-05-31 |
-- #| 7  | 2020-06-01 |
-- #| 7  | 2020-06-02 |
-- #| 7  | 2020-06-02 |
-- #| 7  | 2020-06-03 |
-- #| 1  | 2020-06-07 |
-- #| 7  | 2020-06-10 |
-- #+----+------------+
-- #
-- #Result 表:
-- #+----+----------+
-- #| id | name     |
-- #+----+----------+
-- #| 7  | Jonathan |
-- #+----+----------+
-- #id = 1 的用户 Winston 仅仅在不同的 2 天内登录了 2 次, 所以, Winston 不是活跃用户.
-- #id = 7 的用户 Jonathon 在不同的 6 天内登录了 7 次, , 6 天中有 5 天是连续的, 所以, Jonathan 是活跃用户.
-- #
-- #
-- #
-- #
-- # 后续问题:
-- #如果活跃用户是那些至少连续 n 天登录账户的用户, 你能否写出通用的解决方案?
-- # 👍 8 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below
-- AC

select distinct t.id, a.name
from (
         select id, count(id) as days
         from (
                  select id,
                         login_date,
                         DATEDIFF(login_date, '2000-01-01') - dense_rank() over (partition by id order by login_date) as num
                  from (select distinct id, login_date from Logins) as di
              ) as ti
         group by id, num
     ) as t
         join Accounts as a on t.id = a.id
where days >= 5 order by t.id;

-- #leetcode submit region end(Prohibit modification and deletion)



SELECT DISTINCT r.id,
                r.name
FROM (SELECT a_l.id,
             a_l.name,
             @accu := CASE
                          WHEN a_l.name = @prev AND
                               DATEDIFF(a_l.login_date, @login_date) = 1
                              THEN @accu + 1
                          ELSE 1
                 END                       AS accu,
             @prev := a_l.name             AS prev,
             @login_date := a_l.login_date AS login_date
      FROM (
            (SELECT DISTINCT a.id,
                             a.name,
                             l.login_date
             FROM Accounts a
                      LEFT JOIN Logins l
                                ON a.id = l.id
             ORDER BY a.id,
                      a.name,
                      l.login_date) a_l,
               (SELECT @accu := 0,
            @prev := '',
            @login_date := '') init
               )
     ) r
WHERE r.accu = 5;
