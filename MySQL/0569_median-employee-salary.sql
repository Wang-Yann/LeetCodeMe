-- @Author        : Rock Wayne
-- @Created       : 2020-07-28 20:36:05
-- @Last Modified : 2020-07-28 20:36:05

-- #Employee 表包含所有员工。Employee 表有三列：员工Id，公司名和薪水。
-- #
-- # +-----+------------+--------+
-- #|Id   | Company    | Salary |
-- #+-----+------------+--------+
-- #|1    | A          | 2341   |
-- #|2    | A          | 341    |
-- #|3    | A          | 15     |
-- #|4    | A          | 15314  |
-- #|5    | A          | 451    |
-- #|6    | A          | 513    |
-- #|7    | B          | 15     |
-- #|8    | B          | 13     |
-- #|9    | B          | 1154   |
-- #|10   | B          | 1345   |
-- #|11   | B          | 1221   |
-- #|12   | B          | 234    |
-- #|13   | C          | 2345   |
-- #|14   | C          | 2645   |
-- #|15   | C          | 2645   |
-- #|16   | C          | 2652   |
-- #|17   | C          | 65     |
-- #+-----+------------+--------+
-- #
-- #
-- # 请编写SQL查询来查找每个公司的薪水中位数。挑战点：你是否可以在不使用任何内置的SQL函数的情况下解决此问题。
-- #
-- # +-----+------------+--------+
-- #|Id   | Company    | Salary |
-- #+-----+------------+--------+
-- #|5    | A          | 451    |
-- #|6    | A          | 513    |
-- #|12   | B          | 234    |
-- #|9    | B          | 1154   |
-- #|14   | C          | 2645   |
-- #+-----+------------+--------+
-- #
-- # 👍 22 👎 0
--


-- #leetcode submit region begin(Prohibit modification and deletion)

-- # Write your MySQL query statement below

select b.Id, b.Company, b.Salary
from (
         select Id,
                Company,
                Salary,
                case @com   when Company then @rk := @rk + 1 else @rk := 1 end rk,
                @com := Company
         from Employee as e,
              (select @rk := 0, @com := '') a
         order by company, Salary) b
         left join
     (select Company, count(1) / 2 as cnt from Employee group by Company) c
     on b.Company = c.Company
where b.rk in (cnt + 0.5, cnt + 1, cnt);


-- #leetcode submit region end(Prohibit modification and deletion)
--
-- 创建两个新的column：一个在每个company中排序，产生row number; 另一个column是count这个company有多少员工
-- 最后计算row_number = 中位数


SELECT Id, Company, Salary
FROM
    (
        SELECT Id, Company, Salary,
               ROW_NUMBER() OVER (PARTITION BY Company ORDER BY Salary ASC, Id ASC) AS row_num,
               COUNT(Id) OVER (PARTITION BY Company) AS count_id
        FROM Employee
    ) as ei
WHERE ei.row_num IN (FLOOR((ei.count_id + 1)/2), FLOOR((ei.count_id + 2)/2));