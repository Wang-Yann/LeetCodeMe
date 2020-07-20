#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author        : Rock Wayne 
# @Created       : 2020-05-03 23:13:38
# @Last Modified : 2020-05-03 23:13:38
# @Mail          : lostlorder@gamil.com
# @Version       : alpha-1.0


# 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"都表示数值，但
# "12e"、"1a3.14"、"1.2.3"、"+-5"、"-1E-16"及"12e+5.4"都不是。
#
#
#
#  注意：本题与主站 65 题相同：https://leetcode-cn.com/problems/valid-number/
#  Related Topics 数学
#  👍 30 👎 0

import pytest


class Solution:

    def isNumber(self, s: str) -> bool:
        """
        注意审题 E不合法
        书中解法
        """
        s=s.strip()
        self.i = 0
        length = len(s)

        def scan_integer():
            if self.i<=length-1 and s[self.i] in "+-":
                self.i += 1
            return scan_unsigned_integer()

        def scan_unsigned_integer():
            flag=False
            while self.i <= length-1  and s[self.i].isdigit():
                self.i += 1
                flag=True
            return flag
        if not s:
            return False
        is_numeric = scan_integer()
        if self.i<=length-1 and s[self.i] == ".":
            self.i += 1
            is_numeric = scan_unsigned_integer() or is_numeric
        if self.i<=length-1 and s[self.i] in "e":
            self.i += 1
            is_numeric = is_numeric and scan_integer()
        return is_numeric and self.i == length


@pytest.mark.parametrize("args,expected", [
    ("1.2.3", False),
    ("-123", True),
    ("+1.2", True),
    ("-1E-16", False),
    ("12e+5.4", False),
    ("1 ", True),
    pytest.param("5e2", True),
    pytest.param("+-5", False),
    pytest.param("123e", False),
])
def test_solutions(args, expected):
    assert Solution().isNumber(args) == expected


if __name__ == '__main__':
    pytest.main(["-q", "--color=yes", "--capture=no", __file__])
