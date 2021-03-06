
--
-- #Trips 表中存所有出租车的行程信息。每段行程有唯一键 Id，Client_Id 和 Driver_Id 是 Users 表中 Users_Id 的外键。S
-- #tatus 是枚举类型，枚举成员为 (‘completed’, ‘cancelled_by_driver’, ‘cancelled_by_client’)。
-- #
-- # +----+-----------+-----------+---------+--------------------+----------+
-- #| Id | Client_Id | Driver_Id | City_Id |        Status      |Request_at|
-- #+----+-----------+-----------+---------+--------------------+----------+
-- #| 1  |     1     |    10     |    1    |     completed      |2013-10-01|
-- #| 2  |     2     |    11     |    1    | cancelled_by_driver|2013-10-01|
-- #| 3  |     3     |    12     |    6    |     completed      |2013-10-01|
-- #| 4  |     4     |    13     |    6    | cancelled_by_client|2013-10-01|
-- #| 5  |     1     |    10     |    1    |     completed      |2013-10-02|
-- #| 6  |     2     |    11     |    6    |     completed      |2013-10-02|
-- #| 7  |     3     |    12     |    6    |     completed      |2013-10-02|
-- #| 8  |     2     |    12     |    12   |     completed      |2013-10-03|
-- #| 9  |     3     |    10     |    12   |     completed      |2013-10-03|
-- #| 10 |     4     |    13     |    12   | cancelled_by_driver|2013-10-03|
-- #+----+-----------+-----------+---------+--------------------+----------+
-- #
-- #
-- # Users 表存所有用户。每个用户有唯一键 Users_Id。Banned 表示这个用户是否被禁止，Role 则是一个表示（‘client’, ‘drive
-- #r’, ‘partner’）的枚举类型。
-- #
-- # +----------+--------+--------+
-- #| Users_Id | Banned |  Role  |
-- #+----------+--------+--------+
-- #|    1     |   No   | client |
-- #|    2     |   Yes  | client |
-- #|    3     |   No   | client |
-- #|    4     |   No   | client |
-- #|    10    |   No   | driver |
-- #|    11    |   No   | driver |
-- #|    12    |   No   | driver |
-- #|    13    |   No   | driver |
-- #+----------+--------+--------+
-- #
-- #
-- # 写一段 SQL 语句查出 2013年10月1日 至 2013年10月3日 期间非禁止用户的取消率。基于上表，你的 SQL 语句应返回如下结果，取消率（Can
-- #cellation Rate）保留两位小数。
-- #
-- # 取消率的计算方式如下：(被司机或乘客取消的非禁止用户生成的订单数量) / (非禁止用户生成的订单总数)
-- #
-- # +------------+-------------------+
-- #|     Day    | Cancellation Rate |
-- #+------------+-------------------+
-- #| 2013-10-01 |       0.33        |
-- #| 2013-10-02 |       0.00        |
-- #| 2013-10-03 |       0.50        |
-- #+------------+-------------------+
-- #
-- #
-- # 致谢:
-- #非常感谢 @cak1erlizhou 详细的提供了这道题和相应的测试用例。
-- #


create table Trips
(
    Id         int primary key auto_increment,
    Client_Id  int,
    Driver_Id  int,
    City_Id    int,
    Statue     enum ('completed', 'cancelled_by_driver', 'cancelled_by_client') NOT NULL,
    Request_at DATE                                                             NOT NULL
);
create table Users
(
    Users_Id int primary key auto_increment,
    Banned   char(4),
    Role     enum ('client', 'driver', 'partner') NOT NULL
);

insert into Trips(Id, Client_Id, Driver_Id, City_Id, Status, Request_at)
values (1, 1, 10, 1, 'completed', '2013-10-01'),
       (2, 2, 11, 1, 'cancelled_by_driver', '2013-10-01'),
       (3, 3, 12, 6, 'completed', '2013-10-01'),
       (4, 4, 13, 6, 'cancelled_by_client', '2013-10-01'),
       (5, 1, 10, 1, 'completed', '2013-10-02'),
       (6, 2, 11, 6, 'completed', '2013-10-02'),
       (7, 3, 12, 6, 'completed', '2013-10-02'),
       (8, 2, 12, 12, 'completed', '2013-10-03'),
       (9, 3, 10, 12, 'completed', '2013-10-03'),
       (10, 4, 13, 12, 'cancelled_by_driver', '2013-10-03');

insert into Users(Users_Id, Banned, Role)
values (1, 'No', 'client'),
       (2, 'Yes', 'client'),
       (3, 'No', 'client'),
       (4, 'No', 'client'),
       (10, 'No', 'driver'),
       (11, 'No', 'driver'),
       (12, 'No', 'driver'),
       (13, 'No', 'driver');

-- # 连接条件是行程对应的乘客非禁止且司机非禁止
select t.Request_at as 'Day', round(t.cancelCnt / t.totaOrders, 2) as 'Cancellation Rate'
from (
         select t1.Request_at,
                count(t1.Id) as totaOrders,
                SUM(case t1.Status
                        when 'completed'
                            then 0
                        else 1
                    end)     as cancelCnt
         from Trips t1
         where t1.Request_at between '2013-10-01' and '2013-10-03'
           and t1.Client_Id not in (select Users_Id from Users where Banned = 'YES')
         group by t1.Request_at
     ) as t;


select t.Request_at                                                                 as 'Day',
       round(sum(case when t.Status = 'completed' then 0 else 1 end) / count(*), 2) as 'Cancellation Rate'
from Trips t
         inner join Users u
                    on t.Client_Id = u.Users_Id and u.Banned = 'No'
where t.Request_at between '2013-10-01' and '2013-10-03'
group by t.Request_at;
