-- @Author        : Rock Wayne
-- @Created       : 2020-08-07 22:33:28
-- @Last Modified : 2020-08-07 22:33:28
--
-- #表: TVProgram
-- #
-- #
-- #+---------------+---------+
-- #| Column Name   | Type    |
-- #+---------------+---------+
-- #| program_date  | date    |
-- #| content_id    | int     |
-- #| channel       | varchar |
-- #+---------------+---------+
-- #(program_date, content_id) 是该表主键.
-- #该表包含电视上的节目信息.
-- #content_id 是电视一些频道上的节目的 id.
-- #
-- #
-- #
-- # 表: Content
-- #
-- #
-- #+------------------+---------+
-- #| Column Name      | Type    |
-- #+------------------+---------+
-- #| content_id       | varchar |
-- #| title            | varchar |
-- #| Kids_content     | enum    |
-- #| content_type     | varchar |
-- #+------------------+---------+
-- #content_id 是该表主键.
-- #Kids_content 是枚举类型, 取值为('Y', 'N'), 其中:
-- #'Y' 表示儿童适宜内容, 而'N'表示儿童不宜内容.
-- #content_type 表示内容的类型, 比如电影, 电视剧等.
-- #
-- #
-- #
-- #
-- # 写一个 SQL 语句, 报告在 2020 年 6 月份播放的儿童适宜电影的去重电影名.
-- #
-- # 返回的结果表单没有顺序要求.
-- #
-- # 查询结果的格式如下例所示.
-- #
-- #
-- #
-- #
-- #TVProgram 表:
-- #+--------------------+--------------+-------------+
-- #| program_date       | content_id   | channel     |
-- #+--------------------+--------------+-------------+
-- #| 2020-06-10 08:00   | 1            | LC-Channel  |
-- #| 2020-05-11 12:00   | 2            | LC-Channel  |
-- #| 2020-05-12 12:00   | 3            | LC-Channel  |
-- #| 2020-05-13 14:00   | 4            | Disney Ch   |
-- #| 2020-06-18 14:00   | 4            | Disney Ch   |
-- #| 2020-07-15 16:00   | 5            | Disney Ch   |
-- #+--------------------+--------------+-------------+
-- #
-- #Content 表:
-- #+------------+----------------+---------------+---------------+
-- #| content_id | title          | Kids_content  | content_type  |
-- #+------------+----------------+---------------+---------------+
-- #| 1          | Leetcode Movie | N             | Movies        |
-- #| 2          | Alg. for Kids  | Y             | Series        |
-- #| 3          | Database Sols  | N             | Series        |
-- #| 4          | Aladdin        | Y             | Movies        |
-- #| 5          | Cinderella     | Y             | Movies        |
-- #+------------+----------------+---------------+---------------+
-- #
-- #Result 表:
-- #+--------------+
-- #| title        |
-- #+--------------+
-- #| Aladdin      |
-- #+--------------+
-- #"Leetcode Movie" 是儿童不宜的电影.
-- #"Alg. for Kids" 不是电影.
-- #"Database Sols" 不是电影
-- #"Alladin" 是电影, 儿童适宜, 并且在 2020 年 6 月份播放.
-- #"Cinderella" 不在 2020 年 6 月份播放.
-- #
-- # 👍 1 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below


select distinct title
from TVProgram as tp
         join Content as c on tp.content_id = c.content_id
where c.content_type = 'Movies'
  and c.Kids_content = 'Y'
  and date_format(program_date, '%Y-%m') = '2020-06';

-- #leetcode submit region end(Prohibit modification and deletion)
	