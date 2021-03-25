#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 16:24:26
# @Last Modified : 2020-05-04 16:24:26
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
#
#  例如，
#
#      1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...
#
#
#  示例 1:
#
#  输入: 1
# 输出: "A"
#
#
#  示例 2:
#
#  输入: 28
# 输出: "AB"
#
#
#  示例 3:
#
#  输入: 701
# 输出: "ZY"
#
#  Related Topics 数学
#  👍 239 👎 0

"""

import pytest


class Solution:

    def convertToTitle(self, n: int) -> str:
        base = 26
        # char_map = dict(zip(range(1,base+1),string.ascii_uppercase ))
        res = ""
        while n > 0:
            # 重点
            n -= 1
            res = chr(ord('A') + (n % base)) + res
            n //= base
        return res


@pytest.mark.parametrize("args,expected", [
    (1, "A"),
    (701, "ZY"),
    pytest.param(28, "AB"),
])
def test_solutions(args, expected):
    assert Solution().convertToTitle(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
