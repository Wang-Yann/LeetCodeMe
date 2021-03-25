#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 23:00:22
# @Last Modified : 2020-05-04 23:00:22
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 给定一个整数，写一个函数来判断它是否是 3 的幂次方。
#
#  示例 1:
#
#  输入: 27
# 输出: true
#
#
#  示例 2:
#
#  输入: 0
# 输出: false
#
#  示例 3:
#
#  输入: 9
# 输出: true
#
#  示例 4:
#
#  输入: 45
# 输出: false
#
#  进阶：
# 你能不使用循环或者递归来完成本题吗？
#  Related Topics 数学
#  👍 117 👎 0
import math

import pytest


class Solution:

    def isPowerOfThree(self, n: int) -> bool:
        """
        Key Point: is_integer
        """
        return n > 0 and (math.log10(n) / math.log10(3)).is_integer()


@pytest.mark.parametrize("args,expected", [
    (27, True),
    (0, False),
    (9, True),
    (45, False),
])
def test_solutions(args, expected):
    assert Solution().isPowerOfThree(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
