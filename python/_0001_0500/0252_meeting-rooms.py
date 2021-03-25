#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-22 21:53:02
# @Last Modified : 2020-07-22 21:53:02
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0

"""
# 给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，请你判断一个人是否能够参加
# 这里面的全部会议。 
# 
#  示例 1: 
# 
#  输入: [[0,30],[5,10],[15,20]]
# 输出: false
#  
# 
#  示例 2: 
# 
#  输入: [[7,10],[2,4]]
# 输出: true
#  
#  Related Topics 排序 
#  👍 31 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        return all(a[1] <= b[0] for a, b in zip(intervals, intervals[1:]))


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([[0, 30], [5, 10], [15, 20]], False),
    ([[7, 10], [2, 4]], True),
])
def test_solutions252(args, expected):
    assert Solution().canAttendMeetings(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
