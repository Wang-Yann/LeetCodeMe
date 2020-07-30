-- @Author        : Rock Wayne
-- @Created       : 2020-07-30 23:22:07
-- @Last Modified : 2020-07-30 23:22:07
--
-- #表 point 保存了一些点在 x 轴上的坐标，这些坐标都是整数。
-- #
-- #
-- #
-- # 写一个查询语句，找到这些点中最近两个点之间的距离。
-- #
-- #
-- #
-- # | x   |
-- #|-----|
-- #| -1  |
-- #| 0   |
-- #| 2   |
-- #
-- #
-- #
-- #
-- # 最近距离显然是 '1' ，是点 '-1' 和 '0' 之间的距离。所以输出应该如下：
-- #
-- #
-- #
-- # | shortest|
-- #|---------|
-- #| 1       |
-- #
-- #
-- #
-- #
-- # 注意：每个点都与其他点坐标不同，表 table 不会有重复坐标出现。
-- #
-- #
-- #
-- # 进阶：如果这些点在 x 轴上从左到右都有一个编号，输出结果时需要输出最近点对的编号呢？
-- #
-- #
-- # 👍 15 👎 0
	 


#leetcode submit region begin(Prohibit modification and deletion)
# Write your MySQL query statement below

select min(l-x) shortest
from (
        select x,lead(x,1) over(order by x) l
        from point
    ) t1;

-- #leetcode submit region end(Prohibit modification and deletion)

SELECT
    MIN(ABS(p1.x - p2.x)) AS shortest
FROM
    point p1
        JOIN
    point p2 ON p1.x != p2.x
;
