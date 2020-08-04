-- @Author        : Rock Wayne
-- @Created       : 2020-08-04 21:09:45
-- @Last Modified : 2020-08-04 21:09:45
--
-- #Table: Failed
-- #
-- # +--------------+---------+
-- #| Column Name  | Type    |
-- #+--------------+---------+
-- #| fail_date    | date    |
-- #+--------------+---------+
-- #该表主键为 fail_date。
-- #该表包含失败任务的天数.
-- #
-- #
-- # Table: Succeeded
-- #
-- # +--------------+---------+
-- #| Column Name  | Type    |
-- #+--------------+---------+
-- #| success_date | date    |
-- #+--------------+---------+
-- #该表主键为 success_date。
-- #该表包含成功任务的天数.
-- #
-- #
-- #
-- #
-- # 系统 每天 运行一个任务。每个任务都独立于先前的任务。任务的状态可以是失败或是成功。
-- #
-- # 编写一个 SQL 查询 2019-01-01 到 2019-12-31 期间任务连续同状态 period_state 的起止日期（start_date 和
-- #end_date）。即如果任务失败了，就是失败状态的起止日期，如果任务成功了，就是成功状态的起止日期。
-- #
-- # 最后结果按照起始日期 start_date 排序
-- #
-- # 查询结果样例如下所示:
-- #
-- # Failed table:
-- #+-------------------+
-- #| fail_date         |
-- #+-------------------+
-- #| 2018-12-28        |
-- #| 2018-12-29        |
-- #| 2019-01-04        |
-- #| 2019-01-05        |
-- #+-------------------+
-- #
-- #Succeeded table:
-- #+-------------------+
-- #| success_date      |
-- #+-------------------+
-- #| 2018-12-30        |
-- #| 2018-12-31        |
-- #| 2019-01-01        |
-- #| 2019-01-02        |
-- #| 2019-01-03        |
-- #| 2019-01-06        |
-- #+-------------------+
-- #
-- #
-- #Result table:
-- #+--------------+--------------+--------------+
-- #| period_state | start_date   | end_date     |
-- #+--------------+--------------+--------------+
-- #| succeeded    | 2019-01-01   | 2019-01-03   |
-- #| failed       | 2019-01-04   | 2019-01-05   |
-- #| succeeded    | 2019-01-06   | 2019-01-06   |
-- #+--------------+--------------+--------------+
-- #
-- #结果忽略了 2018 年的记录，因为我们只关心从 2019-01-01 到 2019-12-31 的记录
-- #从 2019-01-01 到 2019-01-03 所有任务成功，系统状态为 "succeeded"。
-- #从 2019-01-04 到 2019-01-05 所有任务失败，系统状态为 "failed"。
-- #从 2019-01-06 到 2019-01-06 所有任务成功，系统状态为 "succeeded"。
-- #
-- # 👍 11 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below
-- 和行号取插值太取巧了
SELECT
    period_state,
    MIN(date) start_date,
    MAX(date) end_date
FROM
    ((SELECT
          'succeeded' period_state,
          success_date date,
          (DATEDIFF(success_date, '1997-01-01')) - row_number() OVER(ORDER BY success_date) num
      FROM Succeeded
      WHERE success_date BETWEEN '2019-01-01' AND '2019-12-31')
     UNION ALL
     (SELECT
          'failed' period_state,
          fail_date date,
          (DATEDIFF(fail_date, '1997-01-01')) - row_number() OVER(ORDER BY fail_date) num
      FROM Failed
      WHERE fail_date BETWEEN '2019-01-01' AND '2019-12-31')) t1
GROUP BY num, period_state
ORDER BY start_date;

-- #leetcode submit region end(Prohibit modification and deletion)



SELECT period_state, MIN(date) as start_date, MAX(date) as end_date
FROM (
         SELECT
             success_date AS date,
             'succeeded' AS period_state,
             IF(DATEDIFF(@pre_date, @pre_date := success_date) = -1, @id, @id := @id+1) AS id
         FROM Succeeded, (SELECT @id := 0, @pre_date := NULL) AS temp
         UNION
         SELECT
             fail_date AS date,
             'failed' AS period_state,
             IF(DATEDIFF(@pre_date, @pre_date := fail_date) = -1, @id, @id := @id+1) AS id
         FROM Failed, (SELECT @id := 0, @pre_date := NULL) AS temp
     ) T  WHERE date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY T.id
ORDER BY start_date ASC;
