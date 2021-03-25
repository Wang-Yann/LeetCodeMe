#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-04 16:24:26
# @Last Modified : 2020-05-04 16:24:26
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


"""
# 给定一个Excel表格中的列名称，返回其相应的列序号。
#
#  例如，
#
#      A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
#     ...
#
#
#  示例 1:
#
#  输入: "A"
# 输出: 1
#
#
#  示例 2:
#
#  输入: "AB"
# 输出: 28
#
#
#  示例 3:
#
#  输入: "ZY"
# 输出: 701
#
#  致谢：
# 特别感谢 @ts 添加此问题并创建所有测试用例。
#  Related Topics 数学
#  👍 159 👎 0

"""

import string

import pytest


class Solution:

    def titleToNumber(self, s: str) -> str:
        base=26
        char_map = dict(zip(string.ascii_uppercase ,range(1,base+1)))
        res = 0
        for char in  s:
            res = res*base+ char_map[char]
        return res


@pytest.mark.parametrize("expected,s", [
    (1, "A"),
    (701, "ZY"),
    pytest.param(28, "AB"),
])
def test_solutions( expected,s):
    assert Solution().titleToNumber(s) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
