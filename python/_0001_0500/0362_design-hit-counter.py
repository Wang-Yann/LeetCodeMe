#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-28 15:21:12
# @Last Modified : 2020-07-28 15:21:12
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 设计一个敲击计数器，使它可以统计在过去5分钟内被敲击次数。 
# 
#  每个函数会接收一个时间戳参数（以秒为单位），你可以假设最早的时间戳从1开始，且都是按照时间顺序对系统进行调用（即时间戳是单调递增）。 
# 
#  在同一时刻有可能会有多次敲击。 
# 
#  示例: 
# 
#  HitCounter counter = new HitCounter();
# 
# // 在时刻 1 敲击一次。
# counter.hit(1);
# 
# // 在时刻 2 敲击一次。
# counter.hit(2);
# 
# // 在时刻 3 敲击一次。
# counter.hit(3);
# 
# // 在时刻 4 统计过去 5 分钟内的敲击次数, 函数返回 3 。
# counter.getHits(4);
# 
# // 在时刻 300 敲击一次。
# counter.hit(300);
# 
# // 在时刻 300 统计过去 5 分钟内的敲击次数，函数返回 4 。
# counter.getHits(300);
# 
# // 在时刻 301 统计过去 5 分钟内的敲击次数，函数返回 3 。
# counter.getHits(301); 
#  
# 
#  进阶: 
# 
#  如果每秒的敲击次数是一个很大的数字，你的计数器可以应对吗？ 
#  Related Topics 设计 
#  👍 26 👎 0

"""

import collections

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__k = 300
        self.__dq = collections.deque()
        self.__count = 0

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.getHits(timestamp)
        if self.__dq and self.__dq[-1][0] == timestamp:
            self.__dq[-1][1] += 1
        else:
            self.__dq.append([timestamp, 1])
        self.__count += 1

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.__dq and self.__dq[0][0] <= timestamp - self.__k:
            self.__count -= self.__dq.popleft()[1]
        return self.__count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
# leetcode submit region end(Prohibit modification and deletion)

class HitCounter1:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = collections.Counter()
        self.time_serials = []

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        self.counter[timestamp] += 1
        if not self.time_serials or self.time_serials[-1] != timestamp:
            self.time_serials.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.time_serials and self.time_serials[0] <= timestamp - 5 * 60:
            ts = self.time_serials.pop(0)
            self.counter.pop(ts)
        return sum(self.counter.values())

@pytest.mark.parametrize("CLS",[HitCounter,HitCounter1])
def test_solution(CLS):
    counter = CLS()
    #
    # // 在时刻 1 敲击一次。
    counter.hit(1)
    #
    # // 在时刻 2 敲击一次。
    counter.hit(2)
    #
    # // 在时刻 3 敲击一次。
    counter.hit(3)
    #
    # // 在时刻 4 统计过去 5 分钟内的敲击次数, 函数返回 3 。
    assert counter.getHits(4) == 3
    #
    # // 在时刻 300 敲击一次。
    counter.hit(300)
    #
    # // 在时刻 300 统计过去 5 分钟内的敲击次数，函数返回 4 。
    assert counter.getHits(300) == 4
    #
    # // 在时刻 301 统计过去 5 分钟内的敲击次数，函数返回 3 。
    assert counter.getHits(301) == 3


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
