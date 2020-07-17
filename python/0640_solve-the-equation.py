#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 17:19:14
# @Last Modified : 2020-05-05 17:19:14
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0

# 求解一个给定的方程，将x以字符串"x=#value"的形式返回。该方程仅包含'+'，' - '操作，变量 x 和其对应系数。
#
#  如果方程没有解，请返回“No solution”。
#
#  如果方程有无限解，则返回“Infinite solutions”。
#
#  如果方程中只有一个解，要保证返回值 x 是一个整数。
#
#  示例 1：
#
#  输入: "x+5-3+x=6+x-2"
# 输出: "x=2"
#
#
#  示例 2:
#
#  输入: "x=x"
# 输出: "Infinite solutions"
#
#
#  示例 3:
#
#  输入: "2x=x"
# 输出: "x=0"
#
#
#  示例 4:
#
#  输入: "2x+3x-6x=x+2"
# 输出: "x=-1"
#
#
#  示例 5:
#
#  输入: "x=x+2"
# 输出: "No solution"
#
#  Related Topics 数学
#  👍 45 👎 0

import re

import pytest


class Solution:

    def solveEquation(self, equation: str) -> str:
        a, b, side = 0, 0, 1
        for eq, sign, num, is_x in re.findall("(=)|([-+]?)(\d*)(x?)", equation):
            print("rows",[eq, sign, num, is_x])
            if eq:
                side = -1
            elif is_x:
                a += side * int(sign + "1") * int(num or 1)
            elif num:
                b -= side * int(sign + num)
        if a:
            return "x=%d" % (b // a)
        else:
            return 'No solution' if b else "Infinite solutions"


@pytest.mark.parametrize("args,expected", [
    ("x+5-3+x=6+x-2", "x=2"),
    ("x=x", "Infinite solutions"),
    ("2x=x", "x=0"),
    ("2x+3x-6x=x+2", "x=-1"),
    ("x=x+2", "No solution"),
])
def test_solutions(args, expected):
    assert Solution().solveEquation(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
