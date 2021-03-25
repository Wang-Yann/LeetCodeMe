#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-26 22:56:14
# @Last Modified : 2020-07-26 22:56:14
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 给定员工的 schedule 列表，表示每个员工的工作时间。 
# 
#  每个员工都有一个非重叠的时间段 Intervals 列表，这些时间段已经排好序。 
# 
#  返回表示 所有 员工的 共同，正数长度的空闲时间 的有限时间段的列表，同样需要排好序。 
# 
#  示例 1： 
# 
#  输入：schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]
# 输出：[[3,4]]
# 解释：
# 共有 3 个员工，并且所有共同的
# 空间时间段是 [-inf, 1], [3, 4], [10, inf]。
# 我们去除所有包含 inf 的时间段，因为它们不是有限的时间段。
#  
# 
#  
# 
#  示例 2： 
# 
#  输入：schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
# 输出：[[5,6],[7,9]]
#  
# 
#  
# 
#  （尽管我们用 [x, y] 的形式表示 Intervals ，内部的对象是 Intervals 而不是列表或数组。例如，schedule[0][0].st
# art = 1, schedule[0][0].end = 2，并且 schedule[0][0][0] 是未定义的） 
# 
#  而且，答案中不包含 [5, 5] ，因为长度为 0。 
# 
#  
# 
#  注： 
# 
#  
#  schedule 和 schedule[i] 为长度范围在 [1, 50]的列表。 
#  0 <= schedule[i].start < schedule[i].end <= 10^8。 
#  
# 
#  注：输入类型于 2019 年 4 月 15 日 改变。请重置为默认代码的定义以获取新方法。 
# 
#  
#  Related Topics 堆 贪心算法 
#  👍 18 👎 0

"""
import heapq

import pytest

from common_utils import Interval

# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""


class Solution(object):

    def employeeFreeTime(self, schedule):
        """
        假设在某个时间段没有员工工作，这个时间段将持续到某个员工要工作时为止。

        我们维护员工下一次要工作的数据。当处理完当前工作时，我们为该员工添加下一次的工作。

        算法：

        我们跟踪最新的时间 anchor。当我们处理尚未处理的工作时，时间为 t，员工 e_id，是该员工的第 e_jx 个工作。如果 anchor < t，则存在一个空闲区间 Interval(anchor, t)


        """
        ans = []
        pq = [(emp[0].start, ei, 0) for ei, emp in enumerate(schedule)]
        heapq.heapify(pq)
        anchor = min(iv.start for emp in schedule for iv in emp)
        while pq:
            t, e_id, e_jx = heapq.heappop(pq)
            if anchor < t:
                ans.append(Interval(anchor, t))
            anchor = max(anchor, schedule[e_id][e_jx].end)
            if e_jx + 1 < len(schedule[e_id]):
                heapq.heappush(pq, (schedule[e_id][e_jx + 1].start, e_id, e_jx + 1))

        return ans


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        """
        TODO TODO TODO GOOD
        事件（扫描线）
        对于每个区间，创建如上所述的两个事件，并对事件进行排序。在事件 t 发生的每个事件，如果 balance == 0，则说明 [prev，t] 是所有员工都不包含的区间，其中 prev 是 t 的前一个值

        """
        OPEN, CLOSE = 0, 1
        events = []
        for intervals in schedule:
            for iv in intervals:
                events.append((iv.start, OPEN))
                events.append((iv.end, CLOSE))
        events.sort()

        ans = []
        prev = None
        balance = 0
        for t, cmd in events:
            if balance == 0 and prev is not None:
                ans.append(Interval(prev, t))
            if cmd == OPEN:
                balance += 1
            else:
                balance += -1
            prev = t
        return ans


@pytest.mark.parametrize("kwargs,expected", [
    [dict(schedule=[[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]), [[3, 4]]],
    pytest.param(dict(schedule=[[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]), [[5, 6], [7, 9]]),
])
@pytest.mark.parametrize("SOL", [Solution1, Solution])
def test_solutions(kwargs, expected, SOL):
    sch = [[Interval(*x) for x in xs] for xs in kwargs["schedule"]]
    expected = [Interval(*x) for x in expected]
    # print(sch,expected)
    res = SOL().employeeFreeTime(sch)
    assert repr(res) == repr(expected)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
