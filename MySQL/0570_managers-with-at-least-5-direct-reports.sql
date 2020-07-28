-- @Author        : Rock Wayne
-- @Created       : 2020-07-28 21:29:37
-- @Last Modified : 2020-07-28 21:29:37

-- #Employee 表包含所有员工和他们的经理。每个员工都有一个 Id，并且还有一列是经理的 Id。
-- #
-- # +------+----------+-----------+----------+
-- #|Id    |Name 	  |Department |ManagerId |
-- #+------+----------+-----------+----------+
-- #|101   |John 	  |A 	      |null      |
-- #|102   |Dan 	  |A 	      |101       |
-- #|103   |James 	  |A 	      |101       |
-- #|104   |Amy 	  |A 	      |101       |
-- #|105   |Anne 	  |A 	      |101       |
-- #|106   |Ron 	  |B 	      |101       |
-- #+------+----------+-----------+----------+
-- #
-- #
-- # 给定 Employee 表，请编写一个SQL查询来查找至少有5名直接下属的经理。对于上表，您的SQL查询应该返回：
-- #
-- # +-------+
-- #| Name  |
-- #+-------+
-- #| John  |
-- #+-------+
-- #
-- #
-- # 注意:
-- #没有人是自己的下属。
-- # 👍 10 👎 0
--
--
--
-- #leetcode submit region begin(Prohibit modification and deletion)
-- # Write your MySQL query statement below



select e1.Name from Employee as e1 where e1.Id in (
    select ManagerId from Employee e group by ManagerId having ManagerId is not NULL and count(ManagerId)>=5
)

-- #leetcode submit region end(Prohibit modification and deletion)
	