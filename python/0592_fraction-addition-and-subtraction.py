#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-05 16:44:59
# @Last Modified : 2020-05-05 16:44:59
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个表示分数加减运算表达式的字符串，你需要返回一个字符串形式的计算结果。 这个结果应该是不可约分的分数，即最简分数。 如果最终结果是一个整数，例如 2，
# 你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为 2/1。
#
#  示例 1:
#
#
# 输入:"-1/2+1/2"
# 输出: "0/1"
#
#
#  示例 2:
#
#
# 输入:"-1/2+1/2+1/3"
# 输出: "1/3"
#
#
#  示例 3:
#
#
# 输入:"1/3-1/2"
# 输出: "-1/6"
#
#
#  示例 4:
#
#
# 输入:"5/3+1/3"
# 输出: "2/1"
#
#
#  说明:
#
#
#  输入和输出字符串只包含 '0' 到 '9' 的数字，以及 '/', '+' 和 '-'。
#  输入和输出分数格式均为 ±分子/分母。如果输入的第一个分数或者输出的分数是正数，则 '+' 会被省略掉。
#  输入只包含合法的最简分数，每个分数的分子与分母的范围是 [1,10]。 如果分母是1，意味着这个分数实际上是一个整数。
#  输入的分数个数范围是 [1,10]。
#  最终结果的分子与分母保证是 32 位整数范围内的有效整数。
#
#  Related Topics 数学
#  👍 28 👎 0

"""

import re

import pytest


class Solution:

    def fractionAddition(self, expression: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        ints = list(map(int, re.findall("[+-]?\d+", expression)))
        # print(ints)
        A, B = 0, 1
        for i in range(0, len(ints), 2):
            a, b = ints[i], ints[i + 1]
            A = A * b + a * B
            B *= b
            g = gcd(A, B)
            A //= g
            B //= g
        return "%d/%d" % (A, B)


@pytest.mark.parametrize("args,expected", [
    ("-1/2+1/2", "0/1"),
    ("5/3+1/3", "2/1"),
    pytest.param("-1/2+1/2+1/3", "1/3"),
    pytest.param("1/3-1/2", "-1/6"),
])
def test_solutions(args, expected):
    assert Solution().fractionAddition(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
