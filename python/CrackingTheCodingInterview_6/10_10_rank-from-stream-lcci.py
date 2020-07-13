#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 14:30:46
# @Last Modified : 2020-07-13 14:30:46
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 假设你正在读取一串整数。每隔一段时间，你希望能找出数字 x 的秩(小于或等于 x 的值的个数)。请实现数据结构和算法来支持这些操作，也就是说： 
# 
#  实现 track(int x) 方法，每读入一个数字都会调用该方法； 
# 
#  实现 getRankOfNumber(int x) 方法，返回小于或等于 x 的值的个数。 
# 
#  注意：本题相对原题稍作改动 
# 
#  示例: 
# 
#  输入:
# ["StreamRank", "getRankOfNumber", "track", "getRankOfNumber"]
# [[], [1], [0], [0]]
# 输出:
# [null,0,null,1]
#  
# 
#  提示： 
# 
#  
#  x <= 50000 
#  track 和 getRankOfNumber 方法的调用次数均不超过 2000 次 
#  
#  👍 8 👎 0

"""

import bisect

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class StreamRank:

    def __init__(self):
        self.arr = []

    def track(self, x: int) -> None:
        bisect.insort_left(self.arr, x)

    def getRankOfNumber(self, x: int) -> int:
        i = bisect.bisect_right(self.arr, x)
        return i


# Your StreamRank object will be instantiated and called as such:
# obj = StreamRank()
# obj.track(x)
# param_2 = obj.getRankOfNumber(x)
# leetcode submit region end(Prohibit modification and deletion)

def test_solution():
    obj = StreamRank()
    assert obj.getRankOfNumber(1) == 0
    obj.track(0)
    assert obj.getRankOfNumber(0) == 1


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
