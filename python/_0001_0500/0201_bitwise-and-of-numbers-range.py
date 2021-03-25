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
        """
        对所有数字执行按位与运算的结果是所有对应二进制字符串的公共前缀再用零补上后面的剩余位
        计算两个二进制字符串的公共前缀
        """
        while m < n:
            n &= (n - 1)
        return n


# leetcode submit region end(Prohibit modification and deletion)

class Solution1:

    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        shift = 0
        # 找到公共前缀
        while m < n:
            m = m >> 1
            n = n >> 1
            shift += 1
        return m << shift


@pytest.mark.parametrize("args,expected", [
    ([5, 7], 4),
    ([0, 1], 0),
])
def test_solutions(args, expected):
    assert Solution().rangeBitwiseAnd(*args) == expected
    assert Solution1().rangeBitwiseAnd(*args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
