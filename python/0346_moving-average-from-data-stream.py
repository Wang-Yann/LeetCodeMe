#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-27 17:34:22
# @Last Modified : 2020-07-27 17:34:22
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数数据流和一个窗口大小，根据该滑动窗口的大小，计算其所有整数的移动平均值。 
# 
#  示例: 
# 
#  MovingAverage m = new MovingAverage(3);
# m.next(1) = 1
# m.next(10) = (1 + 10) / 2
# m.next(3) = (1 + 10 + 3) / 3
# m.next(5) = (10 + 3 + 5) / 3
#  
# 
#  
#  Related Topics 设计 队列 
#  👍 24 👎 0

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class MovingAverage:
    """AC"""

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.size = size
        self.total = 0

    def next(self, val: int) -> float:
        if len(self.q) == self.size:
            self.total -= self.q.pop(0)
        self.total += val
        self.q.append(val)
        return self.total / len(self.q)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
# leetcode submit region end(Prohibit modification and deletion)


def test_solution():
    m = MovingAverage(3)
    assert m.next(1) == 1
    assert m.next(10) == pytest.approx((1 + 10) / 2, 1e-5)
    assert m.next(3) == pytest.approx((1 + 10 + 3) / 3)
    assert m.next(5) == pytest.approx((10 + 3 + 5) / 3)


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
