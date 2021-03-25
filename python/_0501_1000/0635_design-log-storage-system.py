#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-30 17:37:42
# @Last Modified : 2020-07-30 17:37:42
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 你将获得多条日志，每条日志都有唯一的 id 和 timestamp，timestamp 是形如 Year:Month:Day:Hour:Minute:Sec
# ond 的字符串，例如 2017:01:01:23:59:59，所有值域都是零填充的十进制数。 
# 
#  设计一个日志存储系统实现如下功能： 
# 
#  void Put(int id, string timestamp)：给定日志的 id 和 timestamp，将这个日志存入你的存储系统中。 
# 
#  
# 
#  int[] Retrieve(String start, String end, String granularity)：返回在给定时间区间内的所有日志的
#  id。start 、 end 和 timestamp 的格式相同，granularity 表示考虑的时间级。比如，start = "2017:01:01:23
# :59:59", end = "2017:01:02:23:59:59", granularity = "Day" 代表区间 2017 年 1 月 1 日到 2
# 017 年 1 月 2 日。 
# 
#  
# 
#  
# 
#  样例 1 ： 
# 
#  put(1, "2017:01:01:23:59:59");
# put(2, "2017:01:01:22:59:59");
# put(3, "2016:01:01:00:00:00");
# retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Year"); // 返回值 [1,2,3]，返
# 回从 2016 年到 2017 年所有的日志。
# retrieve("2016:01:01:01:01:01","2017:01:01:23:00:00","Hour"); // 返回值 [1,2], 返回
# 从 2016:01:01:01 到 2017:01:01:23 区间内的日志，日志 3 不在区间内。
#  
# 
#  
# 
#  注释 ： 
# 
#  
#  Put 和 Retrieve 的指令总数不超过 300。 
#  年份的区间是 [2000,2017]，小时的区间是 [00,23]。 
#  Retrieve 的输出顺序不作要求。 
#  
# 
#  
#  Related Topics 设计 字符串 
#  👍 25 👎 0

"""

import bisect
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class LogSystem:
    """AC"""

    def __init__(self):
        self.records = []
        self.__granularity = {'Year': 4, 'Month': 7, 'Day': 10, 'Hour': 13, 'Minute': 16, 'Second': 19}

    def put(self, id: int, timestamp: str) -> None:
        bisect.insort_left(self.records, (timestamp, id))

    def retrieve(self, s: str, e: str, gra: str) -> List[int]:
        # Year:Month:Day:Hour:Minute:Sec
        k = self.__granularity[gra]
        dt_s = s[:k]
        dt_e = e[:k]
        l = bisect.bisect_left(self.records, (dt_s, 0))
        ans = []
        # print(self.records)
        for i in range(l, len(self.records)):
            ts, idx, = self.records[i]
            if ts[:k] > dt_e:
                break
            ans.append(idx)
        return sorted(ans)


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)
# leetcode submit region end(Prohibit modification and deletion)

def test_solution():
    obj = LogSystem()

    obj.put(1, "2017:01:01:23:59:59")
    obj.put(2, "2017:01:01:22:59:59")
    obj.put(3, "2016:01:01:00:00:00")
    assert obj.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Year") == [1, 2, 3]
    # ，返回从 2016 年到 2017 年所有的日志。
    assert obj.retrieve("2016:01:01:01:01:01", "2017:01:01:23:00:00", "Hour") == [1, 2]
    # , 返回 从 2016:01:01:01 到 2017:01:01:23 区间内的日志，日志 3 不在区间内。


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
