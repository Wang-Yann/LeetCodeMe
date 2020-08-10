#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-11 21:02:25
# @Last Modified : 2020-04-11 21:02:25
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

"""
# 给出一个无重叠的 ，按照区间起始端点排序的区间列表。
#
#  在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。
#
#  示例 1:
#
#  输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
# 输出: [[1,5],[6,9]]
#
#
#  示例 2:
#
#  输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# 输出: [[1,2],[3,10],[12,16]]
# 解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
#
#  Related Topics 排序 数组
#  👍 165 👎 0

"""

from typing import List

import pytest


class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        low, high = newInterval
        if not intervals:
            return [newInterval]
        length = len(intervals)
        l, r = 0, length - 1
        if intervals[0][0] > high:
            intervals.insert(0, newInterval)
            return intervals
        if intervals[-1][1] < low:
            intervals.append(newInterval)
            return intervals
        while intervals[l][1] < low and l <= r:
            l += 1
        while intervals[r][0] > high and l <= r:
            r -= 1
        # print(l, r)
        new_v = [min(low, intervals[l][0]), max(high, intervals[r][1])]
        intervals[l:r + 1] = [new_v]
        return intervals


class Solution1:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        length = len(intervals)
        idx = 0
        new_start, new_end = newInterval
        while idx <= length - 1 and new_start > intervals[idx][0]:
            res.append(intervals[idx])
            idx += 1
        if not res or res[-1][1] < new_start:
            res.append(newInterval)
        else:
            res[-1][1] = max(res[-1][1], new_end)

        while idx <= length - 1:
            interval = intervals[idx]
            start, end = interval
            if res[-1][1] < start:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], end)
            idx += 1

        return res


@pytest.mark.parametrize("args,expected", [
    [([[1, 3], [6, 9]], [2, 5]), [[1, 5], [6, 9]]],
    [([[2, 3], [6, 9]], [0, 1]), [[0, 1], [2, 3], [6, 9]]],
    [([[2, 3], [6, 9]], [0, 2]), [[0, 3], [6, 9]]],
    [([[2, 3], [6, 9]], [11, 12]), [[2, 3], [6, 9], [11, 12]]],
    [([[2, 3], [6, 9]], [8, 12]), [[2, 3], [6, 12]]],
    [([[2, 3], [6, 9]], [0, 0]), [[0, 0], [2, 3], [6, 9]]],
])
def test_solutions(args, expected):
    assert Solution().insert(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
