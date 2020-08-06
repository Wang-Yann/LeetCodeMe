-- @Author        : Rock Wayne
-- @Created       : 2020-08-06 21:20:34
-- @Last Modified : 2020-08-06 21:20:34
--
-- #表: UserActivity
-- #
-- #
-- #+---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| username      | varchar |
-- #| activity      | varchar |
-- #| startDate     | Date    |
-- #| endDate       | Date    |
-- #+---------------+---------+
-- #该表不包含主键
-- #该表包含每个用户在一段时间内进行的活动的信息
-- #名为 username 的用户在 startDate 到 endDate 日内有一次活动
-- #
-- #
-- #
-- #
-- # 写一条SQL查询展示每一位用户 最近第二次 的活动
-- #
-- # 如果用户仅有一次活动，返回该活动
-- #
-- # 一个用户不能同时进行超过一项活动，以 任意 顺序返回结果
-- #
-- # 下面是查询结果格式的例子：
-- #
-- #
-- #UserActivity 表:
-- #+------------+--------------+-------------+-------------+
-- #| username   | activity     | startDate   | endDate     |
-- #+------------+--------------+-------------+-------------+
-- #| Alice      | Travel       | 2020-02-12  | 2020-02-20  |
-- #| Alice      | Dancing      | 2020-02-21  | 2020-02-23  |
-- #| Alice      | Travel       | 2020-02-24  | 2020-02-28  |
-- #| Bob        | Travel       | 2020-02-11  | 2020-02-18  |
-- #+------------+--------------+-------------+-------------+
-- #
-- #Result 表:
-- #+------------+--------------+-------------+-------------+
-- #| username   | activity     | startDate   | endDate     |
-- #+------------+--------------+-------------+-------------+
-- #| Alice      | Dancing      | 2020-02-21  | 2020-02-23  |
-- #| Bob        | Travel       | 2020-02-11  | 2020-02-18  |
-- #+------------+--------------+-------------+-------------+
-- #
-- #Alice 最近第二次的活动是从 2020-02-24 到 2020-02-28 的旅行, 在此之前的 2020-02-21 到 2020-02-23 她进行
-- #了舞蹈
-- #Bob 只有一条记录，我们就取这条记录
-- #
-- # 👍 1 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below

select u.username, u.activity, u.startDate, u.endDate
from (
         select *,
                rank() over (partition by username order by startDate desc ) as rnk,
                count(*) over (partition by username ) as                    cnt
         from UserActivity
     ) as u
where rnk = 2
   or cnt = 1;


-- #leetcode submit region end(Prohibit modification and deletion)
	