#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# Range 模块是跟踪数字范围的模块。你的任务是以一种有效的方式设计和实现以下接口。 
# 
#  
#  addRange(int left, int right) 添加半开区间 [left, right)，跟踪该区间中的每个实数。添加与当前跟踪的数字部分重叠
# 的区间时，应当添加在区间 [left, right) 中尚未跟踪的任何数字到该区间中。 
#  queryRange(int left, int right) 只有在当前正在跟踪区间 [left, right) 中的每一个实数时，才返回 true。 
# 
#  removeRange(int left, int right) 停止跟踪区间 [left, right) 中当前正在跟踪的每个实数。 
#  
# 
#  
# 
#  示例： 
# 
#  addRange(10, 20): null
# removeRange(14, 16): null
# queryRange(10, 14): true （区间 [10, 14) 中的每个数都正在被跟踪）
# queryRange(13, 15): false （未跟踪区间 [13, 15) 中像 14, 14.03, 14.17 这样的数字）
# queryRange(16, 17): true （尽管执行了删除操作，区间 [16, 17) 中的数字 16 仍然会被跟踪）
#  
# 
#  
# 
#  提示： 
# 
#  
#  半开区间 [left, right) 表示所有满足 left <= x < right 的实数。 
#  对 addRange, queryRange, removeRange 的所有调用中 0 < left < right < 10^9。 
#  在单个测试用例中，对 addRange 的调用总数不超过 1000 次。 
#  在单个测试用例中，对 queryRange 的调用总数不超过 5000 次。 
#  在单个测试用例中，对 removeRange 的调用总数不超过 1000 次。 
#  
# 
#  
#  Related Topics 线段树 Ordered Map

"""

import bisect

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class RangeModule:

    def __init__(self):
        self.ranges = []

    def addRange(self, left: int, right: int) -> None:
        # print("[{}-{}]".format(left,right))
        ranges = self.ranges
        lo, hi = bisect.bisect_left(ranges, left), bisect.bisect_right(ranges, right)
        # 代表有交叉
        if lo % 2 == 1:
            # print("ranges,low",self.ranges,lo,left,right)
            lo -= 1
            left = ranges[lo]
        if hi % 2 == 1:
            # print("ranges,hi",self.ranges,hi,left,right)
            right = ranges[hi]
            hi += 1
        self.ranges = ranges[:lo] + [left, right] + ranges[hi:]

    def queryRange(self, left: int, right: int) -> bool:
        lo = bisect.bisect_right(self.ranges, left)
        return lo % 2 == 1 and lo < len(self.ranges) and self.ranges[lo - 1] <= left < right <= self.ranges[lo]

    def removeRange(self, left: int, right: int) -> None:
        """GOOD"""
        ranges = self.ranges
        lo, hi = bisect.bisect_left(ranges, left), bisect.bisect_right(ranges, right)
        new = []
        if lo % 2 == 1:
            lo -= 1
            new += [ranges[lo], left]
        if hi % 2 == 1:
            new += [right, ranges[hi]]
            hi += 1
        self.ranges = ranges[:lo] + new + ranges[hi:]


# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
# leetcode submit region end(Prohibit modification and deletion)


def test_solutions():
    obj = RangeModule()
    assert obj.addRange(10, 20) is None  #
    # assert obj.addRange(40, 50) is None  #
    assert obj.addRange(13, 19) is None  #
    assert obj.addRange(14, 21) is None  #
    assert obj.removeRange(14, 16) is None  #
    assert obj.queryRange(10, 14)  # true （区间 [10, 14) 中的每个数都正在被跟踪）
    assert obj.queryRange(13, 15) is False  # false （未跟踪区间 [13, 15) 中像 14, 14.03, 14.17 这样的数字）
    assert obj.queryRange(16, 17)  # true （尽管执行了删除操作，区间 [16, 17) 中的数字 16 仍然会被跟踪）


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
