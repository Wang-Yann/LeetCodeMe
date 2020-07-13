#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-07-13 16:34:35
# @Last Modified : 2020-07-13 16:34:35
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定两个整数数组a和b，计算具有最小差绝对值的一对数值（每个数组中取一个值），并返回该对数值的差 
#  示例： 
#  输入：{1, 3, 15, 11, 2}, {23, 127, 235, 19, 8}
# 输出： 3，即数值对(11, 8)
#  
#  提示： 
#  
#  1 <= a.length, b.length <= 100000 
#  -2147483648 <= a[i], b[i] <= 2147483647 
#  正确结果在区间[-2147483648, 2147483647]内 
#  
#  Related Topics 数组 双指针 
#  👍 14 👎 0

"""

from typing import List

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def smallestDifference(self, a: List[int], b: List[int]) -> int:
        a.sort()
        b.sort()
        i = j = 0
        diff = 0x7fffffff
        while i < len(a) and j < len(b):
            diff = min(diff, abs(a[i] - b[j]))
            if a[i] < b[j]:
                i += 1
            else:
                j += 1
        return diff


# leetcode submit region end(Prohibit modification and deletion)

@pytest.mark.parametrize("kw,expected", [
    [dict(a=[1, 3, 15, 11, 2], b=[23, 127, 235, 19, 8]), 3],
])
def test_solutions(kw, expected):
    assert Solution().smallestDifference(**kw) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
