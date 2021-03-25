#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-31 08:00:00
# @Last Modified : 2020-05-31 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0
"""
# 给定一个 24 小时制（小时:分钟）的时间列表，找出列表中任意两个时间的最小时间差并以分钟数表示。 
# 
#  
# 示例 1： 
# 
#  输入: ["23:59","00:00"]
# 输出: 1
#  
# 
#  
# 备注: 
# 
#  
#  列表中时间数在 2~20000 之间。 
#  每个时间取值在 00:00~23:59 之间。 
#  
#  Related Topics 字符串

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)


class Solution(object):

    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        minutes = list(map(lambda x:int(x[:2]) * 60 + int(x[3:]), timePoints))
        minutes.sort()
        return min((y - x) % (24 * 60) for x, y in zip(minutes, minutes[1:] + minutes[:1]))


# leetcode submit region end(Prohibit modification and deletion)
class Solution1:

    def findMinDifference(self, timePoints: List[str]) -> int:
        if len(timePoints) < 2:
            return 0
        minute_list = []
        for t in timePoints:
            h, m = map(int, t.split(":"))
            minute_list.append(60 * h + m)
        minute_list.sort()
        ans = minute_list[0] + 24 * 60 - minute_list[-1]
        for a, b in zip(minute_list, minute_list[1:]):
            ans = min(b - a, ans)
        return ans


@pytest.mark.parametrize("args,expected", [
    (["23:59", "00:00"], 1),
])
def test_solutions(args, expected):
    assert Solution().findMinDifference(args) == expected
    assert Solution1().findMinDifference(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
