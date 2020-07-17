#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 20:21:59
# @Last Modified : 2020-05-04 20:21:59
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0



"""
# 给定一个整数 n，返回 n! 结果尾数中零的数量。
#
#  示例 1:
#
#  输入: 3
# 输出: 0
# 解释: 3! = 6, 尾数中没有零。
#
#  示例 2:
#
#  输入: 5
# 输出: 1
# 解释: 5! = 120, 尾数中有 1 个零.
#
#  说明: 你算法的时间复杂度应为 O(log n) 。
#  Related Topics 数学
#  👍 311 👎 0

"""
import pytest


class Solution:

    def trailingZeroes(self, n: int) -> int:
        res = 0
        while n:
            res += n // 5
            n = n // 5
        return res


@pytest.mark.parametrize("args,expected", [
    (3, 0),
    pytest.param(5, 1),
])
def test_solutions(args, expected):
    assert Solution().trailingZeroes(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
