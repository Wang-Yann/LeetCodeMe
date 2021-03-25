#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 16:09:13
# @Last Modified : 2020-05-04 16:09:13
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定两个整数，分别表示分数的分子 numerator 和分母 denominator，以字符串形式返回小数。
#
#  如果小数部分为循环小数，则将循环的部分括在括号内。
#
#  示例 1:
#
#  输入: numerator = 1, denominator = 2
# 输出: "0.5"
#
#
#  示例 2:
#
#  输入: numerator = 2, denominator = 1
# 输出: "2"
#
#  示例 3:
#
#  输入: numerator = 2, denominator = 3
# 输出: "0.(6)"
#
#  Related Topics 哈希表 数学
#  👍 144 👎 0

"""

import pytest


class Solution:

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        result = ""
        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            result = "-"
        dvd, dvs = abs(numerator), abs(denominator)
        result += str(dvd // dvs)
        dvd %= dvs
        if dvd > 0:
            result += "."
        lookup = {}
        while dvd and dvd not in lookup:
            lookup[dvd] = len(result)
            dvd *= 10
            result += str(dvd // dvs)
            dvd %= dvs
        # print("dvd,dvs,lookup",dvd,dvs,lookup)
        if dvd in lookup:
            idx = lookup[dvd]
            result = result[:idx] + "(" + result[idx:] + ")"
        return result


@pytest.mark.parametrize("kwargs,expected", [
    (dict(numerator=1, denominator=2), "0.5"),
    (dict(numerator=2, denominator=3), "0.(6)"),
    pytest.param(dict(numerator=2, denominator=1), "2"),
])
def test_solutions(kwargs, expected):
    assert Solution().fractionToDecimal(**kwargs) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
