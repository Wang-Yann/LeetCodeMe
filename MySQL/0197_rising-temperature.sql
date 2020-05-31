

-- #给定一个 Weather 表，编写一个 SQL 查询，来查找与之前（昨天的）日期相比温度更高的所有日期的 Id。
-- #
-- # +---------+------------------+------------------+
-- #| Id(INT) | RecordDate(DATE) | Temperature(INT) |
-- #+---------+------------------+------------------+
-- #|       1 |       2015-01-01 |               10 |
-- #|       2 |       2015-01-02 |               25 |
-- #|       3 |       2015-01-03 |               20 |
-- #|       4 |       2015-01-04 |               30 |
-- #+---------+------------------+------------------+
-- #
-- # 例如，根据上述给定的 Weather 表格，返回如下 Id:
-- #
-- # +----+
-- #| Id |
-- #+----+
-- #|  2 |
-- #|  4 |
-- #+----+
-- #
--

select w1.Id
from Weather w1
         join Weather w2 on w1.Temperature > w2.Temperature and DATE_SUB(w1.RecordDate, INTERVAL 1 day) = w2.RecordDate;
select w1.Id
from Weather w1
         join Weather w2 on w1.Temperature > w2.Temperature and TO_DAYS(w1.RecordDate) = TO_DAYS(w2.RecordDate) + 1;
select w1.Id
from Weather w1
         join Weather w2 on w1.Temperature > w2.Temperature and DATEDIFF(w1.RecordDate, w2.RecordDate) = 1;