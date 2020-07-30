-- @Author        : Rock Wayne
-- @Created       : 2020-07-30 23:50:38
-- @Last Modified : 2020-07-30 23:50:38
--
-- #表 point_2d 保存了所有点（多于 2 个点）的坐标 (x,y) ，这些点在平面上两两不重合。
-- #
-- #
-- #
-- # 写一个查询语句找到两点之间的最近距离，保留 2 位小数。
-- #
-- #
-- #
-- # | x  | y  |
-- #|----|----|
-- #| -1 | -1 |
-- #| 0  | 0  |
-- #| -1 | -2 |
-- #
-- #
-- #
-- #
-- # 最近距离在点 (-1,-1) 和(-1,2) 之间，距离为 1.00 。所以输出应该为：
-- #
-- #
-- #
-- # | shortest |
-- #|----------|
-- #| 1.00     |
-- #
-- #
-- #
-- #
-- # 注意：任意点之间的最远距离小于 10000 。
-- #
-- #
-- # 👍 9 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below

SELECT
    ROUND(SQRT(MIN((POW(p1.x - p2.x, 2) + POW(p1.y - p2.y, 2)))),2) AS shortest
FROM
    point_2d p1
        JOIN
    point_2d p2 ON (p1.x < p2.x) OR (p1.x = p2.x AND p1.y < p2.y);




-- #leetcode submit region end(Prohibit modification and deletion)

SELECT
    min(round(sqrt(power(p1.x - p2.x,2)+power(p1.y - p2.y,2)),2)) AS shortest
FROM
    point_2d p1
        JOIN
    point_2d p2 ON not (p1.x = p2.x and p1.y=p2.y)
;