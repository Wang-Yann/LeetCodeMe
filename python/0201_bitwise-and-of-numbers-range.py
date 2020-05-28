#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-07 08:00:00
# @Last Modified : 2020-05-07 08:00:00
# @Mail          : lostlorder@gmail.com
# @Version       : alpha-1.0

"""
# 给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。 
# 
#  示例 1: 
# 
#  输入: [5,7]
# 输出: 4 
# 
#  示例 2: 
# 
#  输入: [0,1]
# 输出: 0 
#  Related Topics 位运算

"""

import pytest


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m<n:
            n&=n-1
        return n


# leetcode submit region end(Prohibit modification and deletion)


@pytest.mark.parametrize("args,expected", [
    ([5, 7], 4),
    ([0, 1], 0),
])
def test_solutions(args, expected):
    assert Solution().rangeBitwiseAnd(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
