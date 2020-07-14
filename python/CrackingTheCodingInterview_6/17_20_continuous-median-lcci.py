#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-14 23:39:09
# @Last Modified : 2020-07-14 23:39:09
# @Mail          : lostlorder@gmail.com
# @Version       : 1.0.0
"""

# 随机产生数字并传递给一个方法。你能否完成这个方法，在每次产生新值时，寻找当前所有值的中间值（中位数）并保存。 
# 
#  中位数是有序列表中间的数。如果列表长度是偶数，中位数则是中间两个数的平均值。 
# 
#  例如， 
# 
#  [2,3,4] 的中位数是 3 
# 
#  [2,3] 的中位数是 (2 + 3) / 2 = 2.5 
# 
#  设计一个支持以下两种操作的数据结构： 
# 
#  
#  void addNum(int num) - 从数据流中添加一个整数到数据结构中。 
#  double findMedian() - 返回目前所有元素的中位数。 
#  
# 
#  示例： 
# 
#  addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3) 
# findMedian() -> 2
#  
#  Related Topics 堆 
#  👍 3 👎 0


"""

import bisect

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.nums = []

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.nums, num)

    def findMedian(self) -> float:
        N = len(self.nums)
        if N % 2 == 0:
            return (self.nums[N // 2] + self.nums[N // 2 - 1]) / 2
        else:
            return self.nums[N // 2]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
# leetcode submit region end(Prohibit modification and deletion)


def test_solution():
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    assert obj.findMedian() == 1.5
    obj.addNum(3)
    assert obj.findMedian() == 2.0


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=tee-sys", __file__])
