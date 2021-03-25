#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-06 08:00:00
# @Last Modified : 2020-05-06 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定一个整数数组 nums，求出数组从索引 i 到 j (i ≤ j) 范围内元素的总和，包含 i, j 两点。 
# 
#  示例： 
# 
#  给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()
# 
# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3 
# 
#  说明: 
# 
#  
#  你可以假设数组不可变。 
#  会多次调用 sumRange 方法。 
#  
#  Related Topics 动态规划

"""
from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = [0]
        for v in nums:
            self.prefix.append(self.prefix[-1] + v)

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix[j + 1] - self.prefix[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
# leetcode submit region end(Prohibit modification and deletion)


def test_solutions():
    nums = [-2, 0, 3, -5, 2, -1]
    sol = NumArray(nums)
    assert sol.sumRange(0, 2) == 1
    assert sol.sumRange(2, 5) == -1
    assert sol.sumRange(0, 5) == -3


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
