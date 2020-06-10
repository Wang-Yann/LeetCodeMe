#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 一个整数区间 [a, b] ( a < b ) 代表着从 a 到 b 的所有连续整数，包括 a 和 b。 
# 
#  给你一组整数区间intervals，请找到一个最小的集合 S，使得 S 里的元素与区间intervals中的每一个整数区间都至少有2个元素相交。 
# 
#  输出这个最小集合S的大小。 
# 
#  示例 1: 
# 
#  
# 输入: intervals = [[1, 3], [1, 4], [2, 5], [3, 5]]
# 输出: 3
# 解释:
# 考虑集合 S = {2, 3, 4}. S与intervals中的四个区间都有至少2个相交的元素。
# 且这是S最小的情况，故我们输出3。
#  
# 
#  示例 2: 
# 
#  
# 输入: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
# 输出: 5
# 解释:
# 最小的集合S = {1, 2, 3, 4, 5}.
#  
# 
#  注意: 
# 
#  
#  intervals 的长度范围为[1, 3000]。 
#  intervals[i] 长度为 2，分别代表左、右边界。 
#  intervals[i][j] 的值是 [0, 10^8]范围内的整数。 
#  
#  Related Topics 贪心算法

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        """
        贪心
        官方题解
        """
        intervals.sort(key=lambda x: (x[0], -x[1]))
        todo = [2] * len(intervals)
        ans = 0
        while intervals:
            (s, e), t = intervals.pop(), todo.pop()
            for p in range(s, s + t):
                for i, (s0, e0) in enumerate(intervals):
                    if todo[i] and p <= e0:
                        todo[i] -= 1
                ans += 1
        return ans


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:
    """
    GOOD
    对end进行排序, 如果之前没有元素被选择过，那么一定选择最后两个元素， 一个元素被选择了，选取当前区间的最后一个元素
    """

    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: x[1])
        if len(intervals) <= 1:
            return len(intervals[0])
        a = intervals[0][1] - 1
        b = intervals[0][1]
        s = {a, b}
        for e in intervals[1:]:
            if e[0] <= a:
                continue
            if e[1] > b >= e[0] > a:
                a = b
                b = e[1]
                s.add(b)
                continue
            a = e[1] - 1
            b = e[1]
            s.add(a)
            s.add(b)

        return len(s)


@pytest.mark.parametrize("kw,expected", [
    [dict(intervals=[[1, 3], [1, 4], [2, 5], [3, 5]]), 3],
    [dict(intervals=[[1, 2], [2, 3], [2, 4], [4, 5]]), 5],
    [dict(intervals=[[1, 15], [0, 8], [13, 14]]), 4],
])
def test_solutions(kw, expected):
    assert Solution1().intersectionSizeTwo(**kw) == expected
    assert Solution().intersectionSizeTwo(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
