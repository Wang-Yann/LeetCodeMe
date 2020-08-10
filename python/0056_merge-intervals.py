#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rocky Wayne 
# @Created       : 2020-04-11 20:48:26
# @Last Modified : 2020-04-11 20:48:26
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给出一个区间的集合，请合并所有重叠的区间。
#
#  示例 1:
#
#  输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
#
#  示例 2:
#
#  输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
#  Related Topics 排序 数组
#  👍 506 👎 0

"""

from typing import List

import pytest


class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = []
        for i in range(0, len(intervals)):
            v = intervals[i]
            if i > 0 and v[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], v[1])
            else:
                res.append(v)
        return res


@pytest.mark.parametrize("args,expected", [
    ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
    ([[1, 4], [4, 5]], [[1, 5]])
])
def test_solutions(args, expected):
    assert Solution().merge(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
